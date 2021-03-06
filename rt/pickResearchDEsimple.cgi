#!/usr/local/bin/perl


# TO DO - don't overwrite in FPde.csv
#       - write keys to FR.codes


########################################################################
#
# pickResearchDEsimple.cgi

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
local $server  = "www4";
local $ftpSite = "hibachi.gartner.com";
local $germanMetaDataFile = "/home/gartner/html/deDocs/docs/metaDataIndex.db";
$date          = `date +'%a, %d %b %Y %T GMT'`;
$yyyymmdd      = `date +'%Y%m%d'`;
chop($date);
chop($yyyymmdd);
local $thisScript = "http://intl.gartner.com/rt/pickResearchDEsimple.cgi";
local $otherScript = "http://intl.gartner.com/rt/pickResearch.cgi";

local $menu =<<EOF;
<p class="footer">menu: edit [<a href="$otherScript?locale=emea&page=update">emea</a> | <a href="$otherScript?locale=it&page=update">it</a> | <a href="$thisScript?locale=de&page=update">de</a>]<p>

EOF

##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    # something submitted
    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;

    $ftpSite = "campsqa.gartner.com" if ($FORM{'site'} =~ /qa/i);

} else {

	$FORM{'locale'} = "de";
	&printInitialForm;
	exit;

}

#########################################################
# process the input

if ($FORM{'page'} eq "update") {
   &printInitialForm;
    exit;
}


# incase it wasn't passed
$FORM{'locale'} = "de"; # if (!$FORM{'locale'});





#################################################
# process news changes
undef @docs;
undef $xhtml;
undef $view;

$processFlag = "news";
$detailFlag = "NEWS";

if (!$FORM{'newscode1'}) {
    $FORM{'newscode1'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'newscode1'}, $FORM{'newshl1'}, $FORM{'newsuri1'});
$msg .= "raw $FORM{'newscode1'}, $FORM{'newshl1'}, $FORM{'newsuri1'} <br>";



if (!$FORM{'newscode2'}) {
    $FORM{'newscode2'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'newscode2'}, $FORM{'newshl2'}, $FORM{'newsuri2'});



if (!$FORM{'newscode3'}) {
    $FORM{'newscode3'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'newscode3'}, $FORM{'newshl3'}, $FORM{'newsuri3'});



if (!$FORM{'newscode4'}) {
    $FORM{'newscode4'} = &dateCode;
    $flagNew = 1;
}
&getDoc($FORM{'newscode4'}, $FORM{'newshl4'}, $FORM{'newsuri4'});



$FORM{'news'} = "$FORM{'newscode1'} $FORM{'newscode2'} $FORM{'newscode3'} $FORM{'newscode4'}";


if ($FORM{'news'} ne $FORM{'origNews'}) {
    &writeCodes('NEWS', $FORM{'locale'}, $FORM{'news'});
}
$news = $view;

&printAllNews($FORM{'news'});


# process research

# research 1 & 2 are the fancy ones with the thumbnail...
if ($FORM{'resid1'} && !$FORM{'title1'} && !$FORM{'url1'} && !$FORM{'desc1'}) {
	&checkGermanResearch($FORM{'resid1'}, $FORM{'key1'});
	$plain .= &formatPlainLink($FORM{'key1'});
} else {
	$plain .= &formatPlainLink( '0', '1');
}
$fancy1 = &formatFancyLink('1');

if ($FORM{'resid2'} && !$FORM{'title2'} && !$FORM{'url2'} && !$FORM{'desc2'}) {
	&checkGermanResearch($FORM{'resid2'}, $FORM{'key2'});
	$plain .= &formatPlainLink($FORM{'key2'});
} else {
	$plain .= &formatPlainLink( '0', '2');
}
$fancy2 = &formatFancyLink('2');

# normal research
if ($FORM{'resid3'} && !$FORM{'title3'} && !$FORM{'url3'}){
	&checkGermanResearch($FORM{'resid3'}, $FORM{'key3'});
 	$plain .= &formatPlainLink($FORM{'key3'});
} else {
	$plain .= &formatPlainLink( '0', '3');
}

if ($FORM{'resid4'} && !$FORM{'title4'} && !$FORM{'url4'}) {
	&checkGermanResearch($FORM{'resid4'}, $FORM{'key4'});
	$plain .= &formatPlainLink($FORM{'key4'})
} else {
	$plain .= &formatPlainLink( '0', '4');
}

if (!$FORM{'resid5'} && !$FORM{'title5'} && !$FORM{'url5'}) {
    # nothing here then... so do nothing
    $FORM{'key5'} = "";
} elsif ($FORM{'resid5'} && !$FORM{'title5'} && !$FORM{'url5'}) {
	&checkGermanResearch($FORM{'resid5'}, $FORM{'key5'});
	$plain .= &formatPlainLink($FORM{'key5'})
} else {
	$plain .= &formatPlainLink( '0', '5');
}

if (!$FORM{'resid6'} && !$FORM{'title6'} && !$FORM{'url6'}) {
    # nothing here then... so do nothing
    $FORM{'key6'} = "";
} elsif ($FORM{'resid6'} && !$FORM{'title6'} && !$FORM{'url6'}) {
	&checkGermanResearch($FORM{'resid6'}, $FORM{'key6'});
	$plain .= &formatPlainLink($FORM{'key6'})
} else {
	$plain .= &formatPlainLink( '0', '6');
}

local $frCodes   = &readCodes('FRde', $FORM{'locale'});
local $codeList  = "$FORM{'key1'} $FORM{'key2'} $FORM{'key3'} $FORM{'key4'} $FORM{'key5'} $FORM{'key6'}";

$msg .= "codeList: $codeList;<br />\n";

&writeCodes('FRde', 'de', $codeList) if ($frCodes ne $codeList);


&saveDb;

&saveOutput;

&printOutput;

exit;





######################################################################
sub saveFile {

    open (OUT, ">$_[0]") || die "Can't write file: $_[0]\n\n";
    print OUT "<!-- created by pickResearchDEsimple.cgi --\>\n\n" if ($_[0] !~ /rss/);
    print OUT $_[1];
    close (OUT);

}


######################################################################
sub formatPlainLink {

	# inputs
	# 1 - resid
	# 2 - key#

	# FEATURED RESEARCH HTML

	local $htmlLink;

	if (!$_[1]) {

		$title{$_[0]} = &replaceCharacters($title{$_[0]});

		$htmlLink =  <<EndofHTML;
\n<!--start research  - $title{$_[0]} ID:$_[0] DATE:$date{$_[0]}  -->
    <tr><td width="356" height="8" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="8" alt="" border="0"></td></tr>
    <tr><td width="22" bgcolor="#FFFFFF" valign="top" align="center"><a href="javascript:void(null)" onclick="openResult('$url{$_[0]}')" class="smallBlueLink"><img src="//img/homepage/reversed_blue_arrow.gif" width="9" height="9" vspace="2" alt="$title{$_[0]}" border="0"></a></td>\n        <td width="328" valign="top" bgcolor="#FFFFFF"><a href="javascript:void(null)" onclick="openResult('$url{$_[0]}')" class="smallBlueLink">$title{$_[0]}</a></td>\n        <td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>\n    </tr>
<!--end research - $title{$_[0]} ID:$_[0] DATE:$date{$_[0]} -->\n
EndofHTML

		$xhtmlPlain .=  <<EndofHTML;
 <li> <a href="\#" onclick="openResult('$url{$_[0]}')">$title{$_[0]}</a></li>
EndofHTML

	} else {

		local $t = "title"."$_[1]";
		local $r = "resid"."$_[1]";
		local $d = "date"."$_[1]";
		local $u = "url"."$_[1]";

		$FORM{$t} = &replaceCharacters($FORM{$t});

		$msg .= "<br />plain linking $t and $FORM{$t}<br />\n";

		$htmlLink =  <<EndofHTML;
\n<!--start research  - $FORM{$t} ID:$_[0] DATE:$FORM{$d}  -->
    <tr><td width="356" height="8" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="8" alt="" border="0"></td></tr>
    <tr><td width="22" bgcolor="#FFFFFF" valign="top" align="center"><a href="javascript:void(null)" onclick="openResult('$FORM{$u}')" class="smallBlueLink"><img src="//img/homepage/reversed_blue_arrow.gif" width="9" height="9" vspace="2" alt="$FORM{$t}" border="0"></a></td>\n        <td width="328" valign="top" bgcolor="#FFFFFF"><a href="javascript:void(null)" onclick="openResult('$FORM{$u}')" class="smallBlueLink">$FORM{$t}</a></td>\n        <td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>\n    </tr>
<!--end research - $FORM{$t} ID:$_[0] DATE:$FORM{$d} -->\n
EndofHTML

		$xhtmlPlain .=  <<EndofHTML;
 <li> <a href="\#" onclick="openResult('$FORM{$u}')">$FORM{$t}</a></li>
EndofHTML

	}

	return ($htmlLink);

}

######################################################################
sub formatFancyLink {

	# SAVE FOCAL POINTS

    	# smarty pants the fps
    	$FORM{'title'.$_[0]} =  &replaceCharacters($FORM{'title'.$_[0]});
    	$FORM{'desc'.$_[0]}  =  &replaceCharacters($FORM{'desc'.$_[0]});

    	local $htmlLink = <<ENDofHTML;
<!-- start fancy link -->
<tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
<tr><td width="350" bgcolor="#FFFFFF" valign="top" colspan="2"><a href="javascript:void(null)" onclick="openResult('$FORM{'url'.$_[0]}')"><img src="$FORM{'img'.$_[0]}" width="100" height="68" hspace="6" align="left" alt="$FORM{'title'.$_[0]}" border="0"></a><table border="0" cellspacing="0" cellpadding="0"><tr><td><a href="javascript:void(null)" onclick="openResult('$FORM{'url'.$_[0]}')" class="largeBlueLink">$FORM{'title'.$_[0]}</a><br /><span class="smallGrayText">$FORM{'desc'.$_[0]}</span><br /></td></tr></table></td><td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td></tr>
<!-- end fancy link -->
ENDofHTML

	$xhtmlFancy[$_[0]] = <<ENDofHTML;
	<div class="focalpoint">
<a href="/regionalization/content/emea/$FORM{'url'.$_[0]}"><img src="$FORM{'img'.$_[0]}" width="100" height="68" alt="$title{$_[0]}" border="0" align="left" /></a>
<p><a href="/regionalization/content/emea/$FORM{'url'.$_[0]}">$FORM{'title'.$_[0]}</a></p>
<p>$FORM{'desc'.$_[0]}</p>
</div>
ENDofHTML


return ($htmlLink);

}


####################################################################
sub readDb {

    local $fileDetail = "/home/gartner/html/rt/content/emea/de/FRde.csv";
    local $store = "";

    open (FP, "$fileDetail") || die "Can't open File Detail to read: $fileDetail\n";

    while (<FP>) {

	    chop();

	    local ($key, $resid, $t, $desc, $u, $i, $d) = split (/\t/);
	    $msg .="<p>$_</p>\n";

	    # create store for all that aren't currently being looked at
	    $store .= "$_\n" if ($frCodes !~ /$key/ && $_[0] eq "read");

	    $msg .= "$frCodes match? $key<br />\n";

	    # skip if doesn't match key and LOOKING FOR A SPECIFIC KEY
	    next if ($_[0] !~ /$key/ && $_[0]); # skip if not in code list

	    $msg .= "matched<br />\n";

	    push @key, $key;
	    $resid{$key} = $resid;
	    $title{$key} = $t;
	    $desc{$key}  = $desc;
	    $url{$key}   = $u;
	    $img{$key}   = $i;
	    $date{$key}  = $d;

    }

    close (FP);

    if ($_[0] ne "read") {

	    # sets up variables for inital form

	    local @cds = split(/ /, $frCodes);

	    local $c = 1;
	    foreach (@cds) {

	        local $k = "key"."$c";
	        $$k = $_; # sets up variable $key1 = $key;

	        $FORM{'key'.$c}   = $_;
	        $FORM{'title'.$c} = $title{$_};
	        $FORM{'resid'.$c} = $resid{$_};
	        $FORM{'desc'.$c}  = $desc{$_};
	        $FORM{'url'.$c}   = $url{$_};
	        $FORM{'img'.$c}   = $img{$_};
	        $FORM{'date'.$c}  = $date{$_};

	        $msg .= "setting $c $FORM{'key'.$c}   eq $_ and $FORM{'title'.$c} eq $title{$_}<br />\n";
	        $c++;
	    }

	    return();

    }

    return($store);

}


####################################################################
sub saveDb {

    local $fileDetail = "/home/gartner/html/rt/content/";

    if ($FORM{'locale'} eq "emea") {
	    $fileDetail = "$fileDetail"."FRde.csv";
    } else {
	    $fileDetail = "$fileDetail"."emea/"."$FORM{'locale'}"."/FRde.csv";
    }

    $frCodes = "$FORM{'key1'} $FORM{'key2'} $FORM{'key3'} $FORM{'key4'} $FORM{'key5'} $FORM{'key6'}";

    local $oldDb = &readDb('read');

    if (!$oldDb) {

        # warn that no old data was found
        $msg .= "<p\><strong\>data store not found so stopping<\/strong\><\/p\>$oldDb\n\n";
        return();

    }

    open (FP, ">$fileDetail") || die "Can't open FP to write: $fileDetail\n";

    print FP $oldDb;

    $msg .= "saveDb: wrote oldDb: $oldDb<br />\n";

    $msg .= "saveDb: opened $fileDetail to write<br />\n";

    # remove ^M from descriptions
    $FORM{'desc1'} =~ s///g;
    $FORM{'desc2'} =~ s///g;
    $FORM{'desc3'} =~ s///g;
    $FORM{'desc4'} =~ s///g;
    $FORM{'desc5'} =~ s///g;
    $FORM{'desc6'} =~ s///g;
    $FORM{'desc1'} =~ s/\n//g;
    $FORM{'desc2'} =~ s/\n//g;
    $FORM{'desc3'} =~ s/\n//g;
    $FORM{'desc4'} =~ s/\n//g;
    $FORM{'desc5'} =~ s/\n//g;
    $FORM{'desc6'} =~ s/\n//g;

    print FP "$FORM{'key1'}\t$FORM{'resid1'}\t$FORM{'title1'}\t$FORM{'desc1'}\t$FORM{'url1'}\t$FORM{'img1'}\t$FORM{'date1'}\n";
    print FP "$FORM{'key2'}\t$FORM{'resid2'}\t$FORM{'title2'}\t$FORM{'desc2'}\t$FORM{'url2'}\t$FORM{'img2'}\t$FORM{'date2'}\n";
    print FP "$FORM{'key3'}\t$FORM{'resid3'}\t$FORM{'title3'}\t$FORM{'desc3'}\t$FORM{'url3'}\t$FORM{'img3'}\t$FORM{'date3'}\n";
    print FP "$FORM{'key4'}\t$FORM{'resid4'}\t$FORM{'title4'}\t$FORM{'desc4'}\t$FORM{'url4'}\t$FORM{'img4'}\t$FORM{'date4'}\n";
    print FP "$FORM{'key5'}\t$FORM{'resid5'}\t$FORM{'title5'}\t$FORM{'desc5'}\t$FORM{'url5'}\t$FORM{'img5'}\t$FORM{'date5'}\n";
 	print FP "$FORM{'key6'}\t$FORM{'resid6'}\t$FORM{'title6'}\t$FORM{'desc6'}\t$FORM{'url6'}\t$FORM{'img6'}\t$FORM{'date6'}\n";


    $msg .= "saveDb: wrote $FORM{'key1'}\t$FORM{'resid1'}\t$FORM{'title1'}\t$FORM{'desc1'}\t$FORM{'url1'}\t$FORM{'img1'}\t$FORM{'date1'}<br />\n";
    $msg .= "saveDb: wrote $FORM{'key2'}\t$FORM{'resid2'}\t$FORM{'title2'}\t$FORM{'desc2'}\t$FORM{'url2'}\t$FORM{'img2'}\t$FORM{'date2'}<br />\n";
    $msg .= "saveDb: wrote $FORM{'key3'}\t$FORM{'resid3'}\t$FORM{'title3'}\t$FORM{'desc3'}\t$FORM{'url3'}\t$FORM{'img3'}\t$FORM{'date3'}<br />\n";
    $msg .= "saveDb: wrote $FORM{'key4'}\t$FORM{'resid4'}\t$FORM{'title4'}\t$FORM{'desc4'}\t$FORM{'url4'}\t$FORM{'img4'}\t$FORM{'date4'}<br />\n";
    $msg .= "saveDb: wrote $FORM{'key5'}\t$FORM{'resid5'}\t$FORM{'title5'}\t$FORM{'desc5'}\t$FORM{'url5'}\t$FORM{'img5'}\t$FORM{'date5'}<br />\n";
    $msg .= "saveDb: wrote $FORM{'key6'}\t$FORM{'resid6'}\t$FORM{'title6'}\t$FORM{'desc6'}\t$FORM{'url6'}\t$FORM{'img6'}\t$FORM{'date6'}<br />\n";

    close (FP);

}

####################################################################
sub checkGermanResearch {

	# checks if document exists in german metadataindex
	#
	# INPUTS
	#
	#  1 - res id
	#  2 - key

	#$key\t$resid{$key}\t$title{$key}\t$desc{$key}\t$url{$key}\t$img{$key}\t$date{$key}\n";

	use Text::Iconv;
	my $utf2iso = Text::Iconv->new("UTF-8", "ISO-8859-1") or die "Can't create converter: utf2iso\n";
	my $utf2utf = Text::Iconv->new("UTF-8", "UTF-8") or die "Can't create converter: utf2utf\n";

	local $match = `grep $_[0] $germanMetaDataFile`;

	chop($match);

	if ($match) {

		#$msg .= "found german doc in metafile: $match<br />\n";

		my $match     = $utf2utf->convert( $match );
		#$utf2iso->raise_error(1);
		#$msg .= eval ($utf2iso->convert($match));
		#my $converted = $utf2iso->convert( $match );
		# can't do this... there is a non-UTF char in the data... probably the '|'

		my @pairs = split (/\|/, $match);

		foreach (@pairs) {

			my ($key, $value) = split (/\=/);
			$meta{$key} = $value;

		}

		# cut summary to first sentence
		$meta{'GGSUMMARY'} = substr ($meta{'GGSUMMARY'}, 0, index($meta{'GGSUMMARY'}, "\.") + 1 );

		$resid{$_[1]}   = $meta{'GGRESID'};
		$title{$_[1]}   = $utf2iso->convert( $meta{'TITLE'} ); # $meta{'TITLE'};
		$url{$_[1]}     = "regionalization/code/document.jsp?resId\=$meta{'GGRESID'}\&amp\;ct\=de\&amp\;gen\=y";
		$date{$_[1]}    = $meta{'LOCALEPUBDATE'};
		$desc{$_[1]}    = $utf2iso->convert( $meta{'GGSUMMARY'} );

		$msg .= "found german doc in metafile: $resid{$_[1]}<br />\n";

		local $keyNumber = substr ($_[1], -1, 1);

		$FORM{'key'.$keyNumber}   = $_[1];
		$FORM{'title'.$keyNumber} = $title{$_[1]};
		$FORM{'resid'.$keyNumber} = $resid{$_[1]};
		$FORM{'desc'.$keyNumber}  = $desc{$_[1]};
		$FORM{'url'.$keyNumber}   = $url{$_[1]};
		$FORM{'img'.$c}   = $img{$_[1]};
		$FORM{'date'.$c}  = $date{$_[1]};


	}

}



####################################################################
sub printInitialForm {


	# get list of current research
	local $frCodes = &readCodes('FRde', $FORM{'locale'});

	# get current research detail
	&readDb($frCodes);

	local $news = &readCodes('NEWS', $FORM{'locale'});

	# get existing news/fr for listing
	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/uk/"."xhtmlnews\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtml_news_headlines\.incl";
	}
	$curNews = &readFile($fn);

	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/uk/"."xhtmlresearch\.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtml_fr_headlines\.incl";
	}
	$curFR = &readFile($fn);



	if ($FORM{'locale'} ne "emea") {

	    # add emea news/research option
	    # allows user to override current locale offering with emea's

	    $emeanews = &readCodes('NEWS', 'emea');
	    $emearesearch = &readCodes('FR', 'emea');

	    # javascript link to call function that does work
	    $useEmeaNews = "<li\><a href\=\"javascript:void\(null\)\;\" onclick\=\"javascript:movenews\(\)\;return false\;\"\>use EMEA News<\/a\> [ $emeanews ]<\/li\>\n";


	}

	$news =~ s/  / /g;
	@checkNews = split (/ /, $news);
	local $c;
	foreach $cd (@checkNews) {
	    $c++;
	    ($FORM{'newscode'.$c}, $FORM{'newshl'.$c}, $FORM{'newsuri'.$c}, $pubDate, $summary, $author) = &readDetail('NEWS', $FORM{'locale'}, $cd);
	    $FORM{'newscode'.$c} = $cd;
	}

	# bring in EMEA news
	$emeanews =~ s/  / /g;
	@emeaNews = split (/ /, $emeanews);


	# add News form for translated research
	$addNewsForm =<<EOF;
            <ul>
              <li> <a href="javascript:void(null);" onclick="javascript:movenewsdown();return false;">move news down</a>
              <li> <input type="text" name="newscode1" value="$FORM{'newscode1'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="newshl1" size="80" value="$FORM{'newshl1'}" /> </li>
                     <li> link: <input type="text" size="80" name="newsuri1" value="$FORM{'newsuri1'}" /></li>
                   </ul>
              <li> <input type="text" name="newscode2" value="$FORM{'newscode2'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="newshl2" size="80" value="$FORM{'newshl2'}" /> </li>
                     <li> link: <input type="text" size="80" name="newsuri2" value="$FORM{'newsuri2'}" /></li>
                   </ul>
              <li> <input type="text" name="newscode3" value="$FORM{'newscode3'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="newshl3" size="80" value="$FORM{'newshl3'}" /> </li>
                     <li> link: <input type="text" name="newsuri3" size="80" value="$FORM{'newsuri3'}" /></li>
                   </ul>
              <li> <input type="text" name="newscode4" value="$FORM{'newscode4'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="newshl4" size="80" value="$FORM{'newshl4'}" /> </li>
                     <li> link: <input type="text" name="newsuri4" size="80" value="$FORM{'newsuri4'}" /></li>
                   </ul>
            </ul>
            <input type="hidden" name="newsemea1" value="$emeaNews[0]" />
            <input type="hidden" name="newsemea2" value="$emeaNews[1]" />
            <input type="hidden" name="newsemea3" value="$emeaNews[2]" />
            <input type="hidden" name="newsemea4" value="$emeaNews[3]" />

EOF

	# add News form for translated research
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
              <li> <input type="text" name="frcode5" value="$FORM{'frcode5'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl5" size="80" value="$FORM{'frhl5'}" /> </li>
                     <li> link: <input type="text" name="fruri5" size="80" value="$FORM{'fruri5'}" /></li>
                   </ul>
              <li> <input type="text" name="frcode6" value="$FORM{'frcode6'}" /></li>
                   <ul>
                     <li> title: <input type="text" name="frhl6" size="80" value="$FORM{'frhl6'}" /> </li>
                     <li> link: <input type="text" name="fruri6" size="80" value="$FORM{'fruri6'}" /></li>
                   </ul>
            </ul>
            <input type="hidden" name="fremea1" value="$emeaFR[0]" />
            <input type="hidden" name="fremea2" value="$emeaFR[1]" />
            <input type="hidden" name="fremea3" value="$emeaFR[2]" />
            <input type="hidden" name="fremea4" value="$emeaFR[3]" />

EOF

    # format Research
    $t1 = &SmartyPants ($title{$key1},1);
    $t2 = &SmartyPants ($title{$key2},1);
    $t3 = &SmartyPants ($title{$key3},1);
    $t4 = &SmartyPants ($title{$key4},1);
    $t5 = &SmartyPants ($title{$key5},1);
    $t6 = &SmartyPants ($title{$key6},1);
    $d1 = &SmartyPants ($desc{$key1},1);
    $d2 = &SmartyPants ($desc{$key2},1);
    $d3 = &SmartyPants ($desc{$key3},1);
    $d4 = &SmartyPants ($desc{$key4},1);
    $d5 = &SmartyPants ($desc{$key5},1);
    $d6 = &SmartyPants ($desc{$key6},1);

    # set unique key if there is none
    $key1 = &dateCode() if (!$key1);
    $key2 = &dateCode() if (!$key2);
    $key3 = &dateCode() if (!$key3);
    $key4 = &dateCode() if (!$key4);
    $key5 = &dateCode() if (!$key5);
    $key6 = &dateCode() if (!$key6);

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

/* focal points - what to do if text longer than image ?? */
.focalpoint       {  float: left; margin: 5px; padding: 5px; padding-right: 10px; background: #fff;  }
.focalpoint img   {  float: left; margin: 2px; padding: 0; }
.focalpoint   p   {  float: left; padding: 0; margin: 0; margin-left: 5px; vertical-align: top;
                     font-size: 11px; color: #4a4a4a;  }
.focalpoint p a   {  font-weight: bold; color: #3088CC; text-decoration: none;
                     line-height: 110%;  margin: 0; padding: 0; }

/* in the news */
.inthenewslist ul             {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;  }
.inthenewslist li             {  list-style-type: circle; list-style-image: url(http://www.gartner.com/images/homepage/reversed_green_arrow.gif);
                                 color: #3088CC; line-height: 110%; padding: 3px;  }
.inthenewslist a              {  font-family: Verdana, Arial, Helvetica, sans-serif;
                                 font-weight: bold; font-size: 11px; color: #3088CC;
                                 text-decoration: none; line-height: 110%;  }
.inthenewslist a:hover        {  text-decoration: underline;  }

/* featured research */
.featuredresearchlist ul      {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;
                                 border: 1px dashed #fff;  }
.featuredresearchlist li      {  list-style-type: circle; list-style-image: url(http://www.gartner.com/images/homepage/reversed_blue_arrow.gif);
                                 color: #3088CC; line-height: 110%; padding: 3px;  }
.featuredresearchlist a       {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold;
                                 font-size: 11px; color: #3088CC; text-decoration: none;
                                 line-height: 110%;  }
.featuredresearchlist a:hover {  text-decoration: underline;  }

.msg {  font-size: .75em; font-family: courier, fixed; color: 333; border: 1px dashed navy; padding: 10px; margin: 10px;  }

</style>
<script type="text/javascript" language="javascript">

function movenews() {
    document.form.newscode4.value = document.form.newsemea4.value;
    document.form.newscode3.value = document.form.newsemea3.value;
    document.form.newscode2.value = document.form.newsemea2.value;
    document.form.newscode1.value = document.form.newsemea1.value;

    document.form.newsuri4.value = "";
    document.form.newsuri3.value = "";
    document.form.newsuri2.value = "";
    document.form.newsuri1.value = "";

    document.form.newshl4.value = "";
    document.form.newshl3.value = "";
    document.form.newshl2.value = "";
    document.form.newshl1.value = "";

}

function movefp() {

    document.form.resid6.value = document.form.resid5.value;
    document.form.title6.value = document.form.title5.value;
    document.form.desc6.value  = document.form.desc5.value;
    document.form.img6.value   = document.form.img5.value;
    document.form.date6.value  = document.form.date5.value;
    document.form.url6.value   = document.form.url5.value;
    document.form.key6.value   = document.form.key5.value;

    document.form.resid5.value = document.form.resid4.value;
    document.form.title5.value = document.form.title4.value;
    document.form.desc5.value  = document.form.desc4.value;
    document.form.img5.value   = document.form.img4.value;
    document.form.date5.value  = document.form.date4.value;
    document.form.url5.value   = document.form.url4.value;
    document.form.key5.value   = document.form.key4.value;

    document.form.resid4.value = document.form.resid3.value;
    document.form.title4.value = document.form.title3.value;
    document.form.desc4.value  = document.form.desc3.value;
    document.form.img4.value   = document.form.img3.value;
    document.form.date4.value  = document.form.date3.value;
    document.form.url4.value   = document.form.url3.value;
    document.form.key4.value   = document.form.key3.value;


    document.form.resid3.value = document.form.resid2.value;
    document.form.title3.value = document.form.title2.value;
    document.form.desc3.value  = document.form.desc2.value;
    document.form.img3.value   = document.form.img2.value;
    document.form.date3.value  = document.form.date2.value;
    document.form.url3.value   = document.form.url2.value;
    document.form.key3.value   = document.form.key2.value;


    document.form.resid2.value = document.form.resid1.value;
    document.form.title2.value = document.form.title1.value;
    document.form.desc2.value  = document.form.desc1.value;
    document.form.img2.value   = document.form.img1.value;
    document.form.date2.value  = document.form.date1.value;
    document.form.url2.value   = document.form.url1.value;
    document.form.key2.value   = document.form.key1.value;

    // set to null
    document.form.resid1.value = ""
    document.form.title1.value = ""
    document.form.desc1.value  = ""
    document.form.img1.value   = ""
    document.form.date1.value  = "$date";
    document.form.url1.value   = ""

    var now = new Date();
    var month = now.getMonth() + 1;
    if (month < 10) {
    	mon = '0' + month.toString();
    } else {
    	mon = month.toString();
    }
    document.form.key1.value = now.getFullYear()+mon+now.getDate()+now.getSeconds();

    return false;
}

function movenewsdown() {

    document.form.newshl4.value = document.form.newshl3.value;
    document.form.newshl3.value = document.form.newshl2.value;
    document.form.newshl2.value = document.form.newshl1.value;
    document.form.newshl1.value = "";


    document.form.newsuri4.value = document.form.newsuri3.value;
    document.form.newsuri3.value = document.form.newsuri2.value;
    document.form.newsuri2.value = document.form.newsuri1.value;
    document.form.newsuri1.value = "";

    document.form.newscode4.value = document.form.newscode3.value;
    document.form.newscode3.value = document.form.newscode2.value;
    document.form.newscode2.value = document.form.newscode1.value;
    document.form.newscode1.value = "";


}


</script>
</head>
</head>
<body>
<form action="$thisScript" name="form" method="post">

    <input type="hidden" name="locale" value="de" />
    <input type="hidden" name="origNews" value="$news" />
    <input type="hidden" name="emeaNews" value="$emeanews" />
    <input type="hidden" name="origFR" value="$research" />
    <input type="hidden" name="emeaResearch" value="$emearesearch" />
    <input type="hidden" name="yyyymmdd" value="$yyyymmdd" />

<h1>Pick Research &amp; Focal Points - $FORM{'locale'}</h1>

<h2>News</h2>
<ul><li>Resid or Doc Codes:</li>
  <ul>
    <li>current news [ $news ]</li>
    $useEmeaNews
    $addNewsForm
    </ul>
</ul>
<ul class="inthenewslist">
$curNews
</ul>


<h2>Fancy Research</h2>

<h3>1</h3>
<table>
    <tr><td>RESID</td>
        <td><input type="text" name="resid1" size="12" width="12" value="$resid{$key1}"/> key <input type="text" size="12" name="key1" value="$key1" /></td></tr>
   <tr><td>Title</td>
        <td><input type="text" name="title1" size="70" width="500" value="$title{$key1}"/></td><td rowspan="5">

<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<a href="/regionalization/content/emea/$url{$key1}"><img src="http://www.gartner.com/$img{$key1}" width="100" height="68" alt="$t1" border="0" class="inline" align="left" />');
    document.write('<p><a href="/regionalization/content/emea/$url{$key1}">$t1</a></p>');
    document.write('<p>$d1</p>');
    document.write('<p>$date{$key1}</p>');
    document.write('</div>');
    document.close();
</script>


        </td></tr>

    <tr><td>URL</td>
        <td><input type="text" name="url1" size="70" width="500" value="$url{$key1}"/></td></tr>
    <tr><td>Desc</td>
        <td><textarea name="desc1" rows="5" cols="40">$desc{$key1}</textarea></td></tr>
    <tr><td>Image location</td>
        <td><input type="text" name="img1"size="70" value="$img{$key1}"  width="500" /></td></tr>
    <tr><td>Pub Date</td>
        <td><input type="text" name="date1" size="70" value="$date{$key1}"  width="500" /></td></tr>
        <tr><td>Updated/New?</td>
        <td><input type="checkbox" name="updated1" value="1" /></td></tr>
  </table>

<p><a href="javascript:void(null);" onclick="javascript:movefp();return false;">move to secondary</a></p>



<h3>2</h3>
<table>
    <tr><td>RESID</td>
        <td><input type="text" name="resid2" size="12" width="12" value="$resid{$key2}"/> key <input type="text" size="12" name="key2" value="$key2" /></td></tr></td></tr>
    <tr><td>Title</td>
        <td><input type="text" name="title2" size="70" width="500" value="$title{$key2}"/></td><td rowspan="5">

<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<a href="/regionalization/content/emea/$url{$key2}"><img src="http://www.gartner.com/$img{$key2}" width="100" height="68" alt="$t2" border="0" class="inline" align="left" />');
    document.write('<p><a href="/regionalization/content/emea/$url{$key2}">$t2</a></p>');
    document.write('<p>$d2</p>');
    document.write('<p>$date{$key2}</p>');
    document.write('</div>');
    document.close();
</script>




        </td></tr>

    <tr><td>URL</td>
        <td><input type="text" name="url2" size="70" width="500" value="$url{$key2}"/></td></tr>
    <tr><td>Desc</td>
        <td><textarea name="desc2" rows="5" cols="40">$desc{$key2}</textarea></td></tr>
    <tr><td>Image location</td>
        <td><input type="text" name="img2" size="70" value="$img{$key2}"  width="500" /></td></tr>
    <tr><td>Pub Date</td>
        <td><input type="text" name="date2" value="$date{$key2}"  width="500" /></td></tr>
    <tr><td>Updated/New?</td>
        <td><input type="checkbox" name="updated2" value="1" /></td></tr>

</table>

<h3>3</h3>
<table>
    <tr><td>RESID</td>
        <td><input type="text" name="resid3" size="12" width="12" value="$resid{$key3}"/> key <input type="text" size="12" name="key3" value="$key3" /></td></tr> </td></tr>
    <tr><td>Title</td>
        <td><input type="text" name="title3" size="70" width="500" value="$title{$key3}"/></td><td rowspan="5">

<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<a href="/regionalization/content/emea/$url{$key3}"><img src="http://www.gartner.com/$img{$key3}" width="100" height="68" alt="$t3" border="0" class="inline" align="left" />');
    document.write('<p><a href="/regionalization/content/emea/$url{$key3}">$t2</a></p>');
    document.write('<p>$d3</p>');
    document.write('<p>$date{$key3}</p>');
    document.write('</div>');
    document.close();
</script>




        </td></tr>

    <tr><td>URL</td>
        <td><input type="text" name="url3" size="70" width="500" value="$url{$key3}"/></td></tr>
    <tr><td>Desc</td>
        <td><textarea name="desc3" rows="5" cols="40">$desc{$key3}</textarea></td></tr>
    <tr><td>Image location</td>
        <td><input type="text" name="img3" size="70" value="$img{$key3}"  width="500" /></td></tr>
    <tr><td>Pub Date</td>
        <td><input type="text" name="date3" value="$date{$key3}"  width="500" /></td></tr>
    <tr><td>Updated/New?</td>
        <td><input type="checkbox" name="updated3" value="1" /></td></tr>

</table>

<h3>4</h3>
<table>
    <tr><td>RESID</td>
        <td><input type="text" name="resid4" size="12" width="12" value="$resid{$key4}"/> key <input type="text" size="12" name="key4" value="$key4" /></td></tr></td></tr>
    <tr><td>Title</td>
        <td><input type="text" name="title4" size="70" width="500" value="$title{$key4}"/></td><td rowspan="5">

<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<a href="/regionalization/content/emea/$url{$key4}"><img src="http://www.gartner.com/$img{$key4}" width="100" height="68" alt="$t4" border="0" class="inline" align="left" />');
    document.write('<p><a href="/regionalization/content/emea/$url{$key4}">$t2</a></p>');
    document.write('<p>$d4</p>');
    document.write('<p>$date{$key4}</p>');
    document.write('</div>');
    document.close();
</script>

        </td></tr>


    <tr><td>URL</td>
        <td><input type="text" name="url4" size="70" width="500" value="$url{$key4}"/></td></tr>
    <tr><td>Desc</td>
        <td><textarea name="desc4" rows="5" cols="40">$desc{$key4}</textarea></td></tr>
    <tr><td>Image location</td>
        <td><input type="text" name="img4" size="70" value="$img{$key4}"  width="500" /></td></tr>
    <tr><td>Pub Date</td>
        <td><input type="text" name="date4" value="$date{$key4}"  width="500" /></td></tr>
    <tr><td>Updated/New?</td>
        <td><input type="checkbox" name="updated4" value="1" /></td></tr>

</table>

<h3>5</h3>
<table>
    <tr><td>RESID</td>
        <td><input type="text" name="resid5" size="12" width="12" value="$resid{$key5}"/> key <input type="text" size="12" name="key5" value="$key5" /></td></tr></td></tr>
    <tr><td>Title</td>
        <td><input type="text" name="title5" size="70" width="500" value="$title{$key5}"/></td><td rowspan="5">

<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<a href="/regionalization/content/emea/$url{$key5}"><img src="http://www.gartner.com/$img{$key5}" width="100" height="68" alt="$t5" border="0" class="inline" align="left" />');
    document.write('<p><a href="/regionalization/content/emea/$url{$key5}">$t2</a></p>');
    document.write('<p>$d5</p>');
    document.write('<p>$date{$key5}</p>');
    document.write('</div>');
    document.close();
</script>

        </td></tr>


    <tr><td>URL</td>
        <td><input type="text" name="url5" size="70" width="500" value="$url{$key5}"/></td></tr>
    <tr><td>Desc</td>
        <td><textarea name="desc5" rows="5" cols="50">$desc{$key5}</textarea></td></tr>
    <tr><td>Image location</td>
        <td><input type="text" name="img5" size="70" value="$img{$key5}"  width="500" /></td></tr>
    <tr><td>Pub Date</td>
        <td><input type="text" name="date5" value="$date{$key5}"  width="500" /></td></tr>
    <tr><td>Updated/New?</td>
        <td><input type="checkbox" name="updated5" value="1" /></td></tr>

</table>

<h3>6</h3>
<table>
    <tr><td>RESID</td>
        <td><input type="text" name="resid6" size="12" width="12" value="$resid{$key6}"/> key <input type="text" size="12" name="key6" value="$key6" /></td></tr></td></tr>
    <tr><td>Title</td>
        <td><input type="text" name="title6" size="70" width="500" value="$title{$key6}"/></td><td rowspan="5">

<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('<a href="/regionalization/content/emea/$url{$key6}"><img src="http://www.gartner.com/$img{$key6}" width="100" height="68" alt="$t6" border="0" class="inline" align="left" />');
    document.write('<p><a href="/regionalization/content/emea/$url{$key6}">$t2</a></p>');
    document.write('<p>$d6</p>');
    document.write('<p>$date{$key6}</p>');
    document.write('</div>');
    document.close();
</script>

        </td></tr>


    <tr><td>URL</td>
        <td><input type="text" name="url6" size="70" width="500" value="$url{$key6}"/></td></tr>
    <tr><td>Desc</td>
        <td><textarea name="desc6" rows="5" cols="60">$desc{$key6}</textarea></td></tr>
    <tr><td>Image location</td>
        <td><input type="text" name="img6" size="70" value="$img{$key6}"  width="500" /></td></tr>
    <tr><td>Pub Date</td>
        <td><input type="text" name="date6" value="$date{$key6}"  width="500" /></td></tr>
    <tr><td>Updated/New?</td>
        <td><input type="checkbox" name="updated6" value="1" /></td></tr>

</table>


server: <input type="radio" name="site" value="prod" checked="checked" /> production <input type="radio" name="site" value="qa" /> qa

<input type="submit">

<h2>Instructions</h3>
<div class="msg">
<p>These forms allow you to update the news, research and focal points on the regional websites</p>
<ul>
  <li> <strong>News &amp; Research</strong></li>
  <ul>

    <li>  For news and research you can enter the resid or doccode of the g.com document you want to add or promote.</li>
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
      <li> If you only want to move one or two in, then use the <u>move news/fr down</u> link and copy the resids from the list next to <u>use emea news/research</u></li>
    </ul>

  </ul>
  <li> <strong>Focal Points</strong></li>
  <ul>
    <li> These currently are only being used for the weekly emailer, test rss fee and the xhtml version of the site.</li>
    <li> <u>move to secondary</u> moves the top fp's contents down</li>
    <li> <strong>PubDate</strong> is for the rss feeds, please attempt to fill it in correctly</li>
    <li> <strong>Updated/New?</strong> tells the tool to republish the fp includes</li>
    <li> NOTE: <i>this tool hasn't been set up for translation of includes yet.</i></li>
  </ul>
  <li> Final Note: <i>this tool also FTPs the news and research headlines to campsqa, so on these sites there is no urlInclude.... it also create a backup of the previous include on the remote server called ...incl.old</i></li>
  <li> Also: <i>I will move these instructions to the bottom of the page when someone metions it. ;-)</i></li>

</ul>


</div>


<h2>Messages</h2>
<p class="msg">$msg</p>

$menu

</form>
</body>
</html>

EndofHTML


}

####################################################################
sub printOutput {

    $title{$key1} = &SmartyPants ($title{$key1},1);
    $title{$key2} = &SmartyPants ($title{$key2},1);
    $title{$key3} = &SmartyPants ($title{$key3},1);
    $title{$key4} = &SmartyPants ($title{$key4},1);
    $title{$key5} = &SmartyPants ($title{$key5},1);
    $title{$key6} = &SmartyPants ($title{$key6},1);
    $desc{$key1}  = &SmartyPants ($desc{$key1},1);
    $desc{$key2}  = &SmartyPants ($desc{$key2},1);
    $desc{$key3}  = &SmartyPants ($desc{$key3},1);
    $desc{$key4}  = &SmartyPants ($desc{$key4},1);
    $desc{$key5}  = &SmartyPants ($desc{$key5},1);
    $desc{$key6}  = &SmartyPants ($desc{$key6},1);


    print <<EndofHTML;
Content-type:  text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>pickResearch.cgi - $ENV{'REMOTE_ADDR'}</title>
<style type="text/css">
h1,h2,h3,ol,li,body {	font-family: Verdana, Arial, Sans;	}
h1	{		font-size: 14pt;	}
h2	{		font-size: 12pt; clear:both;	}
h3	{		font-size: 10pt;	}
li,p,td	{		font-size: 9pt;	        }
/* HOMEPAGE CENTER COLUMN */
/* in the news */
.inthenewslist ul             {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;  }
.inthenewslist li             {  list-style-type: circle; list-style-image: url(http://www.gartner.com/images/homepage/reversed_green_arrow.gif); color: #3088CC; line-height: 110%; padding: 3px;  }
.inthenewslist a              {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #3088CC; text-decoration: none; line-height: 110%;  }
.inthenewslist a:hover        {  text-decoration: underline;  }

/* featured research */
.featuredresearchlist ul      {  margin: 0; padding: 0; margin-top: 7px; margin-left: 25px;   }
.featuredresearchlist li      {  list-style-type: circle; list-style-image: url(http://www.gartner.com/images/homepage/reversed_blue_arrow.gif); color: #3088CC; line-height: 110%; padding: 3px;  }
.featuredresearchlist a       {  font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #3088CC; text-decoration: none; line-height: 110%;  }
.featuredresearchlist a:hover {  text-decoration: underline;  }

/* focal points - what to do if text longer than image ?? */
.focalpoint     {  float: left; margin: 5px; padding: 5px; padding-right: 10px; background: #fff; width: 400px;  }
.focalpoint img {  float: left; margin: 2px; padding: 0; }
.focalpoint   p{  float: left; padding: 0; margin: 0; margin-left: 5px; vertical-align: top; font-size: 11px; color: #4a4a4a;  }
.focalpoint p a{  font-weight: bold; color: #3088CC; text-decoration: none; line-height: 110%;  margin: 0; padding: 0; }

		  .msg {  font-size: .75em; font-family: courier, fixed; color: 333; border: 1px dashed navy; padding: 10px; margin: 10px;  }

.menu { font-size: 8pt; border 1px solid navy; }

</style>

</head>
</head>
<body>
<h1>Output - $FORM{'locale'}</h1>

<h2>News</h2>
<div class="inthenewslist">
<ul>
$xhtmlNews
</ul>
</div>
<br clear="all" />

<h2>FR</h2>
<div class="focalpoint">
$xhtmlFancy[1]
</div>
<br clear="all" />

<div class="focalpoint">
$xhtmlFancy[2]
</div>
<br clear="all" />
<div class="featuredresearchlist">
<ul>
$xhtmlPlain
</ul>
</div>

<h2>Focal Points</h2>
<script type="text/javascript" language="javascript">
    document.open();
    document.write('<div class="focalpoint">');
    document.write('$xhtmlFancy[1]');
    document.write('</div><p> </p>');
    document.write('<div class="focalpoint">');
    document.write('$xhtmlFancy[2]');
    document.write('</div><p> </p>');
    document.close();
</script>

$fancy1
<br clear="all" />
$fancy2
<br clear="all" />
$plain
<br clear="all" />


<h2>Messages</h2>
<p class="msg">$msg</p>
<p class="msg">$ftpmsg</p>

$menu

</body>
</html>

EndofHTML

}



####################################################################
sub getDoc {

    # for processing news only

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
	# $title = &SmartyPants($title, 1);
	$msg .= "replaceChars: $title<br>";
    }


    # rewrite link if passed
    if ($_[2]) {
	$link    = $_[2];
	$docCode =  $link;
	$docCode =~ s/http:\/\/www4.gartner.com//;
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
    $noHangTitle = &noHang($title, 44);
    $noHangTitle =~ s/\& /\&amp\; /g;

    # copy of $title without <br />
    $origTitle = $title;

    # turn & into &amp;
    $title   =~ s/\& /\&amp\; /g;
    $summary =~ s/\& /\&amp\; /g;


    # clean up author
    $auth =~ s/,/ \&amp\;nbsp\; /g; # convert , to a space - for mailing format

    # clean up $pubDate
    $pubDate =~ s/\-/ /g;
    $pubDate =~ s/^0//;
    $pubDate =~ s/Jan/January/;
    $pubDate =~ s/Feb/February/;
    $pubDate =~ s/Mar/March/;
    $pubDate =~ s/Apr/April/;
    $pubDate =~ s/Jun/June/;
    $pubDate =~ s/Jul/July/;
    $pubDate =~ s/Aug/August/;
    $pubDate =~ s/Sep/September/;
    $pubDate =~ s/Oct/October/;
    $pubDate =~ s/Nov/November/;
    $pubDate =~ s/Dec/December/;

    # NEWS HTML
    $htmlNEWS .= <<EndofHTML;
\n<!--start news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->
    <tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
    <tr><td width="22" bgcolor="#FFFFFF" valign="top" align="center"><a href="javascript:void(null)" onclick="openResult('$docCode')" class="largeGrayLink"><img src="/images/homepage/reversed_green_arrow.gif" width="9" height="9" vspace="3" alt="$title" border="0"></a></td>\n        <td width="328" valign="top" bgcolor="#FFFFFF"><a href="javascript:void(null)" onclick="openResult('$docCode');return false;" class="smallBlueLink" target="_new">$noHangTitle</a></td>\n        <td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>\n    </tr>
<!--end news - $origTitle NN:$noteNumber ID:$_[0] DATE:$pubDate -->\n
EndofHTML


    $xhtmlNews .=  <<EndofHTML;
 <li> <a href="\#" onclick="openResult('$docCode')">$origTitle</a></li>
EndofHTML


}

###################################################################
sub saveOutput {



	#####################################################
	# save html versions
	# NEWS
	local $fn = "/home/gartner/html/rt/content/";

	if ($FORM{'locale'} eq "emea") {
		$fn = "$fn"."emea/"."home_news_headlines.incl";
	} else {
		$fn = "$fn"."emea/"."$FORM{'locale'}"."/home_news_headlines.incl";
	}
	&saveFile($fn, $htmlNEWS);
	$msg .= "<br /><br />NEWS<br />$htmlNEWS<br /><br />";
	&FTPfile_good('home_news_headlines.incl', $FORM{'locale'});

	# RESEARCH
	local $fn = "/home/gartner/html/rt/content/";

	if ($FORM{'locale'} eq "emea") {
		$fn = "$fn"."emea/"."home_fr_headlines.incl";
	} else {
		$fn = "$fn"."emea/"."$FORM{'locale'}"."/home_fr_headlines.incl";
	}

	&saveFile($fn, $plain);
	&FTPfile_good('home_fr_headlines.incl', $FORM{'locale'});


	# save html fancy
	open (FP, ">/home/gartner/html/rt/content/emea/de/home_fr_highlight_01.incl") || die "Can't open html FP1\n";
	print FP $fancy1;
	close (FP);
	&FTPfile_good('home_fr_highlight_01.incl', $FORM{'locale'});
	$msg .= "saving html of the fancy one: /home/gartner/html/rt/content/emea/de/home_fr_highlight_01.incl<br />\n$fancy<br \>\n";

	open (FP, ">/home/gartner/html/rt/content/emea/de/home_fr_highlight_02.incl") || die "Can't open html FP2\n";
	print FP $fancy2;
	close (FP);
	&FTPfile_good('home_fr_highlight_02.incl', $FORM{'locale'});
	$msg .= "saving html of the fancy one 2: /home/gartner/html/rt/content/emea/de/home_fr_highlight_02.incl<br />\n$fancy<br \>\n";


	# save xhtml fancy
	open (FP, ">/home/gartner/html/rt/content/emea/de/xhtml_fr1.incl") || die "Can't open xhtml FP1\n";
	print FP $xhtmlFancy[1];
	close (FP);

	open (FP, ">/home/gartner/html/rt/content/emea/de/xhtml_fr2.incl") || die "Can't open xhtml FP2\n";
	print FP $xhtmlFancy[2];
	close (FP);


    	############################################################
    	# XHTML FORMATS

	 local $fn = "/home/gartner/html/rt/content/";

         if ($FORM{'locale'} eq "emea") {
		$fn = "$fn"."emea/"."xhtml_fr_headlines.incl";
	 } else {
		$fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtml_fr_headlines.incl";
	 }
         &saveFile($fn, $xhtmlPlain);
	 local $fn = "/home/gartner/html/rt/content/";

         if ($FORM{'locale'} eq "emea") {
		$fn = "$fn"."emea/"."xhtml_news_headlines.incl";
	 } else {
		$fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtml_news_headlines.incl";
	 }
         &saveFile($fn, $xhtmlNews);
	&FTPfile_good('xhtml_news_headlines.incl', $FORM{'locale'});

	# save all news format
	local $fn = "/home/gartner/html/rt/content/";
	if ($FORM{'locale'} eq "emea") {
	    $fn = "$fn"."emea/"."xhtml_news_all.incl";
	} else {
	    $fn = "$fn"."emea/"."$FORM{'locale'}"."/xhtml_news_all.incl";
	}
	&saveFile($fn, $xhtmlNewsAll);
	&FTPfile_good('xhtml_news_all.incl', $FORM{'locale'});





}

sub FTPfile_good {

    # ftp files to remote servers
    # take 2 args
    # 1. filename
    # 2. relative path from emea/
    # 3. remote filename (<optional> for xhtml)
    # return();


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



#################################################
sub dateCode {

	# counter to make sure its unique
	$dcCounter++;

	local $ds = `date +'%Y%m%d%S'`;
	chop($ds);
	$ds = "$ds"."$dcCounter";
	return($ds);

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


###################################################################
sub printAllNews {

    # prints include for an all news page

    $xhtmlNewsAll = &readDetailAll('NEWS', $FORM{'locale'}, $_[0]); # gets all the news EXCEPT current latest set
    $xhtmlNewsAll =~ &replaceCharacters($xhtmlNewsAll);
    $xhtmlNewsAll  =~ s/\&(?:amp)/\&amp\;/g;

    return();
}
