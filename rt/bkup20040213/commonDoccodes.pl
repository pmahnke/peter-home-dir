#!/usr/local/bin/perl


########################################################################
#
# commonDoccodes.pl
#
#   written: 12 Dec 2003 by Peter Mahnke
#   modified:
#
#   require script, called from pickResearch.cgi
#
#   DESCRIPTION
#     tests, writes and deletes a Codes file for managing News and FR
#     overrides from the regional site editors.
#
#
#     writeCodes subroutine takes 3 attributes
#         1. type - NEWS, FR
#         2. locale - emea, it, de, etc
#         3. code - 0 for none
#
#         eg ('NEWS', $FORM{'locale'}, $FORM{'code'});
#
#         writes a file /<LOCALE>/<TYPE>.codes with <CODE> as the content
#
#         returns 1 if file is written, 0 if there is a failure
#
#
#     testCodes subroutine takes 2 attributes
#         takes 2 attribues
#         1. type - NEWS, FR
#	  2. locale - emea, it, de, etc
#
#         eg ('NEWS', $FORM{'locale'});
#
#         tests for existence of a Codes file
#         returns 1 if file exists, 0 if it doesn't
#
#
#     readCodes subroutine takes 2 attributes
#         takes 2 attribues
#         1. type - NEWS, FR
#	  2. locale - emea, it, de, etc
#
#         eg ('NEWS', $FORM{'locale'});
#
#         tests for existence of a Codes file
#         returns content of file file if exists (codes),
#         0 if it doesn't
#
########################################################################







########################################################################
sub writeCodes {

	# takes 3 attribues, returns 1 if file written
	# 1. type - NEWS, FR
	# 2. locale - emea, it, de, etc
	# 3. code - 0 for none

	# eg ('NEWS', $FORM{'locale'}, $FORM{'code'});

        local $ds = `date +'%Y%m%d'`;
	chop($ds);
	local $fn = "/home/gartner/html/rt/content/";

	if ($_[1] eq "emea") {
		$fn = "$fn"."emea/"."$_[0]"."\.codes";
	} else {
		 $fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.codes";
	}

	# remove double spaces from codes
	$_[2] =~ s/  / /g;

	# write Codes file with code
	open (CODES, ">>$fn") ||  die "Can't open Codes file: $fn\n"; #return (0); #
	print CODES "$ds\t$_[2]\n";
	close (CODES);

	return(1);
}

########################################################################
sub testCodes {

	# test for existence of a Codes file

	# takes 2 attribues, returns 1 if file exists, returns 0 if it doesn't
	# 1. type - NEWS, VR
	# 2. locale - emea, it, de, etc

	# eg ('NEWS', $FORM{'locale'});

	local $fn = "/home/gartner/html/rt/content/";
	local $of = "/home/gartner/html/rt/content/"; # second file to test
	if ($_[1] eq "emea") {
		$fn = "$fn"."emea/"."$_[0]"."\.codes";
	} else {
		 $fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.codes";
		 $of = "$fn"."emea/"."$_[0]"."\.codes";
	}

	if (-e "$fn") {

		# file exists
		return(1);

	} else {

		# file doesn't exist

		if (-e "$of" && $_[1] ne "emea") {
			# return 2 if file doesn't exist in EMEA, but does in higher locale
			# issue for austria....
			return(2);
		}

		return(0);
	}

}

########################################################################
sub readCodes {

    # reads of a Codes file, returns code if it exists of 0 if there is none

    # takes 2 attribues
    # 1. type - NEWS, FR
    # 2. locale - emea, it, de, etc

    # eg ('NEWS', $FORM{'locale'});

    local $code;

    # first test if file exists
    local $test = &testCodes($_[0], $_[1]);
    if ($test) {

	local $fn = "/home/gartner/html/rt/content/";

	if ($_[1] eq "emea" || $test == 2) {
	    $fn = "$fn"."emea/"."$_[0]"."\.codes";
	} else {
	    $fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.codes";
	}
	local $ns = $_[1];

	open (CODES, "$fn") || die "Can't open Codes file to read: $fn\n";
	while (<CODES>) {
		chop();
	    local ($ds, $code) = split (/\t/);
	    push @$ns, $ds;
	    $$ns{$ds} = $code;
	    $codes = $code;
	}
	close (CODES);

	return($codes);

    } else {

	return('0');

    }

}

1;
