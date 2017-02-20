#!/usr/local/bin/perl

########################################################################
#
# pickMQHCVR2.cgi
#
#   written: 09 Dec 2003 by Peter Mahnke
#   modified:
#            05 July 2005 by Peter Mahnke
#            conform with new gartner.com homepage layout
#
#
#   run from a web browser
#   currently only called through update_menu.cgi
#
#   DESCRIPTION
#     allows regional site editors to pick different Magic Quadrants,
#     Hype Cycles and Vendor Ratings than are on gartner.com and reset them
#
#     it reads the CSV lists produced by the getMQlist.pl and getVRlist.pl
#     and offers them as options to the regional site editors to overwrite
#     the default gartner.com selection
#
#     if an alternate selection is picked, it writes a new include (.incl)
#     file and puts a lock on that file that homepage_parser.pl respects
#
#     if homepage_parser.pl sees the lock, it saves the translated default
#     gartner.com include as <filename>.incl.latest
#
#     if an editor picks to go back to the gartner.com default, it moves
#     this <filename>.incl.latest file back and removed the lock file via
#     the script commonLock.pl
#
########################################################################

use CGI_Lite;
require('/home/gartner/html/rt/commonLock.pl');

########################################################################
# variables
$rootDir = "/home/gartner/html/rt/content/";

$fileMQ = "$rootDir"."MQ.csv";
$fileHC = "$rootDir"."HC.csv";
$fileVR = "$rootDir"."VR.csv";
$fileCV = "$rootDir"."CV.csv";

#$currentHC = "/home/gartner/html/rt/content/emea/home_hc_headlines.incl";
#$currentVR = "/home/gartner/html/rt/content/emea/home_vr_headlines.incl";


# TEXT

# Blurbs
$string{'blurbMQ'}{'emea'} = "Find out which vendors are leaders, visionaries, challengers or niche players.";
$string{'blurbMQ'}{'it'}   = "Scopri quali fornitori sono leader, \"visionari\", \"sfidanti\" e \"di nicchia\"";
$string{'blurbMQ'}{'de'}   = "Finden Sie heraus, welche Anbieter f\&uuml\;hrend, vision\&auml\;r, Herausforderer oder Nischenplayer sind";

$string{'blurbHC'}{'emea'} = "Gartner Hype Cycles clearly explain the difference between hype and the future of technology.";
$string{'blurbHC'}{'it'}   = "Gartner Hype Cycles illustra con chiarezza la differenza tra le aspettative non realistiche e il futuro della tecnologia.";
$string{'blurbHC'}{'de'}   = "Gartner Hype Cycles zeigen Unterschiede zwischen dem Hype und der Zukunft von Technologien auf";

$string{'blurbVR'}{'emea'} = "Gartner's latest ratings of vendors and technology providers.";
$string{'blurbVR'}{'it'}   = "Le ultime valutazioni Gartner sui principali fornitori.";
$string{'blurbVR'}{'de'}   = "Gartners neueste Bewertungen der f\&uuml\;hrenden Anbieter";

$string{'blurbCV'}{'emea'} = "Gartner introduces you to the most innovative, impactful, and intriguing vendors in 17 categories.";
$string{'blurbCV'}{'it'} = "Gartner introduces you to the most innovative, impactful, and intriguing vendors in 17 categories.";
$string{'blurbCV'}{'de'} = "Gartner introduces you to the most innovative, impactful, and intriguing vendors in 17 categories.";

# Latest
$string{'LatestMQ'}{'emea'} = "Latest Magic Quadrant:\&nbsp\;<\/b\><\/span\><br \/>";
$string{'LatestMQ'}{'it'}   = "Ultimo Magic Quadrant:\&nbsp\;<\/b\><\/span\><br \/>";
$string{'LatestMQ'}{'de'}   = "Aktuellster Magic Quadrant:<\/b\><\/span\><br \/\>";

$string{'LatestHC'}{'emea'} = "Latest Hype Cycle:\&nbsp\;<\/b\><br \/>";
$string{'LatestHC'}{'it'}   = "Ultimo Hype Cycle:\&nbsp\;<\/b\><br \/>";
$string{'LatestHC'}{'de'}   = "Aktuellster Hype Cycle:\&nbsp\;<\/b\><br \/\>";

$string{'LatestVR'}{'emea'} = "Latest Ratings";
$string{'LatestVR'}{'it'}   = "Ultime valutazioni";
$string{'LatestVR'}{'de'}   = "Aktuellste Vendor Ratings";

# special report
$string{'SpecialHC'}{'emea'} = "View the Special Report";
$string{'SpecialHC'}{'it'}   = "Visualizza lo Special Report";
$string{'SpecialHC'}{'de'}   = "Special Report: Gartner Hype Cycles";


# View all...
$string{'ViewAllMQ'}{'emea'} = "View All Magic Quadrants";
$string{'ViewAllMQ'}{'it'}   = "Visualizza tutti i Magic Quadrants";
$string{'ViewAllMQ'}{'de'}   = "Alle Magic Quadrants";


$string{'ViewAllHC'}{'emea'} = "View All Hype Cycles";
$string{'ViewAllHC'}{'it'}   = "Visualizza tutti gii Hype Cycles";
$string{'ViewAllHC'}{'de'}   = "Alle Hype Cycles";

$string{'ViewAllVR'}{'emea'} = "View All Vendor Ratings";
$string{'ViewAllVR'}{'it'}   = "Visualizza tutti i Vendor Ratings";
$string{'ViewAllVR'}{'de'}   = "Alle Vendor Ratings";

$string{'ViewAllCV'}{'emea'} = "View All Special Reports";
$string{'ViewAllCV'}{'it'}   = "Visualizza tutti gli Special Report";
$string{'ViewAllCV'}{'de'}   = "Alle Special Reports";


##############################################################
# Get the input from the HTML Form
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;

    $FORM{'locale'} = "emea" if (!$FORM{'locale'});

    # what to do

    # deal with going back to the latest
    $FORM{'code'} = "latest" if ($FORM{'code1'} eq "latest");
    if ($FORM{'override'} && $FORM{'code'} eq "latest") {

		# set flag
		$flagLatest = 1;

    	# this will delete/unlink the lock file
    	$FORM{'code'}  = 0;
    	$VRcodes       = 0;

    }


    if ($FORM{'pickMQ'}) {

        &openFile($fileMQ);
        if ($FORM{'locale'} eq "emea") {
            $currentMQ = "/home/gartner/html/rt/content/emea/home_sixpack_magicquadrants_headlines.incl";
        } else {
            $currentMQ = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_magicquadrants_headlines.incl";
        }
        &openCurrent($currentMQ);
        $FORM{'type'} = "MQ";
        &printForm;
        exit;

    } elsif ($FORM{'override'} && $FORM{'type'} eq "MQ") {

    	&openFile($fileMQ);
    	&formatMQ;
        if ($FORM{'locale'} eq "emea") {
            $currentMQ = "/home/gartner/html/rt/content/emea/home_sixpack_magicquadrants_headlines.incl";
        } else {
            $currentMQ = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_magicquadrants_headlines.incl";
        }
    	&writeInclude($currentMQ);
    	$msg = "lock failed<p\>" if (!&writeLock('MQ', $FORM{'locale'}, $FORM{'code'}));
    	&printResults;
    	exit;


   } elsif ($FORM{'pickHC'}) {

        &openFile($fileHC);
        if ($FORM{'locale'} eq "emea") {
            $currentHC = "/home/gartner/html/rt/content/emea/home_sixpack_hypecycles_headlines.incl";
        } else {
            $currentHC = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_hypecycles_headlines.incl";
        }
        &openCurrent($currentHC);
        $FORM{'type'} = "HC";
        &printForm;
        exit;

    } elsif ($FORM{'override'} && $FORM{'type'} eq "HC") {

    	&openFile($fileHC);
    	&formatHC;
    	if ($FORM{'locale'} eq "emea") {
            $currentHC = "/home/gartner/html/rt/content/emea/home_sixpack_hypecycles_headlines.incl";
        } else {
            $currentHC = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_hypecycles_headlines.incl";
        }
    	&writeInclude($currentHC);
    	&writeLock('HC', $FORM{'locale'}, $FORM{'code'});
    	&printResults;
    	exit;

     } elsif ($FORM{'pickVR'}) {

        &openFile($fileVR);
        if ($FORM{'locale'} eq "emea") {
            $currentVR = "/home/gartner/html/rt/content/emea/home_sixpack_vendorratings_headlines.incl";
        } else {
            $currentVR = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_vendorratings_headlines.incl";
        }
		&openCurrent($currentVR);
        $FORM{'type'} = "VR";
        &printForm;
        exit;

    } elsif ($FORM{'override'} && $FORM{'type'} eq "VR") {

    	&openFile($fileVR);
    	&formatVR;
        if ($FORM{'locale'} eq "emea") {
            $currentVR = "/home/gartner/html/rt/content/emea/home_sixpack_vendorratings_headlines.incl";
        } else {
            $currentVR = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_vendorratings_headlines.incl";
        }
        &writeInclude($currentVR);
        $VRcodes = "$FORM{'code1'}\t$FORM{'code2'}\t$FORM{'code3'}" if (!$flagLatest);
    	&writeLock('VR', $FORM{'locale'}, $VRcodes);
    	&printResults;
    	exit;

    } elsif ($FORM{'pickCV'}) {

        &openFile($fileCV);
        if ($FORM{'locale'} eq "emea") {
            $currentVR = "/home/gartner/html/rt/content/emea/home_sixpack_coolvendors_headlines.incl";
        } else {
            $currentVR = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_coolvendors_headlines.incl";
        }
		&openCurrent($currentCV);
        $FORM{'type'} = "CV";
        &printForm;
        exit;

    } elsif ($FORM{'override'} && $FORM{'type'} eq "CV") {

        &openFile($fileCV);
        if ($FORM{'locale'} eq "emea") {
            $currentCV = "/home/gartner/html/rt/content/emea/home_sixpack_coolvendors_headlines.incl";
        } else {
            $currentCV = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_coolvendors_headlines.incl";
        }
		&openCurrent($currentCV);
        $FORM{'type'} = "CV";
        &printForm;
        exit;

    }





} else {

    $FORM{'pickVR'} = 1;
    $FORM{'type'} = "VR";
    $FORM{'locale'} = "emea";
    &openFile($fileVR);
        if ($FORM{'locale'} eq "emea") {
            $currentVR = "/home/gartner/html/rt/content/emea/home_sixpack_vendorratings_headlines.incl";
        } else {
            $currentVR = "/home/gartner/html/rt/content/emea/"."$FORM{'locale'}"."/home_sixpack_vendorratings_headlines.incl";
        }
    &openCurrent($currentVR);

   &printForm;

}
exit;




########################################################################
sub printResults {

	if ($flagLatest) {
		$line = "<tr\><td\>using default<\/td\><\/tr\>";
	}
print <<ENDofHTML;
Content-type:  text/html

<html>
<head>
<script src="/pages/docs/gartner/hc/scripts/utils.js"></script>
<script src="/pages/docs/gartner/mq/scripts/utils.js"></script>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt;	}
h3	{		font-size: 10pt;	}
li	{		font-size: 9pt;	        }
</style>
</head>
<body>
<h2>now</h2>
<table cellpadding="0" cellspacing="0">
$line
</table>

$msg

</body>
</html>
ENDofHTML


}

########################################################################
sub printForm {

if (&testLock($FORM{'type'}, $FORM{'locale'})) {
	$lock = "file override ON";
} else {
	$lock = "file override OFF";
}

print <<ENDofHTML;
Content-type:  text/html

<html>
<head>
<script src="http://www.gartner.com/pages/docs/gartner/hc/scripts/utils.js"></script>
<script src="http://www.gartner.com/pages/docs/gartner/mq/scripts/utils.js"></script>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt;	}
h3	{		font-size: 10pt;	}
li	{		font-size: 9pt;	        }
#current { padding: 10px; font-size: 10px; width: 300px; background: #eee; border: 1px solid #333;  }
</style>

</head>
<body>
<form action="/rt/pickMQHCVR2.cgi" method="POST">

<input type="hidden" name="locale" value="$FORM{'locale'}" />
<input type="hidden" name="type" value="$FORM{'type'}" />

<h1>$FORM{'type'}</h1>
<h2>local - $FORM{'locale'}</h2>

<h3>currently - $lock</h3>
<div id="current">
$current
</div>


<h3>override</h3>
<ol>
$startline
$line
</ol>
<input type="submit" name="override" value="override">
<input type="submit" name="xhtml" value="xhtml">

</form>
</body>
</html>
ENDofHTML
}


########################################################################
sub openFile {

    # 113833	20030320	Noninvasive Legacy Web Enablement Is Still Viable

    open (FILE, "$_[0]") || die "can't open file: $_[0]\n";
    while (<FILE>) {

		chop();
		local ($code, $date, $title) = split (/\t/);

        # remove MQ from title
        $title =~ s/MQ for//;
        $title =~ s/Magic Quadrant for//;
        $title =~ s/ Magic Quadrant//;

        # remove Dates from title
        $title =~ s/, 200\d://;
        $title =~ s/, 200\d//;
        $title =~ s/, \d\w\d\d//;
        $title =~ s/\d\w\d\d//;

        # remove HC from title
        $title =~ s/Hype Cycle for//;

        # remove VR from title
        $title =~ s/Vendor Rating\: //;
        $title =~ s/Vendor Rating Update\: //;

        # remove CV from title
        $title =~ s/Management Update: Cool Vendors in //;
        $title =~ s/Cool Vendors in //;
        $title =~ s/Cool Vendors Will //;



		local $nicedate = &processDate($date);
		$title{$code} = $title;

        if ($FORM{'pickVR'}) {

        	$line .= <<ENDofLINE;
<li> <input type="radio" name="code1" value="$code"/> <input type="radio" name="code2" value="$code"/><input type="radio" name="code3" value="$code"/><a href="/1_researchanalysis/vendor_rating/$code" target="_blank">$title</a> [$nicedate]</li>
ENDofLINE

		} elsif ($FORM{'pickCV'}) {

        	$line .= <<ENDofLINE;
<li> <input type="radio" name="code1" value="$code"/> <input type="radio" name="code2" value="$code"/><input type="radio" name="code3" value="$code"/><a href="http://www.gartner.com/DisplayDocument?id=$code" target="_blank">$title</a> [$nicedate]</li>
ENDofLINE

       } elsif ($FORM{'pickHC'}) {

        	$line .= <<ENDofLINE;
<li> <input type="radio" name="code" value="$code"/><a href="javascript:void(null)" onclick="popUpHypeCycle($code)">$title</a> [$nicedate]</li>
ENDofLINE

       } else {

       	# must be mq
       	$line .= <<ENDofLINE;
<li> <input type="radio" name="code" value="$code"/><a href="javascript:void(null)" onclick="popUpQuadrant($code)">$title</a> [$nicedate]</li>
ENDofLINE

	}



    }
    close(FILE);

    if ($FORM{'pickVR'} || $FORM{'pickCV'}) {

        	$startline .= <<ENDofLINE;
<li> <input type="radio" name="code1" value="latest"/> <strong>use latest instead</strong></li>
ENDofLINE
       } else {
        	$startline = <<ENDofLINE;
<li> <input type="radio" name="code" value="latest"/> <strong>use latest instead</strong></li>
ENDofLINE
       }

}

########################################################################
sub openCurrent {

	open (CUR, "$_[0]") || die "can't open current file: $_[0]\n";
	while (<CUR>) {
	    $current .= $_;
	}
	close (CUR);

	# check to see if there is a latest file....
	local $latest = "$_[0]"."\.latest";
	if (-e "$latest") {
	    # a latest file exists
	    $current .= "<h3\>Latest<\/h3\>\n";
	    open (CUR, "$_[0]"."\.latest") || die "can't open latest file: $_[0]\n";
	    while (<CUR>) {
			$current .= $_;
	    }
	    close (CUR);
	}

    }

########################################################################
sub writeInclude {

    # write includes to locale directory
    # inputs are filename

    if ($flagLatest) {

    	# need to copy latest to current
    	`cp $_[0].latest $_[0]`;
    	$msg .= "cp $_[0].latest $_[0]<br />\n";

    } else {

		# copy current to latest if it doesn't exitst
		local $lfn = "$_[0]"."\.latest";

		`cp $_[0] $_[0].latest` if (!-e "$lfn");
		$msg .= "cp $_[0] $_[0].latest<br />\n" if (!-e "$lfn");

    	# write new file

    	open (OUT, ">$_[0]") || die "Can't write file: $_[0]\n";
    	print OUT $line;
    	close (OUT);

		$msg .= "write: $_[0]<br\/> $line <br\/>\n";

    }

    return;
}

########################################################################
sub processDate {

    local ($d, $m, $y);
    $y = substr ($_[0], 0, 4);
    $m = substr ($_[0], 4, 2);
    $d = substr ($_[0], 6, 2);


    $m{'01'} = "January"; # = "01";
    $m{'02'} = "February"; # = "02";
    $m{'03'} = "March"; # = "03";
    $m{'04'} = "April"; # = "04";
    $m{'05'} = "May"; # = "05";
    $m{'06'} = "June"; # = "06";
    $m{'07'} = "July"; # = "07";
    $m{'08'} = "August"; # = "08";
    $m{'09'} = "September"; # = "09";
    $m{'10'} = "October"; # = "10";
    $m{'11'} = "November"; # = "11";
    $m{'12'} = "December"; # = "12";

    local $newdate = "$d $m{$m} $y";
    return($newdate);

}

########################################################################
sub formatMQ {


#<div class="caption10px">$string{'blurbMQ'}{$FORM{'locale'}}</div>

	$line = <<ENDofHTML;
<ul>
    <li> <a href="/DisplayDocument?id=$FORM{'code'}" onclick="openResult('/DisplayDocument?id=$FORM{'code'}'); return false;" target="_new" class="blueLink55pctBold">$title{$FORM{'code'}}</a></li>
    <li> <a href="/mq/asset_50486.jsp" class="blueLink55pctBold"> $string{'ViewAllMQ'}{$FORM{'locale'}}</a></li>
</ul>

ENDofHTML

}

########################################################################
sub formatHC {


#<div class="caption10px">$string{'blurbHC'}{$FORM{'locale'}}</div>
	$line = <<ENDofHTML;

<ul>
    <li> <a href="/DisplayDocument?id=$FORM{'code'}" onclick="openResult('/DisplayDocument?id=$FORM{'code'}'); return false;" target="_new" class="blueLink55pctBold">$title{$FORM{'code'}}</a></li>
    <!-- <li><a href="#" class="blueLink55pctBold">$string{'SpecialHC'}{$FORM{'locale'}}</a></li> -->
    <li><a href="/hc/asset_50595.jsp" class="blueLink55pctBold">$string{'ViewAllHC'}{$FORM{'locale'}}</a></li>
</ul>


ENDofHTML


}


########################################################################
sub formatVR {



#<div class="caption10px">$string{'blurbVR'}{$FORM{'locale'}}</div>

	$line = <<ENDofHTML;

<ul>
    <li><a href="/DisplayDocument?id=$FORM{'code1'}" onclick="openResult('/DisplayDocument?id=$FORM{'code1'}'); return false;" target="_new" class="blueLink55pctBold"> $title{$FORM{'code1'}}</a></li>
    <li><a href="/DisplayDocument?id=$FORM{'code2'}" onclick="openResult('/DisplayDocument?id=$FORM{'code1'}'); return false;" target="_new" class="blueLink55pctBold"> $title{$FORM{'code2'}}</a></li>
    <li><a href="/DisplayDocument?id=$FORM{'code3'}" onclick="openResult('/DisplayDocument?id=$FORM{'code1'}'); return false;" target="_new" class="blueLink55pctBold"> $title{$FORM{'code3'}}</a></li>
</ul>

ENDofHTML

}


########################################################################
sub formatCV {


#<div class="caption10px">$string{'blurbCV'}{$FORM{'locale'}}</div>
	$line = <<ENDofHTML;

<ul>
    <li><a href="/DisplayDocument?id=$FORM{'code1'}" onclick="openResult('/DisplayDocument?id=$FORM{'code1'}'); return false;" target="_new" class="blueLink55pctBold"> $title{$FORM{'code1'}}</a></li>
    <li><a href="/DisplayDocument?id=$FORM{'code2'}" onclick="openResult('/DisplayDocument?id=$FORM{'code1'}'); return false;" target="_new" class="blueLink55pctBold"> $title{$FORM{'code2'}}</a></li>
    <li><a href="/DisplayDocument?id=$FORM{'code3'}" onclick="openResult('/DisplayDocument?id=$FORM{'code1'}'); return false;" target="_new" class="blueLink55pctBold"> $title{$FORM{'code3'}}</a></li>
</ul>

ENDofHTML

}


########################################################################
