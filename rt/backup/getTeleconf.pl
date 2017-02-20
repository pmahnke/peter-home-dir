#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/html/rt/getEvents.pl");
require ("/home/gartner/html/rt/common.pl");

# Variables
local $server = "regionals4"; # "www4";
local $line = "";

# Locale logic
$locale = "italia" if ($ARGV[0] eq "italia");
$locale = "de"     if ($ARGV[0] eq "de");


# URL to pull events from gartner.com
$FORM{'page'} = "http:\/\/regionals4.gartner.com\/Events?pageName=calendar&previous=false&cboMonth=0&cboType=6&cboRegion=-1";


# call script to get events info in nice HASH
undef %event;
&getEventsDetail($FORM{'page'});


# DATE LOGIC
$FORM{'date'} = 21000000 if (!$FORM{'date'}); # set date way out if none given
$startDate =  `date '+%Y%m%d'`;
if ($locale eq "italia" || $locale eq "de") {
    # give italian site more time for dates
    $startDate = 600 + $startDate;
} else {
    $startDate = 120 + $startDate;
}
$FORM{'date'} = $startDate;
$FORM{'limit'} = 3; # normally set to 2, but without local briefings, moved to 3 (which actually prints 4)


print "date $startDate\n\n";

    foreach $key (sort keys %event) {

	if (!$skip) {
	    
	    # skip first one.
	    $skip = 1;
	    #next;
	}
	

	local ($title, $date, $url, $location) = split (/\t/, $event{$key});
	
	$title =~ s/  / /g; # remove double spaces

	$url = "\/".$url if ($url !~ /^\//);

	print "looking at $title\n";

	local $dateKey = substr ($key, 0, 8);
	
	next if ($dateKey > $FORM{'date'});
	next if ($location =~ /Riyadh/); # not Europe
	next if ($location =~ /Dubai/); # not Europe
	next if ($location =~ /Ankara/); # not Europe
	next if ($location =~ /Istanbul/); # not Europe


	last if ($count > $FORM{'limit'}); # only allow a max of 5 per briefing

	$date = substr ($date, 0, (length($date) -5));

	$title =~ s/ - / \&\#151\; /g;

	if ($locale eq "italia") {
	    
	    print "going to record $title $url $date\n";

	    $date =~ s/^0//;

	    $line .= <<EndofHTML;

         <tr> 

	     <td width="15" bgcolor="#F4F4E5" valign="top"><img src="//img/homepage/reversed_purple_arrow.gif" width="9" height="9" vspace="2" alt="" border="0"></td>

		 <td width="171" bgcolor="#F4F4E5"><a href="$url" class="smallBlueLink">$title</a><br /> 

		     <span class="smallDarkBlueText">$date</span><br /></td>

			 </tr>

			     <tr> 

				 <td colspan="2" width="186" height="15" bgcolor="#F4F4E5"><img src="./img/trans_pixel.gif" width="186" height="15" alt="" border="0"></td>

				     </tr>

EndofHTML

	    $xhtmlLine .= <<EndofHTML;
             <li><p><a href="$url">$title</a></p><p>$date</p></li> 
EndofHTML


} else {

	$line .= <<EndofHTML;

<tr> 
<td width="15" bgcolor="#F4F4E5" valign="top"><img src="//img/homepage/reversed_purple_arrow.gif" width="9" height="9" vspace="2" alt="" border="0"></td>
<td width="171" bgcolor="#F4F4E5"><a href="$url" class="smallBlueLink">$title</a><br> 
<span class="smallDarkBlueText">$date</span><br></td>
</tr>
<tr> 
<td colspan="2" width="186" height="15" bgcolor="#F4F4E5"><img src="./img/trans_pixel.gif" width="186" height="15" alt="" border="0"></td>
</tr>

EndofHTML

    $xhtmlLine .= <<EndofHTML;
             <li><p><a href="$url">$title</a></p><p>$date</p></li> 
EndofHTML

}

	$count++;


}


if ($locale eq "italia") {
    $fileName = "/home/gartner/html/rt/content/emea/it/teleconf.html";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/it/xhtmlTeleconf.html";
} elsif ($locale eq "de") {
    $fileName = "/home/gartner/html/rt/content/emea/de/teleconf.html";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/de/xhtmlTeleconf.html";
} else {
    $fileName = "/home/gartner/html/rt/content/emea/teleconf.html";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/xhtmlTeleconf.html";
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
if ($ARGV[0] eq "italia") {
	
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

