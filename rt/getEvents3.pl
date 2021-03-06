#!/usr/local/bin/perl

#####################################################################
#####################################################################
#
#
#    getEvents3.pl
#
#      written based on a modified getEvent2.pl
#      on 13 April 2005 by Peter Mahnke
#
#      created ahead of 13 Feb 2004 g.com 5.0 release
#      where the worldwide events calendar is going away
#
#      modifications from 26 April 2005 forward
#      26 Apr 2005 by Peter Mahnke
#       - skips all CIO academy events, per Matt Hunter's request
#
#      DESCRIPTION
#      reads flat file listings of events
#      Conf.txt, Teleconf.txt or LocalBriefing.txt in
#      /home/gartner/html/rt/content/
#
#      INPUT:
#       <event type> currently supports:
#       'Conf' (default) or 'Teleconf' or 'LocalBriefing' or 'VisionEvent'
#
#      OUTPUT:
#      returns the hash %event
#
#       - key is in the format     yyyymmdd<event_title><location>
#         this is so that its sortable
#
#       - data is in the format
#         "<event_title>\t<date (formated and translated): d MONTH yyyy>\t
#          <link>\t<location>"
#
#
#####################################################################
#####################################################################



# COMMAND-LINE TEST (COMMENTED OUT)
#if ($ARGV[0]) {
#    &getEventsDetail($ARGV[0]);
#    print "$msg\n\nDone.\n\n";
#    exit;
#}

################################################
sub getEventsDetail {

    # Variables
    local $text   = "";
    local $Output = "";
    local $type   = "Conf";    # default are conferences

    $type = $_[0];

    # action
    &_parseEventsDetailPage($type);
    return (%event);

}

################################################
sub _parseEventsDetailPage {

    local $rootDir = "/home/gartner/html/rt/content";
    local $fileName;
    local $count;

    # open right flat db based on passed type


    if ( $_[0] eq "Symposium") {
    	$fileName = "$rootDir" . "/Conf2.txt";
    	$flagEventType = 1;
    } elsif ( $_[0] eq "Conf") {
    	$fileName = "$rootDir" . "/Conf2.txt";
    	$flagEventType = 2;
    } elsif ( $_[0] eq "VisionEvent" ) {
    	$fileName = "$rootDir" . "/Conf2.txt";
    	$flagEventType = 3;
    } elsif ( $_[0] eq "Teleconf" ) {
    	$fileName = "$rootDir" . "/Teleconf.txt";
    	$flagEventType = 4;
    } elsif ( $_[0] eq "Briefing" ) {
    	$fileName = "$rootDir" . "/Briefings.txt" ;
    	$flagEventType = 5;
    }

    $msg .= "file $fileName\n\n";

    open( FILE, "$fileName" ) || die "Can't open file: $fileName\n\n";

    while (<FILE>) {

        chop();

        s/\"//g; # remove quotes

        ( $resid, $title, $evtType, $date, $href, $location, $endDate ) = split(/\t/);
	$title =~ s/\'//g;
        next if ( $title =~ /Title/ );     # skip header
        next if ( !$title );               # skip events without titles

	next if ($title =~ /CIO Academy/); # skip CIO Academy
	
	# deal with Conf.txt file having both Conferences and Vision Events
	if ($flagEventType == 1) {
	    
	    # symposium/itxpo
	    next if ($evtType !~ /Symposium/);
	    
	} elsif ($flagEventType == 2) {
	    
	    # conferences
	    next if ($evtType ne "Conferences");
	    
	} elsif ($flagEventType == 3) {
	    
	    # conferences
	    next if ($evtType ne "Channel Events");
	    
	}
	
	# change & into html entities
        $href  =~ s/\&/\&amp\;/g;
        $title =~ s/ \& / \&amp\; /g;

        $location = "NA" if ( $flagEventType == 4 ); # teleconferences don't have locations

        &_processEvent( $title, $href, $date, $location, $endDate );

        $msg .= "\n\n\nraw:\t$_\n\tT: $title\n\tH: $href\n\tD: $date\n\tL: $location<br>\n\n";

    }

    close(FILE);

}

######################################################################
sub _processEvent {

    # translate dates into locale standard
    # create key for return hash

    # start date
    local ( $d, $m, $y ) = split( /\//, $_[2] );
    $y = $y + 2000;

    # end date
    local ( $ed, $em, $ey ) = split( /\//, $_[4] );
    $ey = $ey + 2000;

    local $now = `date +%Y%m%d`; # today's date in the same yyyymmdd format
    chop($now);

    local $dkey = "$y$m$d";

    $dO = $d; # keep 0 before dates < 10 for KEY
    $ed0 = $ed0;

    $d =~ s/^0//;    # remove 0 before dates 01...
    $ed =~ s/^0//;    # remove 0 before dates 01...

    return()if ( $dkey < $now ); # don't look at dates that are BEFORE today

    # generic English months
    $m{'January'}   = "01";
    $m{'February'}  = "02";
    $m{'March'}     = "03";
    $m{'April'}     = "04";
    $m{'May'}       = "05";
    $m{'June'}      = "06";
    $m{'July'}      = "07";
    $m{'August'}    = "08";
    $m{'September'} = "09";
    $m{'October'}   = "10";
    $m{'November'}  = "11";
    $m{'December'}  = "12";

    if ( $locale eq "it" ) {

    	# italian months hash

        $mn{'01'} = "gennaio";
        $mn{'02'} = "febbraio";
        $mn{'03'} = "marzo";
        $mn{'04'} = "aprile";
        $mn{'05'} = "maggio";
        $mn{'06'} = "giugno";
        $mn{'07'} = "luglio";
        $mn{'08'} = "agosto";
        $mn{'09'} = "settembre";
        $mn{'10'} = "ottobre";
        $mn{'11'} = "novembre";
        $mn{'12'} = "dicembre";

    } elsif ( $locale eq "de" ) {

    	# german months hash

        $mn{'01'} = "Januar";
        $mn{'02'} = "Februar";
        $mn{'03'} = "M&auml;rz";
        $mn{'04'} = "April";
        $mn{'05'} = "Mai";
        $mn{'06'} = "Juni";
        $mn{'07'} = "Juli";
        $mn{'08'} = "August";
        $mn{'09'} = "September";
        $mn{'10'} = "Oktober";
        $mn{'11'} = "November";
        $mn{'12'} = "Dezember";

    }
    else {

    	# english months hash

        $mn{'01'} = "January";
        $mn{'02'} = "February";
        $mn{'03'} = "March";
        $mn{'04'} = "April";
        $mn{'05'} = "May";
        $mn{'5'} = "May";
        $mn{'06'} = "June";
        $mn{'07'} = "July";
        $mn{'08'} = "August";
        $mn{'09'} = "September";
        $mn{'10'} = "October";
        $mn{'11'} = "November";
        $mn{'12'} = "December";

    }

    # create a unique key based on date and title
    $key = "$y" . "$m" . "$dO" . "$_[0]" . "$_[3]";
    $key =~ tr/[a-z]/[A-Z]/; # make upper case

    $msg .= "\n\nevent key: $key month $m $mn{$m} locale $locale <br>\n\n";



	# deal with spanning date logic

	# is there an end date at all
	if (!$endDate) {

		# yes
		if ( $locale eq "de" ) {
			$dateString = "$d\. $mn{$m} $y";
		} else {
			$dateString = "$d $mn{$m} $y";
		}

	} elsif ($m == $em && $d == $ed)  {

		# is it the same month and day

		# yes
		if ( $locale eq "de" ) {
			$dateString = "$d\. $mn{$m} $y";
		} else {
			$dateString = "$d $mn{$m} $y";
		}

	} elsif ($m == $em) {

		# is it the same month?

		# yes
		if ( $locale eq "de" ) {
			$dateString = "$d\.\-$ed\. $mn{$m} $y";
		} else {
			$dateString = "$d\-$ed $mn{$m} $y";
		}

	} else {

		# no
		if ( $locale eq "de" ) {
			$dateString = "$d\.\&nbsp\;$mn{$m} \- $ed\.\&nbsp\;$mn{$em} $y";
		} else {
			$dateString = "$d\&nbsp\;$mn{$m} \- $ed\&nbsp\;$mn{$em} $y";
		}

	}


	# CREATE HASH
    # $title, $href, $date, $location
    if ( $locale eq "de" ) {

        $event{$key} = "$_[0]\t$dateString\t$_[1]\t$_[3]";

    }
    else {

        $event{$key} = "$_[0]\t$dateString\t$_[1]\t$_[3]";

    }

    $msg .= "event output: $_[0]\t$dateString\t$_[1]\t$_[3]<br>\n\n";
    return();

}

1;    # return true

