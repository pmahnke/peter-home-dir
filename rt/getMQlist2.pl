#!/usr/local/bin/perl

########################################################################
#
#  getMQlist.pl
#
#  written: 1 Dec 2003 by Peter Mahnke
#
#  run from command line, or cron
#
#  script goes and gets all the recent Magic Quadrants and
#  Hype Cycles from their main pages on gartner.com and
#  saves them as a comma separated values (csv) file
#  this data is read in the pickMQHCVR.cgi script
#
#
########################################################################

require ("/home/gartner/cgi-bin/glogin_regionals.pl");


########################################################################
# HCshttp://www.gartner.com/Search?op=1&keywords=%22Magic+Quadrant%22

print "\n\n GETTING MAGIC QUADRANTS \n\n";
$URL  = "http:\/\/www.gartner.com\/Search?keywords\=\%22Magic\+Quadrant\%22\&op\=1";
$URL2 = "http:\/\/www.gartner.com\/Search?op\=73";

&getList;

&save('MQ');


print "\n\n GETTING HYPE CYCLES \n\n";
undef %output;
$URL  = "http:\/\/www.gartner.com\/Search?keywords\=\%22Hype\+Cycle\+for\%22\&op\=1";
$URL2 = "";

&getList;

&save('HC');


print "\n\n GETTING VENDOR RATINGS \n\n";
undef %output;
$URL = "http://www.gartner.com/Search?op\=2&contentType\=10&sort\=73&dir\=70";
#$URL = "http://www.gartner.com/Search?keywords=%20%22vendor%20ratings%22%20%22research%20note%22&sort=73&dir=70";
&getList;

&save('VR');


print "\n\n GETTING COOL VENDORS \n\n";
undef %output;
#$URL = "http://www.gartner.com/Search?op\=2&contentType10\=10&sort\=73&dir\=70";
$URL = "http://www.gartner.com/Search?keywords=%22Cool%20Vendors%20in%22\&op\=1";
&getList;

&save('CV');


print "\n\nDone.\n\n";

exit;

##########################################################
sub save {

    $file = "/home/gartner/html/rt/content/$_[0]"."\.csv";
    open (FILE, ">$file") || die "Can't open file: $file\n\n";
    foreach (sort { $output{$b} <=> $output{$a} } keys %output) {
	print FILE $output{$_};
    }
    close (FILE);

    return;

}

##########################################################
sub getList {


    $msg .=  "\nurlIncl: GETTING URL $URL\n";

	# get it twice... just ignor the first one... you need to do this to get the date order right...
	my $document = &getGARTNERpage($URL, 'www.');
       $document = &getGARTNERpage($URL2, 'www.') if ($URL2);

    # print $getGARTNERmsg;
	# print $getNOdocmsg;

    undef local $link;
    undef local $title;
    undef local $date;


    #process document
    local @doc = split (/\n/, $document); # split on newlines

    foreach (@doc) {
#print $_;
		s///g;
		$c++;
		#print "$c $_ \n\n" if ( /DisplayDocument\?ref\=g_search\&id\=(\d\d\d\d\d\d)\',\'_blank\'\)\" class\=\"resultTitleLink\"\>/ );


		$start = 1 if (/DisplayDocument/);
		next if (!$start);
#             DisplayDocument\?ref\=g_search\&id\=(\d\d\d\d\d\d)\',\'_blank\'\)\" class\=\"resultTitleLink\"\>
		if (/DisplayDocument\?ref\=g_search\&id\=(\d\d\d\d\d\d)\',\'_blank\'\)\" class\=\"resultTitleLink\"\>((Magic|Hype|Vendor|Cool)[^<]*)</) {

		    # print "found at $_\n   title $2    link  $1\n";
		    $link  = $1;
		    $title = $2;
		}

		if (/<td class\=\"entry2\"\>(\d.*)/) {

			# last thing is the date

		    $date = $1;
		    $date = &processDateYYYYMMDD($date);

		    #print "   date  $date\n\n";

		    if (!$dedupe{$link}) {

		    	$output{$date} .= "$link\t$date\t$title\n";
		    	print "$date\t$title\n";

		    }

		    $dedupe{$link} = "$title\n"; # make sure we don't have the same one again.

    	    undef $link;
		    undef $title;
		    undef $date;
		}

    }
    print "found $c records \n";
}


sub processDateYYYYMMDD {

    local ($d, $m, $y) = split(/ /, $_[0]);


    $m{'January'} = "01";
    $m{'February'} = "02";
    $m{'March'} = "03";
    $m{'April'} = "04";
    $m{'May'} = "05";
    $m{'June'} = "06";
    $m{'July'} = "07";
    $m{'August'} = "08";
    $m{'September'} = "09";
    $m{'October'} = "10";
    $m{'November'} = "11";
    $m{'December'} = "12";

    if ($d < 10) {
	$dO = "0"."$d";
    } else {
	$dO = $d;
    }
    local $key = "$y"."$m{$m}"."$dO";

    return($key);

}

sub processDate {

    local ($d, $m, $y) = split(/ /, $_[0]);


    $m{'January'} = "01";
    $m{'February'} = "02";
    $m{'March'} = "03";
    $m{'April'} = "04";
    $m{'May'} = "05";
    $m{'June'} = "06";
    $m{'July'} = "07";
    $m{'August'} = "08";
    $m{'September'} = "09";
    $m{'October'} = "10";
    $m{'November'} = "11";
    $m{'December'} = "12";

    if ($locale eq "it") {
        $mn{'January'} = "gennaio";
        $mn{'February'} = "febbraio";
        $mn{'March'} = "marzo";
        $mn{'April'} = "aprile";
        $mn{'May'} = "maggio";
        $mn{'June'} = "giugno";
        $mn{'July'} = "luglio";
        $mn{'August'} = "agosto";
        $mn{'September'} = "settembre";
        $mn{'October'} = "ottobre";
        $mn{'November'} = "novembre";
        $mn{'December'} = "dicembre";
    } elsif ($locale eq "de") {
        $mn{'January'} = "Januar";
        $mn{'February'} = "Februar";
        $mn{'March'} = "M&amp;auml;rz";
        $mn{'April'} = "April";
        $mn{'May'} = "Mai";
        $mn{'June'} = "Juni";
        $mn{'July'} = "Juli";
        $mn{'August'} = "August";
        $mn{'September'} = "September";
        $mn{'October'} = "Oktober";
        $mn{'November'} = "November";
        $mn{'December'} = "Dezember";
    } else {
	$mn{'January'} = "January";
	$mn{'February'} = "February";
	$mn{'March'} = "March";
	$mn{'April'} = "April";
	$mn{'May'} = "May";
	$mn{'June'} = "June";
	$mn{'July'} = "July";
	$mn{'August'} = "August";
	$mn{'September'} = "September";
	$mn{'October'} = "October";
	$mn{'November'} = "November";
	$mn{'December'} = "December";

    }
   if ($d < 10) {
	$dO = "0"."$d";
    } else {
	$dO = $d;
    }
    local $key = "$y"."$m{$m}"."$dO";

    local $newdate;

    if ($locale eq "de") {
	$newdate = "$d\. $mn{$m} $y";
    } else {
	$newdate = "$d $mn{$m} $y";
    }

    return($newdate);

}

1;
