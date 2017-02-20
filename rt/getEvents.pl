#!/usr/local/bin/perl

# getEvents.pl has a differnt way to handle authors.... than getNODocument.pl

require ("/home/gartner/cgi-bin/gNOlogin.pl");


################################################
sub getEventsDetail {

    # Variables
    local $text = "";
    local $Output = "";
    
    # action
    $page = $_[0];
    $page = "http:\/\/www4.gartner.com\/Events\?pageName\=calendar\&previous\=false\&cboMonth\=0\&cboType\=5\&cboRegion\=4" if (!$page);
    &parseEventsDetailPage(&getGARTNERpage($_[0]));
    $nextPage = $_[0]."\&btnEvents\=Next";
    &parseEventsDetailPage(&getGARTNERpage($nextPage));
    return (%event);
    
}

################################################
sub parseEventsDetailPage {
    

    local @output = split (/\n/, $_[0]);
    
    local () = "";
    
    foreach (@output) {

	$startLookingFlag = 1 if (/All Events/);
	next if (!$startLookingFlag);


	if (/<a href\=\"(.[^\"]*)\"(.[^\>]*)\>(.[^\<]*)\</i) {

	    # HREF
	    $href = $1; 

	    # TITLE
	    $title = $3;

	}

	if (/tr height\=\"22\"\>/) {
	    $eventDetailFlag = 1;
	    next;
	}

	if ($eventDetailFlag == 1 || $eventDetailFlag == 3 || $eventDetailFlag == 4 || $eventDetailFlag == 5) {
	    # skip these lines
	    $eventDetailFlag++;
	    next;
	} 

	if ($eventDetailFlag == 2) {
	    $eventDetailFlag++;
	    $date = $1 if (/\> (.[^\&]*)\&/);
	    next;
	} 

	if ($eventDetailFlag == 6) {
	    $location = $1 if (/\> (.[^\&]*)\&/);
	    &processEvent($title, $href, $date, $location);
	    $title, $href, $date, $location = "";
	    $eventDetailFlag = 0;
	    next;
	} 


    }
}

sub processEvent {

    local ($d, $m, $y) = split(/ /, $_[2]);

#    $d =~ s/^0//;

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

    if ($locale eq "italia") {
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
	# Januar", "Februar", "M&amp;auml;rz", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"
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
#       commented out 14 feb 2003 on request from jay 
#	$mn{'January'} = "Jan";
#	$mn{'February'} = "Feb";
#	$mn{'March'} = "Mar";
#	$mn{'April'} = "Apr";
#	$mn{'May'} = "May";
#	$mn{'June'} = "Jun";
#	$mn{'July'} = "Jul";
#	$mn{'August'} = "Aug";
#	$mn{'September'} = "Sep";
#	$mn{'October'} = "Oct";
#	$mn{'November'} = "Nov";
#	$mn{'December'} = "Dec";

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
    # as of 4 Sept 2003 - new date formate.. no 0, no year
    #$d = "0"."$d" if ($d < 10);
    if ($d < 10) {
	$dO = "0"."$d";
    } else {
	$dO = $d;
    }
    $key = "$y"."$m{$m}"."$dO"."$_[0]"."$_[3]";
    $key =~ tr/[a-z]/[A-Z]/;

    # $title, $href, $date, $location
    if ($locale eq "de") {
	$event{$key} = "$_[0]\t$d\. $mn{$m} $y\t$_[1]\t$_[3]";
    } else {
	$event{$key} = "$_[0]\t$d $mn{$m} $y\t$_[1]\t$_[3]";
    }
}

1; # return true




