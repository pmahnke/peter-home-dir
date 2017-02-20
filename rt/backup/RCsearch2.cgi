#!/usr/local/bin/perl

# RCsearch.cgi
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
 
    $msg .= "Request: $_[0]\?$buffer<p\>Server: $server<p\>";

    $Page = &getGARTNERpage("$_[0]\?$buffer", $server);
    
    $msg .= "getGARTNERmsg: $getGARTNERmsg<p\>";
    $msg .= "Page: $Page";
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

	$date{$title} =~ s/\&nbsp\;/ /gi;

	$listing .= "$title\t$summary{$title}\t$author{$title}\t$date{$title}\t$noteNumber{$title}\n";

	$i++;
    }

    chop ($date = `date '+%d %b %Y'`);
    $outputFilename = "RCoutput_".time().".xls";

    print <<EndofHTML;
Content-type: text/html

messages: $msg<p>
keywords: $FORM{keywords}<p>


EndofHTML

}


sub excel {
    print <<EndofHTML;
Content-Type: bad/type
Content-Disposition: attachment; filename=$outputFilename

Research Collection Search Results

$FORM{keywords}
$date


Title\tAbstract\tAuthors\tDate\tCode

$listing

EndofHTML


}

