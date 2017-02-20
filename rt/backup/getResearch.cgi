#!/usr/local/bin/perl



use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
require ("/home/gartner/cgi-bin/gNOlogin.pl");
require ("/home/gartner/html/rt/getNODocument2.pl");

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

Enter Full URL: <input type=text width=200 name=doccd><p>
Research: <input type=radio name=type value=Research checked> &nbsp; 
First Take: <input type=radio name=type value=FirstTake><p>
New Look: <input type=checkbox name=style value=on CHECKED><p>
<input type=submit>
</form>
</body>
</html>

EndofHTML

    exit;

}

#local $docCode = $1 if ($FORM{doccd} =~ /DisplayDocument\?id\=(.[^\&]*)\&/);
local $docCode = $1 if ($FORM{doccd} =~ /(DisplayDocument\?id\=.[^\&]*)\&/);
local $docCode = $1 if ($FORM{doccd} =~ /(DisplayDocument\?doc_cd\=.*)/);

local ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber) = &getResearchDetail("$FORM{doccd}",$server);

$getGARTNERmsg =~ s/</\&lt\;/g;

# clean up author
$auth =~ s/</\&lt\;/g; # convert < to html safe &lt;
$auth =~ s/,/ \&amp\;nbsp\; /g; # convert , to a spcae

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


if ($FORM{'style'} eq "on") {

    if ($FORM{type} eq "Research") {

    print  <<EndofHTML;
Content-type:  text/html

<html>
<body>
<p>
<pre>


&lt;!--start research $noteNumber-->
    &lt;tr>
        &lt;td width="356" height="15" colspan="3" bgcolor="#FFFFFF">&lt;img src="//img/trans_pixel.gif" width="356" height="15" alt="" border="0">&lt;/td>
    &lt;/tr>
    &lt;tr>
        &lt;td width="22" bgcolor="#FFFFFF" valign="top" align="center">&lt;img src="//img/homepage/reversed_blue_arrow.gif" width="9" height="9" vspace="2" alt="" border="0">&lt;/td>
        &lt;td width="328" valign="top" bgcolor="#FFFFFF">&lt;a href="javascript:void(null)" onclick="openResult('/$docCode')" class="smallBlueLink">
        $title
        &lt;/a>&lt;/td>
        &lt;td width="6" bgcolor="#FFFFFF">&lt;img src="//img/trans_pixel.gif" width="6" height="1" alt="" border="0">&lt;/td>
    &lt;/tr>
&lt;!--start research $noteNumber-->

EndofHTML

    } else {

         print  <<EndofHTML;
Content-type:  text/html

<html>
<body>
<p>
<pre>


&lt;!--start news $title $noteNumber $pubDate-->
    &lt;tr>
        &lt;td width="356" height="10" colspan="3" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="356" height="10" alt="" border="0">&lt;/td>
    &lt;/tr>
    &lt;tr>
        &lt;td width="22" bgcolor="#FFFFFF" valign="top" align="center">&lt;img src="//img/homepage/reversed_green_arrow.gif" width="9" height="9" vspace="3" alt="" border="0">&lt;/td>
        &lt;td width="328" valign="top" bgcolor="#FFFFFF">&lt;a href="javascript:void(null)" onclick="openResult('/$docCode')" class="largeGrayLink">
$title
        &lt;/a>&lt;/td>
        &lt;td width="6" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="6" height="1" alt="" border="0">&lt;/td>
    &lt;/tr>
&lt;!--start news $noteNumber-->

EndofHTML

    }

} else {

    print  <<EndofHTML;
Content-type:  text/html

<html>
<body>
<p>
<pre>


&lt;!--start doc $noteNumber-->


&lt;tr>
 &lt;td align="left" valign="top">&lt;a class="linkTextBold3" href="javascript:void(null)" onclick="openResult('/$docCode')">
$title
&lt;/a>&lt;br>&lt;/td>
&lt;/tr>
&lt;tr>
 &lt;td align="left" class="textBlackReg2" valign="top">$pubDate&lt;/td>
&lt;/tr>
EndofHTML

    if ($FORM{type} eq "Research") {
print  <<EndofHTML;
&lt;tr>
 &lt;td align="left" valign="top">
$auth 
 &lt;/td>
&lt;/tr>
EndofHTML
}

print  <<EndofHTML;
&lt;tr>
 &lt;td class="contentTextMain" align="left" valign="top">&lt;img src="./img/trans_pixel.gif" width="1" height="1" border="0" alt="" />&lt;/td>
&lt;/tr>
&lt;tr>
 &lt;td class="contentTextMain" align="left" valign="top">
$summary
&lt;/td>
&lt;/tr>
&lt;tr>
 &lt;td class="contentTextMain" align="left" valign="top">&lt;img src="./img/trans_pixel.gif" width="1" height="1" vspace="3" border="0" alt="" />&lt;/td>
&lt;/tr> 

&lt;!--end doc $noteNumber-->


</pre>
</body>
</html>


EndofHTML

}




    exit;
