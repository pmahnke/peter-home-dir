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
<title>getResearch2.cgi</title>
</head>
<body>
<form method=GET>

Doc Codes: <input type=text width=200 name=doccd><i>spaces between</i><p>
Research: <input type=radio name=type value=Research checked> &nbsp; 
First Take: <input type=radio name=type value=FirstTake><p>
Mailing Format: <input type=checkbox name=mailing><p>
Focal Point Format: <input type=checkbox name=focal><p>
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
	
    # clean up title
    $title =~ s/EMEA/Europe, Middle East and Africa/g;
    $title =~ s/ \(Executive Summary\)//g;
    $title = &noHang($title, 44);
    #$title =~ s/\&/\&amp\;/g;
    if (!$FORM{'mailing'}  && !$FORM{'focal'}) {
	$title =~ s/\</\&lt\;/g;
    } else {
	$title =~ s/<br \/\>//g;
    }




    if ($FORM{type} eq "Research"  && !$FORM{'mailing'} && !$FORM{'focal'}) {

	$line .=  <<EndofHTML;

&lt;!--start research $title $noteNumber $_[0] $pubDate-->
    &lt;tr>
        &lt;td width="356" height="15" colspan="3" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="356" height="15" alt="" border="0">&lt;/td>
    &lt;/tr>
    &lt;tr>
        &lt;td width="22" bgcolor="#FFFFFF" valign="top" align="center">&lt;img src="//img/homepage/reversed_blue_arrow.gif" width="9" height="9" vspace="2" alt="" border="0">&lt;/td>
        &lt;td width="328" valign="top" bgcolor="#FFFFFF">&lt;a href="javascript:void(null)" onclick="openResult('/$docCode')" class="smallBlueLink">
$title
&lt;/a>&lt;/td>
        &lt;td width="6" bgcolor="#FFFFFF">&lt;img src="./img/trans_pixel.gif" width="6" height="1" alt="" border="0">&lt;/td>
    &lt;/tr>
&lt;!--end research $title $noteNumber $_[0] $pubDate -->

EndofHTML

     } elsif ($FORM{type} eq "FirstTake" && !$FORM{'mailing'}  && !$FORM{'focal'}) {

	 $line .= <<EndofHTML;

&lt;!--start news $title $noteNumber $_[0] $pubDate -->
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
&lt;!--end news $title $noteNumber $_[0] $pubDate -->

EndofHTML

} elsif ($FORM{'mailing'}) {

    $auth  =~ s/\&lt\;a href\=(.[^\>]*)\>//g;
    $auth  =~ s/\&lt\;\/a\>//g;
    $auth  =~ s/ \&amp\;nbsp\;/\,/g;

    $link =~ s/http(.[^\?]*)\?(.*)/http:\/\/europe.gartner.com\/emea\/DisplayDocument.html\?$2/;

 $line .= <<EndofHTML;

<a href="$link">$title</a>
$pubDate &#151; $auth
EndofHTML
    


} elsif ($FORM{'focal'}) {

    $link =~ s/http(.[^\?]*)\?(.*)/\/DisplayDocument\?$2/;

 $line .= <<EndofHTML;

<a href="Javascript:void(null)" onClick="openResult('$link')" class="smallBlueLink">$title</a>
<p />

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

    print  <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>getResearch2.cgi</title>
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
