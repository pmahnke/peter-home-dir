#!/usr/bin/perl

$dir = "/var/log/mailman";

opendir (DIR, $dir) || die "can't open $dir\n";
@files = readdir(DIR);
closedir (DIR);

foreach $file (@files) {

    if ($file =~ /error/) {

	$filename = "$dir/$file";


	print "unlinking $filename\n";
	unlink ($filename);

    }

}

exit;
