#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/cgi-bin/glogin.pl");


sub search {

    # Variables
    $server = "www4";

    &GetPage("http:\/\/$server.gartner.com\/Search\?$_[0]");

    local $i = 0;
    until ($i == 9) {
	$i++;
	
	$realURL = "http:\/\/$server.gartner.com\/".$searchURL{$title[$i]}."\&acsFlg\=accessBought" if ($searchURL{$title[$i]});
	
	push @results, $realURL;
    }
    return(@results);
    
        
}


###########################################################
sub GetPage {
 
    print "getting $_[0]\n\n<p\>";

    $Page = &getGARTNERpage("$_[0]");

#    print "PAGE $Page\n<p\>\n\n";

    &parseSearchResults;

    # added ! below to force only 1 page

    if (!$pageOneFlag) {
	# get other pages
	
	foreach $URL (@URLS) {
	    $URL = "http:\/\/www4.gartner.com\/Search\?".$URL;
	    $msg .= "getting page $URL<p\>";
	    $Page = &getGARTNERpage("$URL", $server);
	    &parseSearchResults;
	}
    }

}


###########################################################
sub parseSearchResults {


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

