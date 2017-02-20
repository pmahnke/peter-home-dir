#!/usr/bin/perl

#Variables
#####################
$thisScript    = "tm.cgi";
$rootDir       = "/home/transitionelement/";
$templateDir   = "template/";
$includeDir    = "html/"; # "include/";
$htmlDir       = "html/";

# Read command line
#####################

# Split the name - value pairs

if ($ENV{'QUERY_STRING'}) {	# assumes that form has been filled out

    @pairs = split(/&/, $ENV{'QUERY_STRING'});
    foreach $pair (@pairs) {

	($name, $value) = split(/=/, $pair);
	$FORM{$name} = $value;

    }

    &parsePage($FORM{'page'});
    &addMarkup($out);
    &printPage if ($buffer);
    exit;

				# End of foreach $pair
} elsif (@ARGV) {

    if ($#ARGV < 1) {

	print "tm.cgi <input file or dir> <output dir>\n";
	exit;

    } elsif (-d "$rootDir$ARGV[1]") {

	print "\n\n$ARGV[1] directory not found\n";
	print "tm.cgi <input file or dir> <output dir>\n";
	exit;

    } elsif (-d "$rootDir$ARGV[0]") {     

	# first argument is a directory
	opendir (DIR, "$rootDir$ARGV[0]");
	readdir (DIR); # ignor .
	readdir (DIR); # ignor ..
	@files = readdir (DIR);
	closedir (DIR);
	
	foreach $file (@file) {
	
	    &parsePage($file);
	    &addMarkup($out);
	    &savePage;
	    print "$file\n";
	}
	
	print "Done!\n\n";
	exit;

    } elsif (-e "$rootDir$ARGV[0]") {

	&parsePage($ARGV[0]);
	&addMarkup($out);
	&savePage;
	print "Done!\n\n";
	exit;

    } else {

	print "\n\n$ARGV[1] directory or file not found\n";
	print "tm.cgi <input file or dir> <output dir>\n";
	exit;

	exit;

    }

} else {
      
    # Nothing to do

    print "Content-type: text\n\n";
    print "\n\n$ARGV[0] not found\n";
    print "tm.cgi <input file> <output dir> or tm.cgi?page=<inputfile>\n";
    
    exit;
    
}

exit;


sub addMarkup {

    &readStyleSheet;

    foreach (split ("\n", $out)) {
	foreach $tag (keys %STYLE) {
	    s/$tag/$STYLE{$tag}/gi;
	}	
	$final .= "$_\n";
    }
    return;
}              # end sub addMarkup 


sub readStyleSheet {

    # set a default style sheet if one wasn't found in the main file

    # it is actually more of a replace string with another string

    $styleFile = "$rootDir$includeDir"."SS_default.style" if (!$styleFile);

    open (STYLE, "$styleFile") || die "ERR opening $styleFile\n";

    while (<STYLE>) {

	chop();
	local ($key, $value) = split (/\|/);
	$key =~ s/ //g;
	$STYLE{$key} = $value;
    }

    close (STYLE);
    return;

}               # end sub readStyleSheet 

sub savePage {

#    $ARGV[1] = $ARGV[1].".new" if (-e "$rootDir$htmlDir$ARGV[1]");
    open (OUTPUT, ">$rootDir$ARGV[1]$ARGV[0]") || die "ERR saving $ARGV[1]$ARGV[0]\n";
    print OUTPUT $final;
    close (OUTPUT);
    print "wrote $rootDir$ARGV[1]$ARGV[0]\n";

}


sub printPage {

    print <<EOF;
Content-type: text\html


$final


EOF



}               # end sub printPage


# Parse the input file
######################
sub parsePage {

    open (INPUT, "$rootDir$htmlDir$_[0]") || die "Can't open: $rootDir$_[0]\n";
    while (<INPUT>) {		# step through the Input File

	if (/\<tm/) {	# look for a <peter tag

	    &parseInclude($_);

	} else {

	    $out .= "$_";	# if there is no <tm tag, simply
	      	                # write the line to the output and move on
	    
	}	

    }		
    close (INPUT);

}                   # end sub parsePage





sub parseInclude {

    # we got here because a <tm tag was found

    # first seperate out... before the tag, the tag and after the tag
   
    /(.+)<tm ([^\>]*)>(.+)/i;
    
    $out      .= $1;
    local $tag = $2;
    local $at  = $3;
    
    print "\n\nfunky\nin $_\n1 $1 \n2 $2 \n3 $3\n\n\n";
    # now to deal with the tag


    # first split the key=value pairs apart

    foreach (split (" ", $tag)) {

	s/\"//g; # remove quotes

	local ($name, $value) = split ("\=");
	$FORM{$name} = $value;

    }
    
    local $key = "";

    foreach $key (keys %FORM) {

#	print "$key eq $FORM{$key}\n";

	# deal with each key of the key value pair


	if ($key =~ /src/i) {
	    
	    # this is asking for another file to be included
	    
	    $out .= &getInclude($FORM{$key});
	    
	} elsif ($key =~ /style/i) {

	    # this is telling us what style sheet to use

	    $styleFile = $FORM{$key};

	}

    }

    # done with the tag, now append the text from the line
    # after the tag and return

    $out .= "$at\n";
    

}                       # sub parseInclude {

sub getInclude {

    # get include file, don't process it

    local $include = "\n\n\<!\-\- START INCLUDE FILE $rootDir$_[0] \-\-\>\n";

    open (INCL, "$rootDir$htmlDir$_[0]") || die "Err\: include $rootDir$_[0]\n";

    while (<INCL>) {
	$include .= "    $_";
    }
    
    close (INCL);

    $include .= "\n\<!\-\- END INCLUDE FILE $rootDir$_[0] \-\-\>\n\n";

    return($include);
}                       # end sub getInclude








