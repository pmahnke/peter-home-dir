#!/usr/local/bin/perl


#####################################################################
#####################################################################
#
#
#	getSymposium.pl
#
#	  written in 13 April 2005 by Peter Mahnke
#
#	  modifed
#     - 23 Apr 2005 by Peter Mahnke
#       if no matching events... write a blank file and quit...
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
require ("/home/gartner/html/rt/getEvents3.pl");
require ("/home/gartner/html/rt/common.pl");
require ("/home/gartner/html/rt/commonCity.pl");

# Variables
local $line  = "";
local $count = 0;
local $skip  = 0;

# UI string
$UIstring{'viewall'}{'emea'} = "View all Symposia";
$UIstring{'viewall'}{'it'}   = "Visualizza tutti i<br\>Symposium";
$UIstring{'viewall'}{'de'}   = "Alle Symposien";
$UIstring{'viewall'}{'at'}   = "Alle Symposien";

$UIstring{'more'}{'emea'} = "More about Symposium/Itxpo";
$UIstring{'more'}{'it'}   = "Altri Vision Events";
$UIstring{'more'}{'de'}   = "Weitere Informationen zum<br>Symposium/ITxpo";
$UIstring{'more'}{'at'}   = "Weitere Informationen zum<br>Symposium/ITxpo";

# Locale logic
$locale = "emea"; # default
$locale = "emea"   if ($ARGV[0] eq "emea");
$locale = "it"	   if ($ARGV[0] eq "it");
$locale = "de"	   if ($ARGV[0] eq "de");

# Number of Confs to Skip (i.e. to avoid a promo)
$num2skip = 0; # default
$num2skip = $ARGV[1] if ($ARGV[1]);

# Strictness on locales, strict for locale only, loose or null for europe;
local %strict;
$strict{'emea'} = "";
$strict{'it'}   = "";
$strict{'de'}   = "";


# call script to get events info in nice HASH
undef %event;
&getEventsDetail('Symposium');

if (!%event) {
	# no matching events... write a blank file and quit....
	goto WRITEFILE;
}

# DATE LOGIC
$FORM{'limit'} = 2; # normally set to 2, but without local briefings, moved to 3 (which actually prints 4)

foreach $key (sort keys %event) {

	local ($title, $date, $url, $location) = split (/\t/, $event{$key});

	# some overridding rules to skip events that are promoted lower down....
	next if ($title =~ /Gartner Application Integration/ && $locale =~ /(emea|de)/);


	if ($skip < $num2skip && $num2skip > 0) {

		# change the limit to set how many to skip (usually because there is a promo for 1 or 2)
		$skip++;
		next;

	}



	local ($title, $date, $url, $location) = split (/\t/, $event{$key});

	$title =~ s/  / /g; # remove double spaces
	$title =~ s/^ //g;  # remove leading spaces
	$title =~ s/\(Invite\)//g; # remove (Invite) for channel confs

	$url = "\/".$url if ($url !~ /^\// && $url !~ /^http/);

	print "$count > $FORM{'limit'}\n\tlooking at $title\n";

	local $dateKey = substr ($key, 0, 8);


	# localise location
	$location = &localiseLocation($location, $locale, $strict{$locale}); # not strict filtering



	last if ($count > $FORM{'limit'}); # only allow a max of 5 per briefing

	$date = substr ($date, 0, (length($date) -5));

	$title =~ s/ - / \&\#8212\; /g;

	local $NHtitle = &noHang($title, 25);

	if ($locale eq "it") {

		print "going to record $title $url $date\n";

		$date =~ s/^0//;

		# create HTML version
		$line .= <<EndofHTML;

<!-- $title -->
  <tr>
	  <td width="15" bgcolor="#F4F4E5" valign="top"><img src="/images/homepage/reversed_purple_arrow.gif" width="9" height="9" vspace="2" alt="" border="0"></td>
						 <td width="171" bgcolor="#F4F4E5"><a href="$url" class="smallBlueLink">$NHtitle</a><br>
 <span class="smallDarkBlueText">$date<br>$location</span><br></td>
	</tr>
	<tr>
	  <td colspan="2" width="186" height="20" bgcolor="#F4F4E5"><img src="/images/trans_pixel.gif" width="186" height="20" alt="" border="0"></td>
	</tr>

EndofHTML

		# create XHTML version
		$xhtmlLine .= <<EndofHTML;
	    <li><a href="$url">$date</a><br><a href="$url">$location</a></li>
EndofHTML


	} else {

		# create HTML version
		$line .= <<EndofHTML;

<!-- $title -->
  <tr>
	  <td width="15" bgcolor="#F4F4E5" valign="top"><img src="/images/homepage/reversed_purple_arrow.gif" width="9" height="9" vspace="2" alt="" border="0"></td>
						 <td width="171" bgcolor="#F4F4E5"><a href="$url" class="smallBlueLink">$NHtitle</a><br>
 <span class="smallDarkBlueText">$date<br>$location</span><br></td>
	</tr>
	<tr>
	  <td colspan="2" width="186" height="20" bgcolor="#F4F4E5"><img src="/images/trans_pixel.gif" width="186" height="20" alt="" border="0"></td>
	</tr>
EndofHTML

		# create XHTML version
		$xhtmlLine .= <<EndofHTML;
	    <li><a href="$url">$date</a><br><a href="$url">$location</a></li>
EndofHTML

	}

	$count++;


}

# setup whole include

my $output =<<EndofListing;
    <div id="regionalEventsSymposium">

        <a href="/2_events/symposium/worldwide.html"><img src="/images/homepage/hdr_sym.gif" height="60" width="198" alt="Gartner Symposium" border="0"></a>

        <ul class="regionalEventList">
$xhtmlLine
        </ul>

        <ul class="regionalEventMore">
            <li><a href="/2_events/symposium/worldwide.html">$UIstring{'viewall'}{$locale}</a></li>
            <li><a href="/2_events/symposium/sym2005_contact.html">$UIstring{'more'}{$locale}</a></li>
        </ul>

        <br clear="all">
    </div><!-- end div regionalEventsSymposium -->
EndofListing


if ($locale eq "it") {
	$fileName = "/home/gartner/html/rt/content/emea/it/home_symposium.incl";
	$xhtmlFileName = "/home/gartner/html/rt/content/emea/it/xhtmlSymposium.incl";
} elsif ($locale eq "de") {
	$fileName = "/home/gartner/html/rt/content/emea/de/home_symposium.incl";
	$xhtmlFileName = "/home/gartner/html/rt/content/emea/de/xhtmlSymposium.incl";
} else {
	$fileName = "/home/gartner/html/rt/content/emea/home_symposium.incl";
	$xhtmlFileName = "/home/gartner/html/rt/content/emea/xhtmlSymposium.incl";
}

WRITEFILE: open (OUTPUT, ">$fileName") || die "Can't open OUTPUT to write: $fileName\n";
print  OUTPUT $line;
close (OUTPUT);

open (XHTMLOUTPUT, ">$xhtmlFileName") || die "Can't open OUTPUT to write xhtml: $xhtmlFileName\n";
print  XHTMLOUTPUT $output;
close (XHTMLOUTPUT);

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

