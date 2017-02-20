
#!/usr/local/bin/perl


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
    

    local @output = split (/\n/, $_[0]);
    
    
    local ($title, $pubDate, $summary, $resId, $auth, $authFlag, $body, $bodyFlag, $summaryFlag) = "";
    
    foreach (@output) {

	# TITLE
	$title = $1 if (/<META NAME\=\"TITLE\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# PUBDATE GGPUBDT
	$pubDate = $1 if (/<META NAME\=\"GGPUBDT\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# RESID
	$resId   = $1 if (/<META NAME\=\"GGRESID\" CONTENT\=\"(.[^\"\>]*)\"\>/i);

	# NOTE NUMBER
	$noteNumber = $1 if (/<META NAME\=\"GGNOTENUM\" CONTENT=\"(.[^\"\>]*)\"\>/i);


	# SUMMARY
	# $summary = $1 if (/<META NAME\=\"GGSUMMARY\" CONTENT\=\"(.[^\"\>]*)\"\>/i);
	if (/<META NAME\=\"GGSUMMARY\" CONTENT\=\"(.*)/i || $summaryFlag) {

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
	    
	    if (/openBio\(\'\/(AnalystBiography\?authorId\=.*[^<\/A\>])<\/A\>/) {
		
		$auth .= "<a href\=http:\/\/www.gartner.com\/".$1."<\/a\>\n ";
		# $auth .= "$1, ";
		
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
    
    return ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber);

}

1; # return true




