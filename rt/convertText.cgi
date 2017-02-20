#!/usr/local/bin/perl


use CGI_Lite;
require ("/home/gartner/html/rt/common.pl");
require ("/home/gartner/html/rt/replaceChars.pl");
require ("/home/gartner/html/rt/SmartyPants.pl");
require ("/home/gartner/cgi-bin/Textile.pm");
require ("/home/gartner/html/rt/uiStrings.pl");
require ("/home/gartner/html/rt/acronym.pl");



##############################################################
# Variables


##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {
    
    
    local $buffer = "";
    read(STDIN,$buffer,$ENV{CONTENT_LENGTH});
    
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ s/\+/ /g; # spaces
	# $value =~ s/\&lt\;/\</g; # less thans
	# $value =~ s/\&amp\;/\&/g; # ampersans
	$value =~ s/%26(.[^%]*)%3B/\&amp\;$1\;/g; # nbsp
	$value =~ s/%(..)/pack("c",hex($1))/ge; # rest
	
	$FORM{$name} = $value;
    }
    
	
	# something submitted
	#$cgi = new CGI_Lite;
	#%FORM = $cgi->parse_form_data;
	
	&processText;
	
} else {

	$FORM{'locale'} = "emea";
	&printInitialForm;
	exit;
	
}
exit;




sub processText {

    $output = $FORM{'input'};
    if ($FORM{'textile'}) {
	
	$textile = new Text::Textile;
	$output  = $textile->process($output);
	
    }
    
    $output = &translateUIstring ($output, $FORM{'from'}, $FORM{'to'}) if ($FORM{'ui'});
    $output = &SmartyPants ($output, 1)                                if ($FORM{'smarty'});
    $output = &replaceCharacters($output)                              if ($FORM{'chars'});
    $output = &noHang($output, $FORM{'noHang'})                        if ($FORM{'noHang'});
    $output = &acronym($output, $FORM{'acronym'})                      if ($FORM{'acronym'});
    
    
    $preoutput = $output;
    
    $preoutput =~ s/\&amp\;/\&/g;
    $preoutput =~ s/\&/\&amp\;/g;
    $preoutput =~ s/</&lt\;/g;
    $preoutput =~ s/>/&gt\;/g;
    
    #$output =~ s/\n/<br \/\>\n/g;
    $output =~ s/\&amp\;/\&/g;

    $fU = "checked=\"checked\"" if ($FORM{'ui'});
    $fS = "checked=\"checked\"" if ($FORM{'smarty'});
    $fR = "checked=\"checked\"" if ($FORM{'chars'});
    $fT = "checked=\"checked\"" if ($FORM{'textile'});
    $fA = "checked=\"checked\"" if ($FORM{'acronym'});
    
    $select =<<EOF;
 <option value="eu">english</option>
 <option value="it">italian</option>
 <option value="de">german</option>
 <option value="fr">french</option>
</select>
EOF

    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>convertText - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt; clear:both;	}
h3	{		font-size: 10pt;	}
li,p,td	{		font-size: 9pt;	        }
</style>
</head>
<body>
<form method="post" enctype="application/x-www-form-urlencoded">

<h1>Convert Text</h1>
<h2>Output</h2>
<p>
$output
</p>

<p>
<textarea rows="10" cols="80">
$preoutput
</textarea></p>

<h2>Input</h2>
<p><textarea name="input" rows="15" cols="80">$FORM{'input'}</textarea></p>

<p>
 <ul>
  <li> Textile: <input type="checkbox" name="textile" value="on" $fT/> <a href="/rt/mtmanual_textile2.html" target="_blank">?</a> </li>
  <li> Smarty: <input type="checkbox" name="smarty" value="on" $fS/> </li>
  <li> Replace Chars: <input type="checkbox" name="chars" value="on" $fR /> </li>
  <li> Hang: <input type="text" name="noHang" value="$FORM{'noHang'}" /> <em>0 or nothing for no hang</em></li>
  <li> Acronyms: <input type="checkbox" name="acronym" value="on" $fA /> <em>Gartner Acronyms</em></li>
  <li> UI Translate: <input type="checkbox" name="ui" value="on" $fU /> from: <select name="from"><option value="$FORM{'from'}">$FORM{'from'}</option>$select to: <select name="to"><option value="$FORM{'to'}">$FORM{'to'}</option>$select</li>
 </ul>
</p>

<p><input type="submit" /></p>

</form>

<h3>messages</h3>
<p>$msg</p>
<h3>buffer</h3>
<p>$buffer</p>
</body>
</html>

EndofHTML

}

sub printInitialForm {
    
    $select =<<EOF;
 <option value="eu">english</option>
 <option value="it">italian</option>
 <option value="de">german</option>
 <option value="fr">french</option>
</select>
EOF

    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>convertText - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt; clear:both;	}
h3	{		font-size: 10pt;	}
li,p,td	{		font-size: 9pt;	        }
</style>
</head>
<body>
<form method="post" enctype="application/x-www-form-urlencoded">

<h1>Convert Text</h1>

<p><textarea name="input" rows="15" cols="80"></textarea></p>

<p>
 <ul>
  <li> Textile: <input type="checkbox" name="textile" value="on" /> <a href="/rt/mtmanual_textile2.html" target="_blank">?</a> </li>
  <li> Smarty: <input type="checkbox" name="smarty" value="on" /> </li>
  <li> Replace Chars: <input type="checkbox" name="chars" value="on" /> </li>
  <li> Hang: <input type="text" name="noHang" /> <em>0 or nothing for no hang</em> </li>
  <li> Acronyms: <input type="checkbox" name="acronym" value="on" /> <em>Gartner Acronyms</em></li>
  <li> UI Translate: <input type="checkbox" name="ui" value="on" $fU /> from: <select name="from">$select to: <select name="to">$select</li>
 </ul>
</p>

<p><input type="submit" /></p>

</form>
</body>
</html>

EndofHTML
}
