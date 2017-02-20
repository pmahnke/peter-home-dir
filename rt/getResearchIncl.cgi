#!/usr/local/bin/perl

require ("/home/gartner/cgi-bin/glogin.pl");
require ("/home/gartner/html/rt/getDocument.pl");

# get CGI input
use CGI_Lite;
$cgi = new CGI_Lite;
%FORM = $cgi->parse_form_data;

$FORM{URL} = "http:\/\/www4.gartner.com\/$FORM{URL}\&acsFlg\=accessBought";

local ($title, $pubDate, $summary, $resId, $auth, $body) = &getResearchDetail($FORM{URL});

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

print <<EndofHTML;
Content-type:  text/html

<html>
 <body>
<form>

<textarea rows=40 cols=80>
&lt;a href=$FORM{URL} class=headline target=research>$title&lt;/a><br>
$pubDate<br>
$auth<br>
$summary<p>
</textarea>


</form>
<p>
</body>
</html>

EndofHTML


    exit;




