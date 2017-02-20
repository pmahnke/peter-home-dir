

sub noHang {

    # three inputs
    # 1. text
    # 2. where to wrap
    # 3. delimiter (optional-defaults to <br />

    undef local @words;
    local $charCount = 0;
    local $noHang = ""; 
    local $wordNumber = 0;
    
    local $delim = "<br \/\>";
    $delim = "\n" if ($_[2] =~ /no/i);

    @words = split (" ", $_[0]);

    foreach (@words) {
	
	local $len = length($_);
	local $len1 = $charCount + $len;
	local $len2 = $charCount + $len + length($words[$wordNumber + 1]);

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


1;
