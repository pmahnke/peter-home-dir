#!/usr/local/bin/perl

#####################################################################
#####################################################################
#
#
#	getTeleconf.pl
#
#	  written: 04 May 2002 by Peter Mahnke
#
#	  modifed:
#              23 Apr 2005 by Peter Mahnke
#              print empty file if no events
#
#			   21 Jan 2004 by Peter Mahnke
#			   ahead of g.com 5.0 release to use new getEvents2.pl scripts
#
#			   31 Mar 2004 by Peter Mahnke
#			   allow limit to come in on command line in ARGV[1]
#
#			   AND many times for date format changes and new locales
#
#	  DESCRIPTION
#	  creates an html and xhtml (currently not used) include of the
#	  teleconferences section of the regionals homepage
#	  the includes sit on this server and are called into the regionals CMT
#
#	  INPUT:
#	  run from a command-line of called from update_menu.cgi script
#	  there are two command-line argument
#	   1: <locale> 'emea' (default) or 'it' or 'de�
#	   2: <limit> the number of teleconferences to show
#
#	  OUTPUT:
#	  the script writes 2 files, one is the html include
#	  and the other is an xhtml version
#	  in /home/gartner/html/content/emea/<locale>/teleconf.incl
#	  and /home/gartner/html/content/emea/<locale>/xhtmlTeleconf.incl
#
#
#####################################################################
#####################################################################

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/html/rt/getEvents2.pl");
require ("/home/gartner/html/rt/common.pl");

# Global Variables
local $server = "www4";
local $line = "";

# set up number of teleconferences to print...
$FORM{'limit'} = 2; # defalts to 2, but without local briefings, moved to 3 (which actually prints 4)
$FORM{'limit'} = ($ARGV[1] - 1) if ($ARGV[1]);


# Locale logic
$locale = "emea"; # default
$locale = "emea" if ($ARGV[0] eq "emea");
$locale = "it"   if ($ARGV[0] eq "it");
$locale = "de"   if ($ARGV[0] eq "de");

# UI string
$UIstring{'title'}{'emea'} = "Teleconferences";
$UIstring{'title'}{'it'}   = "Teleconferenze";
$UIstring{'title'}{'de'}   = "Telekonferenzen";
$UIstring{'title'}{'at'}   = "Telekonferenzen";

$UIstring{'text'}{'emea'} = "Dial in, listen in, and speak <br>with Gartner analysts about <br>key topics.";
$UIstring{'text'}{'it'}   = "Telefona, partecipa e consulta gli analisti Gartner.";
$UIstring{'text'}{'de'}   = "Einw&auml;hlen, zuh&ouml;ren und mit Gartner-Analysten &uuml;ber Schl&uuml;sselthemen sprechen (englischsprachig).";
$UIstring{'text'}{'at'}   = "Einw&auml;hlen, zuh&ouml;ren und mit Gartner-Analysten &uuml;ber Schl&uuml;sselthemen sprechen (englischsprachig).";

$UIstring{'more'}{'emea'} = "More Teleconferences";
$UIstring{'more'}{'it'}   = "Altre teleconferenze";
$UIstring{'more'}{'de'}   = "Weitere Telekonferenzen";
$UIstring{'more'}{'at'}   = "Weitere Telekonferenzen";

# call script to get events info in nice HASH
undef %event;
&getEventsDetail('Teleconf');


# DATE LOGIC
$startDate = &addDays(15);
$FORM{'date'} = $startDate;


print "date $startDate\n\n";



foreach $key (sort keys %event) {

	print "looking at $key\n";

	if (!$skip) {

		# currently not skipping.... need to uncomment the 'next'

		# skip first one.
		$skip = 1;
		#next;
	}


	local ($title, $date, $url, $location) = split (/\t/, $event{$key});

	$title =~ s/  / /g; # remove double spaces

	$url = "\/".$url if ($url !~ /^\//);

	print "looking at $title $FORM{'date'} $date\n";

	local $dateKey = substr ($key, 0, 8);

	# broke over year barier
	next if ($dateKey > $FORM{'date'});

	# reject localations that are not in Europe
	next if ($location =~ /Riyadh/);   # not Europe
	next if ($location =~ /Dubai/);    # not Europe
	next if ($location =~ /Ankara/);   # not Europe
	next if ($location =~ /Istanbul/); # not Europe


	# only allow a max of 5 listings per briefing
	last if ($count > $FORM{'limit'});

	$date = substr ($date, 0, (length($date) -5));

	# turn dashes into proper mdash html entity
	$title =~ s/ - / \&\#8212\; /g;

	$contentFlag = 1; # must be real events if we got this far

	if ($locale eq "it") {

		# special spacing for italy to deal with long dates...

		print "going to record $title $url $date\n";

		$date =~ s/^0//;

		# create HTML version
		$line .= <<EndofHTML;
		<tr>
		<td width="15" bgcolor="#F4F4E5" valign="top"><img src="/images/homepage/reversed_purple_arrow.gif" width="9" height="9" vspace="2" alt="" border="0"></td>
		<td width="171" bgcolor="#F4F4E5"><a href="$url" class="smallBlueLink">$title</a><br />
			<span class="smallDarkBlueText">$date</span><br /></td>
			</tr>
				<tr>
				<td colspan="2" width="186" height="15" bgcolor="#F4F4E5"><img src="/images/trans_pixel.gif" width="186" height="15" alt="" border="0"></td>
			</tr>

EndofHTML

		# create XHTML version
		$xhtmlLine .= <<EndofHTML;
			<li><a href="$url">$title</a><br>$date</li>
EndofHTML


	} else {

		# HTML for non-Italia locales...

		# create HTML version
		$line .= <<EndofHTML;

<tr>
  <td width="15" bgcolor="#F4F4E5" valign="top"><img src="/images/homepage/reversed_purple_arrow.gif" width="9" height="9" vspace="2" alt="" border="0"></td>
  <td width="171" bgcolor="#F4F4E5"><a href="$url" class="smallBlueLink">$title</a><br>
  <span class="smallDarkBlueText">$date</span><br></td>
</tr>
<tr>
  <td colspan="2" width="186" height="15" bgcolor="#F4F4E5"><img src="/images/trans_pixel.gif" width="186" height="15" alt="" border="0"></td>
</tr>

EndofHTML

		# create XHTML version
		$xhtmlLine .= <<EndofHTML;
            <li><a href="$url">$title</a><br>$date</li>
EndofHTML

	}

	$count++;

}

$output =<<EndofListing;
    <div id="regionalEventTeleconferences">

        <h3><a href="/teleconferences/teleconferences_landing.jsp">$UIstring{'title'}{$locale}</a></h3>

        <p>$UIstring{'text'}{$locale}</p>

        <ul class="regionalEventList">
$xhtmlLine
        </ul>

        <ul class="regionalEventMore">
            <li><a href="/teleconferences/teleconferences_landing.jsp">$UIstring{'more'}{$locale}</a></li>
        </ul>

        <br clear="all">
    </div><!-- end div regionalEventTeleconferences -->
EndofListing





# OUTPUT FILE

# pick filename based on locale
if ($locale eq "it") {
	$fileName = "/home/gartner/html/rt/content/emea/it/teleconf.html";
	$xhtmlFileName = "/home/gartner/html/rt/content/emea/it/xhtmlTeleconf.incl";
} elsif ($locale eq "de") {
	$fileName = "/home/gartner/html/rt/content/emea/de/teleconf.html";
	$xhtmlFileName = "/home/gartner/html/rt/content/emea/de/xhtmlTeleconf.incl";
} else {
	$fileName = "/home/gartner/html/rt/content/emea/teleconf.html";
	$xhtmlFileName = "/home/gartner/html/rt/content/emea/xhtmlTeleconf.incl";
}

# if no $contentFlag then zero out files
if (!$contentFlag) {
	$line = "";
	$output = "";
}

# save HTML file
open (OUTPUT, ">$fileName") || die "Can't open OUTPUT to write\n";
print  OUTPUT $line;
close (OUTPUT);

# save XHTML file
open (XHTMLOUTPUT, ">$xhtmlFileName") || die "Can't open OUTPUT to write\n";
print  XHTMLOUTPUT $output;
close (XHTMLOUTPUT);

print "Done.\n";

exit;





###############################################################
sub titleTranslation {

	# translate titles from a Known title to a Known Translation
	# currently these translations are out of date...

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

