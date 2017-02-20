#!/usr/local/bin/perl

################################################################################
#
# common_spelling.pl
#
#   written:  31 Mar 2004 by Peter Mahnke
#   modified:
#
#   command line or require script that checks the spelling of text
#
#   DESCRIPTION OF SUBROUTINES
#
#     checkSpelling
#       input: text to check
#       output: html with marked up errors and suggestions
#
#
#
#
################################################################################


if ($ARGV[0]) {
    print &checkSpelling(@ARGV);
    exit;
}


sub checkSpelling {

	# input: text to check
	# output: html with marked up errors and suggestions

    my $spell;

    my @input;

    @input = split (/\n/, $_[0]);

    foreach (@input) {

		s/\n//g;
		s/\r//g;

		s/<(.[^\>]*)\>//ge;
		s/  / /ge;
		next if (!$_);

		$spell .= "<p\>$_<\/p\>\n";

		use Lingua::Ispell qw( spellcheck );
    	  Lingua::Ispell::allow_compounds(1);

		for my $r ( spellcheck( $_ ) ) {
		    if ( $r->{'type'} eq 'miss' ) {

			$spell .= "<p class\=\"err\"\>spelling? <strong\>'$r->{'term'}'<\/strong\><\/p\>\n";
			$spell .= "<p class\=\"sug\"\>suggestions: @{$r->{'misses'}}<\/p\>\n";

		    }

		}
    }
    return($spell);
}

1;
