#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/cgi-bin/gNOlogin.pl");
require ("/home/gartner/html/rt/getNODocument3.pl");
require ("/home/gartner/html/rt/common.pl");

# Variables
local $server = "www4";


# expects full url to doc
# i.e. http://www4.gartner.com/DisplayDocument?id=361453&acsFlg=accessBought

#    print <<EndofHTML;
#Content-type:  text/html

#<html>
#<body>
#message: $msg<p>$getGARTNERmsg<p>
#EndofHTML

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
<head>
<title>getResearch5.cgi</title>
</head>
<body>
<form method=GET>

Doc Codes: <input type=text width=200 name=doccd><i>spaces between</i><p>
Research: <input type=radio name=type value=Research checked> &nbsp; 
First Take: <input type=radio name=type value=FirstTake><p>
Mailing HTML Format: <input type=checkbox name=mailing><p>
Mailing TEXT Format: <input type=checkbox name=focal><p>
ecomm Mailing Format: <input type=checkbox name=ecomm_mailing><p>
ecomm Page Format: <input type=checkbox name=ecomm_page><p>
ecomm Listing Format: <input type=checkbox name=ecomm_listing><p>
ecomm Type:
<select name=ecomm_type>
<option value="">
<option value="hw">Hardware & Systems
<option value="serv">IT Services
<option value="semi">Semiconductors
<option value="sw">Software
<option value="tel">Telecommunications
</select><p>
Focal Point Format: <input type=checkbox name=fp><p>
EXP in the news Format: <input type=checkbox name=exp><p>
<input type=submit>
</form>
</body>
</html>

EndofHTML

    exit;

}


@docs = split (/ /, $FORM{'doccd'});

foreach (@docs) {
    &getDoc($_);
}

&printOutput;
exit;


sub getDoc {

    local $docCode = "DisplayDocument\?id\="."$_[0]";
    $link = "http:\/\/www4.gartner.com\/"."$docCode";  # .\&acsFlg\=accessBought";
    
    local ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price) = &getResearchDetail($link,$server);

    if (!$title) {
	$msg .= "didn't get $link<br\>\n" if (!$title);
	$docCode = "DisplayDocument\?doc_cd\="."$_[0]";
	$link = "http:\/\/www4.gartner.com\/"."$docCode"; # ."\&acsFlg\=accessBought";
	($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price) = &getResearchDetail($link,$server);
	$msg .= "didn't get $link<br\>\n" if (!$title);
    }

    $getGARTNERmsg =~ s/</\&lt\;/g;

    # clean up author
    $auth =~ s/</\&lt\;/g if (!$FORM{'fp'}); # convert < to html safe &lt;
    if ($FORM{'fp'}) {
	$auth =~ s/,/ \&nbsp\; /g; # convert , to a space
    } else {
	$auth =~ s/,/ \&amp\;nbsp\; /g; # convert , to a space
    }

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
	
    # clean up title
    $title =~ s/EMEA/Europe, Middle East and Africa/g;
    $title =~ s/ \(Executive Summary\)//g;
    
    # copy of $title without <br />
    $origTitle = $title;             

    # do the no hanging word logic on $title
    $title = &noHang($title, 44);
    #$title =~ s/\&/\&amp\;/g;
    if (!$FORM{'mailing'}  && !$FORM{'focal'} && !$FORM{'fp'}) {
	$title =~ s/\</\&lt\;/g;
    } else {
	$title =~ s/<br \/\>//g;
    }




    if ($FORM{type} eq "Research"  && !$FORM{'mailing'} && !$FORM{'focal'} && !$FORM{'fp'} && !$FORM{'ecomm_mailing'} && !$FORM{'ecomm_page'}  && !$FORM{'ecomm_listing'}) {

	$line .=  <<EndofHTML;

&lt;!--start research  - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate-->
    &lt;tr>
        &lt;td width="356" height="15" colspan="3" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="356" height="15" alt="" border="0">&lt;/td>
    &lt;/tr>
    &lt;tr>
        &lt;td width="22" bgcolor="#FFFFFF" valign="top" align="center">&lt;a href="javascript:void(null)" onclick="openResult('/$docCode')" class="smallBlueLink">&lt;img src="//img/homepage/reversed_blue_arrow.gif" width="9" height="9" vspace="2" alt="$origTitle" border="0">&lt;/a>&lt;/td>
        &lt;td width="328" valign="top" bgcolor="#FFFFFF">&lt;a href="javascript:void(null)" onclick="openResult('/$docCode')" class="smallBlueLink">
$title
&lt;/a>&lt;/td>
        &lt;td width="6" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="6" height="1" alt="" border="0">&lt;/td>
    &lt;/tr>
&lt;!--end research - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->

EndofHTML

     } elsif ($FORM{type} eq "FirstTake" && !$FORM{'mailing'}  && !$FORM{'focal'} && !$FORM{'fp'} && !$FORM{'exp'} && !$FORM{'ecomm_mailing'} && !$FORM{'ecomm_page'}  && !$FORM{'ecomm_listing'}) {

	 $line .= <<EndofHTML;

&lt;!--start news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->
    &lt;tr>
        &lt;td width="356" height="10" colspan="3" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="356" height="10" alt="" border="0">&lt;/td>
    &lt;/tr>
    &lt;tr>
        &lt;td width="22" bgcolor="#FFFFFF" valign="top" align="center">&lt;a href="javascript:void(null)" onclick="openResult('/$docCode')" class="largeGrayLink">&lt;img src="//img/homepage/reversed_green_arrow.gif" width="9" height="9" vspace="3" alt="$origTitle" border="0">&lt;/a>&lt;/td>
        &lt;td width="328" valign="top" bgcolor="#FFFFFF">&lt;a href="javascript:void(null)" onclick="openResult('/$docCode')" class="largeGrayLink">
$title
        &lt;/a>&lt;/td>
        &lt;td width="6" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="6" height="1" alt="" border="0">&lt;/td>
    &lt;/tr>
&lt;!--end news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->

EndofHTML

} elsif ($FORM{'mailing'}) {

    $auth  =~ s/\&lt\;a href\=(.[^\>]*)\>//g;
    $auth  =~ s/\&lt\;\/a\>//gi;
    $auth  =~ s/<\/a\>//gi;
    $auth  =~ s/ \| /\, /gi;
    
    $auth = &noHang($auth,'37'); #,'no');
    $auth = &preSpace ($auth,'4');

    $link =~ s/http(.[^\?]*)\?(.*)/http:\/\/regionals4.gartner.com\/regionalization\/content\/emea\/DisplayDocument.html\?$2/;

    $mailerTitle = &noHang($origTitle,'37'); #,'no');
#    $mailerTitle =~ tr/[a-z]/[A-Z]/;
    $mailerTitle = &preSpace ($mailerTitle,'4');
    chop($mailerTitle);
    $mailerSummary = &noHang($summary,'45'); #,'no');
#    $mailerSummary = &preSpace ($mailerSummary,'4');




 $line .= <<EndofHTML;


<a href="$link" style="font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 12px; color: #3088CC; text-decoration: none;  line-height: 1;">
$mailerTitle
</a>

<span style="font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 11px; color: #313131; text-decoration: none; cursor:default; line-height: 1.5;">
 &nbsp; <br />
$pubDate
 &nbsp; <br />
</span>

<span style="font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: normal; font-style: italic; font-size: 11px; color: #4D4D4D; text-decoration: none; line-height: 1.5;">
$auth
 &nbsp; <br />
</span>

<span style="font-family: Verdana, Arial, Helvetica, sans-serif; font-size: 11px; color: #4D4D4D; text-decoration: none; cursor:default;  line-height: 1;">
$mailerSummary
</span>
<br />

&nbsp; <p />


EndofHTML


    

} elsif ($FORM{'ecomm_mailing'}) {


    $fullPageFlag = 1;

#    $auth  =~ s/\&lt\;a href\=(.[^\>]*)\>//g;
#    $auth  =~ s/\&lt\;\/a\>//gi;
#    $auth  =~ s/<\/a\>//gi;
#    $auth  =~ s/ \| /\, /gi;
    
#    $auth = &noHang($auth,'37'); #,'no');
#    $auth = &preSpace ($auth,'4');

    $link =~ s/http(.[^\?]*)\?id=(.[^&]*)&*/http:\/\/regionals4.gartner.com\/regionalization\/content\/emea\/gpress\/dq\/gpress_mq_rpt_$2.html/;

    $mailerTitle = &noHang($origTitle,'44', 'no'); #,'no');
#    $mailerTitle =~ tr/[a-z]/[A-Z]/;
#    $mailerTitle = &preSpace ($mailerTitle,'4');
#    chop($mailerTitle);
#    $mailerSummary = &noHang($summary,'44', 'no');
    $mailerSummary = $summary;
#    $mailerSummary = &preSpace ($mailerSummary,'4');

    $price =~ s/\,//g;

    if ($price == 95) {
	$euroPrice = "75";
	$euroDiscount = "OVER 10\% OFF!"; #AND SAVE &euro;8 <br \/\>
    } elsif ($price == 495) {
	$euroPrice = "395";
	$euroDiscount = "OVER 10\% OFF!"; #AND SAVE &euro;41 <br \/\>
   } elsif ($price == 795) {
	$euroPrice = "625";
	$euroDiscount = "OVER 10\% OFF!"; #AND SAVE &euro;70 <br \/\>
    } elsif ($price == 1295) {
	$euroPrice = "995";
	$euroDiscount = "OVER 10\% OFF!"; #AND SAVE &euro;130 <br \/\>
    } elsif ($price == 1495) {
	$euroPrice = "1185";
	$euroDiscount = "OVER 10\% OFF!"; # &euro;112
    } elsif ($price == 2495) {
	$euroPrice = "1985";
	$euroDiscount = "OVER 10\% OFF!"; # &euro;198 
    } elsif ($price == 6995) {
	$euroPrice = "5495";
	$euroDiscount = "OVER 10\% OFF!"; # &euro;625 
    } elsif ($price == 9995) {
	$euroPrice = "7845";
	$euroDiscount = "OVER 10\% OFF!"; # &euro;801 
    } else {
	$euroPrice = ($price * 0.8839) * 0.9;
	$euroDiscount = $euroPrice * 0.1;
	$euroDiscount .= " ~ NEED PRICING \(USD \$ \|$price\| \)";
    }

    $line .= "<tr\>"    if (!$listingCount);

 $line .= <<EndofHTML;

        <td width="275" valign="top">

<a href="http://regionals4.gartner.com/regionalization/content/emea/gpress/mq/gpress_mq_rpt_$_[0].html" style="font-family:Verdana, Arial, Helvetica, sans-serif; color:#669966; font-size:9pt; font-weight:bold; text-decoration:underline; cursor:default; line-height: 1.2;" target="main">
$origTitle</a>

<span style="font-family:Verdana, Arial, Helvetica, sans-serif; color:#666666; font-size:9pt; line-height: 1.2;">
<br />
$mailerSummary
<br />
</span>

<a href="http://regionals4.gartner.com/regionalization/content/emea/gpress/mq/gpress_mq_rpt_$_[0].html" style="font-family:Verdana, Arial, Helvetica, sans-serif; color:#000000; font-size:9pt; line-height: 1.5; font-weight: bold; text-decoration: none;">
BUY IT TODAY FOR ONLY &euro;$euroPrice<br />
$euroDiscount</a>
<br /><br /><br />
</span>

        </td>


EndofHTML

    if ($listingCount) {
	$line .= "    <\/tr\>\n\n\n";
	$listingCount = 0;
    } else {
	$line .= "\n\n        <td width\=\"22\"\><\/td\>\n\n";
	$listingCount = 1;
    }

    

} elsif ($FORM{'ecomm_listing'}) {

    $fullPageFlag = 1;

    $line .= <<EndofHTML;
<li><a href="gpress_mq_rpt_$_[0].html" class="smallLinkText" target="main">$origTitle</a></li>

EndofHTML


} elsif ($FORM{'ecomm_page'}) {
    
    $fullPageFlag = 1;

    $auth  =~ s/\&lt\;a href\=(.[^\>]*)\>//g;
    $auth  =~ s/\&lt\;\/a\>//gi;
    $auth  =~ s/<\/a\>//gi;
    $auth  =~ s/ \| /\, /gi;
    
    $auth = &noHang($auth,'37'); #,'no');
    $auth = &preSpace ($auth,'4');

    $mailerTitle = &noHang($origTitle,'33'); #,'no');
    $ppTitle = $mailerTitle;
    $ppTitle =~ s/<br \/\>//g;
    $urlTitle = $origTitle;
    $urlTitle =~ s/ /\+/g;
    $mailerSummary = &noHang($summary,'40'); #,'no');


    # edit TOC
    undef local $links;
    @toc = split (/\n/, $toc);
    foreach (@toc) {
	
	s/<table BORDER\=0 CELLSPACING\=0 CELLPADDING\=0 WIDTH\=\"650\" \>/<table BORDER\=0 CELLSPACING\=0 CELLPADDING\=5 WIDTH\=\"100\%\" bgcolor\=\"\#f7f7f7\"\>/;
	
#	s/width\=578/width\=100/ig;
	s/header3/header2/;

	s/<HR SIZE\=1\>//ig;

	if (/table of contents</i) {
	    s/table of contents/<a name\=\"toc\"\>Table of Contents<\/a\>/i;
	    $links = <<EndofList
<a href="\#toc" class="smallLinkText"><img src="http://regionals.gartner.com/regionalization/img/gray_arrow.gif" alt="Table of Contents" width="10" height="10" border="0"></a> &nbsp; <a href="\#toc" class="smallLinkText">Table of Contents</a><br />
EndofList

        }  

        if (/list of figures</i) {
	    s/list of figures/<a name\=\"lof\"\>List of Figures<\/a\>/i;
	    $links .= <<EndofList
<a href="\#lof" class="smallLinkText"><img src="http://regionals.gartner.com/regionalization/img/gray_arrow.gif" alt="List of Figures" width="10" height="10" border="0"></a> &nbsp; <a href="\#lof" class="smallLinkText">List of Figures</a><br />
EndofList
        }
	
        if (/list of tables</i) {
            s/list of tables/<a name=\"lot"\>List of Tables<\/a\>/i;
	    $links .= <<EndofList
<a href="\#lot" class="smallLinkText"><img src="http://regionals.gartner.com/regionalization/img/gray_arrow.gif" alt="List of Tables" width="10" height="10" border="0"></a> &nbsp; <a href="\#lot" class="smallLinkText">List of Tables</a><br />
EndofList
        }

	$tocTRflag = 0 if (/<\/tr\>/i && $tocTRflag);
	if (/<table/i) {
	    $tocClean .= "                    $_\n";
	    $tocTRflag = 1;
	}
	next if ($tocTRflag);

	$tocClean .= "                    $_\n";
    }

    # remove first TR /TR completely
    # s/width=578/width=100/

    $price =~ s/\,//g;

    if ($price == 95) {
	$euroPrice = "75";
	$euroDiscount = "OVER 10\% OFF!"; #AND SAVE &euro;8 <br \/\>
    } elsif ($price == 495) {
	$euroPrice = "395";
	$euroDiscount = "OVER 10\% OFF!"; #AND SAVE &euro;41 <br \/\>
   } elsif ($price == 795) {
	$euroPrice = "625";
	$euroDiscount = "OVER 10\% OFF!"; #AND SAVE &euro;70 <br \/\>
    } elsif ($price == 1295) {
	$euroPrice = "995";
	$euroDiscount = "OVER 10\% OFF!"; #AND SAVE &euro;130 <br \/\>
    } elsif ($price == 1495) {
	$euroPrice = "1185";
	$euroDiscount = "OVER 10\% OFF!"; # &euro;112
    } elsif ($price == 2495) {
	$euroPrice = "1985";
	$euroDiscount = "OVER 10\% OFF!"; # &euro;198 
    } elsif ($price == 6995) {
	$euroPrice = "5495";
	$euroDiscount = "OVER 10\% OFF!"; # &euro;625 
    } elsif ($price == 9995) {
	$euroPrice = "7845";
	$euroDiscount = "OVER 10\% OFF!"; # &euro;801 
    } else {
	$euroPrice = ($price * 0.8839) * 0.9;
	$euroDiscount = $euroPrice * 0.1;
	$euroDiscount .= " ~ NEED PRICING \(USD \$ \|$price\| \)";
    }

 $line .= <<EndofHTML;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd">
<html>
 <head>
  <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">  
  <META HTTP-EQUIV="Content-Language" CONTENT="us-en">  
  <title>Gartner Magic Quadrant Reports - $origTitle</title>
 </head>

 <body  topmargin="0" leftmargin="0" marginwidth="0" marginheight="0" bgcolor="#BBBBBB">


<style>

td  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#000000; font-size:9pt; line-height: 1.5;}
.greyText  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#666666; font-size:9pt; line-height: 1.5;}
.buy { font-family:Verdana, Arial, Helvetica, sans-serif; color:#666666; font-size:18px; font-weith: normal; line-height: 1.2;}
.header1  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#000000; font-size:11pt; font-weight:bold; text-decoration:none; font-style:normal; font-style:normal; }
.header2  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#ffffff; font-size:9pt; font-weight:bold; font-weight:bold; background:#999999; }
.largeLinkText  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#F8981D; font-size:14px; font-weight:bold; font-style:normal; font-style:normal; text-decoration:none; cursor:default; }
.smallLinkText { font-family:Verdana, Arial, Helvetica, sans-serif; color:#F8981D; font-size:9pt; line-height: 1.5; text-decoration:none; }
.resIdText      { font-family:verdana,arial,helvetica; color:#BBBBBB; font-size:11px; text-decoration:none; font-style:normal; font-style:normal; } 
a:active        { text-decoration:underline; }
a:link          { text-decoration:none; }
a:hover         { text-decoration:underline; }
</style>


<!-- begin header -->
<table cellspacing=0 cellpadding=0 width="766" border="0" align="center" bgcolor="#ffffff">


    <tr><td colspan="3" width="766" height="2" bgcolor="bbbbbb"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="766" height="2"></span></td></tr>
    <tr><td colspan="3" width="766" height="2" bgcolor="ffffff"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="766" height="2"></span></td></tr>

    <tr>
	<td width="2" bgcolor="ffffff"><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width=2></td>
	    <td bgcolor="#F8981D" height="100" width="762" >
		<img src="http://regionals.gartner.com/regionalization/img/gpress/header_mq_762_100.gif" width="762" height="100" alt="Gartner Magic Quadrants"><br />
		    </td>
			<td width="2" bgcolor="ffffff">
			        <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width=2></span>
				    </td>
    </tr>
    <tr><td colspan="5" width="766" height="2" bgcolor="ffffff"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="766" height="2"></span></td></tr>
    <tr><td colspan="5" width="766" height="2" bgcolor="bbbbbb"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="766" height="2"></span></td></tr>

</table>
<!-- end header -->
  

<table cellspacing=0 cellpadding=0 width="766" border="0" align="center" bgcolor="#ffffff">
<tr>
    <td rowspan="20" width="40"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="40" height="0"></span></td>
	<td rowspan="1" width="328"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="328" height="0"></span></td>
	    <td rowspan="1" width="30" ><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="30" height="0"></span></td>
		<td rowspan="1" width="328"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="328" height="0"></span></td>
		    <td rowspan="20" width="40"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="40" height="0"></span></td>
</tr>


<tr>
    <td colspan="3"><span class="greyText">
&nbsp; <p />
Gartner Magic Quadrants provide a snapshot of how vendors are performing in a market segment and highlight the leaders to show how others compare.<br /><br />

Magic Quadrants help you make better informed decisions on companies you are looking to partner with, or whose services or products you want to buy.<br /><br /> 

</span>
 </td>
</tr>


<tr>
    <td width="328" valign="top">
            <br />
<!-- TITLE -->
<span class="largeLinkText">$mailerTitle</span>
 &nbsp; <br /><br />

<!-- PUB DATE -->
$pubDate
 &nbsp; <br /><br />

<!-- AUTHOR -->
<i>$auth</i>
 &nbsp; <br /><br />

<!-- SUMMARY -->
$mailerSummary
 &nbsp; <br /><br />

<!-- LINKS -->
<span class="header2"></span>
<a href="#toc" class="smallLinkText"><img src="http://regionals.gartner.com/regionalization/img/gray_arrow.gif" alt="Learn more" width="10" height="10" border="0"></a> &nbsp; <a href="#toc" class="smallLinkText">Typical Table of Contents</a><br />

<!-- IMAGE -->
<a href="#image" class="smallLinkText"><img src="http://regionals.gartner.com/regionalization/img/gray_arrow.gif" alt="Learn more" width="10" height="10" border="0"></a> &nbsp; <a href="#image" class="smallLinkText">Example Magic Quadrant</a><br /><br />
<a name=image><img src="http://regionals.gartner.com/regionalization/img/gpress/mq_icon.gif" width="229" height="240" alt="image of a magic quadrant"></a><br />


     <!-- END detail -->
	     
	     
	 </td>
	     <td width="30" bgcolor="#eeeeee">
            <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="30" height="0"></span>
        </td>
	    <td valign="top" bgcolor="#eeeeee">
            <br />

      <!-- img src="http://regionals.gartner.com/regionalization/img/gpress/greytext_dq_offer_$price.gif" width="328" height="56" alt="BUY THE REPORT TODAY FOR &euro;$euroPrice $euroDiscount!" -->
<span class=buy>BUY THIS MAGIC QUADRANT<br />
TODAY FOR ONLY &euro;$euroPrice <br />
$euroDiscount!<br /><br />
</span>
<!-- PayPal Add to Cart -->
<form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<span><a href="Javascript:void(null);" onClick="Javascript:window.open('gpress_mq_popup_invoice.html','invoice','menubar=no,toolbar=no,width=500,height=430');" class=smallLinkText><img src="http://regionals.gartner.com/regionalization/img/gpress/bullet_invoice_me.gif" alt="Invoice Me" width="113" height="21" border="0"></a></span><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="10" height="21"></span>
<input type="hidden" name="cmd" value="_cart">
<input type="hidden" name="business" value="peter.mahnke\@gartner.com">
<input type="hidden" name="item_name" value="$ppTitle">
<input type="hidden" name="item_number" value="$_[0]">
<input type="hidden" name="amount" value="$euroPrice">
<input type="hidden" name="image_url" value="https://regionals4.gartner.com/regionalization/img/gpress/gartner_logo_150_50.gif">
<input type="hidden" name="return" value="http://intl.transitionelement.com/cgi-bin/mqIPN.cgi">
<input type="hidden" name="cancel_return" value="http://regionals4.gartner.com/regionalization/content/emea/dq/gpress_mq_cancel.html">
<input type="hidden" name="currency_code" value="EUR">
<input type="image" src="https://regionals4.gartner.com/regionalization/img/gpress/add_to_cart.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">
<input type="hidden" name="add" value="1">
</form>

<span class="smallGrayText">Gartner has many other <br />
Magic Quadrants for sale.
<br /><br />
</span>

<a href="Javascript:void(null);" onClick="Javascript:window.open('gpress_mq_popup.html','listing','menubar=no,toolbar=no,scrollbars=yes,width=520,height=500');" class=smallLinkText><img src="http://regionals.gartner.com/regionalization/img/gray_arrow.gif" alt="View complete listing" width="10" height="10" border="0"></a> &nbsp; <a href="Javascript:void(null);" onClick="Javascript:window.open('gpress_mq_popup.html','listing','menubar=no,toolbar=no,scrollbars=yes,width=520,height=500');" class=smallLinkText>View complete listing</a><br /><br />
    
<span class="smallGrayText">This is a one-off mailing from Gartner.<br /> 
To receive quarterly updates highlighting the<br />
latest Gartner Magic Quadrants, please:<br />  <br />  
</span>


<a href="Javascript:void(null);" onClick="Javascript:window.open('/cgi/gpress_mq_popup_email.cgi','email','menubar=no,toolbar=no,width=500,height=500');" class=smallLinkText><img src="http://regionals.gartner.com/regionalization/img/gray_arrow.gif" alt="Sign up for our newsletter" width="10" height="10" border="0"></a> &nbsp; <a href="Javascript:void(null);" onClick="Javascript:window.open('/cgi/gpress_mq_popup_email.cgi','email','menubar=no,toolbar=no,width=500,height=500');" class="smallLinkText">Sign up for our newsletter</a><br /><br />


<!-- PayPal View Cart -->
<form target="paypal" action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_cart">
<input type="hidden" name="business" value="peter.mahnke\@gartner.com">
<input type="image" src="https://regionals4.gartner.com/regionalization/img/gpress/view_cart.gif" border="0" name="submit" alt="Make payments with PayPal - it's fast, free and secure!">
<input type="hidden" name="display" value="1">
</form>


<!-- begin cmt template : gpress_contact_us.incl  [locale = wcw] -->
            <span class="smallGrayText">
             If you experience any difficulties with this order, <br />
            please contact a member of Gartner's European <br />
            Support Center on +44 1784 267056 <br />
            or e-mail us at </span><a href=mailto:emea.wcw\@gartner.com class=smallLinkText>emea.wcw\@gartner.com</a><br /><br />
<!-- end cmt template : gpress_contact_us.incl -->
            
        <br/>           
        </td>
</tr>

<tr>
     <td colspan="3">
     <br /><br />


                   <!-- START - Table of Contents-->
<a name="toc">&nbsp;</a>
                   <table BORDER=0 CELLSPACING=0 CELLPADDING=5 WIDTH="100%" bgcolor="#f7f7f7">
                    <tr>
                     <td VALIGN=BOTTOM COLSPAN="2" HEIGHT="30" class="header2">
                    Typical Table of Contents</a></td>
                    </tr>
                    <tr>
                     <td>
<p />
<ul>Market Overview &amp; Trends</ul>

<ul>Magic Quadrant Criteria</ul>

<ul>Leaders
  <ul><i>Vendors in the Leaders segment are most likely to have high revenue in this market, high market share and products that are of interest to a wide audience.</i></ul>
</ul>

<ul>Challengers
  <ul><i>Challengers have focused significant resources on this market, but they have a narrower understanding of the market and a less-impressive product strategy, or they have deliberately chosen to limit the scope of their product lines.</i></ul>
</ul>

<ul>Visionaries
  <ul><i>Visionaries understand the market and customer requirements well, but have fewer assets committed to the pursuit of this particular market than the leaders.</i></ul>
</ul>

<ul>Niche Players
  <ul><i>Niche Players are limited to a particular geographical or industry segment, or have a smaller range of features or resources that, taken together, preclude them from competing across the board in many major segments of the integration market.</i></ul>
</ul>
                     </td>
                     <td width="40"><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="40" height="10"></td>
                    </tr>
                    </TABLE>
                   <!-- END - Table of Contents -->

&nbsp; <p />
<a name="method">&nbsp;</a>


<!-- END DETAIL -->
    </td>
</tr>

<tr>
     <td colspan="3" height="10">
         <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" height="10"></span>
     </td>
</tr>


<tr>
     <td colspan="3">
<!-- begin cmt template : gpress_mq_methodology.incl  [locale = wcw] -->
<!-- <span class="header1" >Methodology:</span>
<br />

Gartner Dataquest information is compiled using a combination of research techniques and data analysis, which is supported by a worldwide data collection process and integrated database.
<br /><br />

An indispensable tool for IT business planners, Gartner Dataquest's market forecasts clarify expectations about the future of technologies and help executives reduce business risk by creating plans and strategies based on fact.
-->
     </td>
</tr>

<tr>
     <td colspan="3" height="10">
         <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" height="10"></span>
     </td>
</tr>


<tr>
     <td colspan="3">
<span class="resIdText"><b>Note on PayPal</b></span><br />
<!-- begin cmt template : gpress_paypal.incl  [locale = wcw] -->
<span class="resIdText">
    Gartner uses PayPal to securely process and authorize transactions online. Registration to the service is free; however, there is a refundable Membership Fee (see below).  Please press the "Add to Cart" button to continue.<br /><br />

If you have a Visa, MasterCard, American Express, or Discover card: PayPal has a USD\$1.95 Membership Fee that will be charged to your credit card.  This fee will be refunded to your PayPal account after your successfully enter your Member Number from your credit card statement.<br /><br />

    If you have a Switch or Solo card: Your card will receive two small charges of less than &pound;1.00 each.  PayPal will refund these charges after you complete your PayPal Membership.<br /><br />

If you are already a member of PayPal, no Membership Fee will be charged.<br /><br /><br />
</span>
<!-- end cmt template : gpress_paypal.incl -->
     </td>
</tr>


<tr>
     <td colspan="3" height="20">
         <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" height="20"></span>
     </td>
</tr>


<tr>
    <td colspan="3" valign="bottom">
	    <img src=http://regionals.gartner.com/pages/docs/exp/images/dbd/gartner_logo.gif valign=bottom align=right><br /><br />
		</td>
</tr>

<tr>
    <td colspan="3" height="10">
        <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" height="10"></span>
    </td>
</tr>


</table>





<!-- THIS CREATES THE 5 PIXEL SPACER THAT IS BETWEEN THE PAGE BODY AND THE FOOTER ON ALL PAGES -->
<table cellspacing="0" cellpadding="0" width="766" align="center" border="0">
  <tbody>
  <tr>
    <td width="766"><img height="5" alt="" src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="766" border="0"></td></tr></tbody></table>

  <br><font color="#bbbbbb">gpress_mq_rpt_$_[0].html</font>
 </body>
</html>

EndofHTML


} elsif ($FORM{'focal'}) {

    $link =~ s/http(.[^\?]*)\?(.*)/DisplayDocument.html\?$2/;
    
    $title =~ tr/[a-z]/[A-Z]/;
    $mailerSummary = &noHang($summary,'50'); #,'no');
    $spacedSummary = &preSpace($mailerSummary, 2);

    $line .= <<EndofHTML;
    
  $title
  http:\/\/europe.gartner.com\/regionalization\/content\/emea\/$link
  $pubDate
  $spacedSummary

EndofHTML
    


} elsif ($FORM{'fp'}) {


    $fpFlag++;
    
    if ($fpFlag == 1) {
	
	$line .= <<EndofList;
</pre>


	<table bgcolor="#FFFFFF" valign="top" align="left" border="0" cellspacing="0" cellpadding="0">
EndofList

    } 

    if ($fpFlag % 2 != 0) {

	$line .= <<EndofList;
	
	    <tr>
		<td valign="top" width="345"><a class="largeBlueLink" href="$link" onclick="openResult('$link'); return false;">$title</a><br>
<font class="smallGrayText">$pubDate</font><br>

$auth
<div class="smallDarkGrayText">$summary</div>
	    <img src="./img/trans_pixel.gif" height="25" border="0"><br>
		</span></td>
EndofList

} else {

    $line .= <<EndofList;
		    <td width="25" nowrap><br></td>
		<td valign="top" width="345"><a class="largeBlueLink" href="$link" onclick="openResult('$link'); return false;">$title</a><br>
<font class="smallGrayText">$pubDate</font><br>

$auth
<div class="smallDarkGrayText">$summary</div>
	    <img src="./img/trans_pixel.gif" height="25" border="0"><br>
		</span></td>
		    <td width="25" nowrap><br></td>
			</tr>

EndofList

}
	if ($fpFlag > $#docs) {
	    $line .= "\n			    <\/table\>\n\n";
	}


} elsif ($FORM{'exp'}) {

    # exp version

#    $EXPtitle = &noHang($origTitle, 69);
#    $EXPtitle =~ s/\</\&lt\;/g;

    
    $EXPline .= <<EndofHTML;

                                             &lt;tr>
                                                 &lt;td width="10" valign="top">&lt;img src="/pages/docs/exp/images/common/bullet_gray.gif" width="10" height="8" vspace="3">&lt;/td>
                                                 &lt;td width="398"valign="top">&lt;a href="/$docCode" onclick="researchPop('/$docCode'); return false;" class="grey11pxBoldLk" target="_new">$origTitle&lt;/a>&lt;br>&lt;/td>
                                             &lt;/tr>
                                             &lt;tr>&lt;td width="428" height="11" colspan="2">&lt;img src="/pages/docs/common/images/x.gif" width="1" height="11">&lt;/td>&lt;/tr>

EndofHTML


}
}


sub noHangOld {

    undef local @words;
    local $charCount = 0;
    local $noHang = ""; 
    local $wordNumber = 0;

    @words = split (" ", $_[0]);

#    $noHang = "\n\n<\!\-\- $_[0] \-\-\>\n\n";

    foreach (@words) {
	
	local $len = length($_);
	local $len1 = $charCount + $len;
	local $len2 = $charCount + $len + length($words[$wordNumber + 1]);

	if ($len2 > 44 && $wordNumber == $#words - 2 ) {
	    
	    # if chars in current line + this word and the next are > 44
	    # and its the third last word, break
	    
	    $noHang .= " <br \/\>$_ $words[$wordNumber + 1] $words[$wordNumber + 2]";
	    last;
	    
	} elsif ($len1 >= 44 && $wordNumber == $#words - 1 ) {
	    
	    # if chars in current line + this word > 44
	    # and its the second last word, break
	    
	    $noHang .= " <br \/\>$_ $words[$wordNumber + 1]";
	    last;
	    
	} elsif ($charCount + $len < 44 ) {

	    $charCount = $charCount + $len + 1;
	    $noHang .= " $_";

	} else {

	    $noHang .= " <br \/\>$_";
	    $charCount = $len;

	}

	$wordNumber++;
    }
    
    $noHang =~ s/^ //;

    if (!$FORM{'mailing'}  && !$FORM{'focal'}) {
       
	$noHang =~ s/\</\&lt\;/g;

    } else {
	$noHang = $_[0];
    }
    return($noHang);
	
}



sub printOutput {

    if ($FORM{'embed'} eq "on") {
	$line =~ s/\&lt\;/\</g;
	$line =~ s/\&gt\;/\>/g;
	print <<EndofHTML
Content-type:  text/html

$line
EndofHTML

} else {

    if ($FORM{'exp'}) {


	$line = <<EndofLine;

	&lt;table width="428" cellpadding="0" cellspacing="0" border="0">
	    &lt;tr valign="top">
		&lt;td width="428" bgcolor="#D3DDE5">
		    &lt;table width="428" cellpadding="0" cellspacing="0" border="0">&lt;tr>&lt;td height="6">&lt;img src="/pages/docs/common/images/x.gif" width="1" height="6">&lt;/td>&lt;/tr>&lt;/table>
			&lt;table width="428" cellpadding="0" cellspacing="0" border="0">
			    &lt;tr>
				&lt;td width="10">&lt;img src="/pages/docs/common/images/x.gif" width="10" height="1">&lt;/td>
				    &lt;td width="408">
					&lt;table width="408" cellpadding="0" cellspacing="0" border="0">
					    

$EXPline

                                         &lt;/table>
                                     &lt;/td>
                                 &lt;td width="10">&lt;img src="/pages/docs/common/images/x.gif" width="10" height="1">&lt;/td>
                             &lt;/tr>
                         &lt;/table>
                     &lt;/td>
                  &lt;/tr>
              &lt;/table>


EndofLine


    }

    if ($fullPageFlag) {


	if ($FORM{'ecomm_listing'}) {
	    
	    
	    
	    $line =<<EndofListing;
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd">
<html>
 <head>
  <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
  <META HTTP-EQUIV="Content-Language" CONTENT="us-en">
  <title>Gartner Magic Quadrant Reports Listing</title>
 </head>

 <body  topmargin="0" leftmargin="0" marginwidth="0" marginheight="0" bgcolor="#BBBBBB">


<style>

td  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#000000; font-size:9pt; line-height: 1.5;}
.greyText  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#666666; font-size:9pt; line-height: 1.5;}
.buy { font-family:Verdana, Arial, Helvetica, sans-serif; color:#666666; font-size:18px; font-weith: bold; line-height: 1.2;}
.header1  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#000000; font-size:11pt; font-weight:bold; text-decoration:none; font-style:normal; font-style:normal; }
.header2  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#ffffff; font-size:9pt; font-weight:bold; font-weight:bold; background:#999999; }
.largeLinkText  { font-family:Verdana, Arial, Helvetica, sans-serif; color:#F8981D; font-size:14px; font-weight:bold; font-style:normal; font-style:normal; text-decoration:none; cursor:default; }
.smallLinkText { font-family:Verdana, Arial, Helvetica, sans-serif; color:#F8981D; font-size:9pt; text-decoration:none; }
.resIdText      { font-family:verdana,arial,helvetica; color:#BBBBBB; font-size:11px; text-decoration:none; font-style:normal; font-style:normal; } 
a:active        { text-decoration:underline; }
a:link          { text-decoration:none; }
a:hover         { text-decoration:underline; }
ul { list-style-image: url(http://regionals4.gartner.com/regionalization/img/gpress/bullet_orange.gif) }
</style>



<table cellspacing=0 cellpadding=0 width="500" border="0" align="center" bgcolor="#ffffff">


    <tr><td colspan="3" width="500" height="2" bgcolor="bbbbbb"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="500" height="2"></span></td></tr>
    <tr><td colspan="3" width="500" height="2" bgcolor="ffffff"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="500" height="2"></span></td></tr>

    <tr>
	<td width="2" bgcolor="ffffff"><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width=2></td>
	    <td bgcolor="#F8981D" height="66" width="496" >
		    <img src="http://regionals.gartner.com/regionalization/img/gpress/header_mq_sm.gif" width="496" height="66"><br />
        </td>
	    <td width="2" bgcolor="ffffff">
            <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width=2></span>
        </td>
    </tr>
    <tr><td colspan="5" width="500" height="2" bgcolor="ffffff"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="500" height="2"></span></td></tr>
    <tr><td colspan="5" width="500" height="2" bgcolor="bbbbbb"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="500" height="2"></span></td></tr>

</table>

<table cellspacing=0 cellpadding=0 width="500" border="0" align="center" bgcolor="#ffffff">
<tr>
    <td rowspan="10" width="40"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="40" height="0"></span></td>
    <td rowspan="1" width="420"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="420" height="0"></span></td>
    <td rowspan="10" width="40"><span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" width="40" height="0"></span></td>
</tr>



<tr>
    <td><span class="greyText">
<br />
Gartner Magic Quadrants provide a snapshot of how vendors are performing in a market segment and highlight the leaders to show how others compare.<br /><br />

Magic Quadrants help you make better informed decisions on companies you are looking to partner with, or whose services or products you want to buy.<br /><br /> 
</span>
 </td>
</tr>


<tr>
    <td valign="top">
<ul>
$line
</ul>

     </td>
</tr>




<tr>
     <td bgcolor=#f7f7f7>
<span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" height="1" width="400"></span>
     </td>
</tr>
<tr>
     <td bgcolor=#f7f7f7>
&nbsp;&nbsp;&nbsp;This is a one-off mailing from Gartner.<br /> 
&nbsp;&nbsp;&nbsp;To receive quarterly updates highlighting the<br />
&nbsp;&nbsp;&nbsp;latest Gartner Magic Quadrants, please:<br />

&nbsp;&nbsp;&nbsp;<a href="Javascript:void(null);" onClick="Javascript:window.open('/cgi/gpress_mq_popup_email.cgi','listing','menubar=no,toolbar=no,width=500,height=500');" class=smallLinkText><img src="http://regionals.gartner.com/regionalization/img/gray_arrow.gif" alt="Sign up for our newsletter" width="10" height="10" border="0"></a> &nbsp; <a href="Javascript:void(null);" onClick="Javascript:window.open('/cgi/gpress_mq_popup_email.cgi','listing','menubar=no,toolbar=no,width=500,height=500');" class="smallLinkText">Sign up for our newsletter</a><br />
     </td>
</tr>
<tr>
     <td bgcolor=#f7f7f7>
<span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" height="1" width="400"></span>
     </td>
</tr>


<tr>
     <td height="5">
         <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" height="5"></span>
     </td>
</tr>

<tr>
    <td valign="bottom">
<img src=http://regionals.gartner.com/pages/docs/exp/images/dbd/gartner_logo.gif valign=bottom align=right>
<br /><br />
    </td>
</tr>

<tr>
    <td height="10">
        <span><img src="http://regionals.gartner.com/regionalization/img/trans_pixel.gif" height="10"></span>
    </td>
</tr>


</table>

<font color=#bbbbbb>gpress_mq_popup.html</font><br />

<p>
</body>
</html>
EndofListing

} elsif ($FORM{'ecomm_mailing'}) {

    
    $line .= "\n        <td\><\/td\>\n    <\/tr\>\n\n\n" if ($listingCount);

$line =<<EndofListing
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/1999/REC-html401-19991224/loose.dtd">
<html>
 <head>
  <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
  <META HTTP-EQUIV="Content-Language" CONTENT="us-en">
  <title>Gartner Magic Quadrant Reports Listing - $bannerAlt</title>
 </head>

 <body  topmargin="0" leftmargin="0" marginwidth="0" marginheight="0" bgcolor="#ffffff">


$line


<p />
</body>
</html>

EndofListing

}

	print  <<EndofHTML;
Content-type:  text/html

$line

EndofHTML

    } else {

	print  <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>getResearch5.cgi</title>
</head>
<body>
$msg 
<p>
<pre>
$line
</pre>
<p>
</body>
</html>

EndofHTML

}
}
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
