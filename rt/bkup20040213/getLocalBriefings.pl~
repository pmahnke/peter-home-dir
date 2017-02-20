#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/html/rt/getEvents.pl");
require ("/home/gartner/html/rt/common.pl");

# Variables
local $server = "regionals4"; #"www4"


# Locale setup
$locale = "italia" if ($ARGV[0] eq "italia");
$locale = "de" if ($ARGV[0] eq "de");

# URL to get data from
$FORM{'page'} = "http:\/\/regionals4.gartner.com\/Events?pageName=calendar&previous=false&cboMonth=0&cboType=5&cboRegion=4";


# Get events information
&getEventsDetail($FORM{'page'});

# Date Logic
$FORM{'date'} = 21000000 if (!$FORM{'date'}); # set date way out if none given
$startDate =  `date '+%Y%m%d'`;
$today = $startDate;

if ($locale eq "italia" || $locale eq "de") {

    # give italian and german site more time for dates
    $startDate = 600 + $startDate;

} else {

    $startDate = 200 + $startDate; # was 100 - changed 15 Sept 2003

}


$FORM{'date'} = $startDate;
$FORM{'limit'} = 2;


# Step through each event
$msg .= "date $startDate\n\n";

    foreach $key (sort keys %event) {

	local ($title, $date, $url, $location) = split (/\t/, $event{$key});

	$url = "\/"."$url" if ($url !~ /^\//); # add slash before events that are missing them.

	$title =~ s/  / /g; # remove double spaces

	# fix bad titles
	$title = "IT and Your Business \&\#151\; Strategic Trends and Directions" 
	    if ($title =~ /IT and Your Business/i); # 24 Nov 2003



	local $name = $title;
	local $dateKey = substr ($key, 0, 8);
	

	# skip events for today
	next if ($dateKey <= $today);

	next if ($dateKey > $FORM{'date'});
	next if ($location =~ /Riyadh/); # not Europe
	next if ($location =~ /Dubai/); # not Europe
	next if ($location =~ /Ankara/); # not Europe
	next if ($location =~ /Istanbul/); # not Europe


	$name =~ tr/[a-z]/[A-Z]/;
	next if ($count{$name} > $FORM{'limit'}); # only allow a max of 5 per briefing

	# location clean up#
	$location =  $1 if ($location =~ /(.[^\,]*)\,/); # dump comma contry
	$location =~ s/[0-9]//g; # dump numbers
	$location =~ s/CH\-//; # some strange Swiss thing
	$location =~ s/, M90 3RA//; # some strange UK Postcode

	# fix some bad spellings
	$location = "Rome" if ($location eq "Roma");
	$location = "Dusseldorf" if ($location eq "Duesseldorf"
				     || $location =~ /Neuss \- Duesseldorf/);
#	$location = "Geneva" if ($location eq "Geneve");
#	$location = "Vienna" if ($location =~ /Wien/);
#	$location = "Lisbon" if ($location eq "Lisboa");



	# add countries to lesser known places
	$location = "Zurich" if ($location =~ /Glattbrugg/);
	$location = "Stockholm" if ($location =~ /Solna/);
	$location = "Madrid" if ($location =~ /Las Rozas/);
	$location = "Helsinki" if ($location =~ /Helskinki/);
#	$location = "Helsinki, Finland" if ($location =~ /Helsinki/);
#	$location = "Zagreb, Croatia" if ($location =~ /Zagreb/);
	$location = "Copenhagen" if ($location =~ /Klampenborg/);
	$location = "Amsterdam" if ($location =~ /Hoofddorp/);


	# locale localisation
	
	# ITALIA
	if ($locale eq "italia") {
	    if ($location =~ /(Rome|Roma|Milan|Geneva|Zurich)/) { #    || 
		$location = "Roma" if ($location eq "Rome");
		$location = "Milano" if ($location eq "Milan");
		$location = "Zurigo" if ($location eq "Zurich");
		$location = "Ginevra" if ($location eq "Geneva");
		next if ($title =~ /Leveraging Technology For a Better Public Sector/); # 22 Nov 2003 - on Chiarabla Bollini's request
	    } else {
		# commented out by PRM on 19 June, until more briefings occur for italy
		# next;
		$location = "Londra"    if ($location eq "London");
		$location = "Bruxelles" if ($location eq "Brussels");
		
	    }
	}
	

	# DEUTCHLAND
	# add german city logic here... when we get some briefings
	if ($locale eq "de") {
            if ($location =~ /(Hamburg|Munich|Berlin|Frankfurt|Vienna|Duesseldorf)/) {
                $location = "M\&uuml\;nchen" if ($location eq "Munich");
                $location = "Wein" if ($location eq "Vienna");
                #$location = "Zurigo" if ($location eq "Zurich");
                #$location = "Ginevra" if ($location eq "Geneva");
            } else {
                # commented out by PRM on 19 June, until more briefings occur for italy
		# next;
		$location = "Br\&uuml\;ssel" if ($location eq "Brussels");
            }
        }



	$date = "\&nbsp\;"."$1" if ($date =~ /^0(.*)/); # dump precending 0 on dates - NO LONGER WORKS
	$date = "\&nbsp\;"."$date" if (substr($date, 0, index ($date, " ", 1)) < 10); # add space in from of dates less than 10

	$date = substr ($date, 0, (length($date) -5));

	    
	$detail{$name} .= <<EndofHTML;
	    
<tr>
 <td width="3" bgcolor="#f5f5f5"><img src="/images/trans_pixel.gif" width="3" height="1" border="0" alt=""></td>
 <td width="105"valign="top" bgcolor="#f5f5f5"><a href="$url" class="smallThinBlueLink">$location</a></td>
 <td width="90" valign="top" align="left" bgcolor="#f5f5f5"><span class="smallGrayText">$date&nbsp;</span></td>
</tr>
EndofHTML

    $xhtmlDetail{$name}.= <<EndofHTML;
        <tr><td width="50%" class="lbCityDate"><a href="$url">$location</a></td><td width="50%" class="lbCityDate">$date</td></tr>
EndofHTML

	$count{$name}++;

	# TITLE clean-ups, etc...
	$title =~ s/ - / \&\#151\; /g;
	$title = &uppercase($title);
	$title{$name} = $title;
	
    }


foreach $title (sort keys %title) {
	
	local $name = $title;
	$name =~ tr/[a-z]/[A-Z]/;
	#$title{$title} = &noHang($title{$title}, 30);
	$title{$title} = &titleTranslation($title{$title})  if ($locale);
	

	$line .= <<EndofHTML;

<!-- $title{$title} START -->
          
          <tr>
               <td width="3"><img src="/images/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td>
               <td width="195" colspan="2">
<img src="/images/trans_pixel.gif" width="191" height="3" border="0" alt="spacer"><br />
<span class="smallGrayText">
$title{$title}
</span>
<img src="/images/trans_pixel.gif" width="191" height="5" border="0" alt="spacer"><br />
                </td>
          </tr>

          <tr><td colspan="3" height="7" width="198" bgcolor="#f5f5f5"><img src="/images/trans_pixel.gif" width="194" height="7" border="0" alt="spacer"></td></tr>

$detail{$name}

           <tr><td colspan="3" height="7" width="198" bgcolor="#f5f5f5"><img src="/images/trans_pixel.gif" width="198" height="7" border="0" alt="spacer"></td>
           </tr>
           <tr><td colspan="3" width="198" height="1" bgcolor="#cecece"><img src="/images/trans_pixel.gif" width="194" height="1" border="0" alt="spacer"></td></tr>


<!-- $title{$title} END -->

EndofHTML

	$xhtmlLine .= <<EndofHTML;


<!-- $title{$title} START -->
    <table class="localbriefings" cellpadding="0" cellspacing="0" width="198" summary="Local Briefings - $title{$title}">
        <tr><td colspan="2" class="lbTitle">$title{$title}</td></tr>
$xhtmlDetail{$name}
    </table>

<!-- $title{$title} END -->

EndofHTML

}


# OUTPUT FILE

# pick filename
if ($locale eq "italia") {
    $fileName = "/home/gartner/html/rt/content/emea/it/localBriefingTable.html";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/it/xhtmlLocalBriefingTable.html";
} elsif ($locale eq "de") {
    $fileName = "/home/gartner/html/rt/content/emea/de/localBriefingTable.html";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/de/xhtmlLocalBriefingTable.html";
} else {
    $fileName = "/home/gartner/html/rt/content/emea/localBriefingTable.html";
    $xhtmlFileName = "/home/gartner/html/rt/content/emea/xhtmlLocalBriefingTable.html";
}

# save file
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
    if ($locale eq "italia") {
	
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
	
	$t = "Business Intelligence e Knowledge Management dal 2003 in poi"
	    if ($t =~ /Business Intelligence/); 


    }

    return ($t);



}

