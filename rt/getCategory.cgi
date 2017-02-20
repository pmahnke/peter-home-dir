#!/usr/local/bin/perl

# Variables


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
please pass a command line parameter cat=0-5<p>

</body>
</html>

EndofHTML

    exit;

}



    print  <<EndofHTML;
    Content-type:  text/html

    <script>var category=$FORM{'cat'};</script>
EndofHTML



exit;
