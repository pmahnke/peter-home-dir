#!c:/perl/bin/perl

#######################################################################
#
# editPages.cgi
#
#  HTML front end to content management system
#
#   written by Peter Mahnke 1 Nov 2001
#
#   last modified by Peter Mahnke on 17 Dec 2001
#
#######################################################################

#######################################################################
#Variables

$thisScript       = "editPages.cgi";
$buildPagesScript = "build.cgi";
$rootDir          = "/home/transitionelement/html/";
$outputDir        = "";
$inputDir         = "staging/";
$siteName         = "transitionelement.com";
$localeDB         = "$rootDir"."locale.db";
$localhost        = "localhost";
$CMDcp            = "/bin/cp";
$CMDgrep          = "/bin/grep";
$CMDls            = "/bin/ls";

#######################################################################
# read post
read(STDIN,$input,$ENV{CONTENT_LENGTH});

@pairs = split(/&/, $input);
foreach $pair (@pairs) {


	($name, $value) = split(/=/, $pair);
	$value =~ s/\+/ /g; # spaces
	$value =~ s/\&lt\;/\</g; # less thans
	$value =~ s/\&amp\;/\&/g; # ampersans
	$value =~ s/%(..)/pack("c",hex($1))/ge; # rest

	$FORM{$name} = $value;

}

#######################################################################
# decide what to do
&readLocaleInfo;
$siteDir = $dir{$FORM{'site'}};

if (!%FORM) {

	# nothing was submitted.... print the list of locales
	&printDirectoryMenu;

} elsif ($FORM{'page'} eq "site") {

	# the locale was selected and now get the pages to edit
	&printFirstPage;

} elsif ($FORM{'page'} eq "build all") {

	&printBuildAllPage;

} elsif ($FORM{'page'} eq "auto build all") {

	&autoBuildAll;


} elsif ($FORM{'page'} eq "edit") {

	# a file was passed to be edited
	`$CMDcp $rootDir$inputDir$siteDir$FORM{'file'} $rootDir$inputDir$siteDir$FORM{'file'}.temp`;
	$page = &readPage($FORM{'file'});
	&printEditPage;

} elsif ($FORM{'page'} eq "review") {

	# the user wants to look at the proposed changes...
	local $tempFileName = "$FORM{'file'}".".temp";
	&saveTempFile($tempFileName);
	$page = $FORM{'text'};
	&printEditPage;

} elsif ($FORM{'page'} eq "save") {

	# the user wants to save the changes...
	&saveTempFile($FORM{'file'});
	&printSavePage;

} elsif ($FORM{'page'} eq "") {

} else {

	&printDirectoryMenu;
}
exit;

#######################################################################
sub printSavePage {

    $popupPage = $FORM{'file'};
    $popupPage = "Content\-type: text\/html\n\nnothing to display\n" if ($FORM{'file'} =~ /.incl/);
    
    local $build = "";
    local $file   = "";
    
    if ($FORM{'file'} =~ /.incl/) {
	
	# if its an include file, you can't build the normal page
	@inclFiles = &grepDir($FORM{'file'});
	
	$build .= "This include file (\<b\>$FORM{'file'}\<\/b\>) affects the following pages:\<p\>";
	
	foreach $file (sort @inclFiles) {
	    $build .= "Click here to publish \<a href\=$buildPagesScript?page\=$file\&extraDir\=staging\&locale\=$FORM{'site'}\&action\=build target=print onClick\=\"printPopup(\'$file\',\'print\',\'resizable\=yes,toolbar\=yes,scrollbars\=yes,menubar\=yes,width\=510,height\=400\')\"\>\<b\>$file\<\/b\>\<\/a\>\<br\>";
	}
	
	$build .= "\<p\>Press each link, one at a time to build each of the pages that uses the include file.<p>";
	
    } else {
	
	$build = "Click here to publish \<a href\=$buildPagesScript?page\=$FORM{'file'}\&extraDir\=staging\&locale\=$FORM{'site'}\&action\=build target=print onClick\=\"printPopup(\'$popupPage\',\'print\',\'resizable\=yes,toolbar\=yes,scrollbars\=yes,menubar\=yes,width\=510,height\=400\')\"\>\<b\>$FORM{'file'}\<\/b\>\<\/a\>\<p\>";
	
    }
    
    $menu = "";
    
    print <<EndofHTML;
Content-type: text/html


<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	<title>Publish Saved Page</title>

	<!-- javascript begin -->
	<SCRIPT LANGUAGE="JavaScript">
	<!--
	// Article Printing JavaScript Popup Function -- Begin

	// This overides the window.open which breaks when used in a "Javascript:" line
	// in Netscape 3.
	function printPopup( szWindowURL, szWindowName, szWindowAttributes )
	{
		wndPopup = window.open(szWindowURL, szWindowName, szWindowAttributes);
	}

	// Article Printing JavaScript Popup Function -- End
	// -->
	</SCRIPT>

	<!-- javascript end -->

	</head>
	<body>

	<h1>$siteName ~ $siteName{$FORM{'site'}}</h1>
	<h2>Publish Saved Page ~ $FORM{'file'} </h2>
	<a href=editPages.html>help</a> | <a href=$thisScript>edit different page</a><p>

	Nothing will happen to the live site if you do not select the link below.  You can go back and edit this page some more, but all your previous changes have been saved to the staging server.  If you made a mistake, do not press this link, email <a href="mailto:peter\@mahnke.net">Peter Mahnke</a>.<p>

	$build

	<p>
	</body>
	</html>

EndofHTML
	exit;



} # end sub printSavePage


sub autoBuildAll {

	&readDir($siteDir);
	&readDir($dir{$locale{$FORM{'site'}}});

	foreach $file (sort keys %buildFileList) {

	    $URL = "http://localhost/staging/$buildPagesScript?page\=$file\&extraDir\=staging\&locale\=$FORM{'site'}\&action\=build";
	    $output .= &Connection($URL);
	    
	}
	
	print <<EndofHTML;
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head></head>
	<body>

	$output

	</body>
	</html>

	EndofHTML

}

#######################################################################
sub printBuildAllPage {

    &readDir($siteDir);
    &readDir($dir{$locale{$FORM{'site'}}});
    &readDir($dir{$locale{$locale{$FORM{'site'}}}});
    
    foreach $file (sort keys %buildFileList) {
	
	$buildFileList .= "\<a href\=$buildPagesScript?page\=$file\&extraDir\=staging\&locale\=$FORM{'site'}\&action\=build target=print onClick\=\"printPopup(\'$file\',\'print\',\'resizable\=yes,toolbar\=yes,scrollbars\=yes,menubar\=yes,width\=510,height\=400\')\"\>\<b\>$file\<\/b\>\<\/a\>\<br\>";
	
    }

    print <<EndofHTML;
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	<title>Edit Page</title>

	<!-- javascript begin -->
	<SCRIPT LANGUAGE="JavaScript">
	<!--
	// Article Printing JavaScript Popup Function -- Begin

	// This overides the window.open which breaks when used in a "Javascript:" line
	// in Netscape 3.
	function printPopup( szWindowURL, szWindowName, szWindowAttributes )
	{
		wndPopup = window.open(szWindowURL, szWindowName, szWindowAttributes);
	}

	// Article Printing JavaScript Popup Function -- End
	// -->
	</SCRIPT>

	<!-- javascript end -->

	</head>
	<body>
	<form method=post action=$thisScript>

	<h1>$siteName ~ $siteName{$FORM{'site'}}</h1>

	<h2>Click to publish</h2>

	<!-- from sitedir $siteDir<p>
	dirlocaleformsite $dir{'memea'} $dir{$locale{$FORM{'site'}}} <p> $FORM{'site'}<p>
	$locale{$FORM{'site'}} -->


	$buildFileList

	<p>
	</body>
	</html>


EndofHTML

	exit;

}


#######################################################################
#
sub printEditPage {

	local $review = "";
	local $file   = "";
	
	if ($FORM{'file'} =~ /.incl/) {
	    
	    # if its an include file, you can't build the normal page
	    @inclFiles = &grepDir($FORM{'file'});

	    $review .= "<p\>This include file (\<b\>$FORM{'file'}\<\/b\>) affects the following pages:\<p\>";
	    
	    foreach $file (sort @inclFiles) {
		$review .= "\<li\> \<b\>$file\<\/b\>\<br\>";
		# for show $review .= "\<li\> <a href\=\"\"\>\<b\>$file\<\/b\><\/a\>\<br\>";
	    }
	    $review .= "\<p\>You can not preview the page before you save it, so when you are sure of the changes, press the \<b\>Save\<\/b\> button and build these pages.\<p\>";
	    $cType = "<font color\=navy\>Content Component<\/font\>";
	    
	} else {
	    
	    $review = "| \<a href\=$buildPagesScript?page\=$locale$FORM{'file'}.temp\&locale\=$FORM{'site'}\&extraDir\=staging target\=print onClick\=\"printPopup(\'$buildPagesScript\?page\=$FORM{'file'}.temp\&locale\=$FORM{'site'}\&extraDir\=staging\',\'print\',\'resizable\=yes,toolbar\=yes,scrollbars\=yes,menubar\=yes,width\=510,height\=400\'\)\"\>preview this page\<\/a\>\<br\>";
	    
	    #	$review = "\<a href\=$buildPagesScript?page\=$file.temp\&locale\=$FORM{'site'}\&extraDir\=staging target\=print onClick\=\"printPopup(\'$buildPagesScript\?page\=$FORM{'file'}.temp\&locale\=$FORM{'site'}\&extraDir\=staging\',\'print\',\'resizable\=yes,toolbar\=yes,scrollbars\=yes,menubar\=yes,width\=510,height\=400\'\)\"\>Click here to see the page as it is...\<\/a\>\<p\>";
	    
	    #$buildPagesScript?page\=$file\&extraDir\=staging\&locale\=$FORM{'site'}\&action\=build target=print onClick\=\"printPopup(\'$file\',\'print\',\'resizable\=yes,toolbar\=yes,scrollbars\=yes,menubar\=yes,width\=510,height\=400\')\"\>\<b\>$file\<\/b\>\<\/a\>\<br\>";
	    $cType = "<font color\=red\>Template Page<\/font\>";
	}

	# print the HTML page
	print <<EndofHTML;
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	<title>Edit Page</title>

	<!-- javascript begin -->
	<SCRIPT LANGUAGE="JavaScript">
	<!--
	// Article Printing JavaScript Popup Function -- Begin

	// This overides the window.open which breaks when used in a "Javascript:" line
	// in Netscape 3.
	function printPopup( szWindowURL, szWindowName, szWindowAttributes )
	{
		wndPopup = window.open(szWindowURL, szWindowName, szWindowAttributes);
	}

	// Article Printing JavaScript Popup Function -- End
	// -->
	</SCRIPT>

	<!-- javascript end -->

	</head>
	<body>
	<form method=post action=$thisScript>

	<h1>$siteName ~ $siteName{$FORM{'site'}}</h1>

	<h2>Edit $cType  ~ $FORM{'file'} </h2>
	<a href=editPages.html>help</a> | <a href=$thisScript>edit different page</a>

	$review

	<textarea name="text" ROWS=20 COLS=80 wrap>
	$page
	</TEXTAREA><p>

	<input type=hidden name=site value="$FORM{'site'}">
	<input type=hidden name=file value="$FORM{'file'}">
	<input type=submit name=page value=review>
	<input type=submit name=page value=save>

	<p>
	Some instructions<p>
	<li> <b>&lt;br></b> means break, it is a single line carriage return<br>
	<li> <b>&lt;p></b> means paragraph, it is a double line carriage return<br>
	<li> <b>&lt;b></b> means bold and <li> <b>&lt;/b></b> means end bold<br>
	<li> <b>&lt;i></b> means italics <b>&lt;/i></b> means end italics  <br>
	<li> <b>&lt;!--</b> starts to comment out a section of text that you want to hide and the <b>--></b> ends the comment<br>
	<li> <b>&amp;nbsp;</b> adds a space character<p>


	<p>
	</form>
	</body>
	</html>

EndofHTML
	exit;



} # end sub printEditPage

#######################################################################
#
sub readPage {

	open (PAGE, "$rootDir$inputDir$siteDir$_[0]") ||
	die "readPage: can't open: $_[0]";

	$FORM{'text'} = "";

	while (<PAGE>) {
		s/\&/\&amp\;/g; # turn ampersans into html tag
		s/\</\&lt\;/g; # turn less thans into html tag
		s/\r\n\r\n/\n/g;
		s/\r\n/\n/g;
		$FORM{'text'} .= $_;
	}
	close (PAGE);

	return ($FORM{'text'});

} # end sub readPage


#######################################################################
#
sub printDirectoryMenu {

	print <<EndofHTML;
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	<title>Select a Page</title>
	</head>
	<body>
	<form method=post action=$thisScript>

	<h1>$siteName</h1>

	<h2>Select a Site to Edit</h2>
	<a href=editPages.html>help</a><p>

	<select name=site>
	$FORMdir
	</select><p>
	<input type=submit name=page value=site>

	<p>
	</form>
	</body>
	</html>

EndofHTML

	exit;


}

#######################################################################
#
sub printFirstPage {

	local @files = &readDir($siteDir);
	local ($file, $template, $content) = "";


	foreach $file (sort @files) {
		$template .= "<tr\><td\>\<input type\=radio name\=file value\=$file\><\/td\><td\>$file<\/td\><td\><font color\=red\>template<\/font\><\/td\><\/tr\>\n" if ($file =~ /htm/);
		$content .= "<tr\><td\>\<input type\=radio name\=file value\=$file\><\/td\><td\>$file<\/td\><td\><font color\=navy\>content component<\/font\><\/td\><\/tr\>\n" if ($file =~ /incl/);
		$allFiles .= "file\=$file\&" if ($file =~ /htm/);
	}

	$listing = "$template"."$content";

	print <<EndofHTML;
Content-type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
	<html>
	<head>
	<title>Select a Page</title>
	</head>
	<body>
	<form method=post action=$thisScript>

	<input type=hidden name=site value="$FORM{'site'}">

	<h1>$siteName  ~ $siteName{$FORM{'site'}}</h1>

	<h2>Select a Page to Edit</h2>

	<input type=submit name=page value=edit>
	<input type=submit name=page value="build all">
	<input type=submit name=page value="auto build all"><p>

	<table>
	$listing
	</table>

	<input type=submit name=page value=edit>
	<p>
	<a href=editPages.html>help</a><p>
	</form>
	</body>
	</html>

EndofHTML

	exit;

} # end sub printFirstPage

#######################################################################
#
sub grepDir {

	# $siteDir = $dir{$FORM{'site'}};

	# $fileMask = "$rootDir$inputDir$siteDir"."*.html"; # only html files
	# $grep = `$CMDgrep -l -s $_[0] $fileMask`;
	# $grep =~ s/$rootDir$inputDir$siteDir//g;
	# local @file = split ("\n", $grep);
	# return(@file);


	local $file       = "";
	$curDir           = "";
	local $file       = "";

	# LEVEL 0
	# found file in current locale

	$fileMask = "$rootDir$inputDir$dir{$FORM{'site'}}"."*.html";
	$grep = `$CMDgrep -l -s $_[0] $fileMask`;

	$msg = "$rootDir$inputDir$dir{$FORM{'site'}}";

	if ($grep) {
		$grep =~ s/$rootDir$inputDir$dir{$FORM{'site'}}//g;
		local @file = split ("\n", $grep);
		return(@file);
	}

	# file doesn't exist even at the top level
	# return (0)    if ($COOKIE{'locale'} eq "wcw");

	# LEVEL 1
	# look for file up one level

	$fileMask = "$rootDir$inputDir$dir{$locale{$FORM{'site'}}}"."*.html";
	$grep = `$CMDgrep -l -s $_[0] $fileMask`;

	if ($grep) {
		$grep =~ s/$rootDir$inputDir$dir{$locale{$FORM{'site'}}}//g;
		local @file = split ("\n", $grep);
		return(@file);
	}

	# if is doesn't fail if at top level
	#return (0)    if ($locale{$COOKIE{'locale'}} eq "wcw");


	# LEVEL 2
	# look for file up one more level

	$fileMask = "$rootDir$inputDir$dir{$locale{$locale{$FORM{'site'}}}}"."*.html";
	$grep = `$CMDgrep -l -s $_[0] $fileMask`;

	if ($grep) {
		$grep =~ s/$rootDir$inputDir$dir{$locale{$locale{$FORM{'site'}}}}//g;
		local @file = split ("\n", $grep);
		return(@file);
	}


	# if is doesn't fail if at top level
	# probably affects all HTML pages

	$fileMask  = "$rootDir$inputDir$dir{$FORM{'site'}}"."*.html";
	$grep      = `$CMDls -1 $fileMask`;
	$grep      =~ s/$rootDir$inputDir$dir{$FORM{'site'}}//g;

	$fileMask  = "$rootDir$inputDir$dir{$locale{$FORM{'site'}}}"."*.html";
	$grep     .= `$CMDls -1 $fileMask`;
	$grep      =~ s/$rootDir$inputDir$dir{$locale{$FORM{'site'}}}//g;


	# $fileMask  = "$rootDir$inputDir$dir{$locale{$locale{$FORM{'site'}}}}"."*.html";
	# $grep     .= `$CMDls -1 $fileMask`;
	# $grep      =~ s/$rootDir$inputDir$dir{$locale{$locale{$FORM{'site'}}}}//g;


	local @file = split ("\n", $grep);


	return (@file);

}





#######################################################################
#
sub readDir {

	# read inputDir's files

	local $dir = "$rootDir$inputDir$_[0]";

	opendir (DIR, "$dir") || die "Can't open DIR: $dir\n";
	local @files = readdir (DIR);
	closedir (DIR);

	splice @files, 0, 2;  # remove . and .. listings

	# parse out non-editable files
	local $file = "";
	local $fileList = "";

	foreach $file (@files) {

		next if (-d $file);  # next if its a directory

		if ($file =~ /.html$/ || $file =~ /.incl$/ || $file =~ /.htm$/) {
			push @fileList, $file;
			$buildFileList{$file} = $file  if ($file =~ /.html$/ || $file =~ /.htm$/);
		}

	}
	return (@fileList);

} # end sub readDir


#######################################################################
sub saveTempFile {

	local $tempName = "$rootDir$inputDir$siteDir$_[0]";

	open (TEMP, ">$tempName") ||
	die "Can't open TempFile: $tempName\n";
	print TEMP $FORM{'text'};
	close (TEMP);

	return;


} # end sub saveTempFile

#######################################################################

sub readLocaleInfo {

	open (LOCALE, "$localeDB") || die "Can't open locale db: $localeDB\n";

	while (<LOCALE>) {

		chop();

		# example EMEA|emea|en-uk|wcw|emea/
		# format  Long Name|key name|language|above locale|rel dir

		local @listing = split (/\|/);

		$siteName{$listing[1]}= "$listing[0]";
		$locale{$listing[1]}  = "$listing[3]";
		$dir{$listing[1]}     = "$listing[4]";
		$lang{$listing[1]}    = "$listing[2]";

		$FORMdir .= "      \<option value\=\"$listing[1]\">\ $listing[0]\n";

	}

	close (LOCALE);

}

sub Connection {

	local $Output = "";

	# Create a user agent object
	use LWP::UserAgent;
	my $ua = new LWP::UserAgent;
	$ua->agent("Mozilla/5.0");

	# Create a request
	my $req = new HTTP::Request('GET', $_[0]);

	# authentication
$req->authorization_basic('peter', 'hi11top');

	# Pass request to user agent and get response
	my $res = $ua->request($req);

	$Output = $res->content;

	# Check output
	if ($res->is_success) {
		return($Output);
	} else {
		return($Output, $_[0]); # return error info and url attempted
	}


}			# end of sub Connection

