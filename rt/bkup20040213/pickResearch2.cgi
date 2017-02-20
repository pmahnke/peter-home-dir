#!/usr/local/bin/perl


########################################################################
#
# pickResearch2.cgi
#
#   written: 15 Dec 2003 by Peter Mahnke
#   modified:
#
#
#   run from a web browser
#   currently only called through update_menu.cgi
#
#   DESCRIPTION
#     allows regional site editors to pick News,Research and
#     update Focal Points from a single page and output them into
#     all the major output formats required for the regional sites
#
#     namely: html, xhtml, mailing formats, exp formats and rss
#
#     for news and research it taked in doc ids or res ids and logs them
#     per locale, for focal points you input the text and relative file
#     and uri information into a form, it also logs the data
#
#     when the form is submitted, the application looks up the document
#     details for the documents, updates the focal points as required
#     and outputs all the includes again into the /rt/content/<LOCALE>/
#     directory strcuture.
#
########################################################################

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/cgi-bin/gNOlogin.pl");
require ("/home/gartner/html/rt/getNODocument3.pl");
require ("/home/gartner/html/rt/common.pl");
require ("/home/gartner/html/rt/commonDoccodes.pl");



##############################################################
# Variables
local $fileFP = "/home/gartner/html/rt/content/fp.csv";
local $server  = "www4";
$date          = `date +'%a, %d %b %Y %T GMT'`;
$yyyymmdd      = `date +'%Y%m%d'`;
chop($date);
chop($yyyymmdd);



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
	@docs = split (/ /, $FORM{'news'});
	foreach (@docs) {
		&getDoc($_);
	}

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
        @docs = split (/ /, $FORM{'research'});
	foreach (@docs) {
		&getDoc($_);
	}

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

    local $docCode = "DisplayDocument\?id\="."$_[0]";
    $link = "http:\/\/www4.gartner.com\/"."$docCode";  # .\&acsFlg\=accessBought";

    local ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price) = &getResearchDetail($link,$server);

    # didn't get title with resid, try doc id
    if (!$title) {
	$msg .= "didn't get $link<br\>\n" if (!$title);
	$docCode = "DisplayDocument\?doc_cd\="."$_[0]";
	$link = "http:\/\/www4.gartner.com\/"."$docCode"; # ."\&acsFlg\=accessBought";
	($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price) = &getResearchDetail($link,$server);
	$msg .= "didn't get $link<br\>\n" if (!$title);
    }

    #add proper attributes to links
    $link =~ s/uid=Y&fRef=true/call=email&ref=g_emalert/;


    # put dates into proper RSS 2.0 format
    use DateTime::Format::HTTP;
    my $dt = 'DateTime::Format::HTTP';
    $datestring = $dt->parse_datetime($pubDate, 'GMT');
    $dateStr = $dt->format_datetime($datestring);

    # clean up title
    $title =~ s/EMEA/Europe, Middle East and Africa/g;
    $title =~ s/ \(Executive Summary\)//g;

    # do the no hanging word logic on $title
    $noHangTitle = &noHang($title, 44);
    $noHangTitle =~ s/\&/\&amp\;/g;

    # copy of $title without <br />
    $origTitle = $title;

    # turn & into &amp;
    $title   =~ s/\&/\&amp\;/g;
    $summary =~ s/\&/\&amp\;/g;


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
\n<!--start research  - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate-->
    <tr><td width="356" height="8" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="8" alt="" border="0"></td></tr>
    <tr><td width="22" bgcolor="#FFFFFF" valign="top" align="center"><a href="javascript:void(null)" onclick="openResult('/$docCode')" class="smallBlueLink"><img src="//img/homepage/reversed_blue_arrow.gif" width="9" height="9" vspace="2" alt="$title" border="0"></a></td>\n        <td width="328" valign="top" bgcolor="#FFFFFF"><a href="javascript:void(null)" onclick="openResult('/$docCode')" class="smallBlueLink">$noHangTitle</a></td>\n        <td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>\n    </tr>
<!--end research - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->\n
EndofHTML

	}


	if ($processFlag eq "news") {

		# NEWS HTML
		$htmlNEWS .= <<EndofHTML;
\n<!--start news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->
    <tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
    <tr><td width="22" bgcolor="#FFFFFF" valign="top" align="center"><a href="javascript:void(null)" onclick="openResult('/$docCode')" class="largeGrayLink"><img src="/images/homepage/reversed_green_arrow.gif" width="9" height="9" vspace="3" alt="$title" border="0"></a></td>\n        <td width="328" valign="top" bgcolor="#FFFFFF"><a href="$docCode" onclick="openResult('/$docCode');return false;" class="smallBlueLink" target="_new">$noHangTitle</a></td>\n        <td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>\n    </tr>
<!--end news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->\n
EndofHTML

		# EXP FORMAT
		$EXPline .= <<EndofHTML;
                                             <tr>
                                                 <td width="10" valign="top"><img src="/pages/docs/exp/images/common/bullet_gray.gif" width="10" height="8" vspace="3"></td>
                                                 <td width="398"valign="top"><a href="/$docCode" onclick="researchPop('/$docCode'); return false;" class="grey11pxBoldLk" target="_new">$title</a><br></td>
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


    $rss .= "<item>\n  <title>$title</title>\n  <description>$summary</description>\n  <pubDate>$dateStr</pubDate>\n  <link><![CDATA[$link]]></link>\n</item>\n";

    $xhtml{$processFlag} .=  <<EndofHTML;
 <li> <a href="\#" onclick="openResult('/$docCode')">$title</a></li>
EndofHTML

    $view .=  <<EndofHTML;
 <li> <a href="\#" onclick="openResult('/$docCode')">$title</a></li>
EndofHTML

}

####################################################################
sub saveOutput {




    #####################################################
    # save html versions
    local $fn = "/home/gartner/html/rt/content/";

    if ($FORM{'locale'} eq "emea") {
	$fn = "$fn"."emea/"."home_news_headlines\.incl";
    } else {
	$fn = "$fn"."emea/"."$FORM{'locale'}"."/home_news_headlines\.incl";
    }
    &saveFile($fn, $htmlNEWS);


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
	$fn = "$fn"."emea/"."home_fr_headlines\.incl";
    } else {
	$fn = "$fn"."emea/"."$FORM{'locale'}"."/home_fr_headlines\.incl";
    }
    &saveFile($fn, $htmlFR);


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
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/"."xhtml"."$key"."\.incl";
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

	# save HTML fp
	open (FP, ">/home/gartner/html/rt/content/emea/home_fr_highlight_01.incl") || die "Can't open FP1\n";
	print FP <<ENDofHTML;
<!-- start featured research highlight 1 -->
<tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
<tr><td width="350" bgcolor="#FFFFFF" valign="top" colspan="2"><a href="$FORM{'url1'}"><img src="$FORM{'img1'}" width="100" height="68" hspace="6" align="left" alt="$FORM{'title1'}" border="0"></a><table border="0" cellspacing="0" cellpadding="0"><tr><td><a href="$FORM{'url1'}" class="largeBlueLink">$FORM{'title1'}</a><br /><span class="smallGrayText">$FORM{'desc1'}</span><br /></td></tr></table></td><td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td></tr>
<!-- end featured research highlight 2 -->
ENDofHTML
	close (FP);

	open (FP, ">/home/gartner/html/rt/content/emea/home_fr_highlight_02.incl") || die "Can't open FP2\n";
	print FP <<ENDofHTML;
<!-- start featured research highlight 1 -->
<tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
<tr><td width="350" bgcolor="#FFFFFF" valign="top" colspan="2"><a href="$FORM{'url2'}"><img src="$FORM{'img2'}" width="100" height="68" hspace="6" align="left" alt="$FORM{'title2'}" border="0"></a><table border="0" cellspacing="0" cellpadding="0"><tr><td><a href="$FORM{'url2'}" class="largeBlueLink">$FORM{'title2'}</a><br /><span class="smallGrayText">$FORM{'desc2'}</span><br /></td></tr></table></td><td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td></tr>
<!-- end featured research highlight 2 -->
ENDofHTML
	close (FP);

	# save xhtml fp
	open (FP, ">/home/gartner/html/rt/content/emea/xhtml_fr1.incl") || die "Can't open xhtml FP1\n";
	print FP <<ENDofHTML;
	<div class="focalpoint">
<a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url1'}"><img src="http://regionals4.gartner.com/$FORM{'img1'}" width="100" height="68" alt="$FORM{'title1'}" border="0" align="left" /></a>
<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url1'}">$FORM{'title1'}</a></p>
<p>$FORM{'desc1'}</p>
</div>
ENDofHTML
	close (FP);


	open (FP, ">/home/gartner/html/rt/content/emea/xhtml_fr2.incl") || die "Can't open xhtml FP2\n";
	print FP <<ENDofHTML;
	<div class="focalpoint">
<a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url2'}"><img src="http://regionals4.gartner.com/$FORM{'img2'}" width="100" height="68" alt="$FORM{'title2'}" border="0" align="left" /></a>
<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$FORM{'url2'}">$FORM{'title2'}</a></p>
<p>$FORM{'desc2'}</p>
</div>
ENDofHTML
	close (FP);



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
	print OUT $_[1];
	close (OUT);

}

####################################################################
sub printOutput {


    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>pickResearch.cgi - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt;	}
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
.focalpoint     {  float: left; margin: 5px; padding: 5px; padding-right: 10px; background: #fff;  }
.focalpoint img {  float: left; margin: 2px; padding: 0; }
.focalpoint   p{  float: left; padding: 0; margin: 0; margin-left: 5px; vertical-align: top; font-size: 11px; color: #4a4a4a;  }
  .focalpoint p a{  font-weight: bold; color: #3088CC; text-decoration: none; line-height: 110%;  margin: 0; padding: 0; }

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
    document.write('<a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key1}"><img src="http://regionals4.gartner.com/$img{$key1}" width="100" height="68" alt="$title{$key1}" border="0" class="inline" align="left" />');
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
    document.write('<a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key2}"><img src="http://regionals4.gartner.com/$img{$key2}" width="100" height="68" alt="$title{$key2}" border="0" class="inline" align="left" />');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key2}">$title{$key2}</a></p>');
    document.write('<p>$desc{$key2}</p>');
    document.write('<p>$date{$key2}</p>');
    document.write('</div>');
    document.close();
</script>


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
<item&gt;
  <title&gt;$FORM{'title'}</title&gt;
  <description&gt;$FORM{'desc'}</description&gt;
  <pubDate&gt;$FORM{'date'}</pubDate&gt;
  <link&gt;$FORM{'url'}</link&gt;
</item&gt;
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
	    $fn = "$fn"."emea/"."xhtmlnews\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtmlnews\.incl";
	}
	$curNews = &readFile($fn);

	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/"."xhtmlresearch\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtmlresearch\.incl";
	}
	$curFR = &readFile($fn);



	if ($FORM{'locale'} ne "emea") {
		$emeanews = &readCodes('NEWS', 'emea');
		$emearesearch = &readCodes('FR', 'emea');
		$useEmeaNews = "<li\><a href\=\"javascript:void\(null\)\;\" onclick\=\"javascript:movenews\(\)\;return false\;\"\>use EMEA News<\/a\><\/li\>\n";
		$useEmeaResearch = "<li\><a href\=\"javascript:void\(null\)\;\" onclick\=\"javascript:moveresearch\(\)\;return false\;\"\>use EMEA Research<\/a\><\/li\>\n";
	}

    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>pickResearch.cgi - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt;	}
h3	{		font-size: 10pt;	}
li,p,td	{		font-size: 9pt;	        }

/* focal points - what to do if text longer than image ?? */
.focalpoint       {  float: left; margin: 5px; padding: 5px; padding-right: 10px; background: #fff;  }
.focalpoint img   {  float: left; margin: 2px; padding: 0; }
.focalpoint   p   {  float: left; padding: 0; margin: 0; margin-left: 5px; vertical-align: top; font-size: 11px; color: #4a4a4a;  }
  .focalpoint p a {  font-weight: bold; color: #3088CC; text-decoration: none; line-height: 110%;  margin: 0; padding: 0; }

/* in the news */
    .inthenewslist ul             {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;  }
.inthenewslist li             {  list-style-type: circle; list-style-image: url(http://regionals4.gartner.com/images/homepage/reversed_green_arrow.gif); color: #3088CC; line-height: 110%; padding: 3px;  }
.inthenewslist a              {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #3088CC; text-decoration: none; line-height: 110%;  }
.inthenewslist a:hover        {  text-decoration: underline;  }

/* featured research */
.featuredresearchlist ul      {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px; border: 1px dashed #fff;  }
.featuredresearchlist li      {  list-style-type: circle; list-style-image: url(http://regionals4.gartner.com/images/homepage/reversed_blue_arrow.gif); color: #3088CC; line-height: 110%; padding: 3px;  }
.featuredresearchlist a       {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #3088CC; text-decoration: none; line-height: 110%;  }
.featuredresearchlist a:hover {  text-decoration: underline;  }

</style>
<script type="text/javascript" language="javascript">

function movenews() {
    document.form.news.value = document.form.emeaNews.value;
    document.form.origNews.value = ""
}
function moveresearch() {
    document.form.research.value = document.form.emeaResearch.value;
    document.form.origFR.value = ""
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
</script>
</head>
</head>
<body>
<form name="form" method="get">
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
    <li><input type="text" size="70" width="500" name="news" value="$news" /><i>spaces between</i></li>
    $useEmeaNews
    </ul>
</ul>
<ul class="inthenewslist">
$curNews
</ul>

<h2>Research</h2>
<ul><li>Resid or Doc Codes:</li>
  <ul>
    <li><input type="text" size="70" width="500" name="research" value="$research"/><i>spaces between</i></li>
    $useEmeaResearch
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
    document.write('<a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key1}"><img src="http://regionals4.gartner.com/$img{$key1}" width="100" height="68" alt="$title{$key1}" border="0" class="inline" align="left" />');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key1}">$title{$key1}</a></p>');
    document.write('<p>$desc{$key1}</p>');
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
    document.write('<a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key2}"><img src="http://regionals4.gartner.com/$img{$key2}" width="100" height="68" alt="$title{$key2}" border="0" class="inline" align="left" />');
    document.write('<p><a href="http://regionals4.gartner.com/regionalization/content/emea/$url{$key2}">$title{$key2}</a></p>');
    document.write('<p>$desc{$key2}</p>');
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



<input type=submit>
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
