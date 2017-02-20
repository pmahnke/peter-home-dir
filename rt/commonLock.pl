#!/usr/local/bin/perl


########################################################################
#
# commonLock.pl
#
#   written: 09 Dec 2003 by Peter Mahnke
#   modified:
#
#   require script, called from homepage_parser.pl and pickMQHCVR.cgi
#
#   DESCRIPTION
#     tests, writes and deletes a lock file for managing MQ, HC and VR
#     overrides from the regional site editors.
#
#     writeLock subroutine takes 3 attributes
#         1. type - MQ, HC, VR
#         2. locale - emea, it, de, etc
#         3. code - 0 for none
#
#         eg ('VR', $FORM{'locale'}, $FORM{'code'});
#
#         writes a file /<LOCALE>/<TYPE>.lock with <CODE> as the content
#         returns 1 if file is written, 0 if there is a failure
#
#
#     testLock subroutine takes 2 attributes
#         takes 2 attribues
#         1. type - MQ, HC, VR
#	      2. locale - emea, it, de, etc
#
#         eg ('VR', $FORM{'locale'});
#
#         tests for existence of a lock file
#         returns 1 if file exists, 0 if it doesn't
#
#
#     readLock subroutine takes 2 attributes
#         takes 2 attribues
#         1. type - MQ, HC, VR
#	      2. locale - emea, it, de, etc
#
#         eg ('VR', $FORM{'locale'});
#
#         tests for existence of a lock file
#         returns content of file file if exists (codes),
#         0 if it doesn't
#
########################################################################







########################################################################
sub writeLock {

	# takes 3 attribues, returns 1 if file written
	# 1. type - MQ, HC, VR, CV
	# 2. locale - emea, it, de, etc
	# 3. code - 0 for none

	# eg ('VR', $FORM{'locale'}, $FORM{'code'});

	local $fn = "/home/gartner/html/rt/content/";

	if ($_[1] eq "emea") {
		$fn = "$fn"."emea/"."$_[0]"."\.lock";
	} else {
		 $fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.lock";
	}
	if ($_[2] eq "0") {

		# null, so delete lock file
		unlink ($fn) || return(0);

	} else {

		# write lock file with code
		open (LOCK, ">$fn") ||  die "Can't open lock file: $fn\n"; #return (0); #
		print LOCK $_[2];
		close (LOCK);

	}

	return(1);
}

########################################################################
sub testLock {

	# test for existence of a lock file

	# takes 2 attribues, returns 1 if file exists, returns 0 if it doesn't
	# 1. type - MQ, HC, VR
	# 2. locale - emea, it, de, etc

	# eg ('VR', $FORM{'locale'});

	local $fn = "/home/gartner/html/rt/content/";

	if ($_[1] eq "emea") {
		$fn = "$fn"."emea/"."$_[0]"."\.lock";
	} else {
		 $fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.lock";
	}

	if (-e "$fn") {

		# file exists
		return(1);

	} else {

		# file doesn't exist
		return(0);
	}

}

########################################################################
sub readLock {

	# reads of a lock file, returns code if it exists of 0 if there is none

	# takes 2 attribues
	# 1. type - MQ, HC, VR
	# 2. locale - emea, it, de, etc

	# eg ('VR', $FORM{'locale'});

	local $code;

	# first test if file exists
	if (&testLock($_[0], $_[1])) {

		local $fn = "/home/gartner/html/rt/content/";

		if ($_[1] eq "emea") {
			$fn = "$fn"."emea/"."$_[0]"."\.lock";
		} else {
			$fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.lock";
		}

		open (LOCK, "$fn") || die "Can't open lock file: $fn\n";
		while (<LOCK>) {
			$code = $_;
		}
		close (LOCK);

		return($code);
	} else {
		return(0);
	}

}

1;
