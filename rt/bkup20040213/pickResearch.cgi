#!/usr/local/bin/perl


########################################################################
#
# pickResearch.cgi
#
#   written:  15 Dec 2003 by Peter Mahnke
#   modified: 15 Jan 2004 by Peter Mahnke
#              - added ability to add local research and translated titles
#             22 Jan 2004 by Peter Mahnke
#              - turned on FTP to campsqa of news and research
#              - added instructions and cleaned up UI a little
#             12 Feb 2004 by Peter Mahnke
#              - added choice of servers to upload to via site parameter (prod, qa)
#
#
#   run from a web browser
#   currently only called through update_menu.cgi
#
#
#   DESCRIPTION
#
#     allows regional site editors to pick News,Research and
#     update Focal Points from a single page and output them into
#     all the major output formats required for the regional sites
#
#     namely: html, xhtml, mailing formats, exp formats and rss
#
#     for news and research it takes in doc ids or resids and logs them
#     per locale, for focal points you input the text and relative file
#     and uri information into a form, it also logs the data
#
#     when the form is submitted, the application looks up the document
#     details for the documents, updates the focal points as required
#     and outputs all the includes again into the /rt/content/<LOCALE>/
#     directory strcuture.  the lookup will first see if the information
#     is in the local DETAIL cache, if not, it will go to g.com
#
#     CODES
#     codes are saved in a text log file called NEWS.codes or FR.codes
#
#     DETAIL
#     document detail is stored in a text file called NEWS.detail or
#     FT.detail with the translated information
#
#     FTP
#     the html includes are saved on the local server and then FTPed up
#     campsqa.gartner.com.  a remote backup of the previous file is stored
#     as <filename>.old
#
#     currently only FTPing news and research
#
#
#
########################################################################

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
use CGI_Lite;
require ("/home/gartner/cgi-bin/gNOlogin.pl");
require ("/home/gartner/html/rt/getNODocument3.pl");
require ("/home/gartner/html/rt/common.pl");
require ("/home/gartner/html/rt/commonDoccodes.pl");
require ("/home/gartner/html/rt/commonTransDoc.pl");
require ("/home/gartner/html/rt/replaceChars.pl");
require ("/home/gartner/html/rt/SmartyPants.pl");



##############################################################
# Variables
local $fileFP  = "/home/gartner/html/rt/content/fp.csv";
local $server  = "www4";
local $ftpSite = "hibachi.gartner.com";
$date          = `date +'%a, %d %b %Y %T GMT'`;
$yyyymmdd      = `date +'%Y%m%d'`;
chop($date);
chop($yyyymmdd);
local $thisScript = "http://intl.gartner.com/rt/pickResearch.cgi";


local $menu =<<EOF;
<p class="footer">menu: edit [<a href="$thisScript?locale=emea&page=update">emea</a> | <a href="$thisScript?locale=it&page=update">it</a> | <a href="$thisScript?locale=de&page=update">de</a>]<p>

EOF

##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    # something submitted
    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;

    $ftpSite = "campsqa.gartner.com" if ($FORM{'site'} =~ /qa/i);



} else {

	$FORM{'locale'} = "emea";
	&printInitialForm;
	exit;

}



#########################################################
# process the input

if ($FORM{'page'} eq "update") {
    &printInitialForm;
    exit;
}



#################################################
# process news changes
undef @docs;
undef $xhtml;
undef $view;

$processFlag = "news";
$detailFlag = "NEWS";

if (!$FORM{'newscode1'}) {
    $FORM{'newscode1'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'newscode1'}, $FORM{'newshl1'}, $FORM{'newsuri1'});
$msg .= "raw $FORM{'newscode1'}, $FORM{'newshl1'}, $FORM{'newsuri1'} <br>";



if (!$FORM{'newscode2'}) {
    $FORM{'newscode2'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'newscode2'}, $FORM{'newshl2'}, $FORM{'newsuri2'});



if (!$FORM{'newscode3'}) {
    $FORM{'newscode3'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'newscode3'}, $FORM{'newshl3'}, $FORM{'newsuri3'});



if (!$FORM{'newscode4'}) {
    $FORM{'newscode4'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'newscode4'}, $FORM{'newshl4'}, $FORM{'newsuri4'});



$FORM{'news'} = "$FORM{'newscode1'} $FORM{'newscode2'} $FORM{'newscode3'} $FORM{'newscode4'}";


if ($FORM{'news'} ne $FORM{'origNews'}) {
    &writeCodes('NEWS', $FORM{'locale'}, $FORM{'news'});
}
$news = $view;




#################################################
# process research changes
undef @docs;
undef $xhtml;
undef $view;
$processFlag = "research";
$detailFlag = "FR";
if (!$FORM{'frcode1'}) {
    $FORM{'frcode1'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'frcode1'}, $FORM{'frhl1'}, $FORM{'fruri1'} );



if (!$FORM{'frcode2'}) {
    $FORM{'frcode2'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'frcode2'}, $FORM{'frhl2'}, $FORM{'fruri2'} );



if (!$FORM{'frcode3'}) {
    $FORM{'frcode3'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'frcode3'}, $FORM{'frhl3'}, $FORM{'fruri3'} );



if (!$FORM{'frcode4'}) {
    $FORM{'frcode4'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'frcode4'}, $FORM{'frhl4'}, $FORM{'fruri4'} );




$FORM{'research'} = "$FORM{'frcode1'} $FORM{'frcode2'} $FORM{'frcode3'} $FORM{'frcode4'}";


if ($FORM{'research'} ne $FORM{'origResearch'}) {
    &writeCodes('FR', $FORM{'locale'}, $FORM{'research'});
}
$research = $view;




if ($FORM{'updated1'} || $FORM{'updated2'}) {
    &saveFP;
}
&readFP;


&saveOutput;

&printOutput;
exit;


####################################################################
sub getDoc {

    $msg .= "in getDoc $_[0], $_[1], $_[2] <br>";

    ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price) = "";

    if (!$flagNew) {

        # see if detail in detail database first
        ($resId, $title, $link, $pubDate, $summary, $auth) = &readDetail($detailFlag, $FORM{'locale'}, $_[0]);


        if (!$title) {

            # not in detail list, so get from gartner.com

            $_[0] =~ s/ //g; # strip spaces


            $docCode = "\/DisplayDocument\?id\="."$_[0]";
            $link = "http:\/\/www4.gartner.com"."$docCode";  # .\&acsFlg\=accessBought";
            ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price)
		= &getResearchDetail($link,$server);

            # didn't get title with resid, try doc id
            if (!$title) {
	        $docCode = "\/DisplayDocument\?doc_cd\="."$_[0]";
	        $link = "http:\/\/www4.gartner.com"."$docCode"; # ."\&acsFlg\=accessBought";
	        ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price)
		    = &getResearchDetail($link,$server);
            }

            #add proper attributes to links
            $link =~ s/uid=Y&fRef=true/call=email&amp\;ref=g_emalert/;

        }


    } else {
    	$resId = $_[0];
    }

    # rewrite title if passed
    if ($_[1]) {
	$title = $_[1];
	$title = &replaceCharacters($title);
	# $title = &SmartyPants($title, 1);
	$msg .= "replaceChars: $title<br>";
    }


    # rewrite link if passed
    if ($_[2]) {
	$link    = $_[2];
	$docCode =  $link;
	$docCode =~ s/http:\/\/www4.gartner.com//;
	$docCode =~ s/&call=email&ref=g_emalert//;
    }




    # write document information to detail database, this will check if already in.
    &writeDetail($detailFlag, $FORM{'locale'}, $resId, $title, $link, $pubDate, $summary, $auth);



    # create date if missing
    if (!$pubDate) {

        $dateStr = `date +'%a, %d %b %Y %T GMT'`;
        chop($dateStr);

    } else {

        # put dates into proper RSS 2.0 format
        use DateTime::Format::HTTP;
        my $dt = 'DateTime::Format::HTTP';
        $datestring = $dt->parse_datetime($pubDate, 'GMT');
        $dateStr = $dt->format_datetime($datestring);

    }

    # clean up title
    $title =~ s/EMEA/Europe, Middle East and Africa/g;
    $title =~ s/ \(Executive Summary\)//g;

    # do the no hanging word logic on $title
    $noHangTitle = &noHang($title, 44);
    $noHangTitle =~ s/\& /\&amp\; /g;

    # copy of $title without <br />
    $origTitle = $title;

    # turn & into &amp;
    $title   =~ s/\& /\&amp\; /g;
    $summary =~ s/\& /\&amp\; /g;


    # clean up author
    $auth =~ s/,/ \&amp\;nbsp\; /g; # convert , to a space - for mailing format

    # clean up $pubDate
    $pubDate =~ s/\-/ /g;
    $pubDate =~ s/^0//;
    $pubDate =~ s/Jan/January/;
    $pubDate =~ s/Feb/February/;
    $pubDate =~ s/Mar/March/;
    $pubDate =~ s/Apr/April/;
    $pubDate =~ s/Jun/June/;
    $pubDate =~ s/Jul/July/;
    $pubDate =~ s/Aug/August/;
    $pubDate =~ s/Sep/September/;
    $pubDate =~ s/Oct/October/;
    $pubDate =~ s/Nov/November/;
    $pubDate =~ s/Dec/December/;

    if ($processFlag eq "research") {

	# FEATURED RESEARCH HTML
	$htmlFR .=  <<EndofHTML;
\n<!--start research  - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate  -->
    <tr><td width="356" height="8" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="8" alt="" border="0"></td></tr>
    <tr><td width="22" bgcolor="#FFFFFF" valign="top" align="center"><a href="javascript:void(null)" onclick="openResult('$docCode')" class="smallBlueLink"><img src="//img/homepage/reversed_blue_arrow.gif" width="9" height="9" vspace="2" alt="$title" border="0"></a></td>\n        <td width="328" valign="top" bgcolor="#FFFFFF"><a href="javascript:void(null)" onclick="openResult('$docCode')" class="smallBlueLink">$noHangTitle</a></td>\n        <td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>\n    </tr>
<!--end research - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->\n
EndofHTML

    }


    if ($processFlag eq "news") {

	# NEWS HTML
	$htmlNEWS .= <<EndofHTML;
\n<!--start news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->
    <tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
    <tr><td width="22" bgcolor="#FFFFFF" valign="top" align="center"><a href="javascript:void(null)" onclick="openResult('$docCode')" class="largeGrayLink"><img src="/images/homepage/reversed_green_arrow.gif" width="9" height="9" vspace="3" alt="$title" border="0"></a></td>\n        <td width="328" valign="top" bgcolor="#FFFFFF"><a href="javascript:void(null)" onclick="openResult('$docCode');return false;" class="smallBlueLink" target="_new">$noHangTitle</a></td>\n        <td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>\n    </tr>
<!--end news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->\n
EndofHTML

		# EXP FORMAT
		$EXPline .= <<EndofHTML;
                                             <tr>
                                                 <td width="10" valign="top"><img src="/pages/docs/exp/images/common/bullet_gray.gif" width="10" height="8" vspace="3"></td>
                                                 <td width="398"valign="top"><a href="$docCode" onclick="researchPop('$docCode'); return false;" class="grey11pxBoldLk" target="_new">$title</a><br></td>
                                             </tr>
                                             <tr><td width="428" height="11" colspan="2"><img src="/pages/docs/common/images/x.gif" width="1" height="11"></td></tr>

EndofHTML

	}

	# MAILING FORMAT HTML

	$mailingAuth = $auth;
	$mailingAuth  =~ s/\<a href\=(.[^\>]*)\>//gi;
	$mailingAuth  =~ s/\<\/a\>//gi;
	$mailingAuth  =~ s/ \| /\, /gi;
	$mailingAuth = &noHang($mailingAuth,'37'); #,'no');
	#$mailingAuth = &preSpace ($mailingAuth,'4');

	$link =~ s/http(.[^\?]*)\?(.*)/http:\/\/europe.gartner.com\/regionalization\/content\/emea\/DisplayDocument.html\?$2/;

	$mailingTitle = &noHang($origTitle,'37'); #,'no');
	# $mailingTitle = &preSpace ($mailingTitle,'4');
	$mailingTitle =~ s/\&/\&amp\;/g;
	chop($mailerTitle);

	$mailingSummary = &noHang($summary,'45'); #,'no');


	$htmlMAIL{$processFlag} .= <<EndofHTML;

<p class="title"><a href="$link">$mailingTitle</a></p>
<p class="date">$pubDate</p>
<p class="author">$mailingAuth</p>
<p class="desc">$mailingSummary</p>

EndofHTML



	# MAILING TEXT FORMAT
	$textLink = $link;
	$textLink =~ s/http(.[^\?]*)\?(.*)/DisplayDocument.html\?$2/;

	$textTitle = $title;
	$textTitle =~ tr/[a-z]/[A-Z]/;

	$textSummary = &noHang($summary,'50'); #,'no');
	$textSummary   = &preSpace($textSummary, 2);

	$textMAIL{$processFlag} .= <<EndofHTML;

  $textTitle
  http:\/\/europe.gartner.com\/regionalization\/content\/emea\/$textLink
  $pubDate
  $textSummary

EndofHTML


    $rss .= "<item>\n  <title>$title \- $processFlag</title>\n  <description>$summary</description>\n  <pubDate>$dateStr</pubDate>\n  <link><![CDATA[$link]]></link>\n</item>\n";

    $rss =~ s/\&[^amp]/\&amp\;/mg;

    $xhtml{$processFlag} .=  <<EndofHTML;
 <li> <a href="\#" onclick="openResult('$docCode')">$title</a></li>
EndofHTML

    $view .=  <<EndofHTML;
 <li> <a href="\#" onclick="openResult('$docCode')">$title</a></li>
EndofHTML

    $flagNew = 0;

}

####################################################################
sub saveOutput {


    #####################################################
    # save html versions
    local $fn = "/home/gartner/html/rt/content/";

    if ($FORM{'locale'} eq "emea") {
	$fn = "$fn"."emea/"."home_news_headlines.incl";
    } else {
	$fn = "$fn"."emea/"."$FORM{'locale'}"."/home_news_headlines.incl";
    }
    &saveFile($fn, $htmlNEWS);
    &FTPfile_good('home_news_headlines.incl', $FORM{'locale'});



    #####################################################
    # EXP
    $outEXP = <<EndofLine;

	<table width="428" cellpadding="0" cellspacing="0" border="0">
	    <tr valign="top">
		<td width="428" bgcolor="#D3DDE5">
		    <table width="428" cellpadding="0" cellspacing="0" border="0"><tr><td height="6"><img src="/pages/docs/common/images/x.gif" width="1" height="6"></td></tr></table>
			<table width="428" cellpadding="0" cellspacing="0" border="0">
			    <tr>
				<td width="10"><img src="/pages/docs/common/images/x.gif" width="10" height="1"></td>
				    <td width="408">
					<table width="408" cellpadding="0" cellspacing="0" border="0">

$EXPline

                                         </table>
                                     </td>
                                 <td width="10"><img src="/pages/docs/common/images/x.gif" width="10" height="1"></td>
                             </tr>
                         </table>
                     </td>
                  </tr>
              </table>


EndofLine

    local $fn = "/home/gartner/html/rt/content/";

    if ($FORM{'locale'} eq "emea") {
	$fn = "$fn"."emea/EXPemeaNews\.jsp";
    } else {
	$fn = "$fn"."emea/"."$FORM{'locale'}"."/EXP"."$FORM{'locale'}"."News\.jsp";
    }
    &saveFile($fn, $outEXP);


    #####################################################
    # save html versions
    local $fn = "/home/gartner/html/rt/content/";
    if ($FORM{'locale'} eq "emea") {
	$fn = "$fn"."emea/"."home_fr_headlines.incl";
    } else {
	$fn = "$fn"."emea/"."$FORM{'locale'}"."/home_fr_headlines.incl";
    }
    &saveFile($fn, $htmlFR);
    &FTPfile_good('home_fr_headlines.incl', $FORM{'locale'});


    ############################################################
    # MAILING FORMATS

    # save html versions
    foreach $key (keys %htmlMAIL) {
	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/"."mailHTML"."$key"."\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/mailHTML"."$key"."\.incl";
	}
	&saveFile($fn, $htmlMAIL{$key});
    }


    # save text versions
    foreach $key (keys %textMAIL) {
	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/"."mailTEXT"."$key"."\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/mailTEXT"."$key"."\.incl";
	}
	&saveFile($fn, $textMAIL{$key});
    }

    ############################################################
    # XHTML FORMATS

    # save xhtml versions
    foreach $key (keys %xhtml) {

	local $fn = "/home/gartner/html/rt/content/";

	$saveFn = "uk/home_fr_headlines.incl" if ($key eq "research");
	$saveFn = "uk/home_news_headlines.incl" if ($key eq "news");

	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/"."xhtml"."$key"."\.incl";
	    local $ftpFn = "xhtml"."$key"."\.incl";
    	    &FTPfile_good($fn, 'emea', $saveFn); # put xml docs in uk dir as test
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtml"."$key"."\.incl";
	}
	&saveFile($fn, $xhtml{$key});
    }

    ############################################################
    # RSS FORMAT

    $outRSS =<<EndofText;
<?xml version="1.0" ?>
  <rss version="2.0" xmlns:blogChannel="http://backend.userland.com/blogChannelModule">
  <channel>
  <title>Gartner $FORM{'locale'}</title>
  <link>http://$FORM{'locale'}.gartner.com/</link>
  <description>Daily update of the featured news and research from Gartner $FORM{'locale'}, the world's leading IT research and advisory firm.</description>
  <language>en-us</language>
  <copyright>Copyright 2004 Gartner, Inc. and/or its Affiliates. All Rights Reserved. </copyright>
  <lastBuildDate>$date</lastBuildDate>
  <docs>http://backend.userland.com/rss</docs>
  <managingEditor>stephanie.gordon\@gartner.com</managingEditor>
  <webMaster>peter.mahnke\@gartner.com</webMaster>
  <image>
    <url><![CDATA[http://intl.transitionelement.com/img/ge_logo_small.gif]]></url>
    <width>110</width>
    <height>45</height>
    <link><![CDATA[http://europe.gartner.com]]></link>
    <title>Gartner Europe</title>
  </image>
  <ttl>120</ttl>
  <skipDays><day>Saturday</day><day>Sunday</day></skipDays>
  <skipHours><hour>1</hour><hour>2</hour><hour>3</hour><hour>4</hour><hour>5</hour><hour>6</hour><hour>19</hour><hour>20</hour><hour>21</hour><hour>22</hour><hour>23</hour><hour>24</hour></skipHours>
<item>
  <title>$FORM{'title1'} - Feature</title>
  <description>$FORM{'desc1'}</description>
  <pubDate>$FORM{'date1'}</pubDate>
  <link><![CDATA[$FORM{'url1'}]]></link>
</item>
<item>
  <title>$FORM{'title2'} - Feature</title>
  <description>$FORM{'desc2'}</description>
  <pubDate>$FORM{'date2'}</pubDate>
  <link><![CDATA[$FORM{'url2'}]]></link>
</item>
$rss
 </channel>
</rss>
EndofText

    local $fn = "/home/gartner/html/rt/content/";
    if ($FORM{'locale'} eq "emea") {
	$fn = "$fn"."emea/rss\.xml";
    } else {
	$fn = "$fn"."emea/"."$FORM{'locale'}"."/rss\.xml";
    }
    &saveFile($fn, $outRSS);




	# SAVE FOCAL POINTS

    # smarty pants the fps
    $FORM{'title1'} = &SmartyPants ($FORM{'title1'}, 1);
    $FORM{'desc1'} = &SmartyPants ($FORM{'desc1'}, 1);

    $FORM{'title2'} = &SmartyPants ($FORM{'title2'}, 1);
    $FORM{'desc2'} = &SmartyPants ($FORM{'desc2'}, 1);


	# save HTML fp
	open (FP, ">/home/gartner/html/rt/content/emea/home_fr_highlight_01.incl") || die "Can't open FP1\n";
	print FP <<ENDofHTML;
<!-- start featured research highlight 1 -->
<tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
<tr><td width="350" bgcolor="#FFFFFF" valign="top" colspan="2"><a href="$FORM{'url1'}"><img src="$FORM{'img1'}" width="100" height="68" hspace="6" align="left" alt="$FORM{'title1'}" border="0"></a><table border="0" cellspacing="0" cellpadding="0"><tr><td><a href="$FORM{'url1'}" class="largeBlueLink">$FORM{'title1'}</a><br /><span class="smallGrayText">$FORM{'desc1'}</span><br /></td></tr></table></td><td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td></tr>
<!-- end featured research highlight 1 -->
ENDofHTML
	close (FP);
	&FTPfile_good('home_fr_highlight_01.incl');



	open (FP, ">/home/gartner/html/rt/content/emea/home_fr_highlight_02.incl") || die "Can't open FP2\n";
	print FP <<ENDofHTML;
<!-- start featured research highlight 2 -->
<tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
<tr><td width="350" bgcolor="#FFFFFF" valign="top" colspan="2"><a href="$FORM{'url2'}"><img src="$FORM{'img2'}" width="100" height="68" hspace="6" align="left" alt="$FORM{'title2'}" border="0"></a><table border="0" cellspacing="0" cellpadding="0"><tr><td><a href="$FORM{'url2'}" class="largeBlueLink">$FORM{'title2'}</a><br /><span class="smallGrayText">$FORM{'desc2'}</span><br /></td></tr></table></td><td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td></tr>
<!-- end featured research highlight 2 -->
ENDofHTML
	close (FP);

	&FTPfile_good('home_fr_highlight_02.incl');



	# save xhtml fp
	open (FP, ">/home/gartner/html/rt/content/emea/uk/xhtml_fr1.incl") || die "Can't open xhtml FP1\n";
	print FP <<ENDofHTML;
	<div class="focalpoint">
<a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url1'}"><img src="http://regionals4.gartner.com/$FORM{'img1'}" width="100" height="68" alt="$FORM{'title1'}" border="0" align="left" /></a>
<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url1'}">$FORM{'title1'}</a></p>
<p>$FORM{'desc1'}</p>
</div>
ENDofHTML
    close (FP);

    &FTPfile_good('xhtml_fr1.incl', 'uk', 'home_fr_highlight_01.incl'); # put xml docs in uk dir as test




	open (FP, ">/home/gartner/html/rt/content/emea/uk/xhtml_fr2.incl") || die "Can't open xhtml FP2\n";
	print FP <<ENDofHTML;
	<div class="focalpoint">
<a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url2'}"><img src="http://regionals4.gartner.com/$FORM{'img2'}" width="100" height="68" alt="$FORM{'title2'}" border="0" align="left" /></a>
<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url2'}">$FORM{'title2'}</a></p>
<p>$FORM{'desc2'}</p>
</div>
ENDofHTML
    close (FP);

    &FTPfile_good('xhtml_fr2.incl', 'uk', 'home_fr_highlight_02.incl'); # put xml docs in uk dir as test

    # weekly mailing HTML FP email
    open (FP, ">/home/gartner/html/rt/content/emea/mailHTMLfr.incl") || die "Can't open mail HTML FP1\n";
    print FP <<ENDofHTML;
          <p class="title"><a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url1'}" target="blank">$FORM{'title1'}</a></p>
          <p class="desc">$FORM{'desc1'}</p>

               </td>
               <td width="100"><a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url1'}" target="blank" ><img src="http://regionals4.gartner.com/$FORM{'img1'}"      width="100" height="68" hspace="6" align="left" alt="$FORM{'title1'}" border="0" /></a></td>

ENDofHTML
    close (FP);

    # weekly mailing TEXT FP email
    local $mtt = $FORM{'title1'};
    $mtt       =~ tr/[a-z]/[A-Z]/;

    local $mtd = $FORM{'desc1'};
    $mtd       = &noHang($mtd,'50'); #,'no');
    $mtd       = &preSpace($mtd, 2);


    open (FP, ">/home/gartner/html/rt/content/emea/mailTEXTfr.incl") || die "Can't open mail TEXT FP1\n";
    print FP <<ENDofHTML;
  $mtt
  http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url1'}
  $mtd
ENDofHTML
    close (FP);



}

######################################################################
sub saveFile {

    open (OUT, ">$_[0]") || die "Can't write file: $_[0]\n\n";
    print OUT "<!-- created by pickResearch.cgi --\>\n\n" if ($_[0] !~ /rss/);
    print OUT $_[1];
    close (OUT);

}

####################################################################
sub printOutput {

    $title{$key1} = &SmartyPants ($title{$key1},1);
    $title{$key2} = &SmartyPants ($title{$key2},1);
    $desc{$key1} = &SmartyPants ($desc{$key1},1);
    $desc{$key2} = &SmartyPants ($desc{$key2},1);



    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>pickResearch.cgi - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt; clear:both;	}
h3	{		font-size: 10pt;	}
li,p,td	{		font-size: 9pt;	        }
/* HOMEPAGE CENTER COLUMN */
/* in the news */
.inthenewslist ul             {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;  }
.inthenewslist li             {  list-style-type: circle; list-style-image: url(http://regionals4.gartner.com/images/homepage/reversed_green_arrow.gif); color: #3088CC; line-height: 110%; padding: 3px;  }
.inthenewslist a              {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #3088CC; text-decoration: none; line-height: 110%;  }
.inthenewslist a:hover        {  text-decoration: underline;  }

/* featured research */
.featuredresearchlist ul      {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;   }
.featuredresearchlist li      {  list-style-type: circle; list-style-image: url(http://regionals4.gartner.com/images/homepage/reversed_blue_arrow.gif); color: #3088CC; line-height: 110%; padding: 3px;  }
.featuredresearchlist a       {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #3088CC; text-decoration: none; line-height: 110%;  }
.featuredresearchlist a:hover {  text-decoration: underline;  }

/* focal points - what to do if text longer than image ?? */
.focalpoint     {  float: left; margin: 5px; padding: 5px; padding-right: 10px; background: #fff; width: 400px;  }
.focalpoint img {  float: left; margin: 2px; padding: 0; }
.focalpoint   p{  float: left; padding: 0; margin: 0; margin-left: 5px; vertical-align: top; font-size: 11px; color: #4a4a4a;  }
.focalpoint p a{  font-weight: bold; color: #3088CC; text-decoration: none; line-height: 110%;  margin: 0; padding: 0; }

		  .msg {  font-size: .75em; font-family: courier, fixed; color: 333; border: 1px dashed navy; padding: 10px; margin: 10px;  }

.menu { font-size: 8pt; border 1px solid navy; }

</style>

</head>
</head>
<body>
<h1>Output - $FORM{'locale'}</h1>

<h2>News</h2>
<div class="inthenewslist">
<ul>
$news
</ul>
</div>

<h2>FR</h2>
<div class="featuredresearchlist">
<ul>
$research
</ul>
</div>

<h2>Focal Point 1</h2>
<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key1}"><img src="http://regionals4.gartner.com/$img{$key1}" width="100" height="68" alt="$title{$key1}" border="0" class="inline" align="left" /></p>');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key1}">$title{$key1}</a></p>');
    document.write('<p>$desc{$key1}</p>');
    document.write('<p>$date{$key1}</p>');
    document.write('</div>');
    document.close();
</script>


<h2>Focal Point 2</h2>
<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key2}"><img src="http://regionals4.gartner.com/$img{$key2}" width="100" height="68" alt="$title{$key2}" border="0" class="inline" align="left" /></p>');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key2}">$title{$key2}</a></p>');
    document.write('<p>$desc{$key2}</p>');
    document.write('<p>$date{$key2}</p>');
    document.write('</div>');
    document.close();
</script>


<h2>Messages</h2>
<p class="msg">$msg</p>
<p class="msg">$ftpmsg</p>

$menu

</body>
</html>

EndofHTML

}








####################################################################
sub printRSSOutput {

    $header =<<EndofText;
<?xml version="1.0" ?>
  <rss version="2.0" xmlns:blogChannel="http://backend.userland.com/blogChannelModule">
  <channel>
  <title>Gartner Europe</title>
  <link>http://europe.gartner.com/</link>
  <description>Daily update of the featured news and research from Gartner Europe, the world's leading IT research and advisory firm's European website.</description>
  <language>en-us</language>
  <copyright>Copyright 2003 Gartner, Inc. and/or its Affiliates. All Rights Reserved. </copyright>
  <lastBuildDate>$date</lastBuildDate>
  <docs>http://backend.userland.com/rss</docs>
  <managingEditor>stephanie.gordon\@gartner.com</managingEditor>
  <webMaster>peter.mahnke\@gartner.com</webMaster>
  <image>
    <url>http://intl.transitionelement.com/img/ge_logo_small.gif</url>
    <width>110</width>
    <height>45</height>
    <link>http://europe.gartner.com</link>
    <title>Gartner Europe</title>
  </image>
  <ttl>120</ttl>
  <skipDays><day>Saturday</day><day>Sunday</day></skipDays>
  <skipHours><hour>1</hour><hour>2</hour><hour>3</hour><hour>4</hour><hour>5</hour><hour>6</hour><hour>19</hour><hour>20</hour><hour>21</hour><hour>22</hour><hour>23</hour><hour>24</hour></skipHours>
EndofText

$footer =<<EndofText;
  </channel>
  </rss>
EndofText


$header =~ s/</\&lt\;/g;
$footer =~ s/</\&lt\;/g;
$rss   =~ s/</\&lt\;/g;

    print  <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>rss.xml</title>
</head>
<body>
<pre>
$header
<item>
  <title>$FORM{'title1'}</title>
  <description>$FORM{'desc1'}</description>
  <pubDate>$FORM{'date1'}</pubDate>
  <link>$FORM{'url1'}</link>
</item>
<item>
  <title>$FORM{'title2'}</title>
  <description>$FORM{'desc2'}</description>
  <pubDate>$FORM{'date2'}</pubDate>
  <link>$FORM{'url2'}</link>
</item>
$rss
$footer
</pre>
</body>
</html>

EndofHTML

}

####################################################################
sub preSpace {

    # add spaces before a line for mailing format

    local $flag   = 0;
    local $out    = "";
    local $space  = "";
    local @in     = split ("<br \/\>", $_[0]);

    local $i = 0;
    until ($i == $_[1]) {
	$i++;
	$space .= " ";
    }

    foreach (@in) {

	if (!$flag) {
	    $out = "$_\n";
	    $flag = 1;
	} else {
	    $out .= "$space$_\n";
	}
    }
    return($out);

}

####################################################################
sub readFile {

    open (FILE, "$_[0]") || die "can't open file to read: $_[0]\n";
    local $f;
    while (<FILE>) {
	$f .= $_;
    }
    close (FILE);
    return($f);
}

####################################################################
sub readFP {

	open (FP, "$fileFP") || die "Can't open FP: $fileFP\n";
	while (<FP>) {

		chop();
		local ($key, $t, $desc, $u, $i, $d) = split (/\t/);
		push @key, $key;
		$title{$key} = $t;
		$desc{$key}  = $desc;
		$url{$key}   = $u;
		$img{$key}   = $i;
		$date{$key}  = $d;

	}
	close (FP);

	local $c = 1;
	foreach $key (reverse sort @key) {

		last if ($c > 2);
		local $k = "key"."$c";
		$$k = $key;
		$c++;

	}

	close (FP);

}

####################################################################
sub saveFP {

	&readFP;

	open (FP, ">$fileFP") || die "Can't open FP: $fileFP\n";

        print FP "$FORM{'key1'}\t$FORM{'title1'}\t$FORM{'desc1'}\t$FORM{'url1'}\t$FORM{'img1'}\t$FORM{'date1'}\n";
        print FP "$FORM{'key2'}\t$FORM{'title2'}\t$FORM{'desc2'}\t$FORM{'url2'}\t$FORM{'img2'}\t$FORM{'date2'}\n";

	foreach $key (reverse sort @key) {

		next if ($key =~ /$FORM{'key1'}/ && $FORM{'updated1'});
		next if ($key =~ /$FORM{'key2'}/ && $FORM{'updated2'});


		print FP "$key\t$title{$key}\t$desc{$key}\t$url{$key}\t$img{$key}\t$date{$key}\n";

	}

	close (FP);

}

####################################################################
sub printInitialForm {

	&readFP;
	local $news     = &readCodes('NEWS', $FORM{'locale'});
	local $research = &readCodes('FR', $FORM{'locale'});

	# get existing news/fr for listing
	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/uk/"."xhtmlnews\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtmlnews\.incl";
	}
	$curNews = &readFile($fn);

	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/uk/"."xhtmlresearch\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtmlresearch\.incl";
	}
	$curFR = &readFile($fn);



	if ($FORM{'locale'} ne "emea") {

	    # add emea news/research option
	    # allows user to override current locale offering with emea's

	    $emeanews = &readCodes('NEWS', 'emea');
	    $emearesearch = &readCodes('FR', 'emea');

	    # javascript link to call function that does work
	    $useEmeaNews = "<li\><a href\=\"javascript:void\(null\)\;\" onclick\=\"javascript:movenews\(\)\;return false\;\"\>use EMEA News<\/a\> [ $emeanews ]<\/li\>\n";

	    $useEmeaResearch = "<li\><a href\=\"javascript:void\(null\)\;\" onclick\=\"javascript:moveresearch\(\)\;return false\;\"\>use EMEA Research<\/a\> [ $emearesearch ]<\/li\>\n";

	}

	$news =~ s/  / /g;
	@checkNews = split (/ /, $news);
	local $c;
	foreach $cd (@checkNews) {
		$c++;
		($FORM{'newscode'.$c}, $FORM{'newshl'.$c}, $FORM{'newsuri'.$c}, $pubDate, $summary, $author) = &readDetail('NEWS', $FORM{'locale'}, $cd);
		$FORM{'newscode'.$c} = $cd;
	}

	# bring in EMEA news
	$emeanews =~ s/  / /g;
	@emeaNews = split (/ /, $emeanews);


	$research =~ s/  / /g;
	@checkFR = split (/ /, $research);
	undef $c;
	foreach $cd (@checkFR) {
		$c++;
		($FORM{'frcode'.$c}, $FORM{'frhl'.$c}, $FORM{'fruri'.$c}, $pubDate, $summary, $author) = &readDetail('FR', $FORM{'locale'}, $cd);
		$FORM{'frcode'.$c} = $cd;
	}

	# bring in EMEA research
 	$emearesearch =~ s/  / /g;
	@emeaFR = split (/ /, $emearesearch);


	# add News form for translated research
	$addNewsForm =<<EOF;
            <ul>
              <li> <a href="javascript:void(null);" onclick="javascript:movenewsdown();return false;">move news down</a>
              <li> <input type="text" name="newscode1" value="$FORM{'newscode1'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="newshl1" size="80" value="$FORM{'newshl1'}" /> </li>
                     <li> link: <input type="text" size="80" name="newsuri1" value="$FORM{'newsuri1'}" /></li>
                   </ul>
              <li> <input type="text" name="newscode2" value="$FORM{'newscode2'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="newshl2" size="80" value="$FORM{'newshl2'}" /> </li>
                     <li> link: <input type="text" size="80" name="newsuri2" value="$FORM{'newsuri2'}" /></li>
                   </ul>
              <li> <input type="text" name="newscode3" value="$FORM{'newscode3'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="newshl3" size="80" value="$FORM{'newshl3'}" /> </li>
                     <li> link: <input type="text" name="newsuri3" size="80" value="$FORM{'newsuri3'}" /></li>
                   </ul>
              <li> <input type="text" name="newscode4" value="$FORM{'newscode4'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="newshl4" size="80" value="$FORM{'newshl4'}" /> </li>
                     <li> link: <input type="text" name="newsuri4" size="80" value="$FORM{'newsuri4'}" /></li>
                   </ul>
            </ul>
            <input type="hidden" name="newsemea1" value="$emeaNews[0]" />
            <input type="hidden" name="newsemea2" value="$emeaNews[1]" />
            <input type="hidden" name="newsemea3" value="$emeaNews[2]" />
            <input type="hidden" name="newsemea4" value="$emeaNews[3]" />

EOF

	# add News form for translated research
	$addFRForm =<<EOF;
            <ul>
              <li> <a href="javascript:void(null);" onclick="javascript:movefrdown();return false;">move fr down</a>
              <li> <input type="text" name="frcode1" value="$FORM{'frcode1'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl1" size="80" value="$FORM{'frhl1'}" /> </li>
                     <li> link: <input type="text" size="80" name="fruri1" value="$FORM{'fruri1'}" /></li>
                   </ul>
              <li> <input type="text" name="frcode2" value="$FORM{'frcode2'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl2" size="80" value="$FORM{'frhl2'}" /> </li>
                     <li> link: <input type="text" size="80" name="fruri2" value="$FORM{'fruri2'}" /></li>
                   </ul>
              <li> <input type="text" name="frcode3" value="$FORM{'frcode3'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl3" size="80" value="$FORM{'frhl3'}" /> </li>
                     <li> link: <input type="text" name="fruri3" size="80" value="$FORM{'fruri3'}" /></li>
                   </ul>
              <li> <input type="text" name="frcode4" value="$FORM{'frcode4'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl4" size="80" value="$FORM{'frhl4'}" /> </li>
                     <li> link: <input type="text" name="fruri4" size="80" value="$FORM{'fruri4'}" /></li>
                   </ul>
            </ul>
            <input type="hidden" name="fremea1" value="$emeaFR[0]" />
            <input type="hidden" name="fremea2" value="$emeaFR[1]" />
            <input type="hidden" name="fremea3" value="$emeaFR[2]" />
            <input type="hidden" name="fremea4" value="$emeaFR[3]" />

EOF

    $t1 = &SmartyPants ($title{$key1},1);
    $t2 = &SmartyPants ($title{$key2},1);
    $d1 = &SmartyPants ($desc{$key1},1);
    $d2 = &SmartyPants ($desc{$key2},1);



    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>pickResearch.cgi - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1                  {	font-size: 14pt;  }
h2                  {   font-size: 12pt;  }
h3                  {	font-size: 10pt; }
li,p,td	            {	font-size: 9pt;  }

/* focal points - what to do if text longer than image ?? */
.focalpoint       {  float: left; margin: 5px; padding: 5px; padding-right: 10px; background: #fff;  }
.focalpoint img   {  float: left; margin: 2px; padding: 0; }
.focalpoint   p   {  float: left; padding: 0; margin: 0; margin-left: 5px; vertical-align: top;
                     font-size: 11px; color: #4a4a4a;  }
.focalpoint p a   {  font-weight: bold; color: #3088CC; text-decoration: none;
                     line-height: 110%;  margin: 0; padding: 0; }

/* in the news */
.inthenewslist ul             {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;  }
.inthenewslist li             {  list-style-type: circle; list-style-image: url(http://regionals4.gartner.com/images/homepage/reversed_green_arrow.gif);
                                 color: #3088CC; line-height: 110%; padding: 3px;  }
.inthenewslist a              {  font-family: Verdana, Arial, Helvetica, sans-serif;
                                 font-weight: bold; font-size: 11px; color: #3088CC;
                                 text-decoration: none; line-height: 110%;  }
.inthenewslist a:hover        {  text-decoration: underline;  }

/* featured research */
.featuredresearchlist ul      {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;
                                 border: 1px dashed #fff;  }
.featuredresearchlist li      {  list-style-type: circle; list-style-image: url(http://regionals4.gartner.com/images/homepage/reversed_blue_arrow.gif);
                                 color: #3088CC; line-height: 110%; padding: 3px;  }
.featuredresearchlist a       {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold;
                                 font-size: 11px; color: #3088CC; text-decoration: none;
                                 line-height: 110%;  }
.featuredresearchlist a:hover {  text-decoration: underline;  }

.msg {  font-size: .75em; font-family: courier, fixed; color: 333; border: 1px dashed navy; padding: 10px; margin: 10px;  }

</style>
<script type="text/javascript" language="javascript">

function movenews() {
    document.form.newscode4.value = document.form.newsemea4.value;
    document.form.newscode3.value = document.form.newsemea3.value;
    document.form.newscode2.value = document.form.newsemea2.value;
    document.form.newscode1.value = document.form.newsemea1.value;

    document.form.newsuri4.value = "";
    document.form.newsuri3.value = "";
    document.form.newsuri2.value = "";
    document.form.newsuri1.value = "";

    document.form.newshl4.value = "";
    document.form.newshl3.value = "";
    document.form.newshl2.value = "";
    document.form.newshl1.value = "";

}
function moveresearch() {
    document.form.frcode4.value = document.form.fremea4.value;
    document.form.frcode3.value = document.form.fremea3.value;
    document.form.frcode2.value = document.form.fremea2.value;
    document.form.frcode1.value = document.form.fremea1.value;

    document.form.fruri4.value = "";
    document.form.fruri3.value = "";
    document.form.fruri2.value = "";
    document.form.fruri1.value = "";

    document.form.frhl4.value = "";
    document.form.frhl3.value = "";
    document.form.frhl2.value = "";
    document.form.frhl1.value = "";

}
function movefp() {

    document.form.title2.value = document.form.title1.value;
    document.form.desc2.value  = document.form.desc1.value;
    document.form.img2.value   = document.form.img1.value;
    document.form.date2.value  = document.form.date1.value;
    document.form.url2.value   = document.form.url1.value;
    document.form.key2.value   = document.form.key1.value;

    // set to null
    document.form.title1.value = ""
    document.form.desc1.value  = ""
    document.form.img1.value   = ""
    document.form.date1.value  = "$date";
    document.form.url1.value   = ""
    document.form.key1.value   = "$yyyymmdd";

    return false;
}

function movenewsdown() {

    document.form.newshl4.value = document.form.newshl3.value;
    document.form.newshl3.value = document.form.newshl2.value;
    document.form.newshl2.value = document.form.newshl1.value;
    document.form.newshl1.value = "";


    document.form.newsuri4.value = document.form.newsuri3.value;
    document.form.newsuri3.value = document.form.newsuri2.value;
    document.form.newsuri2.value = document.form.newsuri1.value;
    document.form.newsuri1.value = "";

    document.form.newscode4.value = document.form.newscode3.value;
    document.form.newscode3.value = document.form.newscode2.value;
    document.form.newscode2.value = document.form.newscode1.value;
    document.form.newscode1.value = "";


}

function movefrdown() {

    document.form.frhl4.value = document.form.frhl3.value;
    document.form.frhl3.value = document.form.frhl2.value;
    document.form.frhl2.value = document.form.frhl1.value;
    document.form.frhl1.value = "";


    document.form.fruri4.value = document.form.fruri3.value;
    document.form.fruri3.value = document.form.fruri2.value;
    document.form.fruri2.value = document.form.fruri1.value;
    document.form.fruri1.value = "";

    document.form.frcode4.value = document.form.frcode3.value;
    document.form.frcode3.value = document.form.frcode2.value;
    document.form.frcode2.value = document.form.frcode1.value;
    document.form.frcode1.value = "";


}

</script>
</head>
</head>
<body>
<form action="$thisScript" name="form" method="post">

    <input type="hidden" name="locale" value="$FORM{'locale'}" />
    <input type="hidden" name="origNews" value="$news" />
    <input type="hidden" name="emeaNews" value="$emeanews" />
    <input type="hidden" name="origFR" value="$research" />
    <input type="hidden" name="emeaResearch" value="$emearesearch" />
    <input type="hidden" name="yyyymmdd" value="$yyyymmdd" />

<h1>Pick Research &amp; Focal Points - $FORM{'locale'}</h1>

<h2>News</h2>
<ul><li>Resid or Doc Codes:</li>
  <ul>
    <li>current news [ $news ]</li>
    $useEmeaNews
    $addNewsForm
    </ul>
</ul>
<ul class="inthenewslist">
$curNews
</ul>

<h2>Research</h2>
<ul><li>Resid or Doc Codes:</li>
  <ul>
    <li>current research [ $research ]</li>
    $useEmeaResearch
    $addFRForm
  </ul>
</ul>

<ul class="featuredresearchlist">
$curFR
</ul>

<h2>Focal Points</h2>

<h3>Primary</h3>
<table>
   <tr><td>Title</td>
        <td><input type="text" name="title1" size="70" width="500" value="$title{$key1}"/></td><td rowspan="5">

<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key1}"><img src="http://regionals4.gartner.com/$img{$key1}" width="100" height="68" alt="$t1" border="0" class="inline" align="left" />');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key1}">$t1</a></p>');
    document.write('<p>$d1</p>');
    document.write('<p>$date{$key1}</p>');
    document.write('</div>');
    document.close();
</script>


        </td></tr>
    <tr><td>URL</td>
        <td><input type="text" name="url1" size="70" width="500" value="$url{$key1}"/></td></tr>
    <tr><td>Desc</td>
        <td><textarea name="desc1" rows="5" cols="40">$desc{$key1}</textarea></td></tr>
    <tr><td>Image location</td>
        <td><input type="text" name="img1"size="70" value="$img{$key1}"  width="500" /></td></tr>
    <tr><td>Pub Date</td>
        <td><input type="text" name="date1" size="70" value="$date{$key1}"  width="500" /></td></tr>
        <tr><td>Updated/New?</td>
        <td><input type="checkbox" name="updated1" value="1" /></td></tr>
  <input type="hidden" name="key1" value="$key1" />
</table>

<p><a href="javascript:void(null);" onclick="javascript:movefp();return false;">move to secondary</a></p>



<h3>Secondary</h3>
<table>
    <tr><td>Title</td>
        <td><input type="text" name="title2" size="70" width="500" value="$title{$key2}"/></td><td rowspan="5">

<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key2}"><img src="http://regionals4.gartner.com/$img{$key2}" width="100" height="68" alt="$t2" border="0" class="inline" align="left" />');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key2}">$t2</a></p>');
    document.write('<p>$d2</p>');
    document.write('<p>$date{$key2}</p>');
    document.write('</div>');
    document.close();
</script>


        </td></tr>
    <tr><td>URL</td>
        <td><input type="text" name="url2" size="70" width="500" value="$url{$key2}"/></td></tr>
    <tr><td>Desc</td>
        <td><textarea name="desc2" rows="5" cols="40">$desc{$key2}</textarea></td></tr>
    <tr><td>Image location</td>
        <td><input type="text" name="img2" size="70" value="$img{$key2}"  width="500" /></td></tr>
    <tr><td>Pub Date</td>
        <td><input type="text" name="date2" value="$date{$key2}"  width="500" /></td></tr>
    <tr><td>Updated/New?</td>
        <td><input type="checkbox" name="updated2" value="1" /></td></tr>

  <input type="hidden" name="key2" value="$key2" />
</table>

server: <input type="radio" name="site" value="prod" checked="checked" /> production <input type="radio" name="site" value="qa" /> qa

<input type="submit">

<h2>Instructions</h3>
<div class="msg">
<p>These forms allow you to update the news, research and focal points on the regional websites</p>
<ul>
  <li> <strong>News &amp; Research</strong></li>
  <ul>

    <li>  For news and research you can enter the resid or doccode of the g.com document you want to add or promote.</li>
    <ol>
      <li> When you hit submit, it will try to look up the document in its on db of document.</li>
      <li> If it can't find it, it will query g.com for the informaton.</li>
      <li> If it finds the information in its own database, it will use that information.
      <li> So if you have added an alternate/translated title or link, it will use that instead.</li>
      <li> Obviously, if it goes to g.com, it will be in english.</li>
    </ol>
    <li> <strong>Translation</strong></li>
    <ul>
      <li> <strong>Translate Title Only</strong>: you must have the g.com resid or doccode and then simply paste in the translated text into the corresponsing <u>title</u> field.</li>
      <li> <strong>Add Non-Gartner Research</strong>: you must leave the resid field <strong>blank</strong> and add both a <u>title</u> and <u>link</u></li>
    </ul>

    <li>  <u>move news down</u> or <u>move fr down</u> litterally moves all news/research down one set of fields, allowing you to add as many new items as you need.  <i>This is important to do instead of just replacing the resid/doccodes as it will replace the title and links with the old information.</i></li>

    <li> On locales other than emea, you have a option, <u>use EMEA news/research</u>.  This will simply copy all of the emea codes over the locale's.</li>
    <ul>
      <li> If you only want to move one or two in, then use the <u>move news/fr down</u> link and copy the resids from the list next to <u>use emea news/research</u></li>
    </ul>

  </ul>
  <li> <strong>Focal Points</strong></li>
  <ul>
    <li> These currently are only being used for the weekly emailer, test rss fee and the xhtml version of the site.</li>
    <li> <u>move to secondary</u> moves the top fp's contents down</li>
    <li> <strong>PubDate</strong> is for the rss feeds, please attempt to fill it in correctly</li>
    <li> <strong>Updated/New?</strong> tells the tool to republish the fp includes</li>
    <li> NOTE: <i>this tool hasn't been set up for translation of includes yet.</i></li>
  </ul>
  <li> Final Note: <i>this tool also FTPs the news and research headlines to campsqa, so on these sites there is no urlInclude.... it also create a backup of the previous include on the remote server called ...incl.old</i></li>
  <li> Also: <i>I will move these instructions to the bottom of the page when someone metions it. ;-)</i></li>

</ul>


</div>


$menu

</form>
</body>
</html>

EndofHTML


}

sub preSpace {

    # add spaces before a line for mailing format

    local $flag   = 0;
    local $out    = "";
    local $space  = "";
    local @in     = split ("<br \/\>", $_[0]);

    local $i = 0;
    until ($i == $_[1]) {
	$i++;
	$space .= " ";
    }

    foreach (@in) {

	if (!$flag) {
	    $out = "$_\n";
	    $flag = 1;
	} else {
	    $out .= "$space$_\n";
	}
    }
    return($out);

}


sub dateCode {

	# counter to make sure its unique
	$dcCounter++;

	local $ds = `date +'%Y%m%d%S'`;
	chop($ds);
	$ds = "$ds"."$dcCounter";
	return($ds);

}

sub OLDreplaceChars {

    $listFile = "/home/gartner/html/rt/accent_list.txt"; #"c:/bin/accent_list.txt.utf8";

    &openList();

    local $word = $_[0];

    $word =~ s/’/'/g;# in accent list as &acute;, but not working

    foreach $letter (@list) {
	if (/$letter/) {
	    $word =~ s/$letter/$replace{$letter}/g;
	}
    }

    return($word);

}




sub FTPfile_good {

    # ftp files to remote servers
    # take 2 args
    # 1. filename
    # 2. relative path from emea/
    # 3. remote filename (<optional> for xhtml)

    use Net::FTP;


    local $locale = $_[1];
    $locale = "" if ($_[1] =~ /emea/);

    chdir("/home/gartner/html/rt/content/emea/$locale/");

    local $remoteFullPath  = "regionalization/templates/emea/$locale/";

    local $localFile = $_[0];

    local $remoteFile = $_[0];
    $remoteFile = $_[2]  if ($_[2]);

    local $saveFile = "$remoteFile"."\.old";


    $ftpmsg .= "<strong>FTP MESSAGES</strong><br />\n$ftpSite<br />\n\n";

    $ftp = Net::FTP->new($ftpSite)
	or $ftpmsg .= "Can't start FTP session<br>\n";
    $ftp->login("pmahnke","hi11top")
	or $ftpmsg .= "Can't login into FTP session<br>\n";
    $ftp->cwd($remoteFullPath)
        or $ftpmsg .= "Can't change directory on remove server: $remoteFullPath<br>\n";
    $ftp->type('I')
	or $ftpmsg .= "Can't change to ascii mode<br>\n";
    $ftp->rename($remoteFile, $saveFile)
	or $ftpmsg .= "Can't rename file: $locale/$remoteFile to $saveFile<br>\n";
    $ftp->put($localFile,$remoteFile)
	or $ftpmsg .= "Can't PUT file: $locale/$remoteFile<br>\n";
    $ftp->quit();

    $ftpmsg .= "Going to put<br /> $localFile to $remoteFullPath$remoteFile<br /><br />\n\n";

}
