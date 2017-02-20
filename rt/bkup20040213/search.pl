#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/cgi-bin/glogin.pl");


# Variables
$outputDir = "/home/gartner/html/rt/raw/";
$server = "www4";

##############################################################
# Get the input from the HTML Form
read(STDIN,$buffer,$ENV{CONTENT_LENGTH});

$FORM{keywords} = $1 if ($buffer =~ /keywords\=(.[^\&]*)\&/);

# keywords=crm&simple1=1&month1=0&year1=1995&month2=9&year2=2002&doc0=0&doc1=1&doc2=1&doc3=1&resultsPerSearch=200&resultsPerPage=25&type5=4&topic0=0&topic1=0&topic2=1&topic3=2&topic4=3&topic5=4&topic6=5&topic7=6&topic8=7&geography0=0&geography5=0&geography3=1&geography4=2&geography2=3&geography1=4&industry0=0&industry1=0&industry2=1&industry3=2&industry4=3&industry5=4&industry6=5&industry7=6&industry8=7&industry9=8&industry10=9&industry11=10&industry12=11&industry13=12&industry14=13&industry15=14&industry16=15&industry17=16&industry18=17&industry19=18&op=2&startMonthDefault=0&startYearDefault=1995&endMonthDefault=9&endYearDefault=2002&industrySize=19&topicSize=8&folderTypeSize=10&geographySize=5&simple1= 


$URL = "http:\/\/$server.gartner.com\/Search";

&GetPage($URL);
exit;

sub GetPage {
 
    $Page = &getGARTNERpage("$_[0]\?$buffer", $server);

    &parsePage;

    # added ! below to force only 1 page

    if (!$pageOneFlag) {
	# get other pages
	
	foreach $URL (@URLS) {
	    $URL = "http:\/\/www4.gartner.com\/Search\?".$URL;
	    $msg .= "getting page $URL<p\>";
	    $Page = &getGARTNERpage("$URL", $server);
	    &parsePage;
	}
    }

#    &saveIncludes;

    &printPage;

}


###########################################################
sub parsePage {


    @output = split (/\n/, $Page);
    foreach (@output) {

	
	# ADDITIONAL PAGES
	# if (!$pageOneFlag && /Search\?(.[^\"\>]*)\"\>/g) {
	if (!$pageOneFlag && /Search\?/) {
	    
	    @rawURLS = split (/<\/a\> <a href\=\"/);
	    foreach $rawURL (@rawURLS) {
		push @URLS, $1 if  ($rawURL =~ /Search\?(.[^\"\>]*)\"\>/);
		$msg .= "FOUND ADDITIONAL RESULTS PAGE $1<p\>\n\n";
	    }
    
	    $pageOneFlag = 1;
	}
	
	# TITLE
	 if (/resultTitle\"\><a .*\"\>(.*)<\/a\>/i) {

	    $title = $1;
	    push @title, $title;

	}

	# DATE
	$date{$title} = $1 if (/<td class\=\"resultDate\" width\=\"30\%\"\>(.*)/);
	
	# DOC TYPE
	$doctype{$title} = $1 if (/<td class\=\"resultFolder\" width\=\"70\%\"\><img src.*\"\>(.*)/);

	# AUTHOR
	if (/<a href\=\"javascript:openBio/) {
	    
	    @rawAUTHORS = split (/<\/a\>\&nbsp\;/);
	    foreach $rawAUTHOR (@rawAUTHORS) {
		$author{$title} .= " $1," if ($rawAUTHOR =~ /\)\"\>(.[^<]*)/);
	    }
	}
	# SUMMARY
	$summary{$title} = $1 if (/<span class\=\"resultSummary\"\>(.*[^<\/span\>])<\/span\>/);
	
	# URL
	# <span class="resultTitle"><a class="resultTitleLink" href="javascript:openDoc('DisplayDocument?id=352970&acsFlg=accessBought','_blank')">CRM Service Providers 2002: Americas Magic Quadrant</a></span><br>

	$searchURL{$title} = $1 if (/<a class\=\"resultTitleLink\" href\=\"javascript:openDoc\(\'(Display.*[^\&acsFlg\=])\&acsFlg\=/);
				    
    }

}




sub printPage {

    local $i = 1;
    foreach $title (@title) {

	chop ($author{$title}); # remove last comma

	$listing .= <<EndofText;

<tr>
 <td class=number align=middle valign=top rowspan=4>
<font class=number>$i</font>
 </td>
 <td class=title>
<b>
<font class=title>
    $title <a href=http://www4.gartner.com/$searchURL{$title}&&acsFlg=accessBought>link</a>
</font>
 </td>
</tr>

<tr>
 <td>
<font class=date>
$date{$title}
</font>
 </td>
</tr>

<tr>
 <td>
<font class=author>
By $author{$title} - $doctype{$title}
</font>
 </td>
</tr>

<tr>
 <td>
<font class=summary>
$summary{$title}
</font>
 </td>
</tr>

<tr><td></td><td></td></tr>


EndofText

	$i++;
    }

    print <<EndofHTML;
Content-type: text/html

<html>
 <head>
  <link REL="STYLESHEET" TYPE="text/css" HREF="/SearchResultsDefault.css"> 
  <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
  <META HTTP-EQUIV="Content-Language" CONTENT="en-uk">
  <title>GARTNER - SEARCH RESULTS FOR: $FORM{keywords} </title>
 </head>
 <body>
<font>
<img src=/img/logo_gartner.gif><p>

<font class=keywords>

    Search Results for: <i> $FORM{keywords} </i> - $buffer

<hr size=1>

</font>
<p>
<table>
$listing
</table>

</body>
</html>

EndofHTML

}



