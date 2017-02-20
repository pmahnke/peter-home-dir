#!/usr/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.0/';
require ("/home/gartner/cgi-bin/glogin.pl");

sub getResearch {

    # Variables
    local $text = "";
    local $Output = "";
    
    # action
    $Output = &getGARTNERpage($_[0]);
    &parsePage;
    return ($text);
    
}

################################################
sub parsePage {


    @output = split (/\n/, $Output);

    foreach (@output) {

	# TITLE
	$title = $1 if (/<META NAME\=\"TITLE\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# PUBDATE GGPUBDT
	$pubDate = $1 if (/<META NAME\=\"GGPUBDT\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# SUMMARY
	$summary = $1 if (/<META NAME\=\"GGSUMMARY\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# RESID
	$resId   = $1 if (/<META NAME\=\"GGRESID\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# AUTHOR
	if (/<TD class\=details/i) {

	    $authFlag = 1;
	    next;
	    
	} elsif ($authFlag) {
	    
	    if (/<\/td\>/i) { # look for ending </td>

		$authFlag = 0;
		$auth =~ s/  //g;
		chop($auth);
		chop($auth);
		next;

	    }

	    s/\r//g;
	    
	    # for URL  if (/openBio\(\'\/(AnalystBiography\?authorId\=.*[^<\/A\>])<\/A\>/) {
	    if (/openBio\(\'\/AnalystBiography\?authorId\=.*[^\'\)\"\>]\'\)\"\>(.[^<\/A\>]*)<\/A\>/) {

		# for url	$auth .= "<a href\=http:\/\/www4.gartner.com\/".$1."<\/a\>\n ";
		$auth .= "$1, ";
		
	    }
	    
	    next;
	} 
	

	# BODY
	if (/Begin Body/) {

	    $bodyFlag = 1;
	    next;

	} elsif ($bodyFlag) {
	    
	    if (/class\=\"footer\"/) {
		
		$bodyFlag = 0;
		next;

	    }
	    
	    s/<.[^\>]*\>//g; # remove all HTML tags
	    s/\r//g;   
	    s/\n\n/\n/g;  

	    $body .= $_;
	}
	
    }

    $text .= <<EndofText;
<document id=$resId>
     <title>$title</title>
     <body>
Published on: $pubDate
Written By: $auth
Summary: $summary
Text: $body
      </body>
</doc>

EndofText
    
    
}


1;
