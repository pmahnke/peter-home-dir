#!/usr/local/bin/perl

#####################################################################
#####################################################################
#
#
#    getEvents2.pl
#
#      written based on a modified getEvent.pl
#      on 21 Jan 2004 by Peter Mahnke
#
#      created ahead of 13 Feb 2004 g.com 5.0 release
#      where the worldwide events calendar is going away
#
#
#      DESCRIPTION
#      reads flat file listings of events
#      Conf.txt, Teleconf.txt or LocalBriefing.txt in
#      /home/gartner/html/rt/content/
#
#      INPUT:
#       <event type> currently supports:
#       'Conf' (default) or 'Teleconf' or 'LocalBriefing'
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
    $fileName = "$rootDir" . "/Conf.txt"      if ( $_[0] eq "Conf" );
    $fileName = "$rootDir" . "/Teleconf.txt"  if ( $_[0] eq "Teleconf" );
    $fileName = "$rootDir" . "/Briefings.txt" if ( $_[0] eq "Briefing" );

    $msg .= "file $fileName\n\n";

    open( FILE, "$fileName" ) || die "Can't open file: $fileName\n\n";

    while (<FILE>) {

        chop();

        s/\"//g; # remove quotes

        ( $resid, $title, $evtType, $date, $href, $location ) = split(/\t/);

        next if ( $title =~ /Title/ ); # skip header
        next if ( !$title ); # skip events without titles

		# change & into html entities
        $href  =~ s/\&/\&amp\;/g;
        $title =~ s/ \& / \&amp\; /g;

        $location = "NA" if ( $_[0] eq "Teleconf" ); # teleconferences don't have locations

        &_processEvent( $title, $href, $date, $location );

        $msg .=
"\n\n\nraw:\t$_\n\tT: $title\n\tH: $href\n\tD: $date\n\tL: $location<br>\n\n";

    }

    close(FILE);

}

######################################################################
sub _processEvent {

    # translate dates into locale standard
    # create key for return hash
    
    local ( $d, $m, $y ) = split( /\//, $_[2] );

    $y = $y + 2000;

    local $now = `date +%Y%m%d`; # today's date in the same yyyymmdd format
    chop($now);

    local $dkey = "$y$m$d";

    $d =~ s/^0//;    # remove 0 before dates 01...

    next if ( $dkey < $now ); # don't look at dates that are BEFORE today

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

    # as of 4 Sept 2003 - new date format.. no 0, no year
    # $d = "0"."$d" if ($d < 10);
    if ( $d < 10 ) {
        $dO = "0" . "$d";
    } else {
        $dO = $d;
    }
    $key = "$y" . "$m" . "$dO" . "$_[0]" . "$_[3]"; # create a unique key based on date and title
    $key =~ tr/[a-z]/[A-Z]/; # make upper case

    $msg .= "\n\nevent key: $key month $m $mn{$m} locale $locale <br>\n\n";

    # $title, $href, $date, $location
    if ( $locale eq "de" ) {

        $event{$key} = "$_[0]\t$d\. $mn{$m} $y\t$_[1]\t$_[3]";

    }
    else {

        $event{$key} = "$_[0]\t$d $mn{$m} $y\t$_[1]\t$_[3]";

    }

    $msg .= "event output: $_[0]\t$d $mn{$m} $y\t$_[1]\t$_[3]<br>\n\n";

}

1;    # return true

