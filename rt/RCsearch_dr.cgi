#!/usr/local/bin/perl

# RCsearch.cgi
#
#  search results to allow regional sites to creat content includes
#  for LATEST NEWS and FEATURED RESEARCH area

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/cgi-bin/gNOlogin2.pl");
require ("/home/gartner/html/rt/getNODocument3.pl");

use Carp;
no Carp::Assert;



# Variables
$server = "www4";
local $pageOneFlag = "";
local $URL = "http:\/\/$server.gartner.com\/Search";

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
	carp "GETTING NN $count: http:\/\/www4.gartner.com\/$_[0]\&ref\=g_search\n";

	local ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price, $pages, $docType, $contentType, $folderType) = "";

	($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price, $pages, $docType, $contentType, $folderType) = &getResearchDetail($FORM{'URL'});

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

	$docType = $contentType if ($contentType =~ /(Hype|Magic|Vendor Rating)/);

	# clean up docTypes based on drFind.cgi
	#$docType = "Market Trends and Statistics"
	#    if ($docType =~ /(Market|Dataquest|Focus Report|User Wants|Telebriefing)/);
	#$docType = "Strategy and Analysis"
	#    if ($docType =~ /(Research Note|Strategic Analysis Report)/);



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

	$saveOutput .=<<EOF;
catagory=$FORM{'PRM'}|resId=$resId{$resId}|noteNumber=$noteNumber{$resId}|title=$title{$resId}|date=$date{$resId}|author=$author{$resId}|summary=$summary{$resId}|price=$price{$resId}|pages=$pages{$resId}|docType=$docType{$resId}|toc=$toc{$resId}&&&&&
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


    chop ($date = `date '+%d %b %Y'`);
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
