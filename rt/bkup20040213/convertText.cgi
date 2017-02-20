#!/usr/local/bin/perl


use CGI_Lite;
require ("/home/gartner/html/rt/common.pl");
require ("/home/gartner/html/rt/replaceChars.pl");
require ("/home/gartner/html/rt/SmartyPants.pl");



##############################################################
# Variables


##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    # something submitted
    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;

	&processText;

} else {

	$FORM{'locale'} = "emea";
	&printInitialForm;
	exit;

}
exit;




sub processText {

	$output = $FORM{'input'};
	$output = &SmartyPants ($output, 1)         if ($FORM{'smarty'});
	$output = &replaceCharacters($output)       if ($FORM{'chars'});
	$output = &noHang($output, $FORM{'noHang'}) if ($FORM{'noHang'});	

	$preoutput = $output;
	$preoutput =~ s/\&/\&amp\;/g;


	$output =~ s/\n/<br \/\>\n/g;

	$fS = "checked=\"checked\"" if ($FORM{'smarty'});
	$fR = "checked=\"checked\"" if ($FORM{'chars'});

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
<form method="post">

<h1>Convert Text</h1>
<h2>Output</h2>
<p>
$output
</p>

<p>
<textarea rows="20" cols="80">
$preoutput
</textarea></p>

<h2>Input</h2>
<p><textarea name="input" rows="20" cols="80">$FORM{'input'}</textarea></p>

<p>
 <ul>
  <li> Smarty: <input type="checkbox" name="smarty" value="on" $fS/> </li> 
  <li> Replace Chars: <input type="checkbox" name="chars" value="on" $fR /> </li>
  <li> Hang: <input type="text" name="noHang" value="$FORM{'noHang'}" /> <em>0 or nothing for no hang</em> </li>
 </ul>
</p>

<p><input type="submit" /></p>

</form>

	
</body>
</html>

EndofHTML

}

sub printInitialForm {

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
<form method="post">

<h1>Convert Text</h1>

<p><textarea name="input" rows="20" cols="80"></textarea></p>

<p>
 <ul>
  <li> Smarty: <input type="checkbox" name="smarty" value="on" /> </li> 
  <li> Replace Chars: <input type="checkbox" name="chars" value="on" /> </li>
  <li> Hang: <input type="text" name="noHang" /> <em>0 or nothing for no hang</em> </li>
 </ul>
</p>

<p><input type="submit" /></p>

</form>
</body>
</html>

EndofHTML
}
