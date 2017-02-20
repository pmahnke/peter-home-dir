#!/usr/bin/perl

print "\nReplace-string: ";
$find = <STDIN>;
chop($find);

print "\nwith: ";
$replace = <STDIN>;
chop($replace);

$find =~ s/\"/\\\"/g;
$find =~ s/\//\\\//g;


print "looking to replace $find with $replace\nok?";
<STDIN>;


@files = `/usr/local/bin/grep -il \"$find\" \*.*`;


foreach $file (@files) {

    chop($file);
    $findFlag = 0;
    &parseFile($file);
    print "found $countDOS\n";
#    <STDIN>;

}

sub parseFile {

    print "reading $_[0]\n\n";
    open (FILE, "$_[0]") || die "Can't open input file: $_[0]\n";
    undef local $output;
    while (<FILE>) {

	$countDOS++ if (//);

	s///g;

#        chop();
        if (/$find/i) {
	    $findFlag = 1;
            print "changing $_\n\n";
            s/$find/$replace/ig;
            print "\t to $_\n\n";
        }

        $output .= "$_";
    }
    close (FILE);

    if ($findFlag) {

	print "\nwriting $outputFile\n";
	`mkdir ./new` if (!-d "./new");

	$outputFile = "./new/"."$_[0]";
	open (OUTPUT, ">$outputFile") || die "Can't open output file: $ouputFile\n";
	print OUTPUT $output;
	close (OUTPUT);

    }

}
