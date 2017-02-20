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
#	    $msg .= "PAGE RECEIVED $Page<p>\n\n\n";
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




sub savePage {

    open (FILE, ">$_[1]") || die "Can't open for writing: $_[0]\n";
    print FILE $_[0];
    close (FILE);
    return;

}


sub saveIncludes {

    `mkdir $outputDir$fileDate` if (! -e "$outputDir$fileDate");
    $file = "$outputDir"."$fileDate"."/"."$noteNumber";

    &savePage ($title, "$file"."_title.incl");
    &savePage ($pubDate, "$file"."_date.incl");
    &savePage ($auth, "$file"."_author.incl");
    &savePage ($summary, "$file"."_summary.incl");
    &savePage ($event, "$file"."_event.incl");
    &savePage ($take, "$file"."_take.incl");
    &savePage ($sources, "$file"."_sources.incl");
    &savePage($FORM{'page'}, "$file"."_url.incl");
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



