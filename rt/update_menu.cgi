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
	# RUN homepage_parser.pl

    if ($MenuFORM{'MQHCVRupdate'}) {

		$updateMsg .= "<h4\>homepage_parser.pl<\/h4\>\n\n";

		$updateMsg .= `/usr/local/bin/perl /home/gartner/html/rt/homepage_parser.pl`;
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
	# LOCAL BRIEFINGS

    if ($MenuFORM{'lb_europe'} || $MenuFORM{'lb_italia'} || $MenuFORM{'lb_deutschland'}) {

		$updateMsg .= "<h4\>Local Briefings<\/h4\>\n\n";

		if ($MenuFORM{'lb_europe'}) {

		    my $strict = "strict" if ($MenuFORM{'lb_eu_strict'} eq "on");

		    `/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl emea $strict`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/localBriefingTable.html\"\>europe<\/a\><br \/\>\n";

		}

		if ($MenuFORM{'lb_italia'}) {

		    my $strict = "strict" if ($MenuFORM{'lb_it_strict'} eq "on");

		    `/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl it $strict`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/localBriefingTable.html\"\>italia<\/a\><br \/\>\n";

		}

		if ($MenuFORM{'lb_deutschland'}) {

		    my $strict = "strict" if ($MenuFORM{'lb_de_strict'} eq "on");

		    `/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl de $strict`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/localBriefingTable.html\"\>deutschland<\/a\><br \/\>/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl de $MenuFORM{'lb_de_strict'}<br \/\>\n";

		}

		$updateMsg .= "<p \/\>\n\n\n";
    }




	######################################
	# TELECONFERENCES

    if ($MenuFORM{'tel_europe'} || $MenuFORM{'tel_italia'} || $MenuFORM{'tel_deutschland'}) {

		$updateMsg .= "<h4\>Teleconferences<\/h4\>\n\n";

		if ($MenuFORM{'tel_europe'}) {
		    `/usr/local/bin/perl /home/gartner/html/rt/getTeleconf.pl emea $MenuFORM{'emeaTelLimit'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/teleconf.html\"\>europe<\/a\>\n\n";
		    $updateMsg .= "<p \/\>\n\n\n";

		}

		if ($MenuFORM{'tel_italia'}) {


		    `/usr/local/bin/perl /home/gartner/html/rt/getTeleconf.pl it $MenuFORM{'itTelLimit'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/teleconf.html\"\>italia<\/a\>\n\n";
		    $updateMsg .= "<p \/\>\n\n\n";

		}

		if ($MenuFORM{'tel_deutschland'}) {


		    `/usr/local/bin/perl /home/gartner/html/rt/getTeleconf.pl de $MenuFORM{'deTelLimit'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/teleconf.html\"\>deutchland<\/a\>\n\n";
		    $updateMsg .= "<p \/\>\n\n\n";

		}
    }

	######################################
	# SUMMIT EVENTS/CONFERENCES
    if ($MenuFORM{'conf_europe'} || $MenuFORM{'conf_italia'} || $MenuFORM{'conf_deutschland'}) {

		$updateMsg .= "<h4\>Summit Events<\/h4\>\n\n";

		if ($MenuFORM{'conf_europe'}) {
		    `/usr/local/bin/perl /home/gartner/html/rt/getConf.pl emea $MenuFORM{'emeaSkipConf'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/home_events_confs.incl\"\>europe<\/a\>\n\n";
		    $updateMsg .= "$msg /usr/local/bin/perl /home/gartner/html/rt/getConf.pl emea $MenuFORM{'emeaSkipConf'}<p \/\>\n\n\n";

		}

		if ($MenuFORM{'conf_italia'}) {


		    `/usr/local/bin/perl /home/gartner/html/rt/getConf.pl it $MenuFORM{'itSkipConf'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/home_events_confs.incl\"\>italia<\/a\>\n\n";
		    $updateMsg .= "/usr/local/bin/perl /home/gartner/html/rt/getConf.pl it $MenuFORM{'itSkipConf'}<p \/\>\n\n\n";

		}

		if ($MenuFORM{'conf_deutschland'}) {


		    `/usr/local/bin/perl /home/gartner/html/rt/getConf.pl de $MenuFORM{'deSkipConf'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/home_events_confs.incl\"\>deutchland<\/a\>\n\n";
		    $updateMsg .= "/usr/local/bin/perl /home/gartner/html/rt/getConf.pl de $MenuFORM{'deSkipConf'}<p \/\>\n\n\n";

		}
    }


	######################################
	# VISION EVENTS
    if ($MenuFORM{'vision_europe'} || $MenuFORM{'vision_italia'} || $MenuFORM{'vision_deutschland'}) {

		$updateMsg .= "<h4\>Vision Events<\/h4\>\n\n";

		if ($MenuFORM{'vision_europe'}) {
		    `/usr/local/bin/perl /home/gartner/html/rt/getVisionEvents.pl emea $MenuFORM{'emeaSkipConf'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/home_vision_events_confs.incl\"\>europe<\/a\>\n\n";
		    $updateMsg .= "$msg /usr/local/bin/perl /home/gartner/html/rt/getVisionEvents.pl emea $MenuFORM{'emeaSkipConf'}<p \/\>\n\n\n";

		}

		if ($MenuFORM{'vision_italia'}) {


		    `/usr/local/bin/perl /home/gartner/html/rt/getVisionEvents.pl it $MenuFORM{'itSkipConf'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/home_vision_events_confs.incl\"\>italia<\/a\>\n\n";
		    $updateMsg .= "/usr/local/bin/perl /home/gartner/html/rt/getVisionEvents.pl it $MenuFORM{'itSkipVision'}<p \/\>\n\n\n";

		}

		if ($MenuFORM{'vision_deutschland'}) {


		    `/usr/local/bin/perl /home/gartner/html/rt/getVisionEvents.pl de $MenuFORM{'deSkipVision'}`;
		    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/home_vision_events_confs.incl\"\>deutchland<\/a\>\n\n";
		    $updateMsg .= "/usr/local/bin/perl /home/gartner/html/rt/getVisionEvents.pl de $MenuFORM{'deSkipVision'}<p \/\>\n\n\n";

		}
    }


	######################################
	# SYMPOSIUM EVENTS
    if ($MenuFORM{'symp_europe'} || $MenuFORM{'symp_italia'} || $MenuFORM{'symp_deutschland'}) {

	$updateMsg .= "<h4\>Symposium<\/h4\>\n\n";

	if ($MenuFORM{'symp_europe'}) {
	    `/usr/local/bin/perl /home/gartner/html/rt/getSymposium.pl emea $MenuFORM{'emeaSkipSymp'}`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/home_symposium.incl\"\>europe<\/a\>\n\n";
	    $updateMsg .= "$msg /usr/local/bin/perl /home/gartner/html/rt/getSymposium.pl emea $MenuFORM{'emeaSkipSymp'}<p \/\>\n\n\n";

	}
	
	if ($MenuFORM{'symp_italia'}) {
	    
	    
	    `/usr/local/bin/perl /home/gartner/html/rt/getSymposium.pl it $MenuFORM{'itSkipSymp'}`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/home_symposium.incl\"\>italia<\/a\>\n\n";
	    $updateMsg .= "/usr/local/bin/perl /home/gartner/html/rt/getSymposium.pl it $MenuFORM{'itSkipSymp'}<p \/\>\n\n\n";
	    
	}
	
	if ($MenuFORM{'symp_deutschland'}) {
	    
	    
	    `/usr/local/bin/perl /home/gartner/html/rt/getSymposium.pl de $MenuFORM{'deSkipSymp'}`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/home_symposium.incl\"\>deutchland<\/a\>\n\n";
	    $updateMsg .= "/usr/local/bin/perl /home/gartner/html/rt/getSymposium.pl de $MenuFORM{'deSkipSymp'}<p \/\>\n\n\n";
	    
	}
    }
    

	######################################
	# WEBLOGS - no longer on sites
    if ($MenuFORM{'weblog_europe'} || $MenuFORM{'weblog_italia'}) {

		# currently no italia version

		$updateMsg .= "<h4\>Weblog<\/h4\>\n\n";


		$weblog = &urlIncl('\/featured_research.inc', $locale);

		open (WEBLOG, ">\/home\/gartner\/html\/rt\/content\/emea\/weblog.inc");
		print WEBLOG $weblog;
		close (WEBLOG);

		$updateMsg .= "<a href\=\/rt\/content\/weblog.inc\>europe<\/a\><br \/\>\n\n";
		$updateMsg .= "<p \/\>\n\n\n";

    }


	######################################
	# FOCUS AREAS
    if ($MenuFORM{'focus_europe'} || $MenuFORM{'focus_italia'}  || $MenuFORM{'focus_deutschland'}) {

		# currently no europe version

		$updateMsg .= "<h4\>Focus Area (Membership Programs, Research Collections)<\/h4\>\n\n";


		if ($MenuFORM{'focus_europe'}) {
		    $locale = "";
		    &doFocus;
		}

		if ($MenuFORM{'focus_italia'}) {
		    $locale = "it";
		    &doFocus;
		}

		if ($MenuFORM{'focus_deutschland'}) {
		    $locale = "de";
		    &doFocus;
		}



		sub doFocus {

		    $fa = "";

		    $fa = &urlIncl('\/focus_areas.inc', $locale);

		    open (FA, ">\/home\/gartner\/html\/rt\/content\/emea\/$locale\/focus_areas.inc") || die "\n\nCan't open \/home\/gartner\/html\/rt\/content\/emea\/$locale\/focus_areas.inc for writing \n\n";
		    print FA $fa;
		    close (FA);

		    $updateMsg .= "<a href\=\/rt\/content\/emea\/$locale\/focus_areas.inc\>$localeFull{$locale}<\/a\><br \/\>\n\n";

		    $updateMsg .= "<p \/\>\n\n\n";

		}
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
  <td colspan="3" class="head">Local Briefings</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="lb_europe" checked="checked" /></td>
  <td class="selection">europe</td>
  <td class="selection">strict: <input type="checkbox" name="lb_eu_strict" /></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="lb_italia" checked="checked" /></td>
  <td class="selection">italia</td>
  <td class="selection">strict: <input type="checkbox" name="lb_it_strict" /></td>
 </tr>


 <tr>
  <td class="selection"><input type="checkbox" name="lb_deutschland" checked="checked" /></td>
  <td class="selection">deutschland</td>
  <td class="selection">strict: <input type="checkbox" name="lb_de_strict" checked="checked" /></td>
 </tr>



 <tr>
  <td colspan="3" class="head">Teleconferences</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="tel_europe" checked="checked"/></td>
  <td class="selection">europe</td>
  <td class="selection">limit: <input type="text" name="emeaTelLimit" size="2" value="4" /></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="tel_italia" checked="checked" /></td>
  <td class="selection">italia</td>
  <td class="selection">limit: <input type="text" name="itTelLimit" size="2" value="4" /></td>
</tr>

 <tr>
  <td class="selection"><input type="checkbox" name="tel_deutschland" checked="checked" /></td>
  <td class="selection">deutchland</td>
  <td class="selection">limit: <input type="text" name="deTelLimit" size="2" value="4" /></td>
 </tr>

 <tr>
  <td colspan="3" class="head">Summits</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="conf_europe" checked="checked" /></td>
  <td class="selection">europe</td>
  <td class="selection">skip: <input type="text" name="emeaSkipConf" size="2" value="-1" /></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="conf_italia" checked="checked" /></td>
  <td class="selection">italia</td>
  <td class="selection">skip: <input type="text" name="itSkipConf" size="2" value="-1" /></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="conf_deutschland" checked="checked" /></td>
  <td class="selection">deutchland</td>
  <td class="selection">skip: <input type="text" name="deSkipConf" size="2" value="-1" /></td>
 </tr>


 <tr>
  <td colspan="3" class="head">Vision Events</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="vision_europe" checked="checked" /></td>
  <td class="selection">europe</td>
  <td class="selection">skip: <input type="text" name="emeaSkipVision" size="2" value="-1" /></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="vision_italia" checked="checked" /></td>
  <td class="selection">italia</td>
  <td class="selection">skip: <input type="text" name="itSkipVision" size="2" value="-1" /></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="vision_deutschland" checked="checked" /></td>
  <td class="selection">deutchland</td>
  <td class="selection">skip: <input type="text" name="deSkipVision" size="2" value="-1" /></td>
 </tr>

  <tr>
  <td colspan="3" class="head">Symposium</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="symp_europe" checked="checked" /></td>
  <td class="selection">europe</td>
  <td class="selection">skip: <input type="text" name="emeaSkipSymp" size="2" value="-1" /></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="symp_italia" checked="checked" /></td>
  <td class="selection">italia</td>
  <td class="selection">skip: <input type="text" name="itSkipSymp" size="2" value="-1" /></td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="symp_deutschland" checked="checked" /></td>
  <td class="selection">deutchland</td>
  <td class="selection">skip: <input type="text" name="deSkipSymp" size="2" value="-1" /></td>
 </tr>

<!--
 <tr>
  <td colspan="3" class="head">Weblogs</td>
 </tr>

 <tr>
  <td colspan="3" class="selection"> &nbsp; \-\- currently in the HC, MQ and VR section \-\-</td>
 </tr>

<tr>
  <td class="selection"><input type="checkbox" name="weblog_europe" /></td>
  <td class="selection">europe</td>
 </tr>


 <tr>
  <td colspan="3" class="head">Focus Areas</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="focus_italia" /></td>
  <td class="selection">italia</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="focus_deutschland" /></td>
  <td class="selection">deutschland</td>
 </tr>
-->


 <tr>
  <td colspan="3" class="head">Hype Cycles, MQs and Vendor Ratings</td>
 </tr>

 <tr>
  <td class="selection"><input type="checkbox" name="MQHCVRupdate" /></td>
  <td class="selection" colspan="2">re-run homepage_parser.pl</td>
 </tr>

 <tr>
  <td class="selection">europe</td>
  <td class="selection" colspan="2">
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickMQ=true&locale=emea')">MQ</a> [$sMQemea] |
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickHC=true&locale=emea')">HC</a> [$sHCemea] |
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickVR=true&locale=emea')">VR</a> [$sVRemea]
  </td>
 </tr>

  <tr>
  <td class="selection">italia</td>
  <td class="selection" colspan="2">
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickMQ=true&locale=it')">MQ</a> [$sMQit] |
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickHC=true&locale=it')">HC</a> [$sHCit] |
  <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickVR=true&locale=it')">VR</a> [$sVRit]
  </td>
 </tr>

 <tr>
  <td class="selection">deutschland</td>
  <td class="selection" colspan="2">
    <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickMQ=true&locale=de')">MQ</a> [$sMQde] |
    <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickHC=true&locale=de')">HC</a> [$sHCde] |
    <a href="Javascript:windowPopup('http://intl.gartner.com/rt/pickMQHCVR.cgi?pickVR=true&locale=de')">VR</a> [$sVRde]
  </td>
 </tr>


 <tr>
  <td colspan="3" class="head">Focal Point/German Research Archive</td>
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
