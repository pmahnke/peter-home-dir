#!/usr/bin/perl

#Variables
#####################
$thisScript    = "tm.cgi";
$rootDir       = "/home/transitionelement/";
$templateDir   = "template/";
$includeDir    = "html/my/tm/incl/";
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

    &readStyleSheet("$rootDir$htmlDir$FORM{'style'}");
    &parsePage("$rootDir$htmlDir$FORM{'page'}");
    &addMarkup($out);
    &printPage;
    exit;
				# End of foreach $pair
} elsif (@ARGV) {

    $currentDir = `pwd`;
    chop ($currentDir);
    $currentDir = $currentDir."/";

    # set output directory
    $outputDir = "$currentDir";
    $outputDir = "$ARGV[1]" if (-d "$ARGV[1]");
    $outputDir = "$currentDir$ARGV[1]" if (-d "$currentDir$ARGV[1]");
    $outputDir = "$rootDir$htmlDir$ARGV[1]" if (-d "$rootDir$htmlDir$ARGV[1]");
    $outputDir = "$rootDir$ARGV[1]" if (-d "$rootDir$ARGV[1]");

    # set input directory
    local $inputDir = "";
    $inputDir = "$ARGV[0]" if (-d "$ARGV[0]");
    $inputDir = "$currentDir$ARGV[0]" if (-d "$currentDir$ARGV[0]");
    $inputDir = "$rootDir$htmlDir$ARGV[0]" if (-d "$rootDir$htmlDir$ARGV[0]");
    $inputDir = "$rootDir$ARGV[0]" if (-d "$rootDir$ARGV[0]");
   
    # set full path + file name
    local $inputFile = "";
    if (!$inputDir) {
	$inputFile = "$ARGV[0]" if (-f "$ARGV[0]");
	$inputFile = "$currentDir$ARGV[0]" if (-f "$currentDir$ARGV[0]");
	$inputFile = "$rootDir$htmlDir$ARGV[0]" if (-f "$rootDir$htmlDir$ARGV[0]");
	$inputFile = "$rootDir$ARGV[0]" if (-e "$rootDir$ARGV[0]");
    }

    print "
outputDir $outputDir
inputDir  $inputDir
inputFile $inputFile\n";

    if (!@ARGV) {

	print "\n\ntm.cgi <input file or dir> <output dir> \n\n";
	exit;
	
    # tests dir to save output
    } elsif (!$outputDir) { 
	
	print "\n\nNo Output Directory Found: $ARGV[1]";
	print "\n\ntm.cgi <input file or dir> <output dir> \n\n";
	exit;

    # trying input file
    } elsif ($inputFile) {

	$outputFile = substr ($ARGV[0], index ($ARGV[0], "/", -1) + 1 );
	$inputDir = $outputFile;
	$outputFile = "$outputDir$outputFile";
	print "outputfile name $outputFile\n";
	&parsePage($inputFile);
	&readStyleSheet($inputDir);
	&addMarkup($out);
	&savePage($outputFile);
	print "Done!\n\n";
	exit;

    # trying input dir
    } elsif ($inputDir) {     # tests input dir

	# first argument is a directory
	opendir (DIR, "$inputDir");
	readdir (DIR); # ignor .
	readdir (DIR); # ignor ..
	@files = readdir (DIR);
	closedir (DIR);
	
	foreach $file (@files) {
	    
	    next if (-d $file);
	    print "\nprocessing file $file...";
	    &parsePage("$inputDir$file");
	    &readStyleSheet($inputDir);
	    &addMarkup($out);
	    &savePage("$outputDir$file");
	}
	
	print "Done!\n\n";
	exit;


    } else {

	print "\n\nNo Input: $ARGV[0] directory or file found\n\n";
	print "tm.cgi <input file or dir> <output dir>\n";
	exit;

	exit;

    }

} else {
      
    # Nothing to do

    print "Content-type: text/html\n\n";
    print "\n\n$ARGV[0] not found\n";
    print "tm.cgi <input file> <output dir> or tm.cgi?page=<inputfile>\n";
    
    exit;
    
}

exit;


#####################################################################
sub addMarkup {

    $final = "";
    local $inBody = 0;
    foreach (split ("\n", $out)) {

	if ($header) {
	    
	    if (/\<body/i) { # strip body tag, leave rest
		$inBody = 1;
		$_ = $1  if (/\<body[^>]*>(.+)/);
	    } elsif (!$inBody) {
		next;
	    }
	} 

	if ($footer) {
	    if (/\<\/body\>/i) {
		$inBody = 0;
		$_ = $1 if (/(.+)\<\/body\>/i);
	    } elsif (!$inBody) {
		next;
	    }
	}


	local $i = 0;

	foreach $tag (@tags) {
	    print "turning $tag into $style[$i]\n" if (/$tag/ && @ARGV);
	    s/$tag/$style[$i]/gi;
	    $i++;
	}	
	
	# add a font to each table cell
	s/(<td[^\>]*>)/$1$FONT/gi if ($tdTable);

	# add title to page
	s/\<title\>/\<title\> $tmTitle/i if ($tmTitle);

	$final .= "$_\n";
    }

    $final = "$header\n\n$final\n\n$footer\n\n";

    return;
}              # end sub addMarkup 


#####################################################################
sub readStyleSheet {

    # set a default style sheet if one wasn't found in the main file
    # it is actually more of a replace string with another string

#    $styleFile = "$rootDir$includeDir"."SS_default.style" if (!$styleFile);
#    $styleFile = "$rootDir$htmlDir$styleFile" if (-f "$rootDir$htmlDir$styleFile"); # check current dir
    $styleFile = "$rootDir$includeDir$styleFile";# if (-e "$rootDir$includeDir$styleFile"); # check current dir for sub dir incl
    
    print "opening style sheet $styleFile\n" if (@ARGV);

    open (STYLE, "$styleFile") || die "ERR opening $styleFile\n";

    while (<STYLE>) {

	chop();
	next if (!$_);
	local ($key, $value) = split (/\|/);
	$key =~ s/ //g;

	# look for "special" style sheet key values

	# look for header
	$header = &getInclude($value, 1) if ($key eq "header");
	
	#look for footer
	$footer = &getInclude($value, 1) if ($key eq "footer");

	# look for a base font
	$FONT   = "$value" if ($key =~ /<FONT>/);

        # look for TD table cell instructions
	#special to add a font to the start of every table cell
	if ($key =~ /<TD>/ && $value =~ /<FONT>/) {
	    $tdTable = 1;
	    next;
	}

	push @tags, $key;
	push @style, $value;
    }

    close (STYLE);
    return;

}               # end sub readStyleSheet 

#####################################################################
sub savePage {

    open (OUTPUT, ">$_[0]") || die "ERR saving $_[0]\n";
    print OUTPUT $final;
    close (OUTPUT);
    print "wrote $_[0]\n";

}


#####################################################################
sub printPage {

    print <<EOF;
Content-type: text/html


$final


EOF



}               # end sub printPage


# Parse the input file
#####################################################################
sub parsePage {

    $out = "";

    open (INPUT, "$_[0]") || die "Can't open: $_[0]\n";

    while (<INPUT>) {		# step through the Input File
	
	if (/\<tm/) {	# look for a <tm tag

	    &parseInclude($_);

	} else {

	    $out .= "$_";	# if there is no <tm tag, simply
	      	                # write the line to the output and move on
	}	
    }		
    close (INPUT);
}                   # end sub parsePage





#####################################################################
sub parseInclude {

    print "in a parseInclude $_ \n" if (@ARGV);

    # we got here because a <tm tag was found

    # first seperate out... before the tag, the tag and after the tag
   
    /(.+)<tm ([^\>]*)>(.+)/i;

    local ($tag, $at) = "";

    $out  .= $1;
    $tag   = $2;
    $at    = $3;
    

    # now to deal with the tag
    
    # first split the key=value pairs apart
    undef %TAG;

    if (/ /) {
	foreach (split (" ", $tag)) {
	}
	s/\"//g; # remove quotes
	s/\<tm //i; # remove <tm
	s/\>//g; # remove >
	local ($name, $value) = split ("\=");
	$TAG{$name} = $value;
    if (/ /) {
    }
 }   
    local $key = "";

    foreach $key (keys %TAG) {

	# deal with each key of the key value pair
	print "parsing KEY $key\n  and TAG $TAG{$key}\n" if (@ARGV);

	if ($key =~ /src/i) {
	    
	    print "parse tm got a src  at $_\n" if (@ARGV);

	    # this is asking for another file to be included <tm src=
	    $out .= &getInclude($TAG{$key});
	    
	} elsif ($key =~ /style/i) { # <tn style=style.sheet>

	    print "parse tm got a style  at $_\n" if (@ARGV);

	    # this is telling us what style sheet to use
	    $styleFile = $TAG{$key};
	    print "styleFile from parse is $styleFile\n" if (@ARGV);

	} elsif ($key =~ /title/i) { # <td title=DOCUMENT TITLE>

	    print "parse tm got a title  at $_\n" if (@ARGV);
	    $tmTitle = $TAG{$key};
	}

    }

    # done with the tag, now append the text from the line
    # after the tag and return

    $out .= "$at\n";
    

}                       # sub parseInclude {

#####################################################################
sub getInclude {

    # get include file, don't process it
    local $include = "";
    
    $include = "\n\n\<!\-\- START INCLUDE FILE $rootDir$_[0] \-\-\>\n" if (!$_[1]);;

    open (INCL, "$rootDir$htmlDir$_[0]") || die "Err\: include $rootDir$_[0]\n";

    while (<INCL>) {
	$include .= "    $_";
    }
    
    close (INCL);

    $include .= "\n\<!\-\- END INCLUDE FILE $rootDir$_[0] \-\-\>\n\n" if (!$_[1]);

    return($include);

}                       # end sub getInclude








