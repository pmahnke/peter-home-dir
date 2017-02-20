#!/usr/local/bin/perl                                                                                                            

use Time::HiRes qw (gettimeofday);

my @urls = (
	    'www4.scholastic.co.uk/directory',
	    'www.scholastic.co.uk',
	    'www.ubuntu.com',
	    'www.mahnke.net',
	    'www.transitionelement.com',
            'www.canonical.com');

my $url;
foreach $url (@urls) {

    print "trying $url\n";

    my $i = 0;
    my $full = 0;;
    until ($i == 10) {

	$s = gettimeofday();
	$o = `wget -p -q --delete-after $url`;
	$e = gettimeofday();
	
	$i++;
     
	print "test $i was: ".($e-$s)." seconds\n";
	$full += ($e-$s);
    }

    $full = $full/10;
    print qq |$url: $full\n|;
    
}

