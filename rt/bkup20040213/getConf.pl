#!/usr/local/bin/perl


#####################################################################
#####################################################################
#
#
#    getConfs.pl
#
#      written in 21 Jan 2004 by Peter Mahnke
#
#      modifed
#
#      DESCRIPTION
#      builds includes for emea, it and de for the homepage
#      home_events_confs.incl include (html and xhtml versions)
#
#      currently run via a nightly cron and from the update_menu.cgi
#
#      OPTIONS
#       - $FORM{'limit'} sets the number of teleconferences to put
#         in the listing
#
#       - $skip > <number to skip>
#         changes the number of conferences to skip 
#         (usually because there is a promo for 1 or 2)
#      
#
#
#####################################################################
#####################################################################



use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/html/rt/getEvents2.pl");
require ("/home/gartner/html/rt/common.pl");
require ("/home/gartner/html/rt/commonCity.pl");

# Variables
local $line = "";
local $count = 0;
local $skip = 0;

# Locale logic
$locale = "it"     if ($ARGV[0] eq "it");
$locale = "de"     if ($ARGV[0] eq "de");

# Strictness on locales, strict for locale only, loose or null for europe;
local %strict;
$strict{'emea'} = "";
$strict{'it'}   = "";
$strict{'de'}   = "";


# call script to get events info in nice HASH
undef %event;
&getEventsDetail('Conf');


# DATE LOGIC
$FORM{'limit'} = 4; # normally set to 2, but without local briefings, moved to 3 (which actually prints 4)

foreach $key (sort keys %event) {

    if ($skip < 2) {
	
	# change the limit to set how many to skip (usually because there is a promo for 1 or 2)
	$skip++;
	next;
    
    }

    
    
    local ($title, $date, $url, $location) = split (/\t/, $event{$key});
    
    $title =~ s/  / /g; # remove double spaces
    
    $url = "\/".$url if ($url !~ /^\//);
    
    print "$count > $FORM{'limit'}\n\tlooking at $title\n";

    local $dateKey = substr ($key, 0, 8);
    

    # localise location
    $location = &localiseLocation($location, $locale, $strict{$locale}); not strict filtering

    

    last if ($count > $FORM{'limit'}); # only allow a max of 5 per briefing
    
    $date = substr ($date, 0, (length($date) -5));
    
    $title =~ s/ - / \&\#151\; /g;
    
    local $NHtitle = &noHang($title, 25);

    if ($locale eq "it") {

	print "going to record $title $url $date\n";

	$date =~ s/^0//;

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

    $xhtmlLine .= <<EndofHTML;
	<li><p><a href="$url">$title</a></p><p>$date</p><p>$location</p></li>
EndofHTML


} else {

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

    $xhtmlLine .= <<EndofHTML;
	<li><p><a href="$url">$title</a></p><p>$date</p><p>$location</p></li>
EndofHTML

    }

    $count++;


}


if ($locale eq "it") {
    $fileName = "/home/gartner/html/rt/content/emea/it/home_events_confs.incl";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/it/xhtmlConfs.incl";
} elsif ($locale eq "de") {
    $fileName = "/home/gartner/html/rt/content/emea/de/home_events_confs.incl";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/de/xhtmlConfs.incl";
} else {
    $fileName = "/home/gartner/html/rt/content/emea/home_events_confs.incl";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/xhtmlConfs.incl";
}

open (OUTPUT, ">$fileName") || die "Can't open OUTPUT to write\n";
print  OUTPUT $line;
close (OUTPUT);

open (XHTMLOUTPUT, ">$xhtmlFileName") || die "Can't open OUTPUT to write\n";
print  XHTMLOUTPUT $xhtmlLine;
close (XHTMLOUTPUT);

print "Done.\n";



sub uppercase {

    undef local ($ucTitle);
    undef local ($wordCount);
    
    @words = split (" ", $_[0]);
    
    foreach (@words) {
	
	$msg .= "title word: \|$_\|\n";
	
	# skip first word
	if (!$wordCount) {
	    $wordCount = 1;
	}
	
	if ($_ ne "the" &&
	    $_ ne "of"  &&
	    $_ ne "a"   &&
	    $_ ne "in"  &&
	    $_ ne "to"  &&
	    $_ ne "an"  &&
	    $_ ne "and")
	{
	    
	    $_ = ucfirst($_);
	    $msg .= " capping $_ ";
	} else {
	$msg .= " skiping $_ ";
    }
	
	$ucTitle .= "$_ ";
	$wordCount++;
	$msg .= "now: $_ <br\>\n";
    }
    
    return($ucTitle);
    
}

exit;



sub titleTranslation {
    
    local $t = $_[0];
    if ($ARGV[0] eq "it") {
	
	$t = "Il \"Business Value of IT\" richiede l'allineamento di business e IT\: cosa viene prima\?"
	    if ($t =~ /Business Value of IT/);
	
	$t = "Opportunità emergenti nel mercato europeo dell'outsourcing."
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

