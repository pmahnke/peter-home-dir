#!/usr/local/bin/perl


# NOTES
#
# add logic for HTTP_ACCEPT_LANGUAGE
#
#


# precedence based content selection

# VARIABLES
$contentRoot   = "/home/gartner/html/rt/resid/";
$localeDB      = "$contentRoot"."Resid2doccd2notenum.db";
$staticRoot    = "$contentRoot";


if ($ENV{'CONTENT_LENGTH'}) {

	##############################################################
	# read POST if there is one


    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    local @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {


	($name, $value) = split(/=/, $pair);
	$value =~ s/\+/ /g; # spaces
	# $value =~ s/\&lt\;/\</g; # less thans
	# $value =~ s/\&amp\;/\</g; # ampersans
	$value =~ s/%(..)/pack("c",hex($1))/ge; # rest
	$value =~ s/\,//g;
	$FORM{$name} = $value;
	$testvalue .=$value;
    }

	&readDb if ($testvalue);


} elsif ($ENV{'QUERY_STRING'}) {

	##############################################################
	# read GET

    @pairs = split(/&/, $ENV{'QUERY_STRING'});
    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ s/\+/ /g; # spaces
	$value =~ s/%(..)/pack("c",hex($1))/ge; # rest
	$value =~ s/\,//g;
	$FORM{$name} = $value;
$testvalue .= $value;	
    }

	&readDb if ($testvalue);

}





&printPage;

exit;

######################################################################
sub printPage {

    print <<EndofHTML;
Content-type: text/html

<html>
<body>

<form method=get>
<table>
<tr><td>Res Id</td><td><input type="text" name="resId" value="$FORM{'resId'}"></td></tr>
<tr><td>Doc Code</td><td><input type="text" name="docCd" value="$FORM{'docCd'}"></td></tr>
<tr><td>Note Number</td><td><input type="text" name="noteNum" value="$FORM{'noteNum'}"></td></tr>
<tr><td>Title</td><td><input type="text" name="title" value="$FORM{'title'}"></td></tr>
<tr><td></td><td><input type=submit></td></tr>
<tr><td></td><td></td></tr>
</table><p>

<table>

$line

</table>

<p />

</form>
</body>
</html>
EndofHTML

}




#######################################################################
sub readDb {

    open (DB, "$localeDB") || die "Can't open locale db: $localeDB\n";

    while (<DB>) {

	chop();

	# example Res Id	Title Nm	Pub Dt	Doc Cd	Dpub Note Num

	s/\"//g; # remove quotes

	local ($resId, $title, $date, $docCd, $noteNum) = split (/\t/);

	$resId =~ s/\,//;
	$docCd =~ s/\,//;
	$noteNum =~ s/\-//g;
	$formNoteNum = $FORM{'noteNum'};
	$formNoteNum =~ s/\-//g;

	next if ($resId !~ /^$FORM{'resId'}/ && $FORM{'resId'});
	next if ($docCd !~ /^$FORM{'docCd'}/ && $FORM{'docCd'});
	next if ($noteNum !~ /$formNoteNum/ && $FORM{'noteNum'});
	next if ($title !~ /$FORM{'title'}/ && $FORM{'title'});

	$line .= <<eof;
	<tr><td>$resId</td><td>$title</td><td>$date</td><td>$docCd</td><td>$noteNum</td></tr>

eof

    }

    close (DB);

}





















