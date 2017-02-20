#!/usr/local/bin/perl

use CGI_Lite;
require ("/home/gartner/html/rt/SmartyPants.pl");


##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    
    # something submitted
    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;



} else {

    print <<EOF;
Content-type:  text/html

<head>
 <body> 
  <form method="post">
   <h1>Smarty</h1>
   <h2>Input</h2>
   <p><textarea name="input"></textarea></p>
   <p><input type="submit"></p>
  </form>
 </body>
</html>
EOF

	exit;

}



$output = &SmartyPants ($FORM{'input'}, 1);
    
print <<EOF;
Content-type:  text/html

<head>
 <body>
  <h1>Smarty</h1>
  <h2>Input</h2>
  <p>$FORM{'input'};</p>

  <h2>Output</h2>
  <p>$output</p>

 </body>
</html>
EOF



1;
