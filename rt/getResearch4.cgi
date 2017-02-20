#!/usr/local/bin/perl

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/cgi-bin/gNOlogin.pl");
require ("/home/gartner/html/rt/getNODocument2.pl");
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
<title>getResearch4.cgi</title>
</head>
<body>
<form method=GET>

Doc Codes: <input type=text width=200 name=doccd><i>spaces between</i><p>
Research: <input type=radio name=type value=Research checked> &nbsp;
First Take: <input type=radio name=type value=FirstTake><p>
Mailing Format: <input type=checkbox name=mailing><p>
TEXT Format: <input type=checkbox name=focal><p>
New Focal Point Format: <input type=checkbox name=fp><p>
EXP in the news Format: <input type=checkbox name=exp><p>
xhtml format: <input type="checkbox" name="xhtml"><p>
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

    local ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber) = &getResearchDetail($link,$server);

    if (!$title) {
	$msg .= "didn't get $link<br\>\n" if (!$title);
	$docCode = "DisplayDocument\?doc_cd\="."$_[0]";
	$link = "http:\/\/www4.gartner.com\/"."$docCode"; # ."\&acsFlg\=accessBought";
	($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber) = &getResearchDetail($link,$server);
	$msg .= "didn't get $link<br\>\n" if (!$title);
    }

    $getGARTNERmsg =~ s/</\&lt\;/g;

    # clean up author
    $auth =~ s/</\&lt\;/g if (!$FORM{'fp'}); # convert < to html safe &lt;
    if ($FORM{'fp'}) {
	$auth =~ s/,/ \&nbsp\; /g; # convert , to a spcae
    } else {
	$auth =~ s/,/ \&amp\;nbsp\; /g; # convert , to a spcae
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




    if ($FORM{type} eq "Research"  && !$FORM{'mailing'} && !$FORM{'focal'} && !$FORM{'fp'} && !$FORM{'xhtml'}) {

	$line .=  <<EndofHTML;

&lt;!--start research  - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate-->
    &lt;tr>
        &lt;td width="356" height="8" colspan="3" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="356" height="8" alt="" border="0">&lt;/td>
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

     } elsif ($FORM{type} eq "FirstTake" && !$FORM{'mailing'}  && !$FORM{'focal'} && !$FORM{'fp'} && !$FORM{'exp'}  && !$FORM{'xhtml'}) {

	 $line .= <<EndofHTML;

&lt;!--start news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->
    &lt;tr>
        &lt;td width="356" height="10" colspan="3" bgcolor="#FFFFFF">&lt;img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0">&lt;/td>
    &lt;/tr>
    &lt;tr>
        &lt;td width="22" bgcolor="#FFFFFF" valign="top" align="center">&lt;a href="javascript:void(null)" onclick="openResult('/$docCode')" class="largeGrayLink">&lt;img src="/images/homepage/reversed_green_arrow.gif" width="9" height="9" vspace="3" alt="$origTitle" border="0">&lt;/a>&lt;/td>
        &lt;td width="328" valign="top" bgcolor="#FFFFFF">&lt;a href="$docCode" onclick="openResult('/$docCode');return false;" class="smallBlueLink" target="_new">$title&lt;/a>&lt;/td>
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

    $link =~ s/http(.[^\?]*)\?(.*)/http:\/\/europe.gartner.com\/regionalization\/content\/emea\/DisplayDocument.html\?$2/;

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


# $line .= <<EndofHTML;

#    $mailerTitle
#    $link
#    $pubDate
#    By $auth
#    $mailerSummary

#EndofHTML



# $line .= <<EndofHTML;

#     TITLE:    $mailerTitle
#      LINK:    $link
#      DATE:    $pubDate
#ANALYST(S):    $auth
#   SUMMARY:    $mailerSummary

#EndofHTML



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


} elsif ($FORM{'xhtml'}) {

    $line .= <<EndofHTML
 &lt;li> &lt;a href="\#" onclick="openResult('/$docCode')">$origTitle&lt;/a>&lt;/li>
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

    print  <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>getResearch4.cgi</title>
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
