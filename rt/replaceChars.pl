#!/usr/local/bin/perl


#####################################################################
#####################################################################
#
#
#    replaceChars.pl
#
#    written:  07 May 2002 by Peter Mahnke
#              originally written for SSMI Topic Index code
#
#    modified: 10 Feb 2004 by Peter Mahnke
#              added the replacement of angled double quotes with straight ones
#
#
#    DESCRIPTION
#    replaces accent characters with their HTML safe equiv
#
#    INPUTS:
#    2 modes, string or file
#
#    1: text or filename
#    2: "file" if 1: is <filename>
#
#    OUTPUT:
#    returns cleaned up text
#
#
#####################################################################
#####################################################################

#use Carp;

sub replaceCharacters {

    my %replace;
    my %desc;
    my @list;
    my $listFile = "/home/gartner/html/rt/accent_list.txt"; # currently iso-8859-1, for UTF8, use "c:/bin/accent_list.txt.utf8";
    my $out;


    &openList($listFile) if (!$FLAGreplaceChars); # open if flag hasn't been set.

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

#############################################
sub openRCfile {

    my $out;

    open (RCFILE, "$_[0]") || die "Can't open input file: $_[0]\n\n";
    while (<RCFILE>) {

		$out .= &replaceChars($_);

    }
    close (RCFILE);

    return ($out);

}




#############################################
sub replaceChars {


    my $word = $_[0]; # isn't really a word, but a text blob

    $word =~ s/’/'/g;# in accent list as &acute;, but not working

    foreach $letter (@list) {

		# loop through each character to replace...

        next if ($letter =~ /(\(|\))/); # skip parens

		# carp "looking at $word for $letter\n";

        if ($word =~ /$letter/) {
		    $word =~ s/$letter/$replace{$letter}/g; # might need flag to look at multiple lines at once...
            $msg .= "rc: $letter in $word<br>";
		}
    }

    return($word);

}




#############################################
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

	# set a flag so that you don't reopen this list every time you call the function...
    $FLAGreplaceChars = 1;

	return();
}


1;
