#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.0/';

# Variables
$outputDir = "/home/gartner/html/staging/research/firsttakes/raw/";


##############################################################
# Get the input from the HTML Form
$buffer = $ENV{'QUERY_STRING'};

# Split the name - value pairs
if ($buffer) {		  # assumes that form has been filled out
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);

	$value =~ s/\+/ /g; # spaces
	$value =~ s/\&lt\;/\</g; # less thans
	$value =~ s/\&amp\;/\&/g; # ampersans
	$value =~ s/%(..)/pack("c",hex($1))/ge; # rest

	$FORM{$name} = $value;
    }

}

# javascript:openDoc('DisplayDocument?id=329268&acsFlg=accessBought')

$URL = "http:\/\/www.gartner.com\/Search\?target\=search\&op\=1\&keywords\=$FORM{'keywords'}";

&GetPage($URL);
exit;

sub GetPage {
 
    &Connection($_[0]);

    &parsePage;

    if ($pageOneFlag) {
	# get other pages
	
	foreach $URL (@URLS) {
	    $URL = "http:\/\/www.gartner.com\/Search\?".$URL;
	    $msg .= "getting page $URL<p\>";
	    &Connection($URL);
	    # $msg .= $Output;
	    &parsePage;
	}
    }

#    &saveIncludes;

    &printPage;

}

sub parsePage {


    @output = split (/\n/, $Output);
    foreach (@output) {

	
	# ADDITIONAL PAGES
	# if (!$pageOneFlag && /Search\?(.[^\"\>]*)\"\>/g) {
	if (!$pageOneFlag && /Search\?/) {

	    @rawURLS = split (/<\/a\> <a href\=\"/);
	    foreach $rawURL (@rawURLS) {
		push @URLS, $1 if  ($rawURL =~ /Search\?(.[^\"\>]*)\"\>/);
		$msg .= "NEXT PAGE $1 FROM <p\>\n\n";
	    }
    
	    $pageOneFlag = 1;
	}
	
	# TITLE
	 if (/resultTitle\"\><a.*\"\>(.*[^<\/a\>])<\/a\>/i) {
	    push @title, $1;
	    $title = $1;
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



sub Connection {

	 # Create a user agent object
	 use LWP::UserAgent;
	 use HTTP::Cookies;

	 my $ua = new LWP::UserAgent;


	 # $ua->agent("Mozilla/5.0");
	 $ua->agent("$ENV{'HTTP_USER_AGENT'}");

	 # Cookies
	 $cookie = new HTTP::Cookies( ignore_discard => 1 ) if (!$pageOneFlag);
	 $ua->cookie_jar($cookie);

	 # Create a request
	 my $req = new HTTP::Request('GET', $_[0]);

	 # authentication
	 # $req->authorization_basic('connected', 'world');

	 # Pass request to user agent and get response
	 my $res = $ua->request($req);

	 # get cookies from response
	 $cookie->extract_cookies($req);

	 $Output = $res->content;

	 # Check output
	 if ($res->is_success) {
	     return($Output);
	 } else {
	     return($Output, $_[0]); # return error info and url attempted
	 }


       }			# end of sub Connection



1; 			    # return true





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
$title
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
<hr size=1>

<font class=keywords>

Search Results for: $FORM{keywords}

</font>
<p>
<table>
$listing
</table>


</body>
</html>

EndofHTML

}



