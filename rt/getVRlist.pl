#!/usr/local/bin/perl

########################################################################
#
#  getVRlist.pl
#
#  written: 1 Dec 2003 by Peter Mahnke
#
#  run from command line, or cron
#
#  script goes and gets all the recent Vendor Ratings and
#  updates from their main pages on gartner.com and 
#  saves them as a comma separated values (csv) file
#  this data is read in the pickMQHCVR.cgi script
#
#
########################################################################


require ("/home/gartner/cgi-bin/glogin_regionals.pl");

########################################################################
# VRs
#$URL = "http://www.gartner.com/1_researchanalysis/vendor_rating/vr_main.html";
$URL = "http://www.gartner.com/Search?op\=2&contentType10\=10&sort\=73&dir\=70";
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

	print "looking at $_\n";

	$start = 1 if (/newvendors/);
	next if (!$start);
	s/\&nbsp\;/ /g;

	if (/vendor_rating\/(.[^\"]*)\" class\=\"linkTextBold\"\>(.[^<]*)</) {
	    print "found at $_\n   title $2    link  $1\n";
	    $link  = $1;
	    $title = $2;
	}

	if (/class\=\"smallText\" align\=\"right\" nowrap\><b\>(\d.[^<\/]*)<\//
	 || /class\=\"smallText\" align\=\"right\"\><b\>(\d.[^<\/]*)<\//) {
	    $date = $1;
	    $date = &processDateYYYYMMDD($date);
	    print "date \|$1\|\n\n";

	    $output .= "$link\t$date\t$title\n";

            undef $link;
	    undef $title;
	    undef $date;
	}

    }
}

sub processDateYYYYMMDD {

    local ($d, $m, $y) = split(/ /, $_[0]);

    $m = "Oct" if ($m eq "0ct"); # wierd use of a zero

    $m{'Jan'} = "01";
    $m{'Feb'} = "02";
    $m{'Mar'} = "03";
    $m{'Apr'} = "04";
    $m{'May'} = "05";
    $m{'Jun'} = "06";
    $m{'Jul'} = "07";
    $m{'Aug'} = "08";
    $m{'Sep'} = "09";
    $m{'Oct'} = "10";
    $m{'Nov'} = "11";
    $m{'Dec'} = "12";

    if ($d < 10) {
	$dO = "0"."$d";
    } else {
	$dO = $d;
    }
    local $key = "$y"."$m{$m}"."$dO";

    return($key);

}

1;