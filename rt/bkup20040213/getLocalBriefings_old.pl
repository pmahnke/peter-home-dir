#!/usr/local/bin/perl

#use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
use lib '/usr/local/lib/perl5/5.6.1/';
require ("/home/gartner/html/rt/getEvents.pl");

# Variables
local $server = "www4";


$FORM{'page'} = "http:\/\/www4.gartner.com\/Events?pageName=calendar&previous=false&cboMonth=0&cboType=5&cboRegion=4";


&getEventsDetail($FORM{'page'});

$FORM{'date'} = 21000000 if (!$FORM{'date'}); # set date way out if none given
$startDate =  `date '+%y%m%d'`;
$startDate = 20000001 + $startDate;
$FORM{'limit'} = 3;

# new section
 
foreach $key (sort keys %event) {

    # embedded version with new look
    
    local ($title, $date, $url, $location) = split (/\t/, $event{$key});
    local $name = $title;
    local $dateKey = substr ($key, 0, 8);
    
    next if ($dateKey > $FORM{'date'});
    
    $name =~ tr/[a-z]/[A-Z]/;
    next if ($count{$name} > $FORM{'limit'}); # only allow a max of 5 per briefing
    
    $location =  $1 if ($location =~ /(.[^\,]*)\,/); # dump comma contry
    $location =~ s/[0-9]//g; # dump numbers
    
    # fix some bad spellings
    $location = "Rome" if ($location eq "Roma");
    $location = "Dusseldorf" if ($location eq "Duesseldorf");
    $location = "Geneva" if ($location eq "Geneve");


    # do country specific ones....
    if ($FORM{'locale'} eq "it") {
	
	if ($location eq "Rome" ||
	    $location eq "Florence" ||
	    $location eq "Milan" ||
	    $location eq "Venice") {
	} else {
	    next;
	}
	
    $date = "\&nbsp\;"."$1" if ($date =~ /^0(.*)/); # dump precending 0 on dates - NO LONGER WORKS
    
    $date = substr ($date, 0, (length($date) -5));
    
    $detail{$name} .= <<EndofHTML;
    
           <tr class="bgLightGrey">
                <td width="3"><img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td>
                <td width="131"valign="top" ><a href="$url" class="blueNormal">$location</a></td>
                <td width="50" class="blackNormal" valign="top" align="right">$date</td>
           </tr>
EndofHTML
    
    $count{$name}++;
    $title{$name} = $title;
	
}


foreach $title (sort keys %title) {
    
    local $name = $title;
    $name =~ tr/[a-z]/[A-Z]/;
    $title{$title} =~ s/ - / \&\#151\; /g;
    $title{$title} = &uppercase($title{$title});
    
    $title{$title} = &noHang($title{$title});

    $line .= <<EndofHTML;
    
<!-- $title{$title} START -->

          <tr class="bgMedGrey">
               <td width="3"><img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td>
               <td width="191" colspan="3" class="blackNormal">
<img src="//img/trans_pixel.gif" width="191" height="3" border="0" alt="spacer"><br />
$title{$title}<br />
<img src="//img/trans_pixel.gif" width="191" height="5" border="0" alt="spacer"><br />
                </td>
          </tr>

$detail{$name}

           <tr class="bgLightGrey">
                <td colspan="3" height="7" width="194"><img src="//img/trans_pixel.gif" width="194" height="7" border="0" alt="spacer"></td>
           </tr>


<!-- $title{$title} END -->

EndofHTML

}



open (OUTPUT, ">/home/gartner/html/rt/events/localBriefingTable.html") || die "Can't open OUTPUT to write\n";
print  OUTPUT $line;
close (OUTPUT);
print "Done.\n";


sub noHang {

    local @words = split (" ", $_[0]);
    local $charCount = 0;
    local $noHang = ""; 
    local $wordNumber = 0;

    foreach (@words) {
	
	local $len = length($_);
	
	if ($charCount + $len < 30 && $wordNumber < $#words - 1 ) {

	    $charCount = $charCount + $len;
	    $noHang .= " $_";

	} elsif ($wordNumber ==  $#words - 1) {

	    $noHang .= "<br \/\>\n$_";
	    $charCount = $len;

	} elsif ($wordNumber >  $#words - 1) {

	    $noHang .= " $_";
	    $charCount = $len;
	    
	} else {

	    $noHang .= " <br \/\>\n$_";
	    $charCount = $len;

	}

	$wordNumber++;
    }
    return($noHang);
	
}

sub uppercase {
    
    undef local ($ucTitle);
    undef local ($wordCount);
    
    local @words = split (" ", $_[0]);
    
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


sub oldLook {


foreach $key (sort keys %event) {
    
    local ($title, $date, $url, $location) = split (/\t/, $event{$key});
    local $name = $title;
    local $dateKey = substr ($key, 0, 8);
    
    next if ($dateKey > $FORM{'date'});
    
    $name =~ tr/[a-z]/[A-Z]/;
    next if ($count{$name} > $FORM{'limit'}); # only allow a max of 5 per briefing
    
    $location = $1 if ($location =~ /(.[^\,]*)\,/);
    $date = "\&nbsp\;"."$1" if ($date =~ /^0(.*)/); # dump precending 0 on dates
    
    $detail{$name} .= <<EndofHTML;
    
           <tr class="lightShading">
                <td><img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td>
                <td><img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td>
                <td valign="top"><a href="$url" class="linkTextSmall">$location</a></td>
                <td class="textBlackReg2" valign="top"> $date </td>
           </tr>

EndofHTML
    $count{$name}++;
    $title{$name} = $title;
	
}


foreach $title (sort keys %title) {
    
    local $name = $title;
    $name =~ tr/[a-z]/[A-Z]/;
    $title{$title} =~ s/ - / \&\#151\; /g;
    $title{$title} = &uppercase($title{$title});
    $line .= <<EndofHTML;

<!-- $title{$title} START -->
          <tr class="darkShading">
               <td><img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"></td> 
               <td colspan="3" class="textBlackReg2">$title{$title}</td>
          </tr>

$detail{$name}

<!-- $title{$title} END -->

EndofHTML

}


}
