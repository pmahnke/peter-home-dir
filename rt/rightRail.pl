#!/usr/local/bin/perl

use CGI_Lite;
require ("/home/gartner/cgi-bin/glogin.pl");
#$website = "http\:\/\/www4.gartner.com\/";
$website = "";
$dbFile = "/home/gartner/html/rt/correspondingFiles.txt";
$saveDir = "/home/gartner/html/rt/rightRail/";

&readDB;
exit;


sub readDB {

    open (FILE, "$dbFile") || die "Can't open: $dbFile\n\n";
    while (<FILE>) {

	chop();

	local ($area, $sarea, $ssarea, $name, $regUrl, $gcomUrl) = split (/\t/);
	
	# skip homepages
	next if ($area eq "HOMEPAGES");
	$count++;

	# get output filename
	$saveFileName = $regUrl;
	$saveFileName =~ s/http:\/\/regionals4.gartner.com\/regionalization\/content\/emea\///;
	$saveFileName =~ s/http:\/\/regionals.gartner.com\/emea\///;
	print "$count\t$saveFileName\t\@\t";
	next if ($saveFileName eq "NA");

	# get input file name
	$FORM{url} = $gcomUrl;
        $FORM{url} =~ s/http:\/\/www4.gartner.com//; # remove start 
	print "$FORM{url}\n";
	next if ($FORM{url} eq "NA");
	
	$f = index ($FORM{'url'}, "/", 0);
	$l = rindex ($FORM{'url'}, "/");
	$length = $l - $f + 1;
	$relPath = substr ($FORM{'url'}, $f, $length);

	undef $newDocument;
	&getDocument;
	&saveOutput;
	    
    }

    close(FILE);
}

sub saveOutput {

    return if (!$newDocument);
    
    $saveFileName = "$saveDir"."$saveFileName";

    open (OUT, ">$saveFileName") || die "Can't save: $saveFileName\n";
    print OUT "<table cellpadding\=\"0\" cellspacing\=\"0\" border\=\"0\" width\=\"100%\"\>\n" if (!$pageTypeFlag);
    print OUT $newDocument;
    close (OUT);

}

##########################################################
sub getDocument {

    $URL = "$website\/$FORM{url}";
    $URL = "http://www4.gartner.com"."$FORM{url}";
    $msg .=  "\nurlIncl: GETTING URL $URL\n";
    
    local $document = &getGARTNERpage($URL, $ARGV[1]);
    
    #process document
    local @doc = split (/\n/, $document); # split on newlines
    local $inBodyFlag = 0;
    
    foreach (@doc) {
    
	$inBodyFlag = 1 if (/right side gray/);
	
	if (/document.write\(buildSubNav/) {
	    $inBodyFlag = 1;
	    $pageTypeFlag = 1; # non-overview pages
	}
	$inBodyFlag++ if ($inBodyFlag);

	if (/<!-- first right side gray line -->/) {
	    $inBodyFlag = 1;
	    $pageTypeFlag = 0; # overview pages
	    undef $newDocument;
	    undef $prevprevLine;
	    undef $prevLine;
	    next;
	}
	
	if ($pageTypeFlag && /<\/script>/) {
	    undef $newDocument;
	    undef $prevprevLine;
	    undef $prevLine;
	    next;
	}

	next if (!$inBodyFlag);
	next if ($inBodyFlag < 2 && $pageTypeFlag);

	if (/<!-- close TABLE III/i ) { # was <!-- right spacer column -->
	    $newDocument .= "$prevprevLine\n$prevLine\n$`\n";
	    last;
	} 

	if ($pageTypeFlag && /<\/td>/) {
	    $newDocument .= "$prevprevLine\n$prevLine\n$`\n";
	    last;
	}



	# remove comment tags
	################################################
	
	# deal with comments on one line
	if (/<!--.*[^-->]-->/) {
	    #$msg .= "single line comment: $_\n";
	    $_ = "$`$'";
	} elsif (/<!--/) {
	    # look for comment start
	    #$msg .= "comment start:\t$_\n";
	    $commentFlag = 1;
	    $_ = $`;
	    # look for comment end
	    if (/-->/) {
		#$msg .= "comment end:\t$_\n";
		$commentFlag = 0;
		$_ .= $';
	    }
	}

 	# look for comment end
	if (/-->/) {
	    #$msg .= "comment end:\t$_\n";
	    $commentFlag = 0;
	    $_ = $';
	}
	
	# still in a comment
	if ($commentFlag) {
	    #$msg .= "comment:\t$_\n";
	    next;
	}


	$newDocument .= "$prevprevLine\n";

	# fix images
	if (/src\=\"\//i) {
	    # absolute refs
#	    s/(src\=\")\/(.[^\"]*)\"/$1\/$website$2\"/gi;
	} elsif (/src\=\"/i) {
	    # relative refs
#	    s/(src\=\")(.[^\"]*)\"/$1\/$website$relPath$2\"/gi;
	}

	# clean up src="//image issue with src="/
	s/src\=\"\/\//src\=\"\//ig;
	

	# point trans_pixel.gif into local version
	if (/trans_pixel.gif/) {
#	    s/\"\/images\/trans_pixel.gif/\"\/\/img\/trans_pixel.gif/g;
#	    s/\"images\/trans_pixel.gif/\"\/\/img\/trans_pixel.gif/g;
#	    s/\"\/1_researchanalysis\/..\/images\/trans_pixel.gif/\"\/\/img\/trans_pixel.gif/g;
	}
	
	# point new_bullet.gif into local version
	if (/images\/new_bullet.gif/) {
#	    s/\/images\/new_bullet.gif/\/\/img\/new_bullet.gif/g;
#	    s/images\/new_bullet.gif/\/\/img\/new_bullet.gif/g;
	}


	# html
	if ($_ =~ /href\=\"(.[^\"]*)\"(.[^\>]*)\>/i) {
	    
	    $filename     = $1;
	    $rest         = $2;
	    
	    if ($filename =~ /javascript/i || 
		$filename =~ /http:\/\//i) {
		
		$msg .= "urlIncl: ignoring js or http link: $filename\n";
		
		if ($filename !~ /javascript\:void\(null\)/ ) {
		    
		    $_ =~ s/\\'\//\\'$website/;
		    $_ =~ s/(href\=\")/$1$website/g if ($_ !~ /http:\/\//);
		    
		    $_ =~ s/imgdvweb01/www/g; # perhaps not required
		}

	    } elsif ($filename =~ /\#/) {
		
		# index reference to point to same page
		# I think the baseurl on the page screws it up
		$_ =~ s/$filename/javascript\:void\(null\)/;
		$_ =~ s/$rest/ onClick\=\"javascript\:document.location\=\'$filename\'\" $rest/;
		

	    } else {

		$msg .=  "urlIncl: FOUND link $filename\n";
		#$_ =~ s/$filename/$website$filename/;
	    }
	    
	} 

	if ($_ =~ /open(.[^\(]*)\('(.[^']*)'/i) {
	    
	    $filename     = $2;

	    $msg .= "urlIncl: looking at js src issue with Open$1: $filename\n";
		
	    
	    $_ =~ s/'\//'$website/;
	    $_ =~ s/imgdvweb01/www/g; # perhaps not required
	
	}


        $_ =~ s/(this.src\=\')\//$1http:\/\/www.gartner.com/gi; # for mouse overs in strat sourcing page

        $_ =~ s/.com\/\/\//.com\//g; # get rid of triple /// for a single /
        $_ =~ s/.com\/\//.com\//g; # get rid of double // for a single /

	$prevprevLine = $prevLine;
	$prevLine = "$_\n";
	
    }
    
    
}

