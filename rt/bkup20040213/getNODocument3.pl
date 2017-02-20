#!/usr/local/bin/perl

# getNODocument3.pl has a differnt way to handle authors.... than getNODocument.pl

require ("/home/gartner/cgi-bin/gNOlogin.pl");


################################################
sub getResearchDetail {

    # Variables
    local $text = "";
    local $Output = "";
    
    # action
    local @docDetails = &parseResearchDetailPage(&getGARTNERpage($_[0]));
    return (@docDetails);
    
}

################################################
sub parseResearchDetailPage {
    

    #local @output = split (/\n/, $_[0]);
    #foreach (@output) {
	#$tocFlag++ if (/Begin Body/);
	#$tocFlag = 1 if (/begin table of contents/);
	#$toc .= "$_\n" if ($tocFlag == 1);
	#$toc = $1 if (/(<\!\-\- begin table of contents \-\-\>)(.[^<\!\-\- Begin Body \-\-\>]*)<\!\-\- Begin Body \-\-\>/);
    #}

    local @output = split (/\>/, $_[0]);   
    
    local ($title, $pubDate, $summary, $resId, $auth, $authFlag, $body, $bodyFlag, $summaryFlag, $toc) = "";
    
    foreach (@output) {

	$_ .= "\>";

	
	#Table of Contents
	
	# $toc = $1 if (/(<\!\-\- begin table of contents \-\-\>)(.[^<\!\-\- Begin Body \-\-\>]*)<\!\-\- Begin Body \-\-\>/);

	$tocFlag = 0  if (/<TABLE WIDTH\=\"100%\" HEIGHT\=\"1\" CELLSPACING\=\"0\" CELLPADDING\=\"0\" BORDER\=\"0\">/ && $tocFlag);
	$tocFlag = 1 if (/begin table of contents/ || /<table BORDER\=0 CELLSPACING\=0 CELLPADDING\=0 WIDTH\=\"650\" \>/);
	$toc .= "$_\n" if ($tocFlag);

#	$msg .= "$_" if ($tocFlag);


	# PRICE
	$price = $1 if (/US \$ (.[^\.]*)\./);


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
	    chop ($summary);
	}

	$summary = $1 if (/<META NAME\=\"GGSUMMARY\" CONTENT\=\"(.[^\"\>]*)\"\>/i);
	
	
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
		$auth .= " \| " if ($authCount);
		$authFlag = 1;
#		print "\n\nFOUND MULTI LINE AUTHOR NAME $_\n\n";
	    }

	    
	    if (/openBio\(\'\/(AnalystBiography\?authorId\=.*[^<\/A\>])<\/A\>/) {
		
		$auth .= "<a href\=\"javascript:void\(null\)\" class\=\"linkTextSmall\" onclick\=\"openBio\(\'\/".$1."<\/a\>,  ";
		# $auth .= "$1, ";
		
		
	    } elsif (/\'\/AnalystBiography\?authorId\=(.[^\'\)\"\>]*)\'\)\"\>/) {
		
		# multiLine Author
		
		$multiAuthFlag = 1;
		$authCount++;
		
		$auth .= "<a href\=\"javascript:void\(null\)\" class\=\"linkTextSmall\" onclick\=\"openBio\(\'\/AnalystBiography\?authorId\=".$1."\'\)\"\>";
#		print "\n\nFOUND MULTI LINE AUTHOR LINK $1\n\n";
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
	$auth =~ s/ \| $//;
	$auth =~ s/ <\/a\>/<\/a\>/gi;
    }
    
    # clean up toc


    return ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price);

}

1; # return true




