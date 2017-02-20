#!/usr/local/bin/perl


########################################################################
#
# commonTransDoc.pl
#
#   written: 15 Jan 2004 by Peter Mahnke
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
#         writes a file /<LOCALE>/<TYPE>.detail with <CODE> as the content
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
sub writeDetail {

	# takes 5 attribues, returns 1 if file written
	# 0. type - NEWS, FR
	# 1. locale - emea, it, de, etc
	# 2. code - resid or 0 for none
	# 3. title
	# 4. uri
	# 5. pubdate
	# 6. summary
	# 7. author
	# $title, $link, $pubDate, $summary, $resId, $auth

	# eg ('NEWS', $FORM{'locale'}, $FORM{'code'});

	#return(0) if (!&testDetail($_[0], $_[1], $_[2])); # code already in database, don't write

        local $ds = `date +'%Y%m%d%S'`;
	chop($ds);

	# uses code given, if not, then creates one from a date stame YYYYMMDDSS
	$code = $_[2];
	$code = $ds if (!$code);

	local $fn = "/home/gartner/html/rt/content/";
	if ($_[1] eq "emea") {
		$fn = "$fn"."emea/"."$_[0]"."\.detail";
	} else {
		$fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.detail";
	}

	$test = `grep -c $_[2] $fn`;

	if ($test > 0) {
            # already in database
	    return(0);
	} else {
            # write Codes file with code
	    open (CODES, ">>$fn") ||  die "Can't open detail file: $fn\n"; #return (0); #
	    print CODES "$code\t$_[3]\t$_[4]\t$_[5]\t$_[6]\t$_[7]\n";
	    close (CODES);
            return(1);
	}

}

########################################################################
sub testDetail {

	# test for existence of a code file

	# takes 3 attribues, returns 1 if file exists, returns 0 if it doesn't
	# 0. type - NEWS, VR
	# 1. locale - emea, it, de, etc
	# 2. code

	# eg ('NEWS', $FORM{'locale'}, code);

	local $fn = "/home/gartner/html/rt/content/";
	local $of = "/home/gartner/html/rt/content/"; # second file to test
	if ($_[1] eq "emea") {
		$fn = "$fn"."emea/"."$_[0]"."\.detail";
	} else {
		 $fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.detail";
		 $of = "$fn"."emea/"."$_[0]"."\.detail";
	}


	# entry exists
	$_ = `grep -c $_[2] $fn`;

	if ($_ > 0) {
	    $msg .= "test: exists - $_ from $_[2]<br>";
	} else {
            $msg .= "test: doesn't exist - $_ from $_[2] <br>";
        }

	return(1) if ($_);
	return(0);

}

########################################################################
sub readDetail {
    
    # reads of a Codes file, returns code if it exists of 0 if there is none
    
    # takes 2 attribues
    # 0. type - NEWS, FR
    # 1. locale - emea, it, de, etc
    # 2. code

    # eg ('NEWS', $FORM{'locale'});
    
    # returns 0 is code not found and $code, $uri, $title, $pubDate, $summary, $author if found
    
    
    local $code;
    
    # first test if file exists
    
    local $fn = "/home/gartner/html/rt/content/";
    
    if ($_[1] eq "emea") {
	$fn = "$fn"."emea/"."$_[0]"."\.detail";
    } else {
	$fn = "$fn"."emea/"."$_[1]"."/"."$_[0]"."\.detail";
    }
    local $ns = $_[0];
    
    $_ = `grep $_[2] $fn`;
    
    return (0) if ($_ == 1); # grep returned nothing
    
    chop();
    
    local ($code, $title, $uri, $pubDate, $summary, $author) = split (/\t/);
    
    return ($code, $title, $uri, $pubDate, $summary, $author);
    
    
}

1;
