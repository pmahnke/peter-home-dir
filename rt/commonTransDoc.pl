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
#     tests, writes and deletes a document details file for managing News and FR
#     overrides from the regional site editors.
#
#
#     writeDetail
#         takes 5 attribues, returns 1 if file written
#         0. type - NEWS, FR
#         1. locale - emea, it, de, etc
#         2. code - resid or 0 for none
#         3. title
#         4. uri
#         5. pubdate
#         6. summary
#         7. author
#
#         writes a file /<LOCALE>/<TYPE>.detail with:
#         <CODE>\t<TITLE>\t<URI>\t<PUBDATE>\t<SUMMARY>\t<AUTHOR>\n as the content
#
#         returns 1 if file is written, 0 if there is a failure
#
#
#     testDetail
#          test for existence of a code file
#
#          takes 3 attribues, returns 1 if file exists, returns 0 if it doesn't
#          0. type - NEWS, VR
#          1. locale - emea, it, de, etc
#          2. code
#
#
#     readDetail
#         reads of a Detail file, returns code if it exists of 0 if there is none
#
#         takes 2 attribues
#         0. type - NEWS, FR
#         1. locale - emea, it, de, etc
#         2. code
#
#         eg ('NEWS', $FORM{'locale'});
#
#         returns 0 is code not found and $code, $uri, $title, $pubDate, $summary, $author if found
#
#
#     readDetailAll
#         reads of a Codes file, returns code if it exists of 0 if there is none
#
#         takes 2 attribues
#         0. type - NEWS, FR
#         1. locale - emea, it, de, etc
#         2. codes to skip
#
#         eg ('NEWS', $FORM{'locale'});
#
#         returns 0 is code not found and $code, $uri, $title, $pubDate, $summary, $author if found
#
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

	my $output;

	if ($test > 0) {
            
	    # already in database, remove it
	    open (FILE, "$fn");
	    while (<FILE>) {
		next if (/$_[2]/);
		$output .= $_;
	    }
	    close(FILE);

	    open (CODES, ">$fn") ||  die "Can't open detail file: $fn\n"; #return (0); #
	    print CODES $output;
	    print CODES "$code\t$_[3]\t$_[4]\t$_[5]\t$_[6]\t$_[7]\n";
	    close (CODES);
	    
	} else {
	    
	    # write Codes file with code
	    open (CODES, ">>$fn") ||  die "Can't open detail file: $fn\n"; #return (0); #
	    print CODES "$code\t$_[3]\t$_[4]\t$_[5]\t$_[6]\t$_[7]\n";
	    close (CODES);
	    
	}
	return(1);
	

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

    # reads of a Detail file, returns code if it exists of 0 if there is none

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

    $title =~ s/\"/\&quot\;/g; # change quotes to \" to make them form safe.... I hope

    return ($code, $title, $uri, $pubDate, $summary, $author);


}

########################################################################
sub readDetailAll {

    # reads of a Codes file, returns code if it exists of 0 if there is none

    # takes 2 attribues
    # 0. type - NEWS, FR
    # 1. locale - emea, it, de, etc
    # 2. codes to skip

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

    my %all;

    open (FILE, "$fn") || return(0);

    while (<FILE>) {

	chop();

	local ($code, $title, $uri, $pubDate, $summary, $author) = split (/\t/);

	next if ($_[2] =~ /$code/ && $_[2]); # remove ones featured on homepage
	next if (!$title); # remove bad data

	# dedupe
	next if ($t{$title});
	$t{$title} = 1;

	$code++;

	$title =~ s/\"/\&quot\;/g; # change quotes to \" to make them form safe.... I hope

	$all{$code} =  <<EndofHTML;
	<li> <a href="$uri" onclick="openResult('$uri');return false;">$title</a></li>
EndofHTML
    }

    close (FILE);

    local $xhtmlNewsAll;
    foreach $code (reverse sort keys %all) {

	$xhtmlNewsAll .= $all{$code};
	$i++;
	last if ($i > 25);
    }

    return ($xhtmlNewsAll);

}


1;
