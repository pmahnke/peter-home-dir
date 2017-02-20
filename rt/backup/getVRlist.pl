#!/usr/local/bin/perl

require ("/home/gartner/cgi-bin/glogin_regionals.pl");

# VRs
$URL = "http://regionals4.gartner.com/1_researchanalysis/vendor_rating/vr_main.html";
&getList;
&save('VR', $output);
undef $output;


print "\n\nDone.\n\n";

exit;

##########################################################
sub save {

    $file = "/home/gartner/html/rt/content/$_[0]"."\.csv";
    open (FILE, ">$file") || die "Can't open file: $file\n\n";
    print FILE $_[1];
    close (FILE);

    return;

}

##########################################################
sub getList {

    
    $msg .=  "\nurlIncl: GETTING URL $URL\n";
    
    local $document = &getGARTNERpage($URL, $ARGV[1]);
    
    
    undef local $link;
    undef local $title;
    undef local $date;
	
    
    #process document
    local @doc = split (/\n/, $document); # split on newlines
       
#                         <td class="smallText"><A href="/1_researchanalysis/vendor_rating/vr_bearingpoint.jsp" class="linkTextBold">BearingPoint</A></td>
#                         <td class="smallText" align="right" nowrap><b>24 Nov 2003</b></td>
 
    foreach (@doc) {
	
	$start = 1 if (/newvendors/);
	next if (!$start);
    
	if (/vendor_rating\/(.[^\"]*)\" class\=\"linkTextBold\"\>(.[^<]*)</) {
	    print "found at $_\n   title $2    link  $1\n";
	    $link  = $1;
	    $title = $2;
	}
	
	if (/class\=\"smallText\" align\=\"right\" nowrap\><b\>(\d.[^<\/]*)<\//) {
	    $date = $1;
	    print "   date  $1\n\n";

	    $output .= "$link\t$date\t$title\n";

            undef $link;
	    undef $title;
	    undef $date;
	}

    }
}

1;
