#!/usr/local/bin/perl

#############################################################
#############################################################
#
#  update_menu.cgi
#
#    written by Peter Mahnke
#
#    simple web form to help update many
#    of the regional websites homepage
#    components
#
#    modifictations
#    - 29 Mar 2005 - PRM added form and
#                    command line passing of strict
#                    variable for local briefings
#
#
#
#############################################################
#############################################################


use CGI_Lite;
# require ('/home/gartner/html/rt/urlInclude_require.pl');
require('/home/gartner/html/rt/commonLock.pl');

$localeFull{'de'}   = "deutschland";
$localeFull{'it'}   = "italia";
$localeFull{'emea'} = "europe";

###############################################################
# was something POSTED
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    # something submitted
    &parsePage;
    &process;
    &printInitialPage;

    exit;

} else {

    # nothing submitted
    &printInitialPage;
    exit;
}



#################################################################
sub parsePage {

    $cgi = new CGI_Lite;
    %MenuFORM = $cgi->parse_form_data;

}


sub process {

	######################################
	# RUN homepage_parser2.pl

    if ($MenuFORM{'MQHCVRupdate'}) {

		$updateMsg .= "<h4\>homepage_parser2.pl<\/h4\>\n\n";

		$updateMsg .= `/usr/local/bin/perl /home/gartner/html/rt/homepage_parser2.pl`;
		$updateMsg .= "<br \/\>\n<a href\=\"\/rt\/content\/emea\/\"\>europe<\/a\><br \/\>\n";
		$updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/\"\>italia<\/a\><br \/\>\n";
		$updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/\"\>deutschland<\/a\><br \/\>\n";

	}

	######################################
	# RUN FOCAL POINT INDEX GENERATOR

    if ($MenuFORM{'FPtoc'}) {

		$updateMsg .= "<h4\>writeFPtoc.pl<\/h4\>\n\n";

		$updateMsg .= `/usr/local/bin/perl /home/gartner/html/rt/writeFPtoc.pl`;

	}

	######################################
	# RUN GERMAN INDEX GENERATOR

	if ($MenuFORM{'DEtoc'}) {

		$updateMsg .= "<h4\>writeDEindex2.pl<\/h4\>\n\n";

		$updateMsg .= `/usr/local/bin/perl /home/gartner/html/rt/writeDEindex2.pl`;


	}

    
    ######################################
    # EVENTS
    
    if ($MenuFORM{'events_eu'} || $MenuFORM{'events_it'} || $MenuFORM{'events_de'}) {
	
	$updateMsg .= "<h4\>events<\/h4\>\n\n";
	
	if ($MenuFORM{'events_eu'}) {
	    
	    `/usr/local/bin/perl /home/gartner/html/rt/getEvents.cgi emea $MenuFORM{'event_num_eu'} $MenuFORM{'event_strict_eu'}`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/home_events.incl\"\>europe<\/a\><br \/\>\n";
	    
	}
	
	if ($MenuFORM{'events_it'}) {
	    
	    `/usr/local/bin/perl /home/gartner/html/rt/getEvents.cgi it $MenuFORM{'event_num_it'} $MenuFORM{'event_strict_it'}`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/home_events.incl\"\>italia<\/a\><br \/\>\n";
	    
	}
	
	if ($MenuFORM{'events_de'}) {
	    
	    `/usr/local/bin/perl /home/gartner/html/rt/getEvents.cgi de $MenuFORM{'event_num_de'} $MenuFORM{'event_strict_de'}`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/home_events.incl\"\>deutschland<\/a\><br \/\>\n";
	    
	}
	
	$updateMsg .= "<p \/\>\n\n\n";
    }


	######################################
	# HYPE CYCLES, MAGIC QUADRANTS & VENDOR RATINGS

    if ($MenuFORM{'hc_europe'} || $MenuFORM{'hc_italia'} || $MenuFORM{'hc_deutschland'}) {

		# hype cycles, mqs and vrs
		# only for italia right now

		$updateMsg .= "<h4\>Hype Cycle, MQ and Vendor Ratings<\/h4\>\n\n";

		if ($MenuFORM{'hc_europe'}) {
		    $locale = "";
		    &doHCpage;
		}

		if ($MenuFORM{'hc_italia'}) {
		    $locale = "it";
		    &doHCpage;
		}

		if ($MenuFORM{'hc_deutschland'}) {
		    $locale = "de";
		    &doHCpage;
		}

		sub doHCpage {

		    $mq = "";

		    $mq = &urlIncl('\/mq_vr.inc', $locale); #`/usr/local/bin/perl /home/gartner/cgi\-bin/urlIncl.cgi \/mq_vr.inc`;

		    open (MQ, ">\/home\/gartner\/html\/rt\/content\/emea\/$locale\/mq_vr.inc");
		    print MQ $mq;
		    # print MQ "\n<\/table\>\n\n";
		    close (MQ);

		    $updateMsg .= "<a href\=\/rt\/content\/emea\/$locale\/mq_vr.inc\>$localeFull{$locale}<\/a\><br \/\>\n\n";

		    $updateMsg .= "<p \/\>\n\n\n";
		}

    }

} # end sub process




sub printInitialPage {

	# test MQ locks
	if (&testLock('MQ', 'emea')) {
		$sMQemea = "locked";
	} else {
		$sMQemea = "default";
	}
	if (&testLock('MQ', 'it')) {
		$sMQit = "locked";
	} else {
		$sMQit = "default";
	}
	if (&testLock('MQ', 'de')) {
		$sMQde = "locked";
	} else {
		$sMQde = "default";
	}

	# test HC locks
	if (&testLock('HC', 'emea')) {
		$sHCemea = "locked";
	} else {
		$sHCemea = "default";
	}
	if (&testLock('HC', 'it')) {
		$sHCit = "locked";
	} else {
		$sHCit = "default";
	}
	if (&testLock('HC', 'de')) {
		$sHCde = "locked";
	} else {
		$sHCde = "default";
	}

	# test VR locks
	if (&testLock('VR', 'emea')) {
		$sVRemea = "locked";
	} else {
		$sVRemea = "default";
	}

	if (&testLock('VR', 'it')) {
		$sVRit = "locked";
	} else {
		$sVRit = "default";
	}

	if (&testLock('VR', 'de')) {
		$sVRde = "locked";
	} else {
		$sVRde = "default";
	}

	# test CV locks
	if (&testLock('CV', 'emea')) {
		$sCVemea = "locked";
	} else {
		$sCVemea = "default";
	}

	if (&testLock('CV', 'it')) {
		$sCVit = "locked";
	} else {
		$sCVit = "default";
	}

	if (&testLock('CV', 'de')) {
		$sCVde = "locked";
	} else {
		$sCVde = "default";
	}




	print <<EndofHTML;
Content-type: text/html

<html>
<head>
<title>update_menu.cgi</title>
<script type="text/javascript" language="javascript"><!--

function windowPopup(href) {

    window.open(href,'window','width=550,height=700,location=no,scrollbars=yes,status=no,toolbar=no,resizable=yes');

}

//--></script>
</head>
<body>

<style>
    .head {background-color:#003399; font-family:verdana,arial,helvetica; color:#FFFFFF; font-size:11pt; font-weight:bold; text-decoration:none; font-style:normal; font-style:normal; }
    .selection {font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #666666; text-decoration: none; cursor:default;}
    .listing {font-family:verdana,arial,helvetica; color:#3366CC; font-size:11px; font-weight:normal; font-style:normal; font-style:normal;}

</style>

<form method=get>

<table>

 <tr>
  <td colspan="4" class="head">Events</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="events_eu" checked="checked" /></td>
  <td class="selection">europe</td>
  <td class="selection">number <input type="radio" name="event_num_eu" value="3"/> 3 <input type="radio" name="event_num_eu" value="4" /> 4 </td>
  <td class="selection">strict <input type="checkbox" name="event_strict_eu" value="strict"/></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="events_it" checked="checked" /></td>
  <td class="selection">italia</td>
  <td class="selection">number <input type="radio" name="event_num_it" value="3"/> 3 <input type="radio" name="event_num_it" value="4" /> 4 </td>
  <td class="selection">strict <input type="checkbox" name="event_strict_it" value="strict"/></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="events_de" checked="checked" /></td>
  <td class="selection">deutchland</td>
  <td class="selection">number <input type="radio" name="event_num_de" value="3"/> 3 <input type="radio" name="event_num_de" value="4" /> 4 </td>
  <td class="selection">strict <input type="checkbox" name="event_strict_de" value="strict"/></td>
 </tr>


 <tr>
  <td colspan="4" class="head">Hype Cycles, MQs and Vendor Ratings</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="MQHCVRupdate" /></td>
  <td class="selection" colspan="2">re-run homepage_parser2.pl</td>
 </tr>

 <tr>
  <td class="selection">europe</td>
  <td class="selection" colspan="2">
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickMQ=true&locale=emea')">MQ</a> [$sMQemea] |
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickHC=true&locale=emea')">HC</a> [$sHCemea] |
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickVR=true&locale=emea')">VR</a> [$sVRemea]
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickCV=true&locale=emea')">CV</a> [$sCVemea]
  </td>
 </tr>

  <tr>
  <td class="selection">italia</td>
  <td class="selection" colspan="2">
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickMQ=true&locale=it')">MQ</a> [$sMQit] |
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickHC=true&locale=it')">HC</a> [$sHCit] |
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickVR=true&locale=it')">VR</a> [$sVRit]
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickCV=true&locale=it')">CV</a> [$sCVit]
  </td>
 </tr>

 <tr>
  <td class="selection">deutschland</td>
  <td class="selection" colspan="2">
    <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickMQ=true&locale=de')">MQ</a> [$sMQde] |
    <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickHC=true&locale=de')">HC</a> [$sHCde] |
    <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickVR=true&locale=de')">VR</a> [$sVRde]
    <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR2.cgi?pickVR=true&locale=de')">CV</a> [$sCVde]
  </td>
 </tr>


 <tr>
  <td colspan="4" class="head">Focal Point/German Research Archive</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="FPtoc" /></td>
  <td class="selection" colspan="2">build Focal Point Archive</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="DEtoc" /></td>
  <td class="selection" colspan="2">build German Research Archive</td>
 </tr>



 <tr>
  <td></td>
  <td class="selection"><input type=submit></td>
 </tr>


</table>
<p />
<!-- <input type="checkbox" name=intl value=true> use safe local version? -->
</form>

<hr size=1>
<span class=listing>
$updateMsg
$msg
</span>
<p />
</body>
</html>

EndofHTML


}
