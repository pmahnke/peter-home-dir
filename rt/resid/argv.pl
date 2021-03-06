#!/usr/local/bin/perl




# VARIABLES
$dlcontentRoot   = "/home/gartner/html/rt/resid/";
$dllocaleDB      = "$dlcontentRoot"."Resid2doccd2notenum.db";
$metaDataFile = "/home/gartner/html/itaDocTest/"."metaDataIndex.db";


if ($ARGV[0]) {

    $value = $ARGV[1];
    $value =~ s/ //g; # spaces
    $value =~ s/\,//g;
    $FORM{$ARGV[0]} = $value;
    $testvalue .= $value;

    $formNoteNum = $FORM{'noteNum'};
    $formNoteNum =~ s/\-//g;
    


    if ($testvalue) {

	&readMetaData;
 	&readresidDb if (!$dlline);
	
    }


    &printDocLink;

    
} else {

    print "

nothing submitted

USAGE: argv.pl <type \- resId docCd noteNum title\> <value\>

";
    exit;

}







exit;



######################################################################
sub printDocLink {

    print <<EndofHTML;
$dlline
EndofHTML

}




#######################################################################
sub readresidDb {

    open (DB, "$dllocaleDB") || die "Can't open locale db: $localeDB\n";

    while (<DB>) {

	chop();

	# example Res Id	Title Nm	Pub Dt	Doc Cd	Dpub Note Num

	s/\"//g; # remove quotes

	local ($resId, $title, $date, $docCd, $noteNum) = split (/\t/);

	$resId =~ s/\,//;
	$docCd =~ s/\,//;
	$noteNum =~ s/\-//g;

	next if ($resId !~ /^$FORM{'resId'}/ && $FORM{'resId'});
	next if ($docCd !~ /^$FORM{'docCd'}/ && $FORM{'docCd'});
	next if ($noteNum !~ /$formNoteNum/  && $FORM{'noteNum'});
	next if ($title !~ /$FORM{'title'}/ && $FORM{'title'});

	$dlline = "<a href\=\"javascript:void\(null\)\" onclick\=\"openDocFromDoc\(\'\/DisplayDocument\?doc_cd=$docCd\'\)\"\>$FORM{'noteNum'}<\/a\>";


	if ($dlline) {
	    return($dlline);
	}
	

    }

    close (DB);
    return(0);
}



##############################################################
sub readMetaData {

    open (FILE, "$metaDataFile") if (-e "$metaDataFile");
    while (<FILE>) {

	local $metaline = $_;
	chop();
	

	$itNoteNum = $1 if (/GGNOTENUM\=(.[^\|]*\|)/);
	$itResId   = $1 if (/GGRESID\=(.[^\|]*\|)/);
	$itDocCd   = $1 if (/GGDOCCD\=(.[^\|]*\|)/);

	$itNoteNum =~ s/\-//g;

	next if ($itDocCd !~ /^$FORM{'docCd'}/ && $FORM{'docCd'});
	next if ($itResId !~ /^$FORM{'resId'}/ && $FORM{'resId'});
	next if ($itNoteNum !~ /$formNoteNum/  && $FORM{'noteNum'});

	$dlline = "<a href\=\"javascript:void\(null\)\" onclick\=\"openDocFromDoc\(\'\/regionalization\/code\/document.jsp\?resId\=$itResId\'\)\"\>$FORM{'noteNum'}<\/a\>";
	
	if ($dlline) {
	    return($dlline);
	}



    }
    
    close (FILE);

    return(0);

}




















1; # return true
