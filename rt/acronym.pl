#!/usr/local/bin/perl


# replaces an Acronym string with a Gartner Acronmae in an <abbr title=""></abbr> tag
#
#  written:
#            30 September 2004 by Peter
#
#  modified:
#
#
#  usage:
#    acronym('string');
#
#


sub acronym {

    my @list;
    my $out;
        
    &_openACROstringsList('/home/gartner/html/rt/acronym.db');
    
    if ($_[1] eq "file") {

	# run on file
	$out = &_openInputfile($_[0]);
	
    } else {
	
	# passed info
	$msg .= "in rc with: $_[0]<br>";
	$out = &_translateACROstrings($_[0]);
    }
    
    return ($out);

}




sub _translateACROstrings {

    # does the actual translation

    my $result = "";
    my $method = "tag";
    my %usedacro;

    # tokenize html
    my $tokens ||= _tokenize($_[0]);


    foreach my $cur_token (@$tokens) {
	
	if ($cur_token->[0] eq "tag") {

            # Don't mess with quotes inside tags.
	    my $tag = $cur_token->[1];
            $result .= $tag;
	    $msg .= "in tag $tag ... so skipping\n";

	} else {

	    my $input = $cur_token->[1];

	    foreach $acro (keys %acro) {
		
		if ($input =~ /(\b|\b\()($acro)(\b|s\b|\)\b)/) {
		    
		    # found phrase

		    next if (!$2); # skip if blank

		    # only convert it once per time...
		    next if ($usedacro{$acro});
		    $usedacro{$acro} = 1;

		    # 2 methods

		    if ($method eq "tag") {
			
			# <abbr tag method
			$input =~ s/$2/<abbr title\=\"$acro{$acro}\"\>$acro<\/abbr\>/;

		    } else {

			# inline method
			#  should we only do it once per instance?

			local $cleanacro = $acro{$acro};

			# remove (text)
			$cleanacro = substr ($cleanacro, 0, index ($cleanacro, "(")) if ($acro{$acro} =~ /\(/); 

			$input =~ s/$acro/$cleanacro \($acro\)/;

		    }

		    $msg .= "acro: found $acro [$acro{$acro}] <br />\n";
		    
		}
		
	    }
	    
	    $result .= $input;
	}
    }
    
    return($result);
	
}



sub _openACROstringsList {

	# opens list of Acronym strings

    open (ACROLIST, "$_[0]") || die "can't open ACROLIST: $[0]\n";

    local $acro;
    local $string;
    
    while (<ACROLIST>) {

	chop();

	($acro, $string) = split (/\t/);

	$acro{$acro} .= "$string "; # dealing with multiple ones?
	
    }
    close(ACROLIST);

}

sub _openInputfile {

    # opens a passed file to parse

    open (RCFILE, "$_[0]") || die "Can't open input file: $_[0]\n\n";
    while (<RCFILE>) {

	$out .= &_translateACROstrings($_);

    }
    close (RCFILE);

    return ($out);

}


sub _tokenize {
#
#   Parameter:  String containing HTML markup.
#   Returns:    Reference to an array of the tokens comprising the input
#               string. Each token is either a tag (possibly with nested,
#               tags contained therein, such as <a href="<MTFoo>">, or a
#               run of text between tags. Each element of the array is a
#               two-element array; the first is either 'tag' or 'text';
#               the second is the actual value.
#
#
#   Based on the _tokenize() subroutine from Brad Choate's MTRegex plugin.
#       <http://www.bradchoate.com/past/mtregex.php>
#

    my $str = shift;
    my $pos = 0;
    my $len = length $str;
    my @tokens;

    my $depth = 6;
    my $nested_tags = join('|', ('(?:<(?:[^<>]') x $depth) . (')*>)' x  $depth);
    my $match = qr/(?s: <! ( -- .*? -- \s* )+ > ) |  # comment
                   (?s: <\? .*? \?> ) |              # processing instruction php
                   $nested_tags/x;                   # nested tags


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
