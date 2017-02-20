#!/usr/local/bin/perl


sub buildDocLink {

    # precedence based content selection

    # VARIABLES
    $dlcontentRoot   = "/home/gartner/html/rt/resid/";
    $dllocaleDB      = "$dlcontentRoot"."Resid2doccd2notenum.db";
    $metaDataFile    = "/home/gartner/html/itaDocTest/"."metaDataIndex.db";
    undef local $testValue;
    undef local $value;
    undef $dlline;

    $value = $_[1];
    $value =~ s/ //g; # spaces
    $value =~ s/\,//g;
    undef $FORM{$_[0]};

    $FORM{$_[0]} = $value;
    $testvalue .= $value;

    $formNoteNum = $FORM{'noteNum'};
    $formNoteNum =~ s/\-//g;

    if ($testvalue) {

	&readMetaData if (!$germanFlag);
 	&readresidDb if (!$dlline);
	$dlline =~ s/\|//g;
	$dlline = $_[1] if (!$dlline); # return note number if there is nothing there
    
    }

    return($dlline);

    exit;

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
	next if ($noteNum !~ /$formNoteNum/  && $formNoteNum);
	next if ($title !~ /$FORM{'title'}/  && $FORM{'title'});

	$dlline = "<a href\=\"javascript:void\(null\)\" onclick\=\"openDocFromDoc\(\'\/DisplayDocument\?doc_cd=$docCd\'\)\"\>$FORM{'noteNum'}<\/a\>";



	if ($dlline) {
	    close (DB);
	    return($dlline);
	}


    }

    close (DB);
    return(0);
}



##############################################################
sub readMetaData {

    carp "require.pl: readMetaData: FORM{'docCd'} is $FORM{'docCd'}, FORM{'resId'} is $FORM{'resId'}, formNoteNum is $formNoteNum\n";

    open (FILE, "$metaDataFile") if (-e "$metaDataFile")  || die "Can't open metaDataFile: $metaDataFile\n";
    
    while (<FILE>) {

	local $metaline = $_;
	chop();


	$itNoteNum = $1 if (/GGNOTENUM\=(.[^\|]*\|)/);
	$itResId   = $1 if (/GGRESID\=(.[^\|]*\|)/);
	$itDocCd   = $1 if (/GGDOCCD\=(.[^\|]*\|)/);

	$itNoteNum =~ s/\-//g;

	next if ($itDocCd   !~ /^$FORM{'docCd'}/ && $FORM{'docCd'});
	next if ($itResId   !~ /^$FORM{'resId'}/ && $FORM{'resId'});
	next if ($itNoteNum !~ /$formNoteNum/    && $FORM{'noteNum'});

	$dlline = "<a href\=\"javascript:void\(null\)\" onclick\=\"openDocFromDoc\(\'\/regionalization\/code\/document.jsp\?resId\=$itResId\'\)\"\>$FORM{'noteNum'}<\/a\>";
	
	if ($dlline) {
	    close (FILE);
	    return($dlline);
	}

    }
    
    close (FILE);
    
    return(0);
    
}




















1; # return true
