#!/usr/local/bin/perl

# RCsearch_dr_xml.cgi
#
#  search results to allow regional sites to creat content includes
#  for LATEST NEWS and FEATURED RESEARCH area

# NOTE
# -- vatCode
# -- missing category info
# -- PDF files
# -- price normalization

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
#require ("/home/gartner/cgi-bin/gNOlogin2.pl");
require ("/home/gartner/html/rt/getLoggedInDoc.pl");
require ("/home/gartner/html/rt/getNODocument3.pl");

use Carp;
no Carp::Assert;



# Variables
$server = "www4";
local $pageOneFlag = "";
local $URL = "http:\/\/$server.gartner.com\/Search";
local $date = `date '+20%y-%m-%dT%H:%M:%S'`; # need YYYY-MM-DDTHH:MI:SS
chop ($date); 
&fakeTOC;
&catCodes;

##############################################################
# Get the input from the HTML Form
##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {
    
    
    # something submitted
    
    use CGI_Lite;
    $cgi = new CGI_Lite;
    
    %FORM = $cgi->parse_form_data;
    
    foreach $key (keys %FORM) {
	
	next if ($key eq "PRM");
	$buffer .= "$key\=$FORM{$key}\&";
	
    }
    
    carp "search buffer is: $buffer\n";
    
} else {
    
    print <<EndofHTML;
Content-Type: text/html

<html>
    <head>
    </head>
    <body>
no input
    </body>
</html>
EndofHTML

	exit;
}



##################################################################################
# MAIN
#
#

# Run initial search and get all documents
$URL = "http:\/\/www4.gartner.com\/Search\?".$buffer;
local $Page = &getGARTNERpage($URL, $server);


# Parse initial search results and find more search results
&parsePage($Page);

# Get additional search results pages and collect document URLS
local $c;
foreach $URL (@URLS) {

    $c++;
    
    $URL = "http:\/\/www4.gartner.com\/Search\?".$URL;
    
    $msg .= "\n\n<br>Getting page: $URL<br>\n\n";
    
    carp "Getting another search page $c of $#URLS: $URL\n";
    
    local $Page = &getGARTNERpage("$URL", $server);
    
    &parsePage($Page);
    
}



# Get each document found on all the search pages
# its a hash to remove dups
foreach $uri (keys %getDocs) {

    carp "LOOPING ON DOC $count: $uri\n";
    
    last if ($uri =~ /Search/); # just incase a Search URL slipped in.
    
    $uriMsg .= "getting doc $count: $uri<br>\n";

    &getNoteNumber($uri);
    
    $count++;
    
}

# Print output
carp "DONE GETTING DOCS, GOING TO PRINT OUTPUT\n";
&printPage;

exit;



##################################################################################
sub parsePage {
    
    
    local @output = split (/\n/, $_[0]);
    
    foreach (@output) {
	
	
	# ADDITIONAL SEARCH RESULTS PAGES
	if (!$pageOneFlag && /Search\?/) {
	    
	    while (/Search\?(.[^\"]*)\"/g) {
		
		push @URLS, $1;
		
		carp "FOUND ADDITIONAL RESULTS PAGE $1<p\>\n";
		
		$msg .= "new FOUND ADDITIONAL RESULTS PAGE $1<p\>\n\n";
		
	    }
	    
			# only get other search result URLs once
	    $pageOneFlag = 1;
	}
	
	# get documents
	if (/javascript:openDoc\(\'(Display.*[^\&ref\=])\&ref\=/) {
	    
	    $getDocs{$1} = 1;
	    
	    $msg .= "\n\n<br>Getting Document: $searchURL<br>\n\n";
	    
	    carp "FOUND DOCUMENT ON SEARCH PAGE: $1\n";
	    
	}
    }
}

##################################################################################
sub getNoteNumber {
    
    local $rId = $_[0];
    $rId =~ s/DisplayDocument\?id\=//;

    
    if (&readDB($rId)) {
	
	# already in database
	carp " \- GOT DOC from Saved DB: $title{$rId}\n";
	return();
	
    } elsif (&readDiscard($rId)) {
	
	# already in discard database for being too cheap or the wrong doctype
	carp " \- GOT DOC from Discard DB: $rId\n";
	$countDiscard++;
	return();

    }
    

    $FORM{URL} = "http:\/\/www4.gartner.com\/$_[0]\&ref\=g_search";
    carp "GETTING NN: $count: http:\/\/www4.gartner.com\/$_[0]\&ref\=g_search\n";
    
    local ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price, $pages, $docType, $contentType, $folderType) = "";
    
    ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price, $pages, $docType, $contentType, $folderType, $keywords, $path, $fileName, $fileSize) = &getResearchDetail($FORM{'URL'});

    #($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price, $pages, $docType, $contentType, $folderType, $keywords, $path, $fileName, $fileSize) = &getLoggedinResearchDetail($FORM{'URL'});

    ($null, $null, $null, $null, $null, $null, $null, $null, $null, $null, $null, $null, $null, $null, $path, $fileName, $fileSize) = &getLoggedinResearchDetail($FORM{'URL'});
    
    carp "got document: $noteNumber: $title $price\n";
    
    return() if (!$price || !$title);
    
    local $p = $price;
    $p =~ s/\,//;
    
    if ($p < 495 && $contentType !~ /(Hype|Magic|Vendor Rating)/) {
	
	$countNoprice++;
	
	carp " \- TOO CHEAP: $p for $title\n";
	
	$saveDiscard .= "$rId\n";
	
	return();
    }
    
    if ($docType eq "Article Top View" || $docType =~ /EXP/ || $docType =~ /Cluster/ || $docType =~ /Comparison/ || $docType =~ /MarketView/ || $contentType =~ /Basic Facts/ || $docType =~ /Executive Summary/) {
	
	$countNodoctype++;
	
	carp " \- WRONG DOC TYPE: $docType for $title\n";
	
	$saveDiscard .= "$rId\n";
	
	return();
    }
    
    carp " \- GOT DOC: $title\n";
    
    if ($contentType =~ /(Hype|Magic|Vendor Rating)/) {
	
	# deal with these as special.... 
	# make the content type a doc type 
	# AND create a mock table of contents
	
	$docType = $contentType;
	$toc = $fakeToc{$docType};
	
    }
    
    # clean up docTypes based on drFind.cgi
    $docType = "Market Trends and Statistics"
	if ($docType =~ /(Market|Dataquest|Focus Report|User Wants|Telebriefing)/);
    $docType = "Strategy and Analysis"
	if ($docType =~ /(Research Note|Strategic Analysis Report)/);
    

    # price normalization
    $price =~ s/,//g; # remove commas
    $price = 399  if ($price == 495);
    $price = 799  if ($price == 995);
    $price = 2449 if ($price == 2995);
    $price = 3999 if ($price == 4995);
    $price = 8249 if ($price == 9999);
		 

    
    
    
    $title{$resId}       = $title;
    $summary{$resId}     = $summary;
    $noteNumber{$resId}  = $noteNumber;
    $date{$resId}        = $pubDate;
    $author{$resId}      = $auth;
    $toc{$resId}         = $toc;
    $price{$resId}       = $price;
    $pages{$resId}       = $pages;
    $resId{$resId}       = $resId;
    $docType{$resId}     = $docType;
    $contentType{$resId} = $contentType;
    $folderType{$resId}  = $folderType;
    $keywords{$resId}    = $keywords;
    $path{$resId}        = $path;
    $fileName{$resId}    = $fileName;
    $fileSize{$resId}    = $fileSize;
    
    $processedCount++;

    return();
    
}


##################################################################################
sub printPage {
    

    local $i = 1;
    foreach $resId (reverse sort keys %title) {
	
	chop ($author{$resId}); # remove last comma
	
	$date{$resId} =~ s/\&nbsp\;/ /gi;
	
	$listing .=<<EOF;
<tr>
 <td rowspan="12" valign="top" bgcolor="lightblue">$i</td>
 <td>title</td>
 <td>$title{$resId}</td>
</tr>

<tr>
 <td>summary</td>
 <td>$summary{$resId}</td>
</tr>

<tr>
 <td>author</td>
 <td>$author{$resId}</td>
</tr>

<tr>
 <td>date</td>
 <td>$date{$resId}</td>
</tr>

<tr>
 <td>ResId</td>
 <td>$resId{$resId}</td>
</tr>

<tr>
 <td>NN</td>
 <td>$noteNumber{$resId}</td>
</tr>

<tr>
 <td>Doc Type</td>
 <td>$docType{$resId}</td>
</tr>

<tr>
 <td>Folder Type</td>
 <td>$folderType{$resId}</td>
</tr>

<tr>
 <td>Content Type</td>
 <td>$contentType{$resId}</td>
</tr>

<tr>
 <td>price</td>
 <td>$price{$resId}</td>
</tr>

<tr>
 <td>pages</td>
 <td>$pages{$resId}</td>
</tr>

<tr>
 <td>Table of Contents</td>
 <td>$toc{$resId}</td>
</tr>

EOF

    $searchLayout .=<<EOF;

	<p class="department">In $FORM{'PRM'}</p>
	<p class="type">$docType{$resId}</p>
	<p class="title">$title{$resId}</p>
	<p class="summary">$summary{$resId}</p>
	<p class="price">PRICE: \$$price{$resId}</p>
	<p class="cartLink"><a href="buy?id=$resId{$resId}">ADD TO CART</a></p>

EOF

    $packageLayout .=<<EOF;

	<p class="type">$docType{$resId}</p>
	<p class="title">$title{$resId}</p>
	<p class="summary">$summary{$resId}</p>
	<p class="authors">Written by $author{$resId}</p>
	<p class="date">Published on $date{$resId}</p>
	<p class="pages">$pages{$resId} pages</p>
	<p class="price">PRICE: \$$price{$resId}</p>
	<p class="cartLink"><a href="buy?id=$resId{$resId}">ADD TO CART</a></p>

EOF

    $detailLayout .=<<EOF;

	<p class="type">$docType{$resId}</p>
	<p class="title">$title{$resId}</p>
	<p class="summary">$summary{$resId}</p>
	<p class="authors">Written by $author{$resId}</p>
	<p class="date">Published on $date{$resId}</p>
	<p class="pages">$pages{$resId} pages</p>
	<p class="price">PRICE: \$$price{$resId}</p>
	<p class="cartLink"><a href="buy?id=$resId{$resId}">ADD TO CART</a></p>
        $toc{$resId}

EOF
    

    $xml .=<<EndofXML;

 <Product>
  <ProductAttribute action="establish" name="Action">
    <Value>insert</Value> 
  </ProductAttribute>
  <ProductAttribute action="establish" name="formalName">
   <Value>$title{$resId}</Value>
  </ProductAttribute>
  <ProductAttribute action="establish" name="hostCategory">
   <Value>$catTopic{$FORM{'PRM'}}{$docType{$resId}}</Value>
  </ProductAttribute>
   <ProductAttribute action="establish" name="hostCategory">
   <Value>$catType{$docType{$resId}}{$FORM{'PRM'}}</Value>
  </ProductAttribute>
 
  <ProductAttribute action="establish" name="productType">
   <Value>Software</Value>
  </ProductAttribute>
  <ProductAttribute action="establish" name="productStatus">
   <Value>1</Value>
  </ProductAttribute>
  <ProductAttribute action="establish" name="itemListing">
   <Value><![CDATA[
       <p class="type">$docType{$resId}</p>
       <p class="title">$title{$resId}</p>
       <p class="summary">$summary{$resId}</p>
   ]]></Value>
  </ProductAttribute>
  <ProductAttribute action="establish" name="SalesPitch">
   <Value><![CDATA[
       <p class="type">$docType{$resId}</p>
       <p class="title">$title{$resId}</p>
       <p class="summary">$summary{$resId}</p>
   ]]></Value>
  </ProductAttribute>
  <ProductAttribute action="establish" name="detailedDescription">
   <Value><![CDATA[
      <p class="type">$docType{$resId}</p>
    	<p class="title">$title{$resId}</p>
    	<p class="summary">$summary{$resId}</p>
    	<p class="authors">Written by $author{$resId}</p>
    	<p class="date">Published on $date{$resId}</p>
    	<p class="pages">$pages{$resId} pages</p>
        $toc{$resId}
  ]]></Value>
  </ProductAttribute>  
  <ProductAttribute action="establish" name="keywords">
   <Value>$keywords{$resId}</Value>
  </ProductAttribute>  
  <ProductAttribute action="establish" name="systemRequirements">
   <Value>Adobe Acrobat Reader</Value>
  </ProductAttribute>
  <ProductAttribute action="establish" name="downloadInfo">
   <Value><![CDATA[This PDF download requires that you have Adobe Acrobat Reader installed.  if you do not, please get a free reader <a href="http://www.adobe.com/products/acrobat/" target="_blank">here</a>.]]></Value>
  </ProductAttribute>
  <ProductAttribute action="establish" name="ProductImage">
   <Value>$imageProd{$docType{$resId}}</Value>
  </ProductAttribute>
  <ProductAttribute action="establish" name="ThumbnailImage">
   <Value>$imageThumb{$docType{$resId}}</Value>  
  </ProductAttribute>
  
  <Version>
   <VersionAttribute action="establish" name="Action">
    <Value>insert</Value>   
   </VersionAttribute>
   <VersionAttribute action="establish" name="versionStatus">
    <Value>1</Value>
   </VersionAttribute>  
   <VersionAttribute action="establish" name="platformID">
    <Value>0</Value>
   </VersionAttribute>  
   <VersionAttribute action="establish" name="manufacturerPartNumber">
    <Value>$resId{$resId}</Value>
   </VersionAttribute>  
   <VersionAttribute action="establish" name="versionName">
    <Value>$noteNumber{$resId}</Value>
   </VersionAttribute>
   <VersionAttribute action="establish" name="ApplicationFileName">
    <Value>$fileName{$resId}</Value>
   </VersionAttribute>
   <VersionAttribute action="establish" name="ApplicationFileSize">
    <Value>$fileSize{$resId}</Value>
   </VersionAttribute>
   <VersionAttribute action="establish" name="vatCode">
    <Value>99809902</Value>
   </VersionAttribute>
   <VersionAttribute action="establish" name="unitOfMeasure">
    <Value>EA</Value>
   </VersionAttribute>
     
   <PriceAttribute action="establish" isocode="978">
    <Price action="establish" name="sellPrice">
     <Value>$price{$resId}</Value>
    </Price>
   </PriceAttribute>

    
   <DeliveryAttribute action="establish" name="format">
    <Value>digital</Value>
   </DeliveryAttribute>

   <DeliveryAttribute action="establish" name="shippingChartID">
    <Value>1</Value>
   </DeliveryAttribute>
   
  </Version>
  
 </Product>
EndofXML


    $saveOutput .=<<EOF;
catagory=$FORM{'PRM'}|resId=$resId{$resId}|noteNumber=$noteNumber{$resId}|title=$title{$resId}|date=$date{$resId}|author=$author{$resId}|summary=$summary{$resId}|price=$price{$resId}|pages=$pages{$resId}|docType=$docType{$resId}|toc=$toc{$resId}|keywords=$keywords{$redId}|path=$path{$resId}|fileName=$fileName{$resId}|fileSize=$fileSize{$resId}&&&&&
EOF


    $i++;


    }
    
    $saveOutput =~ s/\n//g;
    $saveOutput =~ s/\t//g;
    $saveOutput =~ s/  / /g;
    $saveOutput =~ s/\&\&\&\&\&/\n/g;
    
    open (OUT, ">>/home/gartner/html/rt/content/dr.csv");
    print OUT $saveOutput;
    close (OUT);

    open (DIS, ">>/home/gartner/html/rt/content/dr_discard.csv");
    print DIS $saveDiscard;
    close (DIS);

    open (XML, ">/home/gartner/html/rt/content/dr.xml");
    
    # add the wrapper catalog part...
    print XML <<EndofXML;
<?xml version="1.0" encoding="ISO-8859-1"?>
<Catalog>

 <CatalogAttribute name="catalogName">
  <Value>Gartner Store</Value>
 </CatalogAttribute> 
 <CatalogAttribute name="author">
  <Value>Peter Mahnke</Value>
 </CatalogAttribute> 
 <CatalogAttribute name="CreateRequestTS">
  <Value>$date</Value>
 </CatalogAttribute> 
 <CatalogAttribute name="catalogID">
  <Value>51105</Value>
  <ValueType>site_id</ValueType>
  <ValueReference>V3</ValueReference>
 </CatalogAttribute> 
 <CatalogAttribute name="Destination">
  <Value>Live</Value>
 </CatalogAttribute> 

EndofXML
    print XML $xml;
    print XML "\n</Catalog>\n";
    close (XML);


    $outputFilename = "RCoutput_".time().".xls";

    $getGARTNERmsg =~ s/</\&lt\;/g;
    $msg =~ s/</\&lt\;/g;
    
    print <<EndofHTML;
Content-Type: text/html

<html>
<head>
  <title>DR Output Test - $resId</title>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
  <link href="http://intl.gartner.com/css/dr.css" rel="stylesheet" type="text/css">
</head>
<body>

 <h1>Research Collection Search Results</h1>

<p> Found $count records</p>
<p> Processed $processedCount records</p>
<p> No price: $countNoprice </p>
<p> No DocType: $countNodoctype </p>
<p> Discarded already: $countDiscard </p>
<p>$FORM{keywords}</p>
<p>$date</p>
<h2>messages</h2>
<p>getGARTNERmsg</p>
<p>$msg</p>
<p>getNODOCmsg</p>
<p>$uriMsg</p>

<table>
listing
</table>

<h2>search layouts</h2>

$searchLayout


<h2>package layouts</h2>
$packageLayout


<h2>detail layouts</h2>
$detailLayout

</body>
</html>
EndofHTML






}

##################################################################################
sub readDB {

	local $line = `grep $_[0] /home/gartner/html/rt/content/dr.csv`;

	return(0) if (!$line);

	# catagory=$FORM{'PRM'}|resid=$resId{$resId}|notenumber=$noteNumber{$resId}|title=$title{$resId}|date=$date{$resId}|author=$author{$resId}|summary=$summary{$resId}|price=$price{$resId}|pages=$pages{$resId}|type=$docType{$resId}|toc=$toc{$resId}\n

	local @pairs = split (/\|/, $line);
	foreach (@pairs) {
		local ($name, $value) = split(/\=/);
		$$name{$_[0]} = $value;
	}

	return(1);

}


##################################################################################
sub readDiscard {

	local $line = `grep $_[0] /home/gartner/html/rt/content/dr_discard.csv`;

	return(0) if (!$line);
	return(1);

}


##################################################################################
sub fakeTOC {

    # need to put in static table of contents for MQ, HC and VR

    $fakeToc{'Hype Cycle'} =<<EOF;

  <div class="toc">
   <p>What are the 5 phases of a Hype Cycle?</p>
    <ul>
      <li>Technology Trigger</li>
      <ul>
        <li>The first phase of a Hype Cycle is the "technology trigger" or breakthrough, product launch or other event that generates significant press and interest.</li>
      </ul>

      <li>Peak of Inflated Expectations</li>
      <ul>
        <li>In the next phase, a frenzy of publicity typically generates over-enthusiasm and unrealistic expectations. There may be some successful applications of a technology, but there are typically more failures.</li>
      </ul>

      <li>Trough of Disillusionment</li>
      <ul>
        <li>Technologies enter the "trough of disillusionment" because they fail to meet expectations and quickly become unfashionable. Consequently, the press usually abandons the topic and the technology.</li>
      </ul>

      <li>Slope of Enlightenment</li>
      <ul>
        <li>Although the press may have stopped covering the technology, some businesses continue through the "slope of enlightenment" and experiment to understand the benefits and practical application of the technology.</li>
      </ul>

      <li>Plateau of Productivity</li>
      <ul>
        <li>A technology reaches the "plateau of productivity" as the benefits of it become widely demonstrated and accepted. The technology becomes increasingly stable and evolves in second and third generations. The final height of the plateau varies according to whether the technology is broadly applicable or benefits only a niche market.</li>
      </ul>
    </ul>

  </div>
EOF 


    $fakeToc{'Magic Quadrant'} =<<EOF;

  <div class="toc">
    <p>Typical Table of Contents </p>
    <ul>
	<li>Market Overview &amp; Trends</li>

      <li>Magic Quadrant Criteria</li>

      <ul>
         <li>Leaders</li>
           <ul>
             <li><i>Vendors in the Leaders segment are most likely to have high revenue in this market, high market share and products that are of interest to a wide audience.</i></li>
           </ul>

         <li>Challengers</li>
           <ul>
             <li><i>Challengers have focused significant resources on this market, but they have a narrower understanding of the market and a less-impressive product strategy, or they have deliberately chosen to limit the scope of their product lines.</i></li>
           </ul>

         <li>Visionaries</li>
           <ul>
             <li><i>Visionaries understand the market and customer requirements well, but have fewer assets committed to the pursuit of this particular market than the leaders.</i></li>
           </ul>

         <li>Niche Players</li>
           <ul>
             <li><i>Niche Players are limited to a particular geographical or industry segment, or have a smaller range of features or resources that, taken together, preclude them from competing across the board in many major segments of the integration market.</i></li>
           </ul>
       </ul>
    </ul>
</div>

EOF

    $fakeToc{'Vendor Rating'} =<<EOF;

  <div class="toc">
   <p>Vendor Rating Coverage Catagories</p>
   <ul>
     <li>Corporate Viability
     <ul>
       <li>Strategy </li>
       <li>Financial</li>
       <li>Marketing </li>
       <li>Organization </li>
     </ul>
     </li>
     <li>Product/Services/Technologies
     <ul>
       <li>Product/Service </li>
       <li>Technology </li>
       <li>Pricing </li>
     </ul>
     </li>
     <li>Customer Service/Product Support
       <ul>
         <li>Sales/Distribution</li>
         <li>Support Services</li>
       </ul>
       </li>
     </ul>
     
     <p>Ratings Definitions</p>
     <ul>
       <li>Strong positive
       <ul>
         <li><i>Proves itself as a solid provider of strategic products, services or solutions. Gartner advises IT users to continue investing in that vendor&#8217;s products and solutions; potential users of the vendor&#8217;s products and technology should consider this vendor a strong strategic choice. For investors, the vendor represents a low-risk investment opportunity, from a technology standpoint.</i></li>
       </ul>
       </li>
       <li>Positive
       <ul>
         <li><i>Demonstrates strength in specific areas, but is largely opportunistic. Gartner advises IT users to continue incremental investments; potential users of the vendor&#8217;s products and technology should put this vendor on a shortlist of tactical alternatives. Investors should consider the opportunity as short-term, focusing on exit scenarios.</i></li>
       </ul>
       </li>
       <li>Promising
       <ul>
         <li><i>Shows potential in specific areas; however, the initiative or vendor has not fully evolved or matured. Gartner cautions users to watch for a change in status and consider scenarios for short- and long-term impact; potential users of the vendor&#8217;s products and technology should plan for, and be aware of, issues and opportunities that are related to the evolution and maturity of this initiative or vendor. For investors, this represents niche opportunities or medium- or high-risk investments.</i></li>
       </ul>
       </li>
       <li>Caution
       <ul>
         <li><i>Faces challenges in one or more areas. Gartner advises IT users to understand challenges in relevant areas and assess short- and long-term benefits and risks to determine if contingency plans are needed. Potential users of the vendor&#8217;s products and technology &#8212; and investors &#8212; should note the vendor&#8217;s challenges as part of due diligence. The vendor faces challenges in one or more areas.</i></li>
       </ul>
       </li>
       <li>Strong negative
       <ul>
         <li><i>Indicates difficulty in responding to problems in multiple areas. Gartner advises users to exit immediately; potential users of the vendor&#8217;s products and technology should consider this vendor only if there are no alternatives. Investors are advised to stay away.</i></li>
       </ul>
       </li>
     </ul>
  </div>

EOF



}

sub catCodes {

    %catTopic = (
		 
		 "IT & Asset Management" => {
		     "Magic Quadrant" => "31033456",
		     "Hype Cycle" => "31033457",
		     "Vendor Rating" => "31033458",
		     "Market Trends and Statistics" => "31033459",
		     "Strategy and Analysis" => "31033460"
		     },
		 
		 
		 "Business Intelligence & KM" => {
		     "Magic Quadrant" => "31033461",
		     "Hype Cycle" => "31033462",
		     "Vendor Rating" => "31033463",
		     "Market Trends and Statistics" => "31033464",
		     "Strategy and Analysis" => "31033465"
		     },
		 
		 "CRM, ERP & Supply Chain" => {
		     "Magic Quadrant" => "31033466",
		     "Hype Cycle" => "31033467",
		     "Vendor Rating" => "31033468",
		     "Market Trends and Statistics" => "31033469",
		     "Strategy and Analysis" => "31033470"
		     },
		 );
    

    %catType = (
		
		"Magic Quadrant" => {
		    "IT & Asset Management" => "31033471",
		    "Business Intelligence & Knowledge Management" => "31033472",
		    "CRM, ERP & Supply Chain" => "31033473",
		    "Data Center" => "31033474",
		    "Mobile & Wireless" => "31033475",
		    "Security" => "31033476",
		    "Semiconductors" => "31033477",
		    "Software" => "31033478",
		    "Sourcing" => "31033479",
		    "Telecoms & Networking" => "31033480",
		    "Web Services" => "31033481",
		    "What's Hot" => "31033482",
		    "Most Popular" => "31033483",
		    "Editor's Picks" => "31033484"
		    },
		
		"Hype Cycle" => {
		    "IT & Asset Management" => "31033485",
		    "Business Intelligence & Knowledge Management" => "31033486",
		    "CRM, ERP & Supply Chain" => "31033487",
		    "Data Center" => "31033488",
		    "Mobile & Wireless" => "31033489",
		    "Security" => "31033490",
		    "Semiconductors" => "31033491",
		    "Software" => "31033492",
		    "Sourcing" => "31033493",
		    "Telecoms & Networking" => "31033494",
		    "Web Services" => "31033495",
		    "What's Hot" => "31033496",
		    "Most Popular" => "31033497",
		    "Editor's Picks" => "31033498"
		    },
		
		"Vendor Rating" => {
		    "IT & Asset Management" => "31033499",
		    "Business Intelligence & Knowledge Management" => "31033500",
		    "CRM, ERP & Supply Chain" => "31033501",
		    "Data Center" => "31033502",
		    "Mobile & Wireless" => "31033503",
		    "Security" => "31033504",
		    "Semiconductors" => "31033505",
		    "Software" => "31033506",
		    "Sourcing" => "31033507",
		    "Telecoms & Networking" => "31033508",
		    "Web Services" => "31033509",
		    "What's Hot" => "31033510",
		    "Most Popular" => "31033511",
		    "Editor's Picks" => "31033512"
		    },

		"Market Trends and Statistics" => {
		    "IT & Asset Management" => "31033576",
		    "Business Intelligence & Knowledge Management" => "31033577",
		    "CRM, ERP & Supply Chain" => "31033578",
		    "Data Center" => "31033579",
		    "Mobile & Wireless" => "31033580",
		    "Security" => "31033581",
		    "Semiconductors" => "31033582",
		    "Software" => "31033583",
		    "Sourcing" => "31033584",
		    "Telecoms & Networking" => "31033585",
		    "Web Services" => "31033586",
		    "What's Hot" => "31033587",
		    "Most Popular" => "31033588",
		    "Editor's Picks" => "31033589",
		},
		
		"Strategy and Analysis" => {
		    "IT & Asset Management" => "31033590",
		    "Business Intelligence & Knowledge Management" => "31033591",
		    "CRM, ERP & Supply Chain" => "31033592",
		    "Data Center" => "31033593",
		    "Mobile & Wireless" => "31033594",
		    "Security" => "31033595",
		    "Semiconductors" => "31033596",
		    "Software" => "31033597",
		    "Sourcing" => "31033598",
		    "Telecoms & Networking" => "31033599",
		    "Web Services" => "31033600",
		    "What's Hot" => "31033601",
		    "Most Popular" => "31033602",
		    "Editor's Picks" => "31033603",
		},
		);
    
    
    %imageProd = (
		  "Magic Quadrant" => "prod_mq.jpg",
		  "Hype Cycle" => "prod_hc.jpg",
		  "Vendor Ratings" => "prod_vr.jpg",
		  "Market Trends and Statistics" => "prod_dq.jpg",
		  "Strategy and Analysis" => "prod_ras.jpg",
		  );
    %imageThumb = (
		   "Magic Quadrant" => "thumb_mq.jpg",
		   "Hype Cycle" => "thumb_hc.jpg",
		   "Vendor Ratings" => "thumb_vr.jpg",
		   "Market Trends and Statistics" => "thumb_dq.jpg",
		   "Strategy and Analysis" => "thumb_ras.jpg",
		   );

}
