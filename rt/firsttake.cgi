#!/usr/bin/perl

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

&GetPage($FORM{'page'});
exit;

sub GetPage {
 
    &Connection($_[0]);

    &parsePage;

    &saveIncludes;

    &printPage;

}

sub parsePage {


    @output = split (/\n/, $Output);

    foreach (@output) {

	
	# TITLE
	# $title = $1 if (/<title\>([^<\/title\>].*)<\/title\>/i);
	$title = $1 if (/<META NAME\=\"TITLE\" CONTENT\=\"(.[^\"\>]*)\"\>/i);


	# PUBDATE GGPUBDT
	$pubDate = $1 if (/<TD class\=pubDate\>([^<\/td\>].*)<\/td\>/i);
	# (/<META NAME\=\"GGPUBDT\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# author parse
	if (/<TD class\=details\>/i) {
	    $authFlag = 1;
	    next;
	} elsif ($authFlag) {
	    
	    if (/<\/td\>/i) { # look for ending </td>

		$authFlag = 0;

		$auth =~ s/  //g;

		next;
	    }
	    s/\r//g;
	    s/\r//g;
	    $auth .= "$_ ";
	    next;
	} 

	# SUMMARY
	$summary = $1 if (/<META NAME\=\"GGSUMMARY\" CONTENT\=\"(.[^\"\>]*)\"\>/i);


	# EVENT
	if (/<span class\=\"header3\"\>Event\<\/span\>/i) {
	    $eventFlag = 1;
	    next;
	} elsif ($eventFlag) {
	    
	    if (/<span class\=\"header3\"\>First Take\<\/span\>/i) {
		$takeFlag = 1;
		$eventFlag = 0;
		next;
	    }

	    $event .= $_;

	} elsif ($takeFlag) {

	    # remove footnotes to other first takes
	    # EXPERIMENTAL
	    s/\(see [^\"\)].*\"\)/ /;

	    # grab sources
	    if (/<P\><B\>Analytical Sources: <\/B\>([^<\/P\>].*)<\/P\>/i || /<P\><B\>Analytical Sources<\/B\>:([^<\/P\>].*)<\/P\>/i || /<P\><B\>Analytical Source: <\/B\>([^<\/P\>].*)<\/P\>/i || /<P\><B\>Analytical Source<\/B\>:([^<\/P\>].*)<\/P\>/i || /<P\><B\>Analytical Source:<\/B\> ([^<\/P\>].*)<\/P\>/i || /<P\><B\>Analytical Sources:<\/B\> ([^<\/P\>].*)<\/P\>/i) {
		$sources = $1;
		$takeFlag = 0;
		next;
	    }

	    $take .= "$_";
	}

	# NOTE NUMBER
	$noteNumber = $1 if (/<META NAME\=\"GGNOTENUM\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# FILEDate
	$fileDate = $1 if (/<META NAME\=\"GGPUBDT\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

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
	 my $ua = new LWP::UserAgent;
	 $ua->agent("Mozilla/5.0");

	 # Create a request
	 my $req = new HTTP::Request('GET', $_[0]);

	 # authentication
	 $req->authorization_basic('connected', 'world');

	 # Pass request to user agent and get response
	 my $res = $ua->request($req);

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

    print <<EndofHTML;
Content-type: text/html

<html>
 <head>
  <link REL="STYLESHEET" TYPE="text/css" HREF="/FirstTakeDefault.css"> 
  <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
  <META HTTP-EQUIV="Content-Language" CONTENT="en-uk">
  <title>FIRST TAKE TEST</title>
 </head>
 <body>
<font>

<a href="/staging/research/buildPages.cgi">Publish it</a><p>

<table>
<tr>
 <td class=title>
$title
 </td>
</tr>

<tr>
 <td class=pubdate>
$pubDate
 </td>
</tr>


<tr>
 <td class=author>
$auth
 </td>
</tr>


<tr>
 <td class=summary>
<b>SUMMARY</b><br>
$summary
 </td>
</tr>


<tr>
 <td class=event>
<b>EVENT</b>
$event
 </td>
</tr>


<tr>
 <td class=take>
<b>FIRST TAKE</b>
$take
 </td>
</tr>


<tr>
 <td class=sources>
Content Sources: $sources
 </td>
</tr>




</table>
<p>


EndofHTML

}

