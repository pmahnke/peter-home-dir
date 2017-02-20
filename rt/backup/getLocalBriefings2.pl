#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/html/rt/getEvents.pl");
require ("/home/gartner/html/rt/common.pl");

# Variables
local $server = "www4";

$locale = "italia" if ($ARGV[0] eq "italia");

#$FORM{'page'} = "http:\/\/www4.gartner.com\/Events?pageName=calendar&previous=false&cboMonth=0&cboType=5&cboRegion=4";
$FORM{'page'} = "http:\/\/www4.gartner.com\/Events?pageName=calendar&previous=false&cboMonth=0&cboType=5&cboRegion=1";

&getEventsDetail($FORM{'page'});

$FORM{'date'} = 21000000 if (!$FORM{'date'}); # set date way out if none given
$startDate =  `date '+%Y%m%d'`;
if ($ARGV[0] eq "italia") {
 # give italian site more time for dates
    $startDate = 600 + $startDate;
} else {
    $startDate = 120 + $startDate;
}
$FORM{'date'} = $startDate;
$FORM{'limit'} = 15;

print "date $startDate\n\n";

    foreach $key (sort keys %event) {

	local ($title, $date, $url, $location) = split (/\t/, $event{$key});
	
	$title =~ s/  / /g; # remove double spaces

	local $name = $title;
	local $dateKey = substr ($key, 0, 8);
	
	next if ($dateKey > $FORM{'date'});
	next if ($location =~ /Riyadh/); # not Europe
	next if ($location =~ /Dubai/); # not Europe
	next if ($location =~ /Ankara/); # not Europe
	next if ($location =~ /Istanbul/); # not Europe


	$name =~ tr/[a-z]/[A-Z]/;
	next if ($count{$name} > $FORM{'limit'}); # only allow a max of 5 per briefing

	# location clean up
	$location =  $1 if ($location =~ /(.[^\,]*)\,/); # dump comma contry
	$location =~ s/[0-9]//g; # dump numbers
	$location =~ s/CH\-//; # some strange Swiss thing
	$location =~ s/, M90 3RA//; # some strange UK Postcode

	# fix some bad spellings
#	$location = "Rome" if ($location eq "Roma");
#	$location = "Dusseldorf" if ($location eq "Duesseldorf");
#	$location = "Geneva" if ($location eq "Geneve");
#	$location = "Vienna" if ($location =~ /Wien/);
#	$location = "Lisbon" if ($location eq "Lisboa");

	# add countries to lesser known places
	$location = "Zurich" if ($location =~ /Glattbrugg/);
	$location = "Stockholm" if ($location =~ /Solna/);
	$location = "Helsinki" if ($location =~ /Helsinki/);
#	$location = "Helsinki, Finland" if ($location =~ /Helsinki/);
	$location = "Zagreb, Croatia" if ($location =~ /Zagreb/);
	$location = "Copenhagen" if ($location =~ /Klampenborg/);
	$location = "Amsterdam" if ($location =~ /Hoofddorp/);
	$location = "Madrid" if ($location =~ /Las Rozas - Madrid/);


	# locale localisation
	
	# ITALIA
	if ($ARGV[0] eq "italia") {
	    if ($location =~ /(Rome|Roma|Milan|Geneva|Zurich)/) { #    || 
		$location = "Roma" if ($location eq "Rome");
		$location = "Milano" if ($location eq "Milan");
		$location = "Zurigo" if ($location eq "Zurich");
		$location = "Ginevra" if ($location eq "Geneva");
	    } else {
		next;
	    }
	}
	    


	$date = "\&nbsp\;"."$1" if ($date =~ /^0(.*)/); # dump precending 0 on dates - NO LONGER WORKS

	$date = substr ($date, 0, (length($date) -5));

	if ($locale eq "italia") {
	    $detail{$name} .= <<EndofHTML;

           <tr>
                <td width="3" bgcolor="#f5f5f5"><img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td>
                <td width="95"valign="top" bgcolor="#f5f5f5"><a href="$url" class="smallThinBlueLink">$location</a></td>
                <td width="100" valign="top" align="right" bgcolor="#f5f5f5"><span class="smallGrayText">$date&nbsp;</span></td>
           </tr>
EndofHTML

        } else {
	    $detail{$name} .= <<EndofHTML;

           <tr>
                <td width="3" bgcolor="#F4F4E5"><img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td>
                <td width="95" valign="top" bgcolor="#F4F4E5"><a href="$url" class="smallThinBlueLink">$location</a></td>
                <td width="100" valign="top" align="right" bgcolor="#F4F4E5"><span class="smallGrayText">$date&nbsp;</span></td>
           </tr>
EndofHTML
        }

	$count{$name}++;


	$title =~ s/ - / \&\#151\; /g;
	$title = &uppercase($title);
	$title{$name} = $title;
	
    }


    foreach $title (sort keys %title) {
	
	local $name = $title;
	$name =~ tr/[a-z]/[A-Z]/;
	#$title{$title} = &noHang($title{$title}, 30);
	$title{$title} = &titleTranslation($title{$title})  if ($ARGV[0]);
	

	$line .= <<EndofHTML;

<!-- $title{$title} START -->
          
          <tr>
               <td width="3" bgcolor="#F4F4E5"><img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td>
               <td width="195" colspan="2" bgcolor="#F4F4E5">
<img src="//img/trans_pixel.gif" width="191" height="3" border="0" alt="spacer"><br />
<span class="smallGrayText">
$title{$title}
</span>
<img src="//img/trans_pixel.gif" width="191" height="5" border="0" alt="spacer"><br />
                </td>
          </tr>

          <tr><td colspan="3" height="7" width="198" bgcolor="#F4F4E5"><img src="//img/trans_pixel.gif" width="194" height="7" border="0" alt="spacer"></td>

$detail{$name}

           <tr><td colspan="3" height="7" width="198" bgcolor="#F4F4E5"><img src="//img/trans_pixel.gif" width="198" height="7" border="0" alt="spacer"></td>
           </tr>
           <tr><td colspan="3" width="198" height="1" bgcolor="#cecece"><img src="//img/trans_pixel.gif" width="194" height="1" border="0" alt="spacer"></td></tr>


<!-- $title{$title} END -->

EndofHTML

}

if ($ARGV[0] eq "italia") {
    $fileName = "/home/gartner/html/rt/events/it/localBriefingTable.html";
} else {
    $fileName = "/home/gartner/html/rt/events/localBriefingTable.html";
}
open (OUTPUT, ">$fileName") || die "Can't open OUTPUT to write\n";
print  OUTPUT $line;
close (OUTPUT);
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

