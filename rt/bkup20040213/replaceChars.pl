#!/usr/local/bin/perl


# replaces accent characters with their HTML safe equiv
#
#  originally written for SSMI Topic Index code
#
#  modified:
#
#   10 Feb 2004 - Peter Mahnke
#                 added the replacement of angled double quotes with straight ones
#
#
#
#
#
#


sub replaceCharacters {

    my %replace;
    my %desc;
    my @list;
    my $listFile = "/home/gartner/html/rt/accent_list.txt"; #"c:/bin/accent_list.txt.utf8";
    my $out;

    
    &openList($listFile) if (!$FLAGreplaceChars);

    if ($_[1] eq "file") {

	# run on file
	$out = &openRCfile($_[0]);
    
    } else {
	
	# passed info
	$msg .= "in rc with: $_[0]<br>";
	$out = &replaceChars($_[0]);
    }

    return ($out);
	
}


sub openRCfile {

    my $out;

    open (RCFILE, "$_[0]") || die "Can't open input file: $_[0]\n\n";
    while (<RCFILE>) {

	$out .= &replaceChars($_);

    }
    close (RCFILE);

    return ($out);

}
    





sub replaceChars {
    
    
    my $word = $_[0];
    
    $word =~ s/�/'/g;# in accent list as &acute;, but not working
$word =~ s/�/\"/g;
$word =~ s/�/\"/g;
    
    foreach $letter (@list) {
	if ($word =~ /$letter/) {
	    $word =~ s/$letter/$replace{$letter}/g;
$msg .= "rc: $letter in $word<br>";
	}
    }

    return($word);
    
}



sub openList {

    open (LIST, "$_[0]") || die "can't open LIST: $[0]\n";
    
    while (<LIST>) {
	
	chop();
	my ($letter,$code,$desc) = split (/\t/);
	
	$replace{$letter} = $code;
	$desc{$letter} = $desc;
	
	push @list, $letter;
    }
    close(LIST);
    
    $FLAGreplaceChars = 1;    
}


1;
