#!/usr/bin/perl

############################################################################
#
#  build.cgi
#
#  writen by Peter Mahnke on 29 - 31 Oct 2001
#
#  modified
#     by Peter Mahnke
#     17 Dec 2001  -  added urlInclude
#     22 Mar 2004  -  added Template
#
#  Template Interpreter
#
#	currently only has a HTTP API
#
#	usage: build.cgi?
#		page=<template filename>
#		&extraDir=<directory of production environment to use> usually "staging"
#			could be set up to user more environments, but then need to have
#			various locations supported in the build action.....
#		&locale=<locale name as defined in locale.db>
#		&action=<what to do> currently only 2 options,
#			"build" which saves the output in the production environment,
#			or nothing which outputs the built page to the browser in a dynamic
#			environment
#
#  Parses a template file and looks for a special <tm> tag
#  <tm> attributes (case insensitive) can be as follows
#
#	src=<filename>
#
#		the interpreter will look for the <filename>
#		starting in the locale's default directory and
#		move up through a heirarch prescribed in locale.db
#		if it isn't found
#
#	style=<rel or absoult URI to stylesheet to include>
#
#		the interpreter will insert a
#		<link REL="STYLESHEET" TYPE="text/css" HREF="<stylesheet URI>">
#		in the header
#
#	title=<title>
#
#		the interpreter will append the <title> text to the
#		<title> in the header
#
#	jsFile=<rel or absoult URI to javascript file to include>
#
#		the interpreter will insert a
#		<script src\=\"<javascript URI\"\><\/script\>
#		in the header
#
#	jsInclude=<filename>
#
#		the interpreter will look for the <filename>
#		starting in the locale's default directory and
#		move up through a hierarch prescribed in locale.db
#		if it isn't found and insert it in the header
#		ASSUMES that <script></script> tags are in file!
#
#	characterSet=<character set>
#
#		the interpreter will override the default charset (ISO-8859-1)
#		with <character set> in the header META information
#
#	Language=<language>
#
#		the interpreter will override the default language
#		from the locale.db and insert the <language> in the
#		header META information
#
#
#       urlInclude=<URI>
#
#              goes over http to get a file
#
#	Template=<filename>
#
#		the interpreter will override the default master template
#
#
#
############################################################################



# precedence based content selection


require ("/home/transitionelement/cgi-bin/SmartyPants.pl");
require ("/home/mahnke/html/peter/MT/extlib/Text/Textile.pm");


# VARIABLES & FILE LOCATIONS
$defaultLocale = "emea";	# the default locale for system
$date          = time;
$contentRoot   = "/home/transitionelement/html/";
#$getIP         = &getURLinclude('http://intl.gartner.com/cgi-bin/getip.cgi');
#chop($getIP );
$rootURI       = "http://www.transitionelement.com/";
$localeDB      = "$contentRoot"."locale.db";
$staticRoot    = "$contentRoot";


# get locale information from flat file db
&readLocaleInfo;


##############################################################
#  read COOKIES if there are any
#    this is really only if this script is run dyanmically
#    this is not a requirement of the ITG i18n project

if ($ENV{'HTTP_COOKIE'}) {
    
    local @pairs = split(/\;/, $ENV{'HTTP_COOKIE'});
    
    foreach (@pairs) {
	
	s/ //g;
	
	local ($name, $value) = split (/\=/);
	$COOKIE{$name} = $value;
	
    }
    
    $COOKIE{'visits'}    = $COOKIE{'visits'} + 1;    # INCREMENT VISIT
    $COOKIE{'lastvisit'} = $date;                    # ADD TODAY'S DATE
    $COOKIE{'unique_id'} = $date if (!$COOKIE{'unique_id'});
    
} else {
    
    # give the user some default cookies
    $COOKIE{'locale'}    = $defaultLocale;
    $COOKIE{'visits'}    = 1;
    $COOKIE{'lastvisit'} = $date;
    $COOKIE{'unique_id'} = $date;

}

##############################################################
# read POST if there is one
if ($ENV{'CONTENT_LENGTH'}) {
    
    read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
    local @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
	
	
	($name, $value) = split(/=/, $pair);
	$value =~ s/%(..)/pack("c",hex($1))/ge; # clean special chars
	
	$FORM{$name} = $value;
	
    }
}

##############################################################
# read GET if there is one
$buffer = $ENV{'QUERY_STRING'};

# Split the name - value pairs
if ($buffer) {		  # assumes that form has been filled out
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ s/%(..)/pack("c",hex($1))/ge; # clean special chars
	$FORM{$name} = $value;
    }
}


# support a change in locale
$COOKIE{'locale'} = $FORM{'locale'} if ($FORM{'locale'});

# handle current page from cookie if no new one requested
$FORM{'page'} = $COOKIE{'page'} if (!$FORM{'page'});

# if no page at all... then give home page as defaul
$FORM{'page'} = "home.html" if (!$FORM{'page'});



# action of script

# the concept of extraDir is to allow for various different production environments
# currently there is only staging and production
# since this script can be run dyanmically, you have to send a extraDir=staging in the request
$contentRoot = "$contentRoot$FORM{'extraDir'}/" if ($FORM{'extraDir'});

local $header = &getPage(&dirLogic("header.incl"));

if ($FORM{'page'} =~ /rec_/) {

    # special navigation for recognised user pages
    # should probably remove this to templates at this point
    # since it is based on a file naming convention
    
    $navigation           = &getPage(&dirLogic("rec_navigation.incl"));
    
} else {
    
    $navigation           = &getPage(&dirLogic("navigation.incl"));
    
}
local $footer             = &getPage(&dirLogic("footer.incl"));
local $content            = &getPage(&dirLogic($FORM{'page'}));

&buildPage;

if ($FORM{'action'} eq "build") {
    
    &savePage;
    
} else {
    
    &printPage;
    
}

exit;


##############################################################
sub dirLogic {
    
    # look for file starting in directory and go up hierarchy
    # as described in locale.db
    
    # assumes that max depth is 3 levels
    # assumes level 0 is deepest /wcw/emea/de but might be /wcw/emea or even /wcw
    # assumes that all files for a site are in a single directory
    
    local $file       = "";
    local $curDir     = "";
    local $file       = "";
    
    
    # LEVEL 0
    $curDir = "$contentRoot"."$dir{$COOKIE{'locale'}}";
    $file   = "$curDir"."$_[0]";
    
    if (-e "$file") {
	
	# found file in current locale
	$msg .= "\n\<br\> found $file at level 0";
	return($file);
    }
    
    # file wasn't in expected dir, are we at the top level?
    # return, file doesn't exist even at the top level
    return (0)    if ($COOKIE{'locale'} eq "wcw");
    
    
    # LEVEL 1
    # look for file up one level based on locale.db defined hierarcy
    $curDir = "$contentRoot"."$dir{$locale{$COOKIE{'locale'}}}";
    $file   = "$curDir"."$_[0]";
    
    # if it exists, send directory info
    if (-e "$file") {
	$msg .= "\n\<br\> found $file at level 1";
	return($file);
    }
    
    # file wasn't in expected dir, are we at the top level?
    # return, file doesn't exist even at the top level
    return (0)    if ($locale{$COOKIE{'locale'}} eq "wcw");
    
    
    # LEVEL 2
    # look for file up one more level
    $curDir = "$contentRoot";
    $file   = "$curDir"."$_[0]";
    
    # if it exists, send directory info
    if (-e "$file") {
	$msg .= "\n\<br\> found $file at level 2";
	return($file);
    }
    
    $msg .= "\n\<br\> ERROR failed at all levels input $file";
    
    # if is doesn't fail if at top level
    return (0);
    
}

######################################################################
sub printPage {
    
    print <<EndofHTML;
Content-type: text/html
$cookie

$html

EndofHTML

}

######################################################################
sub savePage {
    
    local $pageName = "$staticRoot$dir{$FORM{'locale'}}$FORM{'page'}";
    
    $msg =~ s/<tm/\&lt\;tm/gi;
    
    open (PAGE, ">$pageName") || die "Can't open page to save: $pageName\n";
    print PAGE $html;
    close (PAGE);
    
    print <<EndofHTML;
Content-type: text/html
$cookie

$html

<p>

<font class=tiny>$msg<\/font\><p>


EndofHTML


    exit;

}


######################################################################
sub buildPage {

    # this subroutine sets up any additional meta data,
    # javascript files, and assembles the page
    
    #################################################
    # Meta Tag for Character Set
    if ($tmCharSet) {
	
	# use charset found in template
	$METAcharSet = "<meta http\-equiv\=\"content\-type\" content\=\"text\/html\; charset\=$tmcharset\" \/\>";
    } else {
	
	# default
	$METAcharSet = "<meta http\-equiv\=\"content\-type\" content\=\"text\/html\; charset\=iso\-8859\-1\" \/\>";
    }
    
    #################################################
    # Meta Tag for Language
    if ($tmLanguage) {
	
	# use language found in template
	$METAlang = "<meta http\-equiv\=\"content\-language\" content\=\"$tmlanguage\" \/\>";
	
    } else {
	
	# default
	$METAlang = "<meta http\-equiv\=\"content\-language\" content\=\"$lang{$cookie{locale}}\" \/\>";
	# $METAlang = "<meta http\-equiv\=\"content\-language\" content\=\"en\-us\" \/\>";
	
    }
    
    #################################################
    # Style Sheets
    if (@tmStyleSheet) {
	
	# add more stylesheet references
	foreach (@tmStyleSheet) {
	    $METAstyle .= "  <link rel\=\"stylesheet\" type\=\"text\/css\" href\=\"$rootURI/$_\"\>";
	}
    }
    
    #################################################
    # templates
    if (!$tmTpl) { # || &dirLogic($tmTpl)) {
	
	# load default template
	$tmTpl = "master.tpl";
	
    }
    $msg .= "getting template: ".&dirLogic($tmTpl)."<br />\n";
    $html .= &getPage(&dirLogic($tmTpl));
    
    # layout page, based on Master Templates
    eval $html;

    # textile
    $textile = new Text::Textile;
    $html    = $textile->process($html);

    # smarty pants
    $html    = &SmartyPants ($html, 1);

    

}






##############################################################
sub getPage {
    
    $msg .= "\n<br\>in getPage, looking for $_[0]\n";
    
    $out = "";
    
    open (INPUT, "$_[0]") || die "ERROR in sub getPage: Can't open file: $_[0]\n\n";
    
    while (<INPUT>) {           # step through the Input File
	
        if (/<tm/) {   # look for a <tm tag
	    
            $out .= &parseInclude($_);
	    
        } else {
	    
            $out .= "$_";       # if there is no <tm tag, simply
	    # write the line to the output and move on
        }
    }
    close (INPUT);
    return($out);
}                   # end sub parsePage

####################################################################
sub parseInclude {
    
	# we got here because a <tm tag was found
    
    my ($tag, $afterTag) = "";
    
    # first seperate out... before the tag, the tag and after the tag
    
    $_[0] =~ /<tm(.[^\>]*)\>/i;
    
    
    my $output .= $`;   # append whatever was in front to the $out output
    $tag        = $1;   # the contents of the <tm > tag
    $afterTag   = $';   # additional information after the <tm > tag
    $msg .= "\n<br\>parsing string $_\n\t pre: $output \n\t tag: $tag \n\t after: $afterTag \n";
    
    # now to deal with the tag
    
    # first split the key=value pairs apart
    
    $tag =~ s/\"//g; # remove quotes
    
    my ($name, $value) = split (/=/, $tag);
    
    # deal with each key of the key value pair
    $msg .= "\n<br\>parsing string $_\n\t tag: $tag \n\t name: $name \n\t value: $value \n";
    
    if ($name =~ /src/i) {
	
	# src attribute
	#  need to go and get file to include
	
	$msg .= "\n<br\>parse <tm got a src\= $value  at $_\n";
	
	# this is asking for another file to be included <tm src=
	$output .= &getInclude(&dirLogic($value));
	
    } elsif ($name =~ /style/i) { # <tn style=style.sheet>
	
	# style attribute
	#  need to add this style sheet to header
	
	$msg .= "\n<br\>parse <tm got a style\=  at $_\n";
	push @tmStyleSheet, $value;
	
    } elsif ($name =~ /title/i) {
	
	# title attribute
	#  need to add this to the header
	
	$msg .= "\n<br\>parse <tm got a title $value  at $_\n";
	$tmTitle = $value;
	
    }  elsif ($name =~ /jsFile/i) {

	# jsFile attribute
	#  need to add this to the header
	# <script src=""></script>
	
	$msg .= "\n<br\>parse <tm got a jsFile $value  at $_\n";
	$value = "<script src\=\"$value\"\><\/script\>\n";
	$tmjsFile .= $value;
	
    }  elsif ($name =~ /jsInclude/i) {
	
	# jsInclude attribute
	#  need to add this to the header
	
	$msg .= "\n<br\>parse <tm got a jsInclude $value  at $_\n";
	$tmjsInclude .= &getInclude(&dirLogic($value));
	    
    } elsif ($name =~ /characterSet/i) {
	
	# characterSet attribute
	#  need to add this to the header
	#  in <META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=$value">
	
	$msg .= "\n<br\>parse <tm got a characterSet $value  at $_\n";
	$tmCharSet = $value;
	
    } elsif ($name =~ /Language/i) {
	
	# Language attribute
	#  need to add this to the header
	#  in <META HTTP-EQUIV="Content-Language" CONTENT="">
	
	$msg .= "\n<br\>parse <tm got a Language $value  at $_\n";
	$tmLanguage = $value;
	
    } elsif ($name =~ /urlInclude/i) {
	
	# urlInclude
	#  need to get contents of a web page and insert
	
	$msg .= "\n<br\>parse <tm got a urlIncude $value  at $_\n";
	$output .= "\n".&getURLinclude($value)."\n";
	
    } elsif ($name =~ /Template/i) {
	
	# Template
	#  non-default master template
	
	$msg .= "\n<br\>parse <tm got a Template $value  at $_\n";
	$tmTpl .= $value;
	
    }
    
    
    
    
    # done with the tag, now append the text from the line
    # after the tag and return
    
    if ($afterTag =~ /<tm/i) {
	
    	# there is another <tm tag on the line
    	$msg .= "\n<br\> another <tm tag in the afterTag<br\>\n\n";
    	$output .= &parseInclude($afterTag);
	
    } else {
	
	# append after tag information to output
	$output .= "$afterTag\n";
	
    }
    
    return ($output);
    
}                       # sub parseInclude {

#####################################################################
sub getInclude {
    
    $msg .= "\n<br\>in getInclude: getting file $_[0]\n";
    
    if ($_[0] eq $FLAGlastIncl) {
	
	# just did this include.... so stop
	$msg .= "\n<br\>in getInclude: just parsed this file... must be self refering $_[0]\n";
	return();
	
    }
    
    # get include file, don't process it
    my $include = "";
    
    $include = "\n\n\<!\-\- start include file $_[0] \-\-\>\n" if (!$_[1]);;
    
    open (INCL, "$_[0]") || die "Error getting include\: $_[0] $msg\n";

    while (<INCL>) {

	# rewrite URLs to work in frame set like AskJeeves
	# this was done for prototype... hopefully won't be needed
	s/<a href(\=|\=\")http/<a href$1\/dynamicURL.cgi\?URL\=http/gi;
	
	if (/<tm/) {   # look for a <tm tag
	     
	    &parseInclude($_);
	    
	} else {
	    
	    $include .= "    $_";
	    
	}
    }
    
    close (INCL);
    
    $include .= "\n\<!\-\- end include file $_[0] \-\-\>\n\n" if (!$_[1]);

    $FLAGlastIncl = $_[0]; # prevent circluar parsing of same file.

    return($include);

}                        # end sub getInclude

#######################################################################
sub readLocaleInfo {

    # readLocalInfo reads a flat file database that contains
    # information on the locale name, locale key, default language,
    # locale to borrow content from and the relative directory structure of the locale
    #
    # example:  EMEA|emea|en-uk|wcw|emea/
    
    open (LOCALE, "$localeDB") || die "Can't open locale db: $localeDB\n";
    
    while (<LOCALE>) {
	
	chop();
	
	# example EMEA|emea|en-uk|wcw|emea/

	local @listing = split (/\|/);

	$localeName{$listing[1]} = "$listing[0]";
	$lang{$listing[1]}       = "$listing[2]";
	$locale{$listing[1]}     = "$listing[3]";
	$dir{$listing[1]}        = "$listing[4]";

    }

    close (LOCALE);
    return();

}


#######################################################################
sub getURLinclude {

    local $Output = "";
    
    # Create a user agent object
    use LWP::UserAgent;
    my $ua = new LWP::UserAgent;
    $ua->agent("Mozilla/5.0");
    
    # Create a request
    my $req = new HTTP::Request('GET', $_[0]);
    
    # Pass request to user agent and get response
    my $res = $ua->request($req);
    
    $Output = $res->content;
    
    # Check output
    if ($res->is_success) {
	return($Output);
    } else {
	return($Output, $_[0]); # return error info and url attempted
    }
    
    
}			# end of sub getURLinclude
