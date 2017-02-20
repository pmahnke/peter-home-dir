#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/html/rt/getEvents.pl");

# Variables
local $server = "www4";


# expects full url to doc
# i.e. http://www4.gartner.com/DisplayDocument?id=361453&acsFlg=accessBought



##############################################################
# Get the input from the HTML Form
local $buffer = $ENV{'QUERY_STRING'};

# Split the name - value pairs
if ($buffer) {		  # assumes that form has been filled out
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);

	$value =~ s/\+/ /g; # spaces
	$value =~ s/\&lt\;/\</g; # less thans
	$value =~ s/\&amp\;/\&/g; # ampersans
	$value =~ s/%(..)/pack("c",hex($1))/ge; # rest

	$FORM{$name} = $value;
    }

} else {


    print <<EndofHTML;
Content-type:  text/html

<html>
<body>
<form method=GET>

Enter Full URL: <input type=text width=200 name=page value="http://www4.gartner.com/Events?pageName=calendar&previous=false&cboMonth=0&cboType=5&cboRegion=4"><p>
Enter Last Date to Pull: (format YYYYMMDD) <input type=text width=200 name=date><p>
Limit Max Number:  <input type=text width=2 name=limit value=4><p>
New Look: <input type=checkbox name=style value=on><p>
<input type=submit>
</form>
</body>
</html>

EndofHTML

    exit;

}


&getEventsDetail($FORM{'page'});

$FORM{'date'} = 21000000 if (!$FORM{'date'}); # set date way out if none given
$startDate =  `date '+%y%m%d'`;
$startDate = 20000001 + $startDate;
$FORM{'limit'}--;

if (!$FORM{'embed'} && $FORM{'style'} ne "on") {

    foreach $key (sort keys %event) {

	local ($title, $date, $url, $location) = split (/\t/, $event{$key});
	local $name = $title;
	local $dateKey = substr ($key, 0, 8);
	
	next if ($dateKey > $FORM{'date'} || $dateKey < $startDate);

	$name =~ tr/[a-z]/[A-Z]/;
	next if ($count{$name} > $FORM{'limit'}); # only allow a max of 5 per briefin
	$location = $1 if ($location =~ /(.[^\,]*)\,/); # dump , country on locations
	$date = "\&amp\;nbsp\;"."$1" if ($date =~ /^0(.*)/); # dump precending 0 on dates

	$detail{$name} .= <<EndofHTML;

           &lt;tr class="lightShading"&gt;
                &lt;td&gt;&lt;img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"&gt;&lt;/td&gt;
                &lt;td&gt;&lt;img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"&gt;&lt;/td&gt;
                &lt;td valign="top" &gt;&lt;a href="$url" class="linkTextSmall"&gt;$location&lt;/a&gt;&lt;/td&gt;
                &lt;td class="textBlackReg2" valign="top"&gt; $date &lt;/td&gt;
           &lt;/tr&gt;

EndofHTML
    $count{$name}++;
	$title{$name} = $title;
	
    }


    foreach $title (sort keys %title) {
	
	local $name = $title;
	$name =~ tr/[a-z]/[A-Z]/;
	$title{$title} =~ s/ \- / \&amp\;\#151\; /g; # turn dash into m-dash
	$title{$title} = &uppercase($title{$title});
	$line .= <<EndofHTML;

&lt;!-- $title{$title} START --&gt;
          &lt;tr class="darkShading"&gt;
               &lt;td&gt;&lt;img src="//img/trans_pixel.gif" width="3" height="1" border="0" alt="spacer"&gt;&lt;/td&gt; 
               &lt;td colspan="3" class="textBlackReg2"&gt;$title{$title}&lt;/td&gt;
          &lt;/tr&gt;

$detail{$name}

&lt;!-- $title{$title} END --&gt;

EndofHTML

}

    print  <<EndofHTML;
    Content-type:  text/html

<html>
<head>
<title>output</title>
</head>
<body>
<p>
 <pre>

$line

</pre>
</body>
</html>


EndofHTML

} elsif ($FORM{'style'} eq "on") {

    # embedded version with new look
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
	$location = "Opfikon\-Glattbrugg,<br /> &nbsp; Switzerland" if ($location =~ / Opfikon\-Glattbrugg/);

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


	$title =~ s/ - / \&\#151\; /g;
	$title = &uppercase($title);
	$title{$name} = $title;
	
    }


    foreach $title (sort keys %title) {
	
	local $name = $title;
	$name =~ tr/[a-z]/[A-Z]/;
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

    print  <<EndofHTML;
    Content-type:  text/html

$line

EndofHTML
    
    

} else {

    # embedded version
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

    print  <<EndofHTML;
    Content-type:  text/html

$line

EndofHTML

}


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
