#!/usr/local/bin/perl

require ("/home/gartner/cgi-bin/glogin.pl");
require ("/home/gartner/html/rt/mobileSearch.pl");
require ("/home/gartner/html/rt/research.pl");

use CGI_Lite;

# VARIABLES
$rootDir  = "/home/gartner/html/rt/";
$fileUser = "$rootDir"."user.db";



# get CGI input
$cgi = new CGI_Lite;
%FORM = $cgi->parse_form_data;



&readUserDb;


@results = &search($query);

local $docCount = 0;
foreach $result (@results) {

    $text .= &getResearch($result);
    
    last if ($docCount == 9);
    $docCount++;

}

&printPage;

exit;


#############################################
sub printPage {

    $text =~ s/</\&lt\;/g;

    # <?xml version="1.0"?>

    print <<EndofHTML;
Content-type: text/html

<html>
<body>
<table width=500>
<tr>
 <td>
$text
 </td>
</tr>
</table>
</body>
</html>

EndofHTML

}



#############################################
sub readUserDb {

    open (USER, "$fileUser") || die "\n\nCan't open User DB: $fileUser\n\n";

    while (<USER>) {
	
	chop();
	
	($phone, $userName, $passwd, $query) = split (/\t/);
	
	# next if ($phone !~ /$FORM{'id'}/);

    }
    
    close (USER);
    
}

