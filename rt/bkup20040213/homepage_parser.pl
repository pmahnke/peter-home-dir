#!/usr/local/bin/perl

########################################################################
#
#    homepage_parser.pl
#
#        writen:    09 Dec 2003 by Peter Mahnke
#        modified:  07 Jan 2004 by Peter Mahnke
#                    - added <br /> to push MQ headlines to second line
#                    - added <br /> to push HC headlines to second line
#                    - added <br /> to push VR headlines to second line
#                   18 Jan 2004 by Peter Mahnke
#                    - added FTP to campsqa
#
#
#
#        run from command line, or cron
#
#        script gets the unrecognised homepage of gartner.com and
#        parses out all the sections used by the regional sites
#        then translates the required sections for the local
#        language sites
#
#        this script is required as of 8 Dec 2003 the gartner.com
#        homepages are created by CAMPS and only product a flattened
#        jsp page
#
#        the gartner.com team left comment tags for us to parse
#        sections out
#
#        if an alternate selection is picked via the pickMQHCVR.cgi,
#        it writes a new include (.incl) file and puts a lock on that
#        file that homepage_parser.pl respects
#
#        if homepage_parser.pl sees the lock, via the script
#        commonLock.pl it saves the translated default gartner.com
#        include as <filename>.incl.latest
#
#
#        TODO
#          -  add logic to try other servers if regionals4 is down
#          -  deal with spacing on long MQ, HC and VR latest listings
#          -  create require version
#
########################################################################


require ('/home/gartner/cgi-bin/glogin_regionals.pl');
require ('/home/gartner/html/rt/commonLock.pl');

########################################################################
# variables
$URL = "http:\/\/regionals4.gartner.com\/UnrecognizedUserHomePage.jsp";
undef local $document;
undef local @doc;

########################################################################
# override with known good data.... need to fix up
if ($FORM{'intl'}) {
    $URL = "http:\/\/intl.gartner.com\/rt\/content\/emea\/focus_areas.inc" if ($FORM{'url'} =~ /focus_areas/);
    $URL = "http:\/\/intl.gartner.com\/rt\/content\/emea\/mq_vr.inc" if ($FORM{'url'} =~ /mq_vr/);
}


########################################################################
# get contents of the $URL page
$document = &getGARTNERpage($URL, $ARGV[1]);

# change DOS newlines to UNIX
$document =~ s//\n/g;

########################################################################
#process document
@doc = split (/\n/, $document); # split on newlines

foreach (@doc) {

    #s/\cM//g;

    $inBodyFlag = 1 if (/BEGIN BODY/);
    $inBodyFlag++ if ($inBodyFlag);

    next if ($inBodyFlag < 2);

    if (/END BODY/ ) {
	last;
    }


    #####################################################################
    # Parse out these sections from flatted gartner.com homepage


    # FOCUSAREAS

    # END OF FOCUS AREA
    if (/END FOCUS AREA PACKAGE BLOCK/) {

	$flagFocusArea = 0;
	&write('emea/home_focus_areas.incl', $line);
	&FTPfile('home_focus_areas.incl');
	# &transFocusArea; # currently there are none

    }

    # IN FOCUS AREA
    if ($flagFocusArea) {

	$line .= $_;

    }

    # START OF FOCUS AREA
    if (/BEGIN FOCUS AREA BLOCK/) {

	$flagFocusArea = 1;
	undef $line;

	$line =<<EOF;
<!-- start focus area header -->
<style>
    .smallYellowLink 
      {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; 
         font-size: 70%; color: #D9EF68; text-decoration: none;  }
    .smallYellowLink:hover 
      {  text-decoration: underline;  }
    .smWhiteText 
      {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: normal; 
         font-size: 65%; color: #FFFFFF; text-decoration: none;  }
</style>

<script src="/pages/docs/common/faf/scripts/utils.js"></script>

<table width="200" border="0" cellspacing="0" cellpadding="0">
 <tr> 
  <td bgcolor="#FFFFFF" width="2"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
  <td bgcolor="#FFFFFF" width="196" height="2"><img src="/images/trans_pixel.gif" width="196" height="2" alt="" border="0"></td>
  <td bgcolor="#FFFFFF" width="2"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
 </tr>
 <tr> 
  <td bgcolor="#FFFFFF" width="2"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
  <td width="196" height="33"><a href="/research/focus_areas/asset_51707.jsp"><img src="http://www.gartner.com/images/homepage/newFA_v3.gif" width="196" height="55" alt="New Focus Areas" border="0"></a></td>
  <td bgcolor="#FFFFFF" width="2"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
 </tr>
 <tr> 
  <td bgcolor="#FFFFFF" width="2"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
  <td width="196" height="53" bgcolor="#7A8894" valign="top">
   <table border="0" cellspacing="0" cellpadding="0">
    <tr>
      <td valign="top"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>
<td width="12" align="left" valign="top"><img src="/images/white_arrow.gif" width="4" height="6" vspace="3"></td>
      <td valign="top"><a href="javascript:openFaf();" class="smallYellowLink">Focus Area Guide</a><br><img src="/images/trans_pixel.gif" width="1" height="3" alt="" border="0"><br><span class="smWhiteText">Get help finding the<br> Gartner research you want</span></td>
    </tr>
   </table>
  </td>
  <td bgcolor="#FFFFFF" width="2"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
 </tr>
</table>
<!-- end focus area header -->

EOF


    }


    # MEMBERSHIP PROGRAMS

    # END OF MEMBERSHIP PROGRAMS
    if (/END MEMBERSHIP PROGRAM ASSET/) {

	$flagMemProg = 0;
	&write('emea/home_membershipprogram.incl', $line);
	&FTPfile('home_membershipprogram.incl');
	&transMemProg;

    }

    # IN MEMBERSHIP PROGRAMS
    if ($flagMemProg) {

	$line .= "$_\n";

    }

    # START OF MEMBERSHIP PROGRAMS
    if (/BEGIN MEMBERSHIP PROGRAMS BLOCK/) {

	$flagMemProg = 1;
	undef $line;

    }


    # G2

    # get headlines only

    # END OF PRESS G2 HEADLINE
    if (/END GARTNER G2 ASSET/) {

	$flagG2 = 0;
	&write('emea/home_g2_headlines.incl', $line);
	&xhtmlG2Ver('xhtml_g2_headlines.incl', $line);
	&FTPfile('home_g2_headlines.incl');
    }

    # IN G2
    if ($flagG2) {

	$line .= $_;

    }

    # START OF G2
    if (/START GARTNER G2 ASSET/) {

	$flagG2 = 1;
	undef $line;

    }



    # PRESS RELEASES

    # get headlines only

    # END OF PRESS RELEASES
    if (/END PRESS RELEASE ASSET/) {

	$flagPressRel = 0;
	&write('emea/home_announcements_headlines.incl', $line);
	&FTPfile('home_announcements_headlines.incl');
	#&transPressRel;
	&xhtmlPRVer('xhtml_announcements_headlines.incl', $line);

    }

    # IN PRESS RELEASES
    if ($flagPressRel) {

	$line .= $_;

    }

    # START OF PRESS RELEASES
    if (/BEGIN PRESS RELEASE ASSET/) {

	$flagPressRel = 1;
	undef $line;

    }



    # INVESTOR RELATIONS
    if (/END INVESTOR RELATIONS BLOCK/) {
	&write('emea/home_investor_relations.incl', $line);
	&FTPfile('home_investor_relations.incl');
	$flagInvestorRel = 0;
    }

    # IN INVESTOR RELATIONS
    if ($flagInvestorRel) {

	# just get headline

	# <td width="186" bgcolor="#FFFFFF"><a href="/5_about/investor_information/44a.html" class="smallBlueLink">Investor Relations</a><br><span class="smallGrayText">Gartner announces its full year financial results on Thursday, 5 February 2004. </span></td>

	if (/Investor Relations/) {

	    $line = "<br /><span class\=\"smallGrayText\">".$1."</span>" if (/Text\">(.[^<]*)</);

	}
    }

    if (/BEGIN INVESTOR RELATIONS BLOCK/) {

        $flagInvestorRel = 1;
        undef $line;

    }





    # CENTER COURT PROMO
    if (/END MAIN IMAGE BLOCK/) {

        $flagCenterCourt = 0;
        &write('emea/home_spotlight.incl', $line);
        &FTPfile('home_spotlight.incl');
        #&transCenterCourt;

    }

    # IN CENTER COURT
    if ($flagCenterCourt) {

        $line .= $_;

    }

    # START OF CENTER COURT
    if (/BEGIN MAIN IMAGE BLOCK/) {

		$flagInvestorRel = 0;
        $flagCenterCourt = 1;
        undef $line;

    }


    # MAGIC QUADRANTS

    # structure is
    # BEGIN MQ BLOCK
    # BEGIN MQ ASSET
    # END MQ ASSET


    # END OF MAGIC QUADRANTS HEADLINES
    if (/END MQ ASSET/) {

	$flagMQhead = 0;
	if (!&testLock('MQ', 'emea')) {
	    &write('emea/home_mq_headlines.incl', $line);
	    &FTPfile('home_mq_headlines.incl');
	} else {
	    # lock file exists, so write to a temp file
	    &write('emea/home_mq_headlines.incl.latest', $line);
	}
        &transMQ('home_mq_headlines.incl');
    }

    # END OF MQ TITLE/BEGIN MQ HEADLINES
    if (/BEGIN MQ ASSET/) {

        $flagMQtitle = 0;
	$flagMQhead  = 1;

	&write('emea/home_mq_title.incl', $line);
	&FTPfile('home_mq_title.incl');
	&transMQ('home_mq_title.incl');
	undef $line;
	next;

    }

    # IN MQ
    if ($flagMQtitle || $flagMQhead ) {

	s/span\><a/span\><br \/\><a/;

	$line .= $_;

    }

    # START OF MAGIC QUADRANTS
    if (/BEGIN MQ BLOCK/) {

        $flagMQtitle = 1;
	undef $line;

    }


    # HYPE CYCLES

    # structure is
    # BEGIN HYPE CYCLE BLOCK
    # BEGIN HYPE CYCLE ASSET
    # END HYPE CYCLE ASSET


    # END OF HYPE CYCLES HEADLINES
    if (/END HYPE CYCLE ASSET/) {

	$flagHChead = 0;
	if (!&testLock('HC', 'emea')) {
	    &write('emea/home_hc_headlines.incl', $line);
	    &FTPfile('home_hc_headlines.incl');
	} else {
	    # lock file exists, so write to a temp file
	    &write('emea/home_hc_headlines.incl.latest', $line);
	}
	&transHC('home_hc_headlines.incl');

    }

    # END OF HC TITLE/BEGIN HC HEADLINES
    if (/BEGIN HYPE CYCLE ASSET/) {

        $flagHCtitle = 0;
	$flagHChead  = 1;
	&write('emea/home_hc_title.incl', $line);
	&FTPfile('home_hc_title.incl');
	&transHC('home_hc_title.incl');
	undef $line;
	next;

    }

    # IN HC
    if ($flagHCtitle || $flagHChead ) {

	s/span\><a/span\><br \/\><a/;

	$line .= $_;

    }

    # START OF HYPE CYCLES
    if (/BEGIN HYPE CYCLE BLOCK/) {

        $flagHCtitle = 1;
	undef $line;

    }

    # VENDOR RATING

    # structure is
    # BEGIN VENDOR RATING BLOCK
    # BEGIN VENDOR RATING ASSET
    # END VENDOR RATING BLOCK
    # additional HTML for a grey line, table ends etc....
    # BEGIN WEBLOG BLOCK - using this to catch all missing data


    # END OF VENDOR RATING HEADLINES
    if (/BEGIN WEBLOG BLOCK/) {

	&transVR('home_vr_headlines.incl');
	$flagVRhead = 0;
	undef $line;
	$flagWeblog = 1;

    }

    # END OF VR TITLE/BEGIN VR HEADLINES
    # if (/BEGIN VENDOR RATING ASSET/) {
    if ($flagVRtitle && $_ =~ /table/) {

	$flagVRtitle = 0;
	&write('emea/home_vr_title.incl', $line);
	&FTPfile('home_vr_title.incl');
	&transVR('home_vr_title.incl');
	$flagVRhead  = 1;
	undef $line;
	next;

    }

    # IN VR TITLE
    if ($flagVRtitle) {
	$line .= $_;
    }


    # IN VR HEADLINES
    if ($flagVRhead ) {

	if (/Latest Ratings:/) {
	    $flagVRlr = 1;
	    next;
	}

	if (/arrow_trans_k.gif/ && $flagVRlr) {

	    s/<\/td\>//;
	    push @vrLink, $_;

	}

    }

    # START OF VENDOR RATING
    if (/BEGIN VENDOR RATING BLOCK/) {

        $flagVRtitle = 1;
	undef $line;

    }



    # WEBLOGS

    # END OF WEBLOGS
    if (/BEGIN RESEARCH COLLECTIONS BLOCK/) {

	$flagWeblog = 0;
	&write('emea/home_weblog.incl', $line);
	&FTPfile('home_weblog.incl');
	&transWeblog('home_weblog.incl');
	$flagResCol = 1;

    }

    # IN WEBLOGS
    if ($flagWeblog == 2) {

	$line .= "$_\n";

    }

    # START OF WEBLOGS
    if (/BEGIN WEBLOG BLOCK/ || $flagWeblog == 1) {

	$flagWeblog = 2;
	undef $line;

    }




    # RESEARCH COLLECTIONS

    # END OF RESEARCH COLLECTIONS
    if (/BEGIN GARTNER EXECUTIVE REPORTS/) {

	$flagResCol = 0;
	&write('emea/home_research_collections.incl', $line);
	&FTPfile('home_research_collections.incl');
	&transResCol('home_research_collections.incl');
	$flagExecRpt = 1;

    }

    # IN RESEARCH COLLECTIONS
    if ($flagResCol == 2) {

	$line .= $_;

    }

    # START OF RESEARCH COLLECTIONS
    if (/BEGIN RESEARCH COLLECTIONS BLOCK/ || $flagResCol == 1) {

	$flagResCol = 2;
	undef $line;

    }




    # EXECUTIVE REPORTS

    # END OF EXECUTIVE REPORTS
    if (/END GARTNER EXECUTIVE REPORTS/) {

	$flagExecRpt = 0;
	$line .= <<ENDofHTML;

<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="360" height="2" bgcolor="#ffffff"><img src="/images/trans_pixel.gif" width="360" height="10" alt="" border="0"></td>
</tr>
</table>

ENDofHTML
	&write('emea/home_gartnerexecutivereports.incl', $line);
	&FTPfile('home_gartnerexecutivereports.incl');
	&transExecRpt('home_gartnerexecutivereports.incl');

    }

    # IN EXECUTIVE REPORTS
    if ($flagExecRpt == 2) {

	$line .= $_;

    }

    # START OF EXECUTIVE REPORTS
    if (/BEGIN GARTNER EXECUTIVE REPORTS/ || $flagExecRpt == 1) {

	$flagExecRpt = 2;
	undef $line;

    }









	# fix images
	if (/src\=\"\/images\/trans_pixel.gif/i) {

	    # trans_pixel.gif
	    # s/\/images\/trans_pixel.gif/\.\/img\/trans_pixel.gif/g;
	    # $msg .= "trans_pixel fixed: $_\n\n";

	} elsif (/src\=\"images/) {

	    s/src\=\"images/src\=\"\/images/g;
	    # $msg .= "src\=\"images fixed: $_\n\n";

	} elsif (/src\=\"\//i) {
	    # absolute refs
	    # $msg .= "\n\nimg abs refs: $_\n";
	    # leave alone 31/5 - s/(src\=\")\/(.[^\"]*)\"/$1$website$2\"/gi;
	    # $msg .= "\t$_\n\n";

	} elsif (/src\=\"/i) {
	    # relative refs
	    #$msg .= "\n\nimg rel refs: $_\n";
	    # s/(src\=\")(.[^\"]*)\"/$1$website$relPath$2\"/gi;
	    s/src\=\"/src\=\"$relPath\//gi;
	    # $msg .= "\t$_\n\n";
	}


	# remove widths of 99%
	s/width\=\"99\%\"//g; # remove?


	# html
	if ($_ =~ /href\=\"(.[^\"]*)\"(.[^\>]*)\>/i) {

	    $filename     = $1;
	    $rest = $2;

	    if ($filename =~ /javascript/i ||
		$filename =~ /http:\/\//i) {

		$msg .= "urlIncl: ignoring js or http link: $filename\n";

		if ($filename !~ /javascript\:void\(null\)/ ) {

		    $_ =~ s/\\'\//\\'$website\//;
		    $_ =~ s/(href\=\")/$1$website/g if ($_ !~ /http:\/\//);

		    $_ =~ s/imgdvweb01/www/g; # perhaps not required
		}

	    } elsif ($filename =~ /\#/) {

		# index reference to point to same page
		# I think the baseurl on the page screws it up
		$_ =~ s/$filename/javascript\:void\(null\)/;
		$_ =~ s/$rest/ onClick\=\"javascript\:document.location\=\'$filename\'\" $rest/;


	    } else {

		$msg .=  "urlIncl: FOUND link $filename\n";
		# $_ =~ s/$filename/$website\/$filename/; # removed with 31 May release
	    }

	}

	if ($_ =~ /open(.[^\(]*)\('(.[^']*)'/i) {

	    $filename     = $2;

	    $msg .= "urlIncl: looking at js src issue with Open$1: $filename\n";


	    $_ =~ s/'\//'$website/;
	    $_ =~ s/imgdvweb01/www/g; # perhaps not required

	}


        $_ =~ s/(this.src\=\')\//$1http:\/\/www.gartner.com\//gi; # for mouse overs in strat sourcing page

        $_ =~ s/.com\/\/\//.com\//g; # get rid of triple /// for a single /
        $_ =~ s/.com\/\//.com\//g; # get rid of double // for a single /


    }



########################################################################
sub write {

    # writes files

    # take 2 inputs
    #  $_[0]  -  name of file with extra path information
    #  $_[1]  -  content of file


    $file = "/home/gartner/html/rt/content/"."$_[0]";
    open (FILE, ">$file") || die "Can't open file for writing: $file \n\n";
    print FILE "<!-- created by homepage_parser.pl -->\n\n";
    print FILE $_[1];
    close (FILE);

    return();

}


########################################################################
#
# Following sections are to translate
#  links, text and html of various sections
#


########################################################################
sub transFocusArea {

    # translate the focus areas section
    # as of 9 Dec 2003 Germany is hardcoded and chmod 444.... italy is the same as europe as wcw

    undef local @lines;
    push @lines, split(/\n/, $line);

    foreach (@lines) {

	#chop();

	$output .= "$_\n";
    }

    &write('emea/it/home_focus_areas.incl', $output);
    &FTPfile('home_focus_areas.incl', 'it');

    # german version
     foreach (@lines) {

	#chop();

         $output .= "$_\n";
     }
     &write('emea/de/home_focus_areas.incl', $output);
     &FTPfile('home_focus_areas.incl', 'de');

}


########################################################################
sub transMemProg {

    # translate the membership programs left rail box

    # Italia
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

        #  following if statement point user to Italian language versions of MP pages
        if (/\/pages\/section.php.id.2126.s.8.jsp/) {

	    # http://regionals4.gartner.com/regionalization/content/emea/it/mp_architects.html

	    $msg .= "urlIncl: found mp architects for italia\n\n";
	    #s/\/pages\/section.php.id.2126.s.8.jsp/\/regionalization\/content\/emea\/it\/mp_architects.html/i;

	} elsif (/\/pages\/section.php.id.2123.s.8.jsp/) {

	    # http://regionals4.gartner.com/regionalization/content/emea/it/mp_investment.html

	    $msg .= "urlIncl: found mp investment for italia\n\n";
	    #s/\/pages\/section.php.id.2123.s.8.jsp/\/regionalization\/content\/emea\/it\/mp_investment.html/i;

	} elsif (/\/pages\/section.php.id.2125.s.8.jsp/) {

	    # http://regionals4.gartner.com/regionalization/content/emea/it/mp_network.html

	    $msg .= "urlIncl: found mp network for italia\n\n";
	    #s/\/pages\/section.php.id.2125.s.8.jsp/\/regionalization\/content\/emea\/it\/mp_network.html/i;

	}

	# change the descriptive text to italian
	s/Get the insight, services and<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>tools you need to succeed in<\/div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>your job<div\>/Le conoscenze, i servizi e<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>gli strumenti per raggiungere<\/div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>il successo<div\>/;

	# add in the italian membership program
	 $ssmiIE = <<EndofList;
	 document.write('<option value="/regionalization/content/emea/it/ssmi_unrec_home.jsp"> SSMI - Outsourcing Professionals in Italy</option>');

EndofList

            s/(Telecom Managers<\/option\>\'\)\;)/\1\n$ssmiIE/;

        # add in the italian membership program for netscape
	$ssmiNSCP = <<EndofList;
	 document.write('<div><img src="./img/trans_pixel.gif" width="196" height="1" alt="" border="0"></div><img src="/images/homepage/trans_arrow.gif" width="8" height="8" alt="" hspace="3" border="0"><a href="/regionalization/content/emea/it/ssmi_unrec_home.jsp" class="membershipProgramLink">Outsourcing Professionals in Italy</a>');
EndofList

	s/(Telecom Managers<\/a\>\'\)\;)/\1\n$ssmiNSCP/;

	# text NOSCRIPT version
        $ssmiNOSCRIPT = <<EndofList;
	<div><img src="/images/trans_pixel.gif" width="196" height="1" alt="" border="0"></div>
	<img src="/images/homepage/trans_arrow.gif" width="8" height="8" alt="" hspace="3" border="0"><a href="/regionalization/content/emea/it/ssmi_unrec_home.jsp" class="membershipProgramLink">Outsourcing Professionals in Italy</a>
EndofList

	s/(Telecom Managers<\/a\>)$/\1\n$ssmiNOSCRIPT/;

	s/Choose Your Job Role/Scegli il tuo ruolo/;

	$output .= "$_\n";
    }

    &write('emea/it/home_membershipprogram.incl', $output);
    &FTPfile('home_membershipprogram.incl', 'it');


    # German Version
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;
    foreach (@lines) {

	#chop();

        # change the descriptive text to german
	s/\/images\/homepage\/membership_pro196.gif/\/regionalization\/img\/homepage\/de_membership_pro196.gif/;
	s/Membership Programs/Mitgliederprogramme/;
	s/Get the insight, services and<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>tools you need to succeed in<\/div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>your job<div\>/Wissen, Services und<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>Tools, die Ihren<\/div\><div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"1\" alt\=\"\" border\=\"0\" align\=\"left\" hspace\=\"2\"\>beruflichen Erfolg sichern<div\>/;
        s/Choose Your Job Role/W\&auml\;hlen Sie Ihr T\&auml\;tigkeitsfeld/;

        $output .= "$_\n";
    }
    &write('emea/de/home_membershipprogram.incl', $output);
    &FTPfile('home_membershipprogram.incl', 'de');



}

########################################################################
sub transMQ {

    # translate the Magic Quadrants

    # Italia
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

    	s/dottedline/dottedLine/g; # corrects mispelling in class name

    	s/Find out which vendors are leaders, visionaries, challengers or niche players./Scopri quali fornitori sono leader, \"visionari\", \"sfidanti\", <br \/\>di nicchia/;
	s/Latest Magic Quadrants/Ultimi Magic Quadrants/;
	s/Latest Magic Quadrant/Ultimo Magic Quadrant/;
	s/View All Magic Quadrants/Altri Magic Quadrants/;

	$output .= "$_\n";
    }

    if (!&testLock('MQ', 'it')) {
    	local $fileName = "emea/it/"."$_[0]";
    	&write($fileName, $output);
    	&FTPfile($_[0], 'it');
    } else {
	# lock file exists, so write to a temp file
    	local $fileName = "emea/it/"."$_[0]"."latest";
    	&write($fileName, $output);
    }




    # Germany
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

    	s/dottedline/dottedLine/g;

    	s/Find out which vendors are leaders, visionaries, challengers or niche players./Finden Sie heraus, welche Anbieter f\&uuml\;hrend, vision\&auml\;r, Herausforderer oder Nischenplayer sind/;
	s/View All Magic Quadrants/Alle Magic Quadrants/;
	# enforce <br>
	s/Latest Magic Quadrant:\&nbsp\;<\/b\><\/span\>/Aktuellster Magic Quadrant:<\/b\><\/span\>/;
	# remove <br> if it happens to appear
	s/smallThinBlueLink\"\><b\><br\>/smallThinBlueLink\"\><b\>/;
	s/<img src\=\"\/images\/trans_pixel.gif\" width\=\"1\" height\=\"12\" alt\=\"\" border\=\"0\"\>//; # added 28 Nov 2003 for dumb spacer
	s/<div\><img src\=\"\/images\/trans_pixel.gif\" width\=\"20\" height\=\"12\" alt\=\"\" border\=\"0\"\>/ /;# added 28 Nov 2003 for dumb spacer

	$output .= "$_\n";
    }

    if (!&testLock('MQ', 'de')) {
    	local $fileName = "emea/de/"."$_[0]";
    	&write($fileName, $output);
    	&FTPfile($_[0], 'de');
    } else {
	# lock file exists, so write to a temp file
    	local $fileName = "emea/de/"."$_[0]"."latest";
    	&write($fileName, $output);
    }


}

########################################################################
sub transHC {

    # translate the Hype Cycles

    # Italia
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

    	s/dottedline/dottedLine/g;

    	s/Gartner Hype Cycles clearly explain the difference between hype and the future of technology./Gartner Hype Cycles illustra con chiarezza la differenza tra le aspettative non realistiche e il futuro della tecnologia./;
	s/View All Hype Cycles/Altri Hype Cycles/;
	s/Latest Hype Cycle/Ultimo Hype Cycle/;

	$output .= "$_\n";
    }

    if (!&testLock('HC', 'it')) {
    	local $fileName = "emea/it/"."$_[0]";
    	&write($fileName, $output);
    	&FTPfile($_[0], 'it');
    } else {
	# lock file exists, so write to a temp file
    	local $fileName = "emea/it/"."$_[0]"."latest";
    	&write($fileName, $output);
    }


    # Germany
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

    	s/dottedline/dottedLine/g;

    	s/Gartner Hype Cycles clearly explain the difference between hype and the future of technology./Gartner Hype Cycles machen den Unterschied zwischen Medien-Rummel und den Technologien der Zukunft deutlich./;
	s/View All Hype Cycles/Alle Hype Cycles/;
	s/Latest Hype Cycle:\&nbsp\;<\/b\>/Aktuellster Hype Cycle:\&nbsp\;<\/b\>/;

	$output .= "$_\n";
    }
    if (!&testLock('HC', 'de')) {
    	local $fileName = "emea/de/"."$_[0]";
    	&write($fileName, $output);
    	&FTPfile($_[0], 'de');

    } else {
	# lock file exists, so write to a temp file
    	local $fileName = "emea/de/"."$_[0]"."latest";
    	&write($fileName, $output);
    }


}

########################################################################
sub transVR {

    # translate the Vendor Ratings

    # Europe, just the headlines
    if ($flagVRhead) {

	$line .=<<EndofHTML;
<span class="focusAreaLink"><b>Latest Ratings: </b></span><br />
$vrLink[0]<br />
$vrLink[1]<br />
$vrLink[2]<br />

   </td>
   <td width="10" height="2" bgcolor="#E3E9EC"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
</tr>
<tr>
  <td bgcolor="#E3E9EC" colspan="3"><div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div></td>
</tr>
<tr>
   <td width="356" height="2" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="2" alt="" border="0"></td>
</tr>
<!-- END VENDOR RATING BLOCK -->
</table>

<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="360" height="2" bgcolor="#BBBBBB"><img src="/images/trans_pixel.gif" width="360" height="2" alt="" border="0"></td>
</tr>
</table>

<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td bgcolor="#ffffff"><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></td>
</tr>
</table>
EndofHTML

	if (!&testLock('VR', 'emea')) {
	    &write('emea/home_vr_headlines.incl', $line);
	    &FTPfile('home_vr_headlines.incl');
	} else {
	    # lock file exists, so write to a temp file
	    &write('emea/home_vr_headlines.incl.latest', $line);
	}
    }

    # Italia
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {


    	s/dottedline/dottedLine/g;

	s/Gartner\'s latest ratings of leading vendors/Le ultime valutazioni Gartner sui principali fornitori/;
	s/Latest Ratings/Ultime valutazioni/;
	s/View All Vendor Ratings/Altri Vendor Ratings/;

        # need wider table for lable 'Ultime valutazioni'
	s/width\=\"100\"/width\=\"130\"/g;
	s/width\=\"236\"/width\=\"206\"/g;

	$output .= "$_\n";
    }

    if (!&testLock('VR', 'it')) {
    	local $fileName = "emea/it/"."$_[0]";
    	&write($fileName, $output);
    	&FTPfile($_[0], 'it');
    } else {
	# lock file exists, so write to a temp file
    	local $fileName = "emea/it/"."$_[0]"."latest";
    	&write($fileName, $output);
    }




    # Germany
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {


    	s/dottedline/dottedLine/g;

    	s/Gartner\'s latest ratings of leading vendors/Gartners neueste Bewertungen der f\&uuml\;hrenden Anbieter/;
	s/View All Vendor Ratings/Alle Vendor Ratings/; # was Anbieter-Bewertungen/;
	s/Latest Ratings/Aktuellste Vendor Ratings/; # was Anbieter-Bewertung/;

        # need wider table for lable 'Aktuellste Vendor Ratings'
        s/width\=\"100/width\=\"190/g;
	s/width\=\"236/width\=\"146/g;

	$output .= "$_\n";
    }

    if (!&testLock('VR', 'de')) {
    	local $fileName = "emea/de/"."$_[0]";
    	&write($fileName, $output);
    	&FTPfile($_[0], 'de');
    } else {
	# lock file exists, so write to a temp file
    	local $fileName = "emea/de/"."$_[0]"."latest";
    	&write($fileName, $output);
    }
}

########################################################################
sub transWeblog {

    # translate Weblogs

    # Italia
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

    	s/dottedline/dottedLine/g;

        s/Find out what Gartner analysts are thinking about current business & technology issues/Scoprite il parere degli analisti Gartner su temi attuali di business e tecnologie/;
        s/View All Gartner Weblogs/Visualizza tutti i Gartner Weblog/;

	$output .= "$_\n";
    }
    local $fileName = "emea/it/"."$_[0]";
    &write($fileName, $output);
    &FTPfile($_[0], 'it');



    # Germany
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

    	s/dottedline/dottedLine/g;

    	s/Find out what Gartner analysts are thinking about current business & technology issues/FindenSie heraus, was Gartner-Analysten zu aktuellen Business- und Technologie-Themen zu sagen haben/;
        s/View All Gartner Weblogs/Alle Gartner Weblogs/;
        s/Latest Topic/Aktuellstes Thema/g;

	$output .= "$_\n";
    }
    local $fileName = "emea/de/"."$_[0]";
    &write($fileName, $output);
    &FTPfile($_[0], 'de');

}

########################################################################
sub transResCol {

    # translate Research Collections

    # Italia
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

    	s/dottedline/dottedLine/g;

        s/Research Collections/Raccolte di ricerche/;
        s/Get research articles, tools and other resources./Consulta gli articoli di ricerca, i tool e le altre risorse./;
        s/View All Raccolte di ricerche/Altre Ricerche recenti/;
        s/View All Research Collections/Altre Ricerche recenti/;

	$output .= "$_\n";
    }
    local $fileName = "emea/it/"."$_[0]";
    &write($fileName, $output);
    &FTPfile('home_research_collections.incl', 'it');



    # Germany
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {

	#chop();

    	s/dottedline/dottedLine/g;

    	s/Research Collections/Unser Research/;
        s/Get research articles, tools and other resources./Research, Tools und andere Ressourcen./;
        s/View All Unser Research/Weiterer Research/;
        s/View All Research Collections/Weiterer Research/;

	$output .= "$_\n";
    }
    local $fileName = "emea/de/"."$_[0]";
    &write($fileName, $output);
    &FTPfile('home_research_collections.incl', 'de');

}

########################################################################
sub transExecRpt {

    # translate Executive Reports

    # Italia
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {


        # s/Gartner Executive Reports//;
        s/Five comprehensive reports about CRM, Web Services, Security, Outsourcing and Asset Management./Cinque report completi su CRM, Web Services, Sicurezza, Outsourcing e Asset Management./;
        s/View All Executive Reports/Visualizza tutti gli Executive Reports/;


	$output .= "$_\n";
    }
    local $fileName = "emea/it/"."$_[0]";
    &write($fileName, $output);
    &FTPfile($_[0], 'it');


    # Germany
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;

    foreach (@lines) {


        s/Gartner Executive Reports/Berichte f\&uuml\;r die F\&uuml\;hrungsebene/;
        s/Five comprehensive reports about CRM, Web Services, Security, Outsourcing and Asset Management./F\&uuml\;nf ausf\&uuml\;hrliche Berichte \&uuml\;ber CRM, Web-Services, Sicherheit, Outsourcing und Asset Management./;
        s/View All Executive Reports/Alle Gartner Executive Reports/;

  	$output .= "$_\n";
    }
    local $fileName = "emea/de/"."$_[0]";
    &write($fileName, $output);
    &FTPfile($_[0], 'de');

}




############################################################################
sub xhtmlG2Ver {

#<tr>
#    <td width="186" bgcolor="#FFFFFF"><a href="http://www.gartnerg2.com/na/na-0104-0004.asp"  class="smallBlueLink" target="_blank">Big Banks Getting Bigger; 2004 Off to an Acquisitive Start</a><br><!--  --><div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div></td>
#</tr>

    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;
    local $headline;
    local $link;

    foreach (@lines) {

	$link = $1 if (/href\=\"(.[^\"]*)\"/);

	$headline = $1 if (/_blank\">(.[^<]*)</);
	    
    }

    $output .=<<EOF;

<p><a href="$link"  target="_blank">$headline</a></p>

EOF

    &write($_[0], $output);
    &FTPfile($_[0]);


}


############################################################################
sub xhtmlPRVer {

    #<tr>
    #    <td><a href="/5_about/press_releases/pr9oct2003b.jsp" class="smallThinBlueLink">Gartner Completes Conversion of Notes into Common Stock</a><br>
    #	<img src="/images/trans_pixel.gif" width="186" height="5" alt="" border="0"></td>
    #</tr>         
    #<tr>
    #    <td><a href="/5_about/press_releases/pr1oct2003a.jsp" class="smallThinBlueLink">Gartner, Inc. Announces Two Senior Executive Promotions</a><br>
    #	<img src="/images/trans_pixel.gif" width="186" height="5" alt="" border="0"></td>
    #</tr>
    
    undef local @lines;
    push @lines, split(/\n/, $line);
    undef local $output;
    local @headline;
    local @link;
    local $i = 0;

    foreach (@lines) {
	
	$output.=$_;	
	
	while (/href(.[^<\/a\>]*)<\/a\>/) {

	    if (/href class\=\"smallThinBlueLink\"\>(.[^<]*)</) {
	    
		push @link, $1 if (/\=\"(.[^\"]*)\"/);
		push @headline, $1 if (/Link\"\>(.[^<]*)</);
		
		$ftpmsg .= "\n\n\ $_ n\n";
	    }
	}
    }
    

    foreach (@link) {
	
	$output .=<<EOF;
	
<p><a href="$_"  target="_blank">$headline[$i]</a></p>
	    
EOF
        $i++;
    }
    
    local $fileName = "emea/".$_[0];
    &write($fileName, $output);
    &FTPfile($_[0]);

}




########################################################################
sub FTPfile {

	# ftp files to remote servers
	# take 2 args
	# 1. filename
	# 2. relative path from emea/

	use Net::FTP;

	chdir("/home/gartner/html/rt/content/emea/$_[1]/");

	$remoteFullPath  = "regionalization/templates/emea/$_[1]/";

	$saveFile = "$_[0]"."\.old";

	$ftp = Net::FTP->new("campsqa.gartner.com") or $ftpmsg .= "FTPfile: Can't start FTP session<br>\n";
	$ftp->login("pmahnke","hi11top")            or $ftpmsg .= "FTPfile: Can't login into FTP session<br>\n";
	$ftp->cwd($remoteFullPath)                  or $ftpmsg .= "FTPfile: Can't change directory on remove server: $remoteFullPath<br>\n";
	$ftp->type('I')                             or $ftpmsg .= "FTPfile: Can't change to ascii mode<br>\n";
	$ftp->rename($_[0], $saveFile)              or $ftpmsg .= "FTPfile: Can't rename file: $_[1]/$_[0]<br>\n";
	$ftp->put($_[0],$_[0])                      or $ftpmsg .= "FTPfile: Can't PUT file: $_[1]/$_[0]<br>\n";
	$ftp->quit();


	$pftp = Net::FTP->new("hibachi.gartner.com") or $ftpmsg .= "FTPfile: Can't start FTP session<br>\n";
	$pftp->login("pmahnke","hi11top")            or $ftpmsg .= "FTPfile: Can't login into FTP session<br>\n";
	$pftp->cwd($remoteFullPath)                  or $ftpmsg .= "FTPfile: Can't change directory on remove server: $remoteFullPath<br>\n";
	$pftp->type('I')                             or $ftpmsg .= "FTPfile: Can't change to ascii mode<br>\n";
	$pftp->rename($_[0], $saveFile)              or $ftpmsg .= "FTPfile: Can't rename file: $_[1]/$_[0]<br>\n";
	$pftp->put($_[0],$_[0])                      or $ftpmsg .= "FTPfile: Can't PUT file: $_[1]/$_[0]<br>\n";
	$pftp->quit();

	print $ftpmsg;


}


########################################################################

1;
