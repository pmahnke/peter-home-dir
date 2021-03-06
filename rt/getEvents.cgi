#!/usr/local/bin/perl


#####################################################################
#####################################################################
#
#
#	getVisionEvents.pl
#
#	  written in 13 April 2005 by Peter Mahnke
#
#	  modifed
#         - 23 Apr 2005 by Peter Mahnke
#           if no matching events... write a blank file and quit...
#	  - 31 March 2004 by Peter Mahnke
#		added in option ARGV[1] for num2skip
#	  - 21 Jan 2004 by Peter Mahnke
#		originally written as getConf.pl
#
#	  DESCRIPTION
#	  creates an html and xhtml (currently not used) include of the
#	  conferences section of the regionals homepage
#	  the includes sit on this server and are called into the regionals CMT
#
#	  INPUT:
#	  run from a command-line of called from update_menu.cgi script
#	  there are two command-line argument
#	   1: <locale> 'emea' (default) or 'it' or 'de�
#	   2: <skip> the number of conferences to skip (to allow for a promo)
#
#	  OUTPUT:
#	  the script writes 2 files, one is the html include
#	  and the other is an xhtml version
#	  in /home/gartner/html/content/emea/<locale>/home_events_confs.incl
#	  and /home/gartner/html/content/emea/<locale>/xhtmlVisionEvents.incl
#
#
#
#####################################################################
#####################################################################



use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/html/rt/getEvents4.pl");
require ("/home/gartner/html/rt/common.pl");
require ("/home/gartner/html/rt/commonCity.pl");

# Variables
local $line  = "";
local $count = 0;
local $skip  = 0;


# Locale logic
$locale = "emea"; # default
$locale = "emea"   if ($ARGV[0] eq "emea");
$locale = "it"	   if ($ARGV[0] eq "it");
$locale = "de"	   if ($ARGV[0] eq "de");

# Strictness on locales, strict for locale only, loose or null for europe;
local %strict;
$strict{'emea'} = "";
$strict{'it'}   = "";
$strict{'de'}   = "";
$strict{$ARGV[0]} = $ARGV[2];

# call script to get events info in nice HASH
undef %event;
# &getEventsDetail('Teleconf');
&getEventsDetail('Briefing') if ($ARGV[1] !~ 3);
&getEventsDetail('VisionEvent');
&getEventsDetail('Conf');
&getEventsDetail('Symposium');

if (!%event) {
	# no matching events... write a blank file and quit....
	goto WRITEFILE;
}

# DATE LOGIC
$FORM{'limit'} = 5 if (!$FORM{'limit'}); # normally set to 2
my $count = 0; # set the counter to 0

foreach $key (sort keys %event) {

    local ($title, $date, $url, $location) = split (/\t/, $event{$key});


    local ($title, $date, $url, $location) = split (/\t/, $event{$key});

    # some overridding rules to skip events that are promoted lower down....
    next if ($title =~ /Gartner Application Integration/ && $locale =~ /(emea|de)/);

    $title = "Open Day in Germany" if ($title =~ /Tag der offenen/ && $locale !~ /de/);



    $title =~ s/  / /g; # remove double spaces
    $title =~ s/^ //g;  # remove leading spaces
    $title =~ s/\'//g;   # remove single quotes
    $title =~ s/\(Invite\)//g; # remove (Invite) for channel confs

    $url = "\/".$url if ($url !~ /^\// && $url !~ /^http/);

    print "$count < $FORM{'limit'}\n\tlooking at $title\n\n";

    local $dateKey = substr ($key, 0, 8);



    # $location = &localiseLocation($location, $locale, $strict{$locale}); # strict filtering
    $location = &localiseLocation($location, $locale); # NOT strict filtering


    if ($count >= $FORM{'limit'}) {
	print "LAST\n";
	last; # only allow a max of 5 per briefing
    }

    $date = substr ($date, 0, (length($date) -5));

    $title =~ s/ - / \&\#8212\; /g;

    local $NHtitle = &noHang($title, 25);

    if ($location ne "NA") {
	$location = "<br /> $location";
    } else {
	$location = "";
    }


    print "going to record $title $url $date\n";

    $date =~ s/^0//;

    # create HTML version
    $line .= <<EndofHTML;

<!-- $title -->

      <li><a href="$url" >$title</a><br />
      <span class="sub_text"> $date$location</span></li>

EndofHTML


	$count++;


}

# setup whole include

my $output =<<EndofListing;
    <div  id="regionalEventsVision">

        <a href="/EventsCal?opCode=1&amp;template=3&amp;eventType=7&amp;locationId=4|"><img src="/images/homepage/hdr_vision.gif" width="198" height="60" border="0" alt="Gartner Vision Events"></a>

        <ul class="regionalEventList">
$xhtmlLine
        </ul>

        <ul class="regionalEventMore">
            <li><a href="/EventsCal?opCode=1&amp;template=3&amp;eventType=7&amp;locationId=4|">$UIstring{'viewall'}{$locale}</a></li>
            <li><a href="http://www.visionevents.com/" target="_blank">$UIstring{'more'}{$locale}</a></li>
        </ul>

        <br clear="all">
    </div><!-- end div regionalEventsVision -->
EndofListing


if ($locale eq "it") {
	$fileName = "/home/gartner/html/rt/content/emea/it/home_events.incl";
} elsif ($locale eq "de") {
	$fileName = "/home/gartner/html/rt/content/emea/de/home_events.incl";
} else {
	$fileName = "/home/gartner/html/rt/content/emea/home_events.incl";
}

WRITEFILE: open (OUTPUT, ">$fileName") || die "Can't open OUTPUT to write: $fileName\n";
print  OUTPUT $line;
close (OUTPUT);


print "Done.\n";

exit;



########################################################################
sub titleTranslation {

	# translate known titles to known translations
	# currently out of date...

	local $t = $_[0];

	if ($ARGV[0] eq "it") {

		$t = "Il \"Business Value of IT\" richiede l'allineamento di business e IT\: cosa viene prima\?"
			if ($t =~ /Business Value of IT/);

		$t = "Opportunit� emergenti nel mercato europeo dell'outsourcing."
			if ($t =~ /Emerging Opportunities/);

		$t = "Creazione di un'architettura e di una \"banca\" di informazioni corrette per il CRM"
			if ($t =~ /Creating the Right CRM/);

		$t = "Gestione del ciclo di vita dei contratti nella real-time enterprise"
		if ($t =~ /Cycle Management/);

		$t = "Web Services: Business Drivers e Management"
		if ($t =~ /Web Services:/);


	}

	return ($t);

}

