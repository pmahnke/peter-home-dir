#/usr/local/bin/perl


$phrase = "300 Million Prospects in Europe &#151; Can You Afford to Miss This Opportunity?";

$phrase = &noHang($phrase);

print "$phrase\n\n";

sub noHang {

    local @words = split (" ", $_[0]);
    local $charCount = 0;
    local $noHang = ""; 
    local $wordNumber = 0;

    foreach (@words) {
	
	local $len = length($_);
	
	if ($charCount + $len < 30 && $wordNumber < $#words - 1 ) {

	    $charCount = $charCount + $len;
	    $noHang .= " $_";

	} elsif ($wordNumber ==  $#words - 1) {

	    $noHang .= "<br \/\>\n$_";
	    $charCount = $len;

	} elsif ($wordNumber >  $#words - 1) {

	    $noHang .= " $_";
	    $charCount = $len;
	    
	} else {

	    $noHang .= " <br \/\>\n$_";
	    $charCount = $len;

	}

	$wordNumber++;

    }
    return($noHang);
	
}
