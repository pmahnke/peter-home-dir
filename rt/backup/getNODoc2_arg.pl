#!/usr/local/bin/perl

# getNODocument2.pl has a differnt way to handle authors.... than getNODocument.pl

require ("/home/gartner/cgi-bin/gNOlogin.pl");

$link = "http:\/\/www4.gartner.com\/DisplayDocument\?id\="."$ARGV[0]";  # .\&acsFlg\=accessBought";
&getResearchDetail ($link, 'www4');

foreach $detail (@docDetails) {
    print "detail $detail\n";
}

exit;


################################################
sub getResearchDetail {

    # Variables
    local $text = "";
    local $Output = "";
    
    # action
    @docDetails = &parseResearchDetailPage(&getGARTNERpage($_[0]));
    return();
    
}

################################################
sub parseResearchDetailPage {
    

#    local @output = split (/\n/, $_[0]);
    local @output = split (/\>/, $_[0]);
    
    local ($title, $pubDate, $summary, $resId, $auth, $authFlag, $body, $bodyFlag, $summaryFlag) = "";
    
    foreach (@output) {
	
	$_ .= "\>";
#	print "$_\n" if (/<META/);    


	# TITLE
	$title = $1 if (/<META NAME\=\"TITLE\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# PUBDATE GGPUBDT
	$pubDate = $1 if (/<META NAME\=\"GGPUBDT\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# RESID
	$resId   = $1 if (/<META NAME\=\"GGRESID\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# NOTE NUMBER
	$noteNumber = $1 if (/<META NAME\=\"GGNOTENUM\" CONTENT=\"(.[^\"\>]*)\"\>/i);


	# SUMMARY
	if (/GGSUMMARY/) {
	    $summary = $1 if (/CONTENT\=\"(.[^\>]*)\>/);
	    print "got summary $summary from $_\n\n";
	    chop ($summary);
	}
	
	
	if (/<META NAME\=\"GG PRM SUMMARY\" CONTENT\=\"(.*)/i || $summaryFlag) {

	    if (!$summaryFlag) {
		$summary .= $1; 
		$summaryFlag = 1;	    
	    } else {
		$summary .= $_;
	    }
	    
	    if ($summary =~ /\"\>/) {
		
		# there is the end tag
		$summaryFlag = 0;
		$summary =~ s/\"\>//;
		
	    } 
	}    
	
	

	# AUTHOR
	if (/<TD class\=\"authors/i) {

	    $authFlag = 1;
	    next;
	    
	} elsif ($authFlag) {
	    
	    print "Authors: $_\n";

	    if (/<\/td\>/i) { # look for ending </td>

		$authFlag = 0;
		$auth =~ s/  //g;
		chop($auth) if (!$multiAuthFlag);
		next;

	    }

	    s/\r//g;
	    s/\n//g;

	    if ($authFlag == 2) {
		
		# author name on this line
		$auth .= "$_";
		$auth .= " \| " if ($authCount > 1);
		$authFlag = 1;
		print "\n\nFOUND MULTI LINE AUTHOR NAME $_\n\n";
	    }


	    
	    if (/openBio\(\'\/(AnalystBiography\?authorId\=.*[^<\/A\>])<\/A\>/) {
		
		$auth .= "<a href\=\"javascript:void\(null\)\" class\=\"linkTextSmall\" onclick\=\"openBio\(\'\/".$1."<\/a\>,  ";
		# $auth .= "$1, ";
		
	    } elsif (/\'\/AnalystBiography\?authorId\=(.[^\'\)\"\>]*)\'\)\"\>/) {
		
		# multiLine Author

		$multiAuthFlag = 1;
		$authCount++;

		$auth .= "<a href\=\"javascript:void\(null\)\" class\=\"linkTextSmall\" onclick\=\"openBio\(\'\/AnalystBiography\?authorId\=".$1."\'\)\"\>";
		print "\n\nFOUND MULTI LINE AUTHOR LINK $1\n\n";
		$authFlag = 2;
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

    if ($multiAuthFlag) {
	$auth =~ s/$ \| //;
	$auth =~ s/ <\/a\>/<\/a\>/gi;
    }

    return ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber);

}

1; # return true




