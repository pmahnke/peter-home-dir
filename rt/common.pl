
################################################################################
#
# common.pl
#
#   written:  01 Dec 2003 by Peter Mahnke
#   modified: 21 Jan 2004 by Peter Mahnke
#
#   require script, called from most regional scripts
#
#   DESCRIPTION OF SUBROUTINES
#
#	 noHang
#	   takes a line of text and breaks it at a certain length,
#	   making sure there are no "widows"
#
#
#	 uppercase
#	   turns a title into a properly Capitalized version
#	   ignoring the obvious articles (e.g. 'the', 'of', etc.)
#
#    addDays
#      roughly adds the days to today for a limit in the events pages
#
################################################################################



sub noHang {

	# three inputs
	# 1. text
	# 2. where to wrap
	# 3. delimiter (optional-defaults to <br />

	undef my @words;
	my $charCount = 0;
	my $noHang = "";
	my $wordNumber = 0;

	my $delim = "<br \/\>";
	$delim = "\n" if ($_[2] =~ /no/i);

	@words = split (" ", $_[0]);

	foreach (@words) {

		my $len = length($_);
		my $len1 = $charCount + $len;
		my $len2 = $charCount + $len + length($words[$wordNumber + 1]);

		if ($len2 > $_[1] && $wordNumber == $#words-1 ) {

			# if chars in current line + this word and the next are > $_[1]
			# and its the third last word, break

			$noHang .= " $delim $_ $words[$wordNumber + 1] $words[$wordNumber + 2]";
			last;

		} elsif ($len1 >= $_[1] && $wordNumber == $#words ) {

			# if chars in current line + this word > $_[1]
			# and its the second last word, break

			$noHang .= " $delim $_ $words[$wordNumber + 1]";
			last;

		} elsif ($charCount + $len < $_[1] ) {

			$charCount = $charCount + $len + 1;
			$noHang .= " $_";

		} else {

			$noHang .= " $delim$_";
			$charCount = $len;

		}

		$wordNumber++;
	}

	$noHang =~ s/^ //; # remove leading space
	$noHang =~ s/\<br \/\> /\<br \/\>/g; # remove trailing space

	return($noHang);

}




#################################################################
sub uppercase {

	# properly capitalize the titles, ignoring the obvious articles (e.g. 'the', 'of', etc.)
	# appends to global variable $msg for any messages....

	undef my $ucTitle;
	undef my $wordCount;

	@words = split (" ", $_[0]);

	foreach (@words) {

		$msg .= "title word: \|$_\|\n";

		# skip first word
		if (!$wordCount) {
			$wordCount = 1;
		}

		# DON'T capitalize the following 'special' words...
		# _in reverse logic to make it harder to read_
		if ($_ ne "the" &&
			$_ ne "of"  &&
			$_ ne "a"   &&
			$_ ne "in"  &&
			$_ ne "to"  &&
			$_ ne "an"  &&
			$_ ne "and")
		{

			$_ = ucfirst($_);
			$msg .= " capping $_ ";

		} else {

			$msg .= " skiping $_ ";

		}

		$ucTitle .= "$_ ";
		$wordCount++;
		$msg .= "now: $_ <br\>\n";
	}

	return($ucTitle);

}


sub addDays {

	# roughly adds days based on 30 day months
	# this logic isn't great but close enough

	# input - number of days to add (i.e. 45)
	# output - date in YYYYMMDD format

	my $year =  `date '+%Y'`;
	chop ($year);

	my $mon  =  `date '+%m'`;
	chop ($mon);

	my $day  =  `date '+%d'`;
	chop($day);

	# add number of 30 day months to the current month
	$mon = int ($_[0] / 30) + $mon;

	# add the remainer of 30 day months to the days
	$day = $day + $_[0] % 30;

	# if days are greater than 31, must roll over to new mont (add 1 to month and substract 20 from date)
	if ($day > 31) {
		$day -= 30;
		$mon += 1;
	}

	# if months are greater than 12, must roll over to new year (add 1 to year and substract 12 from month)
	if ($mon > 12) {
		$mon -= 12;
		$year += 1;
	}

	# add preceeding 0 to month if before October for MM format
	if ($mon < 10) {
		$mon = "0".$mon;
	}
	# add preceeding 0 to day if before 10 for DD format
	if ($day < 10) {
		$day = "0".$day;
	}
	return ($year.$mon.$day);

}

1;
