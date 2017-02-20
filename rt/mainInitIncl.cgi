#!/usr/local/bin/perl

################################################################################
#
# mainInitIncl.pl
#
#   written:  01 Dec 2003 by Peter Mahnke
#   modified: 10 Jan 2005 by Peter Mahnke
#             NOTE: currently using single region header
#                   NOT current multi-region version -- ONLY FOR CMT HEADERS
#
#   DESCRIPTION
#   a CGI script to help create standard versions of the regional headers
#   with all locales and versions handeled
#
#   INPUT
#   ?region=(emea|it|de|at)
#
#   OUTPUT
#   html, javascript, versions
#   translation in the uiStrings.pl script
#
#
################################################################################

use CGI_Lite;
require ('/home/gartner/html/rt/uiStrings.pl');

$commonHeader = <<EndofHTML;

<!-- START MAIN_INIT -->

<link rel=stylesheet href="http://www.gartner.com/css/menu.css" type="text/css">

<style>
.gradgray { background:#DDE0E2; background-image:url(http://www.gartner.com/images/header/grad_gray566.gif); }
input.field1 { vertical-align:middle; }
img.down1 { position:relative;top:4;left:0; }
img.down2 { position:relative;top:6;left:0; }
</style>

<script type="text/javascript" language="JavaScript">
  if (((navigator.appVersion.toLowerCase().indexOf('msie') !=-1) && (navigator.appVersion.toLowerCase().indexOf('mac') ==-1)) || (navigator.appVersion.toLowerCase().indexOf('windows') !=-1))
  {
    document.write('<link rel=stylesheet href="http://www.gartner.com/css/win/main.css" type="text/css">');
    document.write('<link rel=stylesheet href="http://www.gartner.com/css/win/navigation.css" type="text/css">');
    document.write('<link rel=stylesheet href="http://www.gartner.com/css/win/homepage.css" type="text/css">');
  }
  else
  {	if (navigator.appVersion.toLowerCase().indexOf('hp-ux') !=-1)
    {
      document.write('<link rel=stylesheet href="http://www.gartner.com/css/hp/main.css" type="text/css">');
      document.write('<link rel=stylesheet href="http://www.gartner.com/css/hp/navigation.css" type="text/css">');
      document.write('<link rel=stylesheet href="http://www.gartner.com/css/hp/homepage.css" type="text/css">');
    }
    else
    {	if (navigator.appVersion.toLowerCase().indexOf('sunos') !=-1)
      {
        document.write('<link rel=stylesheet href="http://www.gartner.com/css/sun/main.css" type="text/css">');
        document.write('<link rel=stylesheet href="http://www.gartner.com/css/sun/navigation.css" type="text/css">');
        document.write('<link rel=stylesheet href="http://www.gartner.com/css/sun/homepage.css" type="text/css">');
      }
      else
      {	if ((navigator.appVersion.toLowerCase().indexOf('mac') !=-1)  || (navigator.appVersion.toLowerCase().indexOf('x11') !=-1))
        {
          document.write('<link rel=stylesheet href="http://www.gartner.com/css/mac/main.css" type="text/css">');
          document.write('<link rel=stylesheet href="http://www.gartner.com/css/mac/navigation.css" type="text/css">');
          document.write('<link rel=stylesheet href="http://www.gartner.com/css/mac/homepage.css" type="text/css">');
        }
        else
        {	if (navigator.appVersion.toLowerCase().indexOf('linux') !=-1)
          {
            document.write('<link rel=stylesheet href="http://www.gartner.com/css/linux/main.css" type="text/css">');
            document.write('<link rel=stylesheet href="http://www.gartner.com/css/linux/navigation.css" type="text/css">');
            document.write('<link rel=stylesheet href="http://www.gartner.com/css/linux/homepage.css" type="text/css">');
          }
          else
          {	if (navigator.appVersion.toLowerCase().indexOf('win') !=-1)
            {
              document.write('<link rel=stylesheet href="http://www.gartner.com/css/netscape/main.css" type="text/css">');
              document.write('<link rel=stylesheet href="http://www.gartner.com/css/netscape/navigation.css" type="text/css">');
              document.write('<link rel=stylesheet href="http://www.gartner.com/css/netscape/homepage.css" type="text/css">');
            }
          }

        }
      }
    }
  }
</script>

<script type="text/javascript" src="http://www.gartner.com/js/navigation.js"></script>
<script type="text/javascript" src="http://www.gartner.com/js/menu.js"></script>
<script type="text/javascript" src="http://www.gartner.com/js/utility.js"></script>
<script type="text/javascript" src="http://www.gartner.com/pages/docs/gartner/mq/scripts/utils.js"></script>
<script type="text/javascript" src="http://www.gartner.com/js/cookie.js"></script>
<script type="text/javascript" src="http://www.gartner.com/js/mouseevents.js"></script>
<script type="text/javascript" src="http://www.gartner.com/js/layerapi.js"></script>

<script type="text/javascript" language="JavaScript">

// set up some variables
  var readyState = null
  var calendar = null
  var formDivs = new Array()
  var zIndex = 2
  var textFocus = 0
  var content = self
  var footer = parent.footer
  var winCTR = 0 ;
  var childWindow = new Array(20);
  var REGISTEREDUSER =0
  var CLIENTADM = 0
  var GARTADM = 0
  var INQACCESS = 0
  var EVENTREG = 0
  var sleeperInc = 1
  var myTimer
  var usercookie=GetCookie("UserType");
  var objSearchForm = document.frmSearch
  var mystrng ;

// set some of the variables if there is a session cookie
    if (usercookie != null) {
      REGISTEREDUSER = parseInt(Mid(usercookie,0,1));
      CLIENTADM = parseInt(Mid(usercookie,1,1));
      GARTADM = parseInt(Mid(usercookie,2,1));
      INQACCESS = parseInt(Mid(usercookie,3,1));
      EVENTREG = parseInt(Mid(usercookie,4,1));
    }

// function to parse the session cookie
    function Mid(str, start, len) {
      if (start < 0 || len < 0) {
        return "";
      }
      var iEnd, iLen = String(str).length;
      if (start + len > iLen) {
        iEnd = iLen;
      } else {
        iEnd = start + len;
      }
      return String(str).substring(start,iEnd);
    }

// Timer to log users out of the page
/*********************************************/
var tID;
if (!tID) {
  tID = setTimeout('executeTimer()',7500000);
}

function resetTimer() {
  clearTimeout(tID); // reset the timer
  tID = setTimeout('executeTimer()',7500000);
}

function executeTimer() {
  location.href = 'http://www.gartner.com/Terminate?src=timeout&url=' +top.location.href;
  clearTimeout(tID);
  tID = null;
}
/***********************************************/


// function to allow return to submit certain forms
function keydown(e) {
  if (bw.ns4 || bw.ns6) {
    intKey=e.which;
  } else {
    intKey=event.keyCode;
  }
  if (intKey==13) {
    switch (textFocus){
      case 0: submitSearch(); break;
      case 1: submitSignin(); break;
      case 2: submitEmail(); break;
      case 3: break;
    }
  }
}


//  specify character(s) in the url
var sectionNumber = location.pathname.substring(1, 2);
var sectionNews = location.pathname.substring(1, 13);
var sectionEvents = location.pathname.substring(1, 3);
var sectionExp = location.pathname.substring(1, 38);
var sectionFocus2 = location.pathname.substring(1, 6);
var sectionPrivacy = location.pathname.substring(1, 6);
var sectionPrinciples = location.pathname.substring(1, 24);


// TAB COLOR HANDELING

  // variables for normal (un-highlighted) top nav tab colors
  var homeTab          = "#656565";
  var researchTab      = "#656565";
  var consultingTab    = "#656565";
  var measurementTab   = "#656565";
  var communityTab     = "#656565";
  var newsTab          = "#656565";

  // variables for highlighted top nav tab colors
  var HLresearchTab    = "#0173EF";
  var HLconsultingTab  = "#84A5F7";
  var HLmeasurementTab = "#527BC6";
  var HLcommunityTab   = "#000099";
  var HLnewsTab        = "#01426B";
  var HLhomeTab        = "#333333";

// logic for finding highlighted tab
if (category != null) {

    if (category == 1) {
       researchTab = HLresearchTab;
       }
    else
    if (category == 2) {
       consultingTab = HLconsultingTab;
       }
    else
    if (category == 3) {
       measurementTab = HLmeasurementTab;
       }
    else
    if (category == 4) {
       communityTab = HLcommunityTab;
       }
    else
    if (category == 5) {
       newsTab = HLnewsTab;
       }
    else
    if (category == 8) {
        newsTab = HLnewsTab;
       }
    else
    if (category == 9) {
       communityTab = HLcommunityTab;
       }
}
else
{
    var category = null
    if (sectionPrinciples == "pages/story.php.id.2635")
        {researchTab = researchTab;}
     else
     if (sectionPrinciples == "pages/story.php.id.2630")
        {researchTab = researchTab;
        }
     else
     if (sectionFocus2 == "pages")
        {researchTab = HLresearchTab;
        }
     else
     if (sectionExp == "1_researchanalysis/executive_programs")
        {communityTab = HLcommunityTab;
        }
     else
      if (sectionEvents == "Ev")
        {communityTab = HLcommunityTab;
        }
     else
      if (sectionNumber == "1")
        {researchTab = HLresearchTab;
        }
     else
      if (sectionNumber == "2")
        {communityTab = HLcommunityTab;
        }
     else
      if (sectionNumber == "3")
        {consultingTab = HLconsultingTab;
        }
     else
      if (sectionNumber == "4")
        {measurementTab = HLmeasurementTab;
        }
     else
      if (sectionNews == "5_about/news")
        {newsTab = HLnewsTab;
        }
}


/*
   determine browser type based on ability to use
   document.layers, document.all or document.getElementByID
*/
var ns4 = (document.layers);
var ie4 = (document.all && !document.getElementById);
var ie5 = (document.all && document.getElementById);
var ns6 = (!document.all && document.getElementById);

function attach(id)
{
   /*
     based on browser type,
     use document.layers, document.all or document.getElementByID
     to select the table cell to change colors
  */
    var obj
    if(ns4) obj = document.layers[id];
    else if(ie4) obj = document.all[id];
    else if(ie5 || ns6) obj = document.getElementById(id);
    return obj
}

function tabColor(id, color)
{
    /*
       this function will reset the background color
       of the tab based on a mouse event to either
       the highlight, or normal color
    */
    tabColorObject = attach(id);
    tabColorObject.style.backgroundColor=color;
}


</script>
</head>
<body marginheight="0" marginwidth="0" topmargin="0" leftmargin="0" bgcolor="#bbbbbb">
EndofHTML

###############################################################
# was something POSTED
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    # something submitted
    &parsePage;

}

&printOutput;



#############################################################
sub parsePage {

    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;

}


#############################################################
sub printOutput {


	$region = $FORM{'region'};
	$region = "emea" if (!$region); # default to emea


	$regionalsLocaleDir          = "emea";
	$regionalsSearchText         = "Search";
	$regionalsSearchResearchText = "Search Research";
	$regionalsSearchDocsOnlyText = "Research Documents Only";
	$regionalsSearchSiteOnlyText = "Site";
	$regionalsSearchTextBox      = "value=\"\"";
	$regionalsBrowseText         = "Browse";
	$regionalsAdvancedSearchText = "Advanced Search";
	$regionalsHelpText           = "Help";
	$regionalsNewText            = "New";

if ($region eq "at") {

	# Austria
	$regionalsLocaleDir          = "emea/de/at/";
	$regionalsSearchText         = "Suchen";
	$regionalsSearchResearchText = "Research durchsuchen";
	$regionalsSearchDocsOnlyText = "Nur Research-Dokumente";
	$regionalsSearchSiteOnlyText = "Website";
	$regionalsSearchTextBox      = "value=\"in English\" onFocus=document.frmSearch.txtSearch.value=\"\"";
	$regionalsBrowseText         = "Browse";
	$regionalsAdvancedSearchText = "Erweiterte Suche";
	$regionalsHelpText           = "Hilfe";
	$regionalsNewText            = "Neu";

} elsif ($region eq "de") {

	# Germany
	$regionalsLocaleDir          = "emea/de/";
	$regionalsSearchText         = "Suchen";
	$regionalsSearchResearchText = "Research durchsuchen";
	$regionalsSearchDocsOnlyText = "Nur Research-Dokumente";
	$regionalsSearchSiteOnlyText = "Website";
	$regionalsSearchTextBox      = "value=\"in English\" onFocus=document.frmSearch.txtSearch.value=\"\"";
	$regionalsBrowseText         = "Browsen";
	$regionalsAdvancedSearchText = "Erweiterte Suche";
	$regionalsHelpText           = "Hilfe";
	$regionalsNewText            = "Neu";

} elsif ($region eq "it") {

	# Italy
	$regionalsLocaleDir          = "emea/it/";
	$regionalsSearchText         = "Ricerca";
	$regionalsSearchResearchText = "Cerca in Research";
	$regionalsSearchDocsOnlyText = "Cerca solo in Reseach";
	$regionalsSearchSiteOnlyText = "Sito";
	$regionalsSearchTextBox      = "value=\"in English\" onFocus=document.frmSearch.txtSearch.value=\"\"";
	$regionalsBrowseText         = "Sfoglia";
	$regionalsAdvancedSearchText = "Ricerca avanzata";
	$regionalsHelpText           = "Aiuto";
	$regionalsNewText            = "Novit&agrave;";

}



$line .=<<EOF;

<script type="text/javascript">
    document.open();
    document.write[<table width="766" height="60" border="0" cellspacing="0" cellpadding="0" align="center">];
    document.write[<tr>];
    document.write[<td rowspan="3" width="2" bgcolor="#FFFFFF"><img src="http://www.gartner.com/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>];
    document.write[<td width="100%" height="2" bgcolor="#FFFFFF"><img src="http://www.gartner.com/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></td>];
    document.write[<td width="566" height="2" bgcolor="#FFFFFF"><img src="http://www.gartner.com/images/trans_pixel.gif" width="566" height="2" alt="" border="0"></td>];
    document.write[<td rowspan="3" width="2" bgcolor="#FFFFFF"><img src="http://www.gartner.com/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>];
    document.write[</tr>];
    document.write[<tr>];
    document.write[<td width="100%" bgcolor="#FFFFFF"><a href="http://www.gartner.com/regionalization/content/$regionalsLocaleDir/home.jsp?refresh=true"><img src="http://www.gartner.com/regionalization/img/header/$regionalsLocaleDir/gartner_logo_$region.gif" width="170" height="43" hspace="4" border="0"></a></td>];
    document.write[<td width="566" align="right" class="gradgray" bgcolor="#ffffff;">];
    document.write[<table width="566" cellpadding="0" cellspacing="0" border="0">];
    document.write[<form method="post" name="frmSearch" onsubmit="submitSearch();return false;">];
    document.write[<tr>];
    document.write[<td valign="middle" width="566" align="right"><div><img src="http://www.gartner.com/images/trans_pixel.gif" width="1" height="1" alt=""border="0"></div>];
    document.write[<img src="http://www.gartner.com/images/trans_pixel.gif" width="100" height="1" alt="" border="0">];

    browserName = navigator.appName;
    browserVersion = parseInt(navigator.appVersion);
    if (browserName == "Netscape" && browserVersion == 4)
    {
        document.write($regionalsSearchText);
    }  else  {
        document.write[<span style="font-family: Arial, Helvetica, sans-serif, Verdana; font-weight: bold; font-size: 100%; color: #636973; text-decoration: none; vertical-align: text-bottom;">$regionalsSearchText</span>];
    }

    document.write[<img src="http://www.gartner.com/images/trans_pixel.gif" width="8" height="18" alt="" border="0" align="abdmiddle">];
    document.write[<img src="http://www.gartner.com/images/header/arrow_gray.gif" width="23" height="20" alt="" border="0" hspace="3" vspace="0" class="down1" align="absmiddle">];
    document.write[<img src="http://www.gartner.com/images/trans_pixel.gif" width="12" height="10" alt="" border="0" align="bottom">];
    document.write[<input type="text" size="27" maxlength="400" name="txtSearch" id="txtSearch" $regionalsSearchTextBox class="field1" align="absmiddle">&nbsp;&nbsp;];
    document.write[<input type="button" value="$regionalsSearchText " onFocus="textFocus=3" onBlur="textFocus=0" onclick="submitSearch();" border="0" style="font-family: Verdana,Arial,Helvetica,sans-serif; font-size: 70%;font-style: normal; font-weight: bold;line-height: 130%; color: #636163; background: #E7E7E7; border-width: 1px; vertical-align: middle;"> &nbsp;&nbsp;];
    document.write[</td>];
    document.write[</tr></form>];
    document.write[</table>];
    document.write[</td>];
    document.write[</tr>];
    document.write[</table>];
    document.write[<table width="766" border="0" cellspacing="0" cellpadding="0" align="center">];
    document.write[<tr>];
    document.write[<td rowspan="4" width="2" bgcolor="#FFFFFF"><img src="http://www.gartner.com/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>];
    document.write[<td colspan="7" width="762" height="2" bgcolor="#FFFFFF"><img src="http://www.gartner.com/images/trans_pixel.gif" width="762" height="2" alt="" border="0"></td>];
    document.write[<td rowspan="4" width="2" bgcolor="#FFFFFF"><img src="http://www.gartner.com/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>];
    document.write[</tr>];
    document.write[</td>];
    document.write[</tr>];
    document.write[<tr>];
    document.write[<td bgcolor="' + homeTab + '" width="53" height="20" align="center" onClick="document.location='/regionalization/content/$regionalsLocaleDir/home.jsp?refresh=true';" id="home" onMouseOver="tabColor('home', '' + HLhomeTab + '');" onMouseOut="tabColor('home', '' + homeTab + '');"><a href="http://www.gartner.com/regionalization/content/$regionalsLocaleDir/home.jsp?refresh=true" class="mainNavLink">home</a></td>];
    document.write[<td bgcolor="' + researchTab + '" width="73" height="20" align="center" onClick="document.location='/regionalization/content/$regionalsLocaleDir/01_research.html';" id="research"  onMouseOver="tabColor('research', '' + HLresearchTab + '');" onMouseOut="tabColor('research', '' + researchTab + '');"><a href="http://www.gartner.com/regionalization/content/$regionalsLocaleDir/01_research.html" class="mainNavLink">research</a></td>];
    document.write[<td bgcolor="' + consultingTab + '" width="87" height="20" align="center" onClick="document.location='/regionalization/content/$regionalsLocaleDir/02_consulting.html';" id="consulting" onMouseOver="tabColor('consulting', '' + HLconsultingTab + '');" onMouseOut="tabColor('consulting', '' + consultingTab + '');"><a href="http://www.gartner.com/regionalization/content/$regionalsLocaleDir/02_consulting.html" class="mainNavLink">consulting</a></td>];
    document.write[<td bgcolor="' + measurementTab + '" width="105" height="20" align="center" onClick="document.location='/regionalization/content/$regionalsLocaleDir/03_measurement.html';" id="measurement" onMouseOver="tabColor('measurement','' + HLmeasurementTab + '');" onMouseOut="tabColor('measurement','' + measurementTab + '');"><a href="http://www.gartner.com/regionalization/content/$regionalsLocaleDir/03_measurement.html" class="mainNavLink">benchmarking</a></td>];
    document.write[<td bgcolor="' + communityTab + '" width="88" height="20" align="center" onClick="document.location='/regionalization/content/$regionalsLocaleDir/04_community.html';" id="community" onMouseOver="tabColor('community','' + HLcommunityTab + '');" onMouseOut="tabColor('community','' + communityTab + '');"><a href="http://www.gartner.com/regionalization/content/$regionalsLocaleDir/04_community.html" class="mainNavLink">community</a></td>];
    document.write[<td bgcolor="' + newsTab + '" width="58" height="20" align="center" onClick="document.location='/regionalization/content/$regionalsLocaleDir/05_news.html';" id="news" onMouseOver="tabColor('news','' + HLnewsTab + '');" onMouseOut="tabColor('news','' + newsTab + '');"><a href="http://www.gartner.com/regionalization/content/$regionalsLocaleDir/05_news.html" class="mainNavLink">news</a></td>];
    document.write[<td bgcolor="#9C9C9C" width="298" height="20" align="right" ><a href="#" onclick="browse(); return false;" class="mainRightNavLink">$regionalsBrowseText</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="#" onclick="javascript:advancedSearch(); return false;" class="mainRightNavLink">$regionalsAdvancedSearchText</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href="http://www.gartner.com/6_help/help_overview.html" class="mainRightNavLink">$regionalsHelpText</a>&nbsp;</td>];
    document.write[</tr>];
    document.write[<tr>];
    document.write[<td class="contentCell" height="3" width="100%" colspan="7"><img height="3" src="http://www.gartner.com/images/trans_pixel.gif"></td>];
    document.write[</tr>];
    document.write[</table>];
    document.close();

</script>

<!-- END MAIN_INIT -->

EOF

	#$line =~ s/\n//g; # remove newlines
	$line =~ s/\' \+/PRE/g;
	$line =~ s/\+ \'/POST/g;

	$line =~ s/\'/\\\'/g;
	$line =~ s/\\\\'/\\'/g;
	$line =~ s/\n\n/\n/g;
	$line =~ s/\[/\(\'/g;
	$line =~ s/\]\;/\'\)\;\n/g;

	$line =~ s/PRE/\' \+/g;
	$line =~ s/POST/\+ \'/g;

	$jsline =~ s/\'/\\\'/g;
	$jsline =~ s/\\\\'/\\'/g;
	$jsline =~ s/\n//g;
	$jsline =~ s/\[/\(\'/g;
	$jsline =~ s/\]/\'\)\;\n/g;


	# translate if required
if ($region ne "emea") {

		# all austrian translations are german, except for above pop-ups
		$region = "de" if ($region eq "at");

		# provide a translation
		$line = &translateUIstring($line, 'eu', $region);
#		$jsline = &translateUIstring($jsline, 'eu', $region);

	}

	$jsline =~ s/\</\&lt\;/g;

	$lineamped =$line;
	#$lineamped =~ s/&(?!amp;)/&amp;/g;
	$lineamped =~ s/http:\/\/www.gartner.com//g;

	$jsline    =~ s/&(?!(amp|lt);)/&amp;/g;

	$commonHeaderClean = $commonHeader;
	$commonHeaderClean =~ s/http:\/\/www.gartner.com//g;
	#$commonHeaderClean =~ s/&(?!amp;)/&amp;/g;

	print <<EOF;
Content-type: text/html

<!DOCTYPE html PUBLIC "W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>main_init header $FORM{'region'} - $FORM{'from'} -> $FORM{'to'}</title>
$commonHeader
$line
<hr>
<h4>HTML</h4>
<p>
<textarea cols="80" rows="10">
$commonHeaderClean
$lineamped
</textarea>
</p>



<h4>messages</h4>
<pre>

$msg

</pre>
</body>
</html>
EOF

}




