#!/usr/local/bin/perl

################################################################################
#
# uiStrings.pl
#
#   written:  16 Mar 2004 by Peter Mahnke
#   modified:
#
#   DESCRIPTION
#   replaces a UI string from one language to another
#   will correctly parse HTML
#   relies on uiStrings.txt for translations
#
#   INPUT
#   translateUIstring('string','from locale','to locale', 'file');
#   valid locales are currently: eu, it, de, at (incomplete)
#
#   OUTPUT
#   translated text
#
#
################################################################################


sub translateUIstring {

	my @list;
	my $out;


	&_openUIstringsList('/home/gartner/html/rt/uiStrings.txt');

	if ($_[3] eq "file") {

		# run on file
		$out = &_openInputfile($_[0], $_[1], $_[2]);

	} else {

		# run against passed info
		$msg .= "in rc with: $_[0]<br>";
		$out = &_translateUIstrings($_[0], $_[1], $_[2]);

	}

	return ($out);

}





####################################
sub _translateUIstrings {

	# does the actual translation

	my $result = "";
	my $from   = $_[1];
	my $to	   = $_[2];


	# tokenize html, know what is in a tag and what isn't.... don't want to translate any html tags...
	my $tokens ||= _tokenize($_[0]);


	foreach my $cur_token (@$tokens) {

		if ($cur_token->[0] eq "tag") {

			# Don't mess with quotes inside tags.
			my $tag = $cur_token->[1];
			$result .= $tag;
			$msg .= "in tag $tag ... so skipping\n";

		} else {

			# not in tag

			my $input = $cur_token->[1];

			# loop through terms to translate
			foreach (keys %$from) {

				if ($input =~ /$$from{$_}/i) {

					# found phrase
					$input =~ s/$$from{$_}/$$to{$_}/ig;
					$msg .= "ui: found $_  $from [ $$from{$_} ] \-\> $to [ $$to{$_} ] <br />\n";

				}

			}

			$result .= $input;
	}
	}

	return($result);

}


####################################
sub _openUIstringsList {

	# opens list of UI strings
	# returns hash based on the string name

	open (UILIST, "$_[0]") || die "can't open UILIST: $[0]\n";

	my @pairs = "";
	my $locale;
	my $string;
	my $euString;

	while (<UILIST>) {

		chop();

		@pairs = split (/\t/);

		# europe strings
		foreach (@pairs) {

			($locale, $string) = split (/~/);

			if ($locale eq "eu") {
				$eu{$string} = $string;
				$euString    = $string;
			}

		}

		# non-europe strings
		foreach (@pairs) {

			($locale, $string) = split (/~/);

			if ($locale ne "eu") {
				if ($string) {
					$$locale{$euString} = $string;
				} else {
					# use EU string if local isn't eu
					$$locale{$euString} = $euString;
				}

			}
		}

	}
	close(UILIST);

}



####################################
sub _openInputfile {

	# opens a passed file to parse

	open (RCFILE, "$_[0]") || die "Can't open input file: $_[0]\n\n";
	while (<RCFILE>) {

		$out .= &_translateUIstrings($_, $_[1], $_[2]);

	}
	close (RCFILE);

	return ($out);

}




####################################
sub _tokenize {

	#
	#   Parameter:  String containing HTML markup.
	#   Returns:	Reference to an array of the tokens comprising the input
	#			   string. Each token is either a tag (possibly with nested,
	#			   tags contained therein, such as <a href="<MTFoo>">, or a
	#			   run of text between tags. Each element of the array is a
	#			   two-element array; the first is either 'tag' or 'text';
	#			   the second is the actual value.
	#
	#
	#   Based on the _tokenize() subroutine from Brad Choate's MTRegex plugin.
	#	   <http://www.bradchoate.com/past/mtregex.php>
	#

	my $str = shift;
	my $pos = 0;
	my $len = length $str;
	my @tokens;

	my $depth = 6;
	my $nested_tags = join('|', ('(?:<(?:[^<>]') x $depth) . (')*>)' x  $depth);
	my $match = qr/(?s: <! ( -- .*? -- \s* )+ > ) |  # comment
				   (?s: <\? .*? \?> ) |			     # processing instruction php
				   $nested_tags/x;				     # nested tags


	# (?s: document\.write\(\'.*?\'\)\; ) |  # javascript PRM


	while ($str =~ m/($match)/g) {
		my $whole_tag = $1;
		my $sec_start = pos $str;
		my $tag_start = $sec_start - length $whole_tag;
		if ($pos < $tag_start) {
			push @tokens, ['text', substr($str, $pos, $tag_start - $pos)];
		}
		push @tokens, ['tag', $whole_tag];
		$pos = pos $str;
	}
	push @tokens, ['text', substr($str, $pos, $len - $pos)] if $pos < $len;
	\@tokens;
}


1;
