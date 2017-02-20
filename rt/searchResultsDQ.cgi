#!/usr/local/bin/perl

# searchResultsDQ.cgi
#  
#  search results to allow regional sites to creat content includes
#  for LATEST NEWS and FEATURED RESEARCH area

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/cgi-bin/gNOlogin.pl");
require ("/home/gartner/html/rt/getNODocument.pl");

# Variables
$server = "www4";

##############################################################
# Get the input from the HTML Form
read(STDIN,$buffer,$ENV{CONTENT_LENGTH});

$FORM{keywords} = $1 if ($buffer =~ /keywords\=(.[^\&]*)\&/);

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

	if (/<a class\=\"resultTitleLink\" href\=\"javascript:openDoc\(\'(Display.*[^\&acsFlg\=])\&acsFlg\=/) {
	    $searchURL = $1;
	    $searchURL{$title} = $searchURL;
	
	    # NOTE NUMBER
	    $noteNumber{$title} = &getNoteNumber($searchURL);
	}
    }

}


sub getNoteNumber {
    
    $FORM{URL} = "http:\/\/www4.gartner.com\/$_[0]\&acsFlg\=accessBought";

    local ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber) = &getResearchDetail($FORM{URL});

    return($noteNumber);

}




sub printPage {

    local $i = 1;
    foreach $title (@title) {

	chop ($author{$title}); # remove last comma

	$listing .= <<EndofText;

<tr>
 <td class=title>
<b>
<font class=title>
[title] <a href=http://www4.gartner.com/$searchURL{$title}&acsFlg=accessBought target=gartner>$title</a>
</font>
 </td>
</tr>

<tr>
 <td>
<font class=date>
[date] $date{$title}
</font>
 </td>
</tr>

<tr>
 <td>
<font class=author>
[author] $author{$title}
</font>
 </td>
</tr>

<tr>
 <td>
<font class=summary>
[abstract] $summary{$title}
</font>
 </td>
</tr>

<tr>
 <td>
<font class=author>
[doctype] $doctype{$title}
</font>
 </td>
</tr>

<tr>
 <td>
<font class=author>
[code] $noteNumber{$title}
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



