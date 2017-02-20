
From iddprm@iddmz4.iddis.com Wed Jun  3 09:41:06 1998
Date: Tue, 2 Jun 1998 12:32:57 -0400
From: Peter Mahnke <iddprm@iddmz4.iddis.com>

#!/usr/bin/perl

# this is Peter Mahnke's attempt at a HTML Template engine
# all it currenly does is take an input file, read it and look for a
# <peter src=""> tag and then include that file in an outputfile with the other
# lines of the input file

# Variables
$logFileName         =  "/tmp/peter_parsed_html.log";
$includeDir          =  "/www/iddnet/include/";
$htmlDir             =  "/www/iddnet/html/";

# Open Log File
# open (LOG, ">>$logFileName") || die ("can not open $logFileName/n");

# Determine if called from a comand line for from a cgi
if (!@ARGV) {   # called from a cgi
    
    $cgi = 1;

    # Get the input from the HTML Form
    $buffer = $ENV{'QUERY_STRING'};
 
    # Split the name - value pairs
    if ($buffer) { 
		  @pairs = split(/&/, $buffer);
		  foreach $pair (@pairs) {
				($name, $value) = split(/=/, $pair);
				$file[0] = $value;
#	    print LOG $file[0];
		  }   
    } else {						  # nothing to do
		  exit;
    }

} else {
    $cgi = 0;
    @file = @ARGV;
}

foreach $file (@file) {
    &parseFile($file);
    if ($cgi) {
		  print "Content-type: text/html\n\n";
		  $out =~ s/a href\=\"/a href\=\"peter\-cgi.pl\?page\=/igm;
		  print "$out\n";
    } else {
		  $fileName = "$file";
		  open (OUTPUT, ">$htmlDir$fileName") || die "can't open output";
		  print OUTPUT $out;
		  close (OUTPUT);
    }
#    print LOG ("***** done with $fileName *****\n\n");
    close (INPUT);
}

# close (LOG);
exit;
###########################################


# Determine if there is domain specific stuff
if ($ENV{'REMOTE_HOST'} =~ /iddis.com/) {
#    print LOG ("REMOTE HOST\t$ENV{'REMOTE_HOST'}\tiddis\n");
} elsif ($ENV{'REMOTE_HOST'} =~ /dowjones.com/) {
#    print LOG ("REMOTE HOST\t$ENV{'REMOTE_HOST'}\tdowjones\n");
} else {
#    print LOG ("REMOTE HOST\t$ENV{'REMOTE_HOST'}\tother\n");
}


if ($input{'on'}) {
    $parseTag = $input{'on'};
} else {
    $parseTag = "\<body\>";     # for <body> </body> parsing, not currently used
}


sub parseFile {

    $fileName = "$file";

     open (INPUT, "$includeDir$fileName");
#    print LOG ("***** opening $fileName *****\n");
    
    while (<INPUT>) { # step through the Input File
    
	if (/\<peter/) { # look for a <peter tag

# in case the <peter tag is in the middle of a line,
# I keep the information before and after the tag and 

	    $prePeterTag = substr ($_, 0, index ($_, "\<peter"));
	    $postPeterTag = substr (substr ($_, index ($_, "\>" , index ($_, "\<peter" + 7 )), - 1), 1);

#	    print LOG ("\tfound \<peter tag \n");

	    if (/src\=/) { # look for a src= parameter to include a file

		if (index ($_, "src\=\"") < 2) { # sees if the "" were included
		    $startingPoint = index ($_, "src\=") + 4;
		    $endingPoint = index ($_, " ", $startingPoint) - $startingPoint - 1;
		} else { # if the "" were included
		    $startingPoint = index ($_, "src\=") + 5; # find where the file name starts  
		    $endingPoint = index ($_, "\"", $startingPoint) - $startingPoint; #  find the length of the file name
		}


		$includeFile = substr ($_, $startingPoint, $endingPoint ); # set the name of the include file to be a variable

#		print LOG ("\tscr file found \t  $includeFile \n");

		&includeFile;

	    }        # end of if src

	} else {
	    $out .= "$_";        # if there is no <peter tag, simply
                                # write the line to the output and move on
	} # end of else
    } # end of while (<input>)
} # end of sub parseFile



# Include Files
#########################################################################
sub includeFile {

    open (INCLUDE, "$includeDir$includeFile") || die "Can not open include file $includeFile";

    $out .="$prePeterTag\n";
    $out .= "\n\<\!-- start of $includeFile --\>\n\n";

    while (<INCLUDE>) {
		  $out .= "     $_";
    }

    $out .= "\n\<\!-- end of $includeFile --\>\n\n";
    $out .= "$postPeterTag\n";

    close (INCLUDE);
    
}# end of sub includefile

#########################################################################























