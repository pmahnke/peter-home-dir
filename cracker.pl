#!/usr/bin/perl

# pass cracker by Peter Mahnke June 28, 1999
#


if (!@ARGV) {
    print "\ncrack <seed> <password text>\n\n";
    exit;
}

$output = crypt ($ARGV[1], $ARGV[0]);

print "\n$ARGV[1] using $ARVG[0] seed is: $output\n\n";
exit;

sub crypt {
    $salt = seedchar().seedchar();
    $c1 = crypt ($FORM{'input1'}, $salt);
    $salt2 = substr ($c1, 0, 2);
    $c2 = crypt ($FORM{'input2'}, $salt2);
    
    if ($c1 eq $c2) {
	$list .= "$FORM{'newname'}:$c1\n";
	open (PASSWD, ">$passwd") || die "Can't open password file\n";
	print PASSWD $list;
	close (PASSWD);
    } else {
	$message = "PASSWORDS DO NOT MATCH";
	&printForm;
	exit;
    }
    
}

sub seedchar {  # from Randal Schwarz
	('a'..'z','A'..'Z','0'..'9','.','/')[rand(64)];
}
