#!/usr/local/bin/perl


########################################################################
#
# pickResearch.cgi
#
#   written:  15 Dec 2003 by Peter Mahnke
#   modified: 15 Jan 2004 by Peter Mahnke
#              - added ability to add local research and translated titles
#             22 Jan 2004 by Peter Mahnke
#              - turned on FTP to campsqa of news and research
#              - added instructions and cleaned up UI a little
#             12 Feb 2004 by Peter Mahnke
#              - added choice of servers to upload to via site parameter (prod, qa)
#              2 Jul 2005 by Peter Mahnke
#              - reduced it to 4 notes only for new 15 July 2005 g.com redesign
#
#
#   run from a web browser
#   currently only called through update_menu.cgi
#
#
#   DESCRIPTION
#
#     allows regional site editors to pick News,Research and
#     update Focal Points from a single page and output them into
#     all the major output formats required for the regional sites
#
#     namely: html, xhtml, mailing formats, exp formats and rss
#
#     for news and research it takes in doc ids or resids and logs them
#     per locale, for focal points you input the text and relative file
#     and uri information into a form, it also logs the data
#
#     when the form is submitted, the application looks up the document
#     details for the documents, updates the focal points as required
#     and outputs all the includes again into the /rt/content/<LOCALE>/
#     directory strcuture.  the lookup will first see if the information
#     is in the local DETAIL cache, if not, it will go to g.com
#
#     CODES
#     codes are saved in a text log file called NEWS.codes or FR.codes
#
#     DETAIL
#     document detail is stored in a text file called NEWS.detail or
#     FT.detail with the translated information
#
#     FTP
#     the html includes are saved on the local server and then FTPed up
#     campsqa.gartner.com.  a remote backup of the previous file is stored
#     as <filename>.old
#
#     currently only FTPing news and research
#
#
#
########################################################################

use lib '/usr/local/lib/perl5/site_perl/5.6.1/';
use CGI_Lite;
require ("/home/gartner/cgi-bin/gNOlogin.pl");
require ("/home/gartner/html/rt/getNODocument3.pl");
require ("/home/gartner/html/rt/common.pl");
require ("/home/gartner/html/rt/commonDoccodes.pl");
require ("/home/gartner/html/rt/commonTransDoc.pl");
require ("/home/gartner/html/rt/replaceChars.pl");
require ("/home/gartner/html/rt/SmartyPants.pl");



##############################################################
# Variables
local $server  = "www";
local $ftpSite = "hibachi.gartner.com";
$date          = `date +'%a, %d %b %Y %T GMT'`;
$yyyymmdd      = `date +'%Y%m%d'`;
chop($date);
chop($yyyymmdd);
local $thisScript = "http://intl.gartner.com/rt/pickResearch2.cgi";

local $menu =<<EOF;
<p class="footer">menu: edit [<a href="$thisScript?locale=emea&page=update">emea</a> | <a href="$thisScript?locale=it&page=update">it</a> | <a href="$thisScript?locale=de&page=update">de</a>]<p>

EOF

##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    # something submitted
    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;

    $ftpSite = "campsqa.gartner.com" if ($FORM{'site'} =~ /qa/i);

	# set default limit if not passed
	$FORM{'limit'} = 3 if (!$FORM{'limit'});

} else {

	$FORM{'locale'} = "emea";
	&printInitialForm;
	exit;

}



#########################################################
# process the input

if ($FORM{'page'} eq "update") {
    &printInitialForm;
    exit;
}



#################################################
# process research changes
undef @docs;
undef $xhtml;
undef $view;

$processFlag = "research";

$detailFlag = "FR";

if (!$FORM{'frcode1'}) {
    $FORM{'frcode1'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'frcode1'}, $FORM{'frhl1'}, $FORM{'fruri1'} );



if (!$FORM{'frcode2'}) {
    $FORM{'frcode2'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'frcode2'}, $FORM{'frhl2'}, $FORM{'fruri2'} );



if (!$FORM{'frcode3'} && $FORM{'frhl3'}) {
    $FORM{'frcode3'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'frcode3'}, $FORM{'frhl3'}, $FORM{'fruri3'} ) if ($FORM{'limit'} > 2); # if ($FORM{'frhl3'});



if (!$FORM{'frcode4'} && $FORM{'frhl4'}) {
    $FORM{'frcode4'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'frcode4'}, $FORM{'frhl4'}, $FORM{'fruri4'} ) if ($FORM{'limit'} > 3); # if ($FORM{'frhl4'});




$FORM{'research'} = "$FORM{'frcode1'} $FORM{'frcode2'} $FORM{'frcode3'} $FORM{'frcode4'}";


if ($FORM{'research'} ne $FORM{'origResearch'}) {
    &writeCodes('FR', $FORM{'locale'}, $FORM{'research'});
}

$research = $htmlFR;



&saveOutput;

&printOutput;
exit;


####################################################################
sub getDoc {

    $msg .= "in getDoc $_[0], $_[1], $_[2] <br>";

    ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price) = "";

    if (!$flagNew) {

        # see if detail in detail database first
        ($resId, $title, $link, $pubDate, $summary, $auth) = &readDetail($detailFlag, $FORM{'locale'}, $_[0]);

        if (!$title) {

            # not in detail list, so get from gartner.com

            $_[0] =~ s/ //g; # strip spaces


            $docCode = "\/DisplayDocument\?id\="."$_[0]";
            $link = "http:\/\/www4.gartner.com"."$docCode";  # .\&acsFlg\=accessBought";
            ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price)
		= &getResearchDetail($link,$server);

            # didn't get title with resid, try doc id
            if (!$title) {
	        $docCode = "\/DisplayDocument\?doc_cd\="."$_[0]";
	        $link = "http:\/\/www4.gartner.com"."$docCode"; # ."\&acsFlg\=accessBought";
	        ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price)
		    = &getResearchDetail($link,$server);
            }

            #add proper attributes to links
            $link =~ s/uid=Y&fRef=true/call=email&amp\;ref=g_emalert/;




        }


    } else {
    	$resId = $_[0];
    }

    # rewrite title if passed
    if ($_[1]) {
		$title = $_[1];
		$title = &replaceCharacters($title);
		$msg .= "replaceChars: $title<br>";
    }


    # rewrite link if passed
   if ($_[2]) {
	$link    = $_[2];
	$docCode =  $link;
	$docCode =~ s/http:\/\/www.gartner.com//;
	$docCode =~ s/http:\/\/www3.gartner.com//g;
	$docCode =~ s/http:\/\/www4.gartner.com//g;

	$docCode =~ s/&call=email&ref=g_emalert//;
    }




    # write document information to detail database, this will check if already in.
    &writeDetail($detailFlag, $FORM{'locale'}, $resId, $title, $link, $pubDate, $summary, $auth);



    # create date if missing
    if (!$pubDate) {

        $dateStr = `date +'%a, %d %b %Y %T GMT'`;
        chop($dateStr);

    } else {

        # put dates into proper RSS 2.0 format
        use DateTime::Format::HTTP;
        my $dt = 'DateTime::Format::HTTP';
        #$datestring = $dt->parse_datetime($pubDate, 'GMT');
        #$dateStr = $dt->format_datetime($datestring);

    }

    # clean up title
    $title =~ s/EMEA/Europe, Middle East and Africa/g;
    $title =~ s/ \(Executive Summary\)//g;

    # do the no hanging word logic on $title
    # $noHangTitle = &noHang($title, 50);
    $noHangTitle = $title; # removed by PRM on 22 July 2005, seems to not be required
    $noHangTitle =~ s/\& /\&amp\; /g;

    # copy of $title without <br />
    $origTitle = $title;

    # turn & into &amp;
    $title   =~ s/\& /\&amp\; /g;
    $summary =~ s/\& /\&amp\; /g;


    # clean up author
    #$auth =~ s/,//g; # convert , to a space - for mailing format
    chop ($auth) if ($auth =~ /,$/);
    # clean up $pubDate
    $pubDate =~ s/\-/ /g;
    $pubDate =~ s/^0//;
    $pubDate =~ s/Jan/January/;
    $pubDate =~ s/Feb/February/;
    $pubDate =~ s/Mar/March/ if ($pubDate !~ /March/);
    $pubDate =~ s/Apr/April/ if ($pubDate !~ /April/);
    $pubDate =~ s/Jun/June/  if ($pubDate !~ /June/);
    $pubDate =~ s/Jul/July/  if ($pubDate !~ /July/);
    $pubDate =~ s/Aug/August/ if  ($pubDate !~ /August/);
    $pubDate =~ s/Sep/September/;
    $pubDate =~ s/Oct/October/;
    $pubDate =~ s/Nov/November/;
    $pubDate =~ s/Dec/December/;

    if ($processFlag eq "research") {

	# FEATURED RESEARCH HTML
	$htmlFR .=  <<EndofHTML;
<li><a href="$docCode" onclick="openResult('$docCode');return false;">$noHangTitle</a></li>
EndofHTML

    }



    $flagNew = 0;

}

####################################################################
sub saveOutput {


    #####################################################
    # save html versions
    local $fn = "/home/gartner/html/rt/content/";
    if ($FORM{'locale'} eq "emea") {
	$fn = "$fn"."emea/"."home_featured_research.incl";
    } else {
	$fn = "$fn"."emea/"."$FORM{'locale'}"."/home_featured_research.incl";
    }
    &saveFile($fn, $htmlFR);
    &FTPfile_good('home_featured_research.incl', $FORM{'locale'});



}

######################################################################
sub saveFile {

    open (OUT, ">$_[0]") || die "Can't write file: $_[0]\n\n";
    print OUT "<!-- created by pickResearch.cgi --\>\n\n" if ($_[0] !~ /rss/);
    print OUT $_[1];
    close (OUT);

}

####################################################################
sub printOutput {

    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>pickResearch.cgi - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt; clear:both;	}
h3	{		font-size: 10pt;	}
li,p,td	{		font-size: 9pt;	        }
/* HOMEPAGE CENTER COLUMN */

/* featured research */
.featuredresearchlist ul      {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;   }
.featuredresearchlist li      {  list-style-type: none; color: #3088CC; line-height: 110%; padding: 3px;  }
.featuredresearchlist a       {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #3088CC; text-decoration: none; line-height: 110%;  }
.featuredresearchlist a:hover {  text-decoration: underline;  }

.msg {  font-size: .75em; font-family: courier, fixed; color: 333; border: 1px dashed navy; padding: 10px; margin: 10px;  }

.menu { font-size: 8pt; border 1px solid navy; }

</style>

</head>
</head>
<body>
<h1>Output - $FORM{'locale'}</h1>

<h2>Featured Research</h2>
<div class="featuredresearchlist">
<ul>
$research
</ul>
</div>


<h2>Messages</h2>
<p class="msg">$msg</p>
<p class="msg">$ftpmsg</p>

$menu

</body>
</html>

EndofHTML

}







####################################################################
sub readFile {

    open (FILE, "$_[0]") || die "can't open file to read: $_[0]\n";
    local $f;
    while (<FILE>) {
	$f .= $_;
    }
    close (FILE);
    return($f);
}

####################################################################
sub printInitialForm {

	local $research = &readCodes('FR', $FORM{'locale'});

	# get existing RESEARCH for listing
	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/"."home_featured_research\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/home_featured_research\.incl";
	}
	$curFR = &readFile($fn);



	if ($FORM{'locale'} ne "emea") {

	    # add emea news/research option
	    # allows user to override current locale offering with emea's

	    $emearesearch = &readCodes('FR', 'emea');

	    # javascript link to call function that does work
	    $useEmeaResearch = "<li\><a href\=\"javascript:void\(null\)\;\" onclick\=\"javascript:moveresearch\(\)\;return false\;\"\>use EMEA Research<\/a\> [ $emearesearch ]<\/li\>\n";

	}


	$research =~ s/  / /g;
	@checkFR = split (/ /, $research);
	undef $c;
	foreach $cd (@checkFR) {
		$c++;
		($FORM{'frcode'.$c}, $FORM{'frhl'.$c}, $FORM{'fruri'.$c}, $pubDate, $summary, $author) = &readDetail('FR', $FORM{'locale'}, $cd);
		$FORM{'frcode'.$c} = $cd;
	}

	# bring in EMEA research
 	$emearesearch =~ s/  / /g;
	@emeaFR = split (/ /, $emearesearch);



	# add Research form for translated research
	$addFRForm =<<EOF;
            <ul>
              <li> <a href="javascript:void(null);" onclick="javascript:movefrdown();return false;">move fr down</a>
              <li> <input type="text" name="frcode1" value="$FORM{'frcode1'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl1" size="80" value="$FORM{'frhl1'}" /> </li>
                     <li> link: <input type="text" size="80" name="fruri1" value="$FORM{'fruri1'}" /></li>
                   </ul>
              <li> <input type="text" name="frcode2" value="$FORM{'frcode2'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl2" size="80" value="$FORM{'frhl2'}" /> </li>
                     <li> link: <input type="text" size="80" name="fruri2" value="$FORM{'fruri2'}" /></li>
                   </ul>
              <li> <input type="text" name="frcode3" value="$FORM{'frcode3'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl3" size="80" value="$FORM{'frhl3'}" /> </li>
                     <li> link: <input type="text" name="fruri3" size="80" value="$FORM{'fruri3'}" /></li>
                   </ul>
              <li> <input type="text" name="frcode4" value="$FORM{'frcode4'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl4" size="80" value="$FORM{'frhl4'}" /> </li>
                     <li> link: <input type="text" name="fruri4" size="80" value="$FORM{'fruri4'}" /></li>
                   </ul>
            </ul>
            <input type="hidden" name="fremea1" value="$emeaFR[0]" />
            <input type="hidden" name="fremea2" value="$emeaFR[1]" />
            <input type="hidden" name="fremea3" value="$emeaFR[2]" />
            <input type="hidden" name="fremea4" value="$emeaFR[3]" />

EOF


    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>pickResearch.cgi - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1                  {	font-size: 14pt;  }
h2                  {   font-size: 12pt;  }
h3                  {	font-size: 10pt; }
li,p,td	            {	font-size: 9pt;  }

/* featured research */
.featuredresearchlist ul      {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;
                                 border: 1px dashed #fff;  }
.featuredresearchlist li      {  list-style-type: none;
                                 color: #3088CC; line-height: 110%; padding: 3px;  }
.featuredresearchlist a       {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold;
                                 font-size: 11px; color: #3088CC; text-decoration: none;
                                 line-height: 110%;  }
.featuredresearchlist a:hover {  text-decoration: underline;  }

.msg {  font-size: .75em; font-family: courier, fixed; color: 333; border: 1px dashed navy; padding: 10px; margin: 10px;  }

</style>
<script type="text/javascript" language="javascript">

function moveresearch() {
    document.form.frcode4.value = document.form.fremea4.value;
    document.form.frcode3.value = document.form.fremea3.value;
    document.form.frcode2.value = document.form.fremea2.value;
    document.form.frcode1.value = document.form.fremea1.value;

    document.form.fruri4.value = "";
    document.form.fruri3.value = "";
    document.form.fruri2.value = "";
    document.form.fruri1.value = "";

    document.form.frhl4.value = "";
    document.form.frhl3.value = "";
    document.form.frhl2.value = "";
    document.form.frhl1.value = "";

}


function movefrdown() {

    document.form.frhl4.value = document.form.frhl3.value;
    document.form.frhl3.value = document.form.frhl2.value;
    document.form.frhl2.value = document.form.frhl1.value;
    document.form.frhl1.value = "";


    document.form.fruri4.value = document.form.fruri3.value;
    document.form.fruri3.value = document.form.fruri2.value;
    document.form.fruri2.value = document.form.fruri1.value;
    document.form.fruri1.value = "";

    document.form.frcode4.value = document.form.frcode3.value;
    document.form.frcode3.value = document.form.frcode2.value;
    document.form.frcode2.value = document.form.frcode1.value;
    document.form.frcode1.value = "";


}

</script>
</head>
</head>
<body>
<form action="$thisScript" name="form" method="post">

    <input type="hidden" name="locale" value="$FORM{'locale'}" />
    <input type="hidden" name="origFR" value="$research" />
    <input type="hidden" name="emeaResearch" value="$emearesearch" />
    <input type="hidden" name="yyyymmdd" value="$yyyymmdd" />

<h1>Pick Research &amp; Focal Points - $FORM{'locale'}</h1>


<h2>Research</h2>

<p>Maximum Number of Research on Homepage: <input type="text" name="limit" value="3" size="5" /><br /><em>you can have up to 4 in list, but it will drop 4th as required...</em></p>

<ul><li>Resid or Doc Codes:</li>
  <ul>
    <li>current research [ $research ]</li>
    $useEmeaResearch
    $addFRForm
  </ul>
</ul>

<ul class="featuredresearchlist">
$curFR
</ul>

server: <input type="radio" name="site" value="prod" checked="checked" /> production <input type="radio" name="site" value="qa" /> qa

<input type="submit">

<h2>Instructions</h3>
<div class="msg">
<p>These forms allow you to update the news, research and focal points on the regional websites</p>
<ul>
  <li> <strong>News &amp; Research</strong></li>
  <ul>

    <li>  For research you can enter the resid or doccode of the g.com document you want to add or promote.</li>
    <ol>
      <li> When you hit submit, it will try to look up the document in its on db of document.</li>
      <li> If it can't find it, it will query g.com for the informaton.</li>
      <li> If it finds the information in its own database, it will use that information.
      <li> So if you have added an alternate/translated title or link, it will use that instead.</li>
      <li> Obviously, if it goes to g.com, it will be in english.</li>
    </ol>
    <li> <strong>Translation</strong></li>
    <ul>
      <li> <strong>Translate Title Only</strong>: you must have the g.com resid or doccode and then simply paste in the translated text into the corresponsing <u>title</u> field.</li>
      <li> <strong>Add Non-Gartner Research</strong>: you must leave the resid field <strong>blank</strong> and add both a <u>title</u> and <u>link</u></li>
    </ul>

    <li>  <u>move news down</u> or <u>move fr down</u> litterally moves all news/research down one set of fields, allowing you to add as many new items as you need.  <i>This is important to do instead of just replacing the resid/doccodes as it will replace the title and links with the old information.</i></li>

    <li> On locales other than emea, you have a option, <u>use EMEA news/research</u>.  This will simply copy all of the emea codes over the locale's.</li>
    <ul>
      <li>If you only want to move one or two in, then use the <u>move news/fr down</u> link and copy the resids from the list next to <u>use emea news/research</u></li>
    </ul>

  </ul>

</ul>


</div>


$menu

</form>
</body>
</html>

EndofHTML


}



sub dateCode {

	# counter to make sure its unique
	$dcCounter++;

	local $ds = `date +'%Y%m%d%S'`;
	chop($ds);
	$ds = "$ds"."$dcCounter";
	return($ds);

}

sub OLDreplaceChars {

    $listFile = "/home/gartner/html/rt/accent_list.txt"; #"c:/bin/accent_list.txt.utf8";

    &openList();

    local $word = $_[0];

    $word =~ s/’/'/g;# in accent list as &acute;, but not working

    foreach $letter (@list) {
	if (/$letter/) {
	    $word =~ s/$letter/$replace{$letter}/g;
	}
    }

    return($word);

}




sub FTPfile_good {

    # ftp files to remote servers
    # take 2 args
    # 1. filename
    # 2. relative path from emea/
    # 3. remote filename (<optional> for xhtml)

    use Net::FTP;


    local $locale = $_[1];
    $locale = "" if ($_[1] =~ /emea/);

   chdir("/home/gartner/html/rt/content/emea/$locale/");

    local $remoteFullPath  = "regionalization/templates/emea/$locale/";

    local $localFile = $_[0];

    local $remoteFile = $_[0];
    $remoteFile = $_[2]  if ($_[2]);

    local $saveFile = "$remoteFile"."\.old";


    $ftpmsg .= "<strong>FTP MESSAGES</strong><br />\n$ftpSite<br />\n\n";

    $ftp = Net::FTP->new($ftpSite)
	or $ftpmsg .= "Can't start FTP session<br>\n";
    $ftp->login("pmahnke","hi11top")#$ftp->login("ismith","spur33")
	or $ftpmsg .= "Can't login into FTP session<br>\n";
    $ftp->cwd($remoteFullPath)
        or $ftpmsg .= "Can't change directory on remove server: $remoteFullPath<br>\n";
    $ftp->type('I')
	or $ftpmsg .= "Can't change to ascii mode<br>\n";
    $ftp->rename($remoteFile, $saveFile)
	or $ftpmsg .= "Can't rename file: $locale/$remoteFile to $saveFile<br>\n";
    $ftp->put($localFile,$remoteFile)
	or $ftpmsg .= "Can't PUT file: $locale/$remoteFile<br>\n";
    $ftp->quit();

    $ftpmsg .= "Going to put<br /> $localFile to $remoteFullPath$remoteFile<br /><br />\n\n";

}
