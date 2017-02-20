#!/usr/local/bin/perl

use CGI_Lite;
require ('/home/gartner/html/rt/urlInclude_require.pl');

$localeFull{'de'} = "deutschland";
$localeFull{'it'} = "italia";
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


    if ($MenuFORM{'lb_europe'} || $MenuFORM{'lb_italia'} || $MenuFORM{'lb_deutschland'}) {

	$updateMsg .= "<h4\>Local Briefings<\/h4\>\n\n";

	if ($MenuFORM{'lb_europe'}) {
	
	    `/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/localBriefingTable.html\"\>europe<\/a\><br \/\>\n";
	    
	} 

	if ($MenuFORM{'lb_italia'}) {

	    `/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl italia`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/localBriefingTable.html\"\>italia<\/a\><br \/\>\n";
	    
	} 

	if ($MenuFORM{'lb_deutschland'}) {

	    `/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl de`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/localBriefingTable.html\"\>deutschland<\/a\><br \/\>\n";
	    
	}
	
	$updateMsg .= "<p \/\>\n\n\n";
    }

    if ($MenuFORM{'tel_europe'} || $MenuFORM{'tel_italia'} || $MenuFORM{'tel_deutschland'}) {
	


	$updateMsg .= "<h4\>Teleconferences<\/h4\>\n\n";
	       
	if ($MenuFORM{'tel_europe'}) {
	    `/usr/local/bin/perl /home/gartner/html/rt/getTeleconf.pl`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/teleconf.html\"\>europe<\/a\>\n\n";
	    $updateMsg .= "<p \/\>\n\n\n";

	} 

	if ($MenuFORM{'tel_italia'}) {


	    `/usr/local/bin/perl /home/gartner/html/rt/getTeleconf.pl italia`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/it\/teleconf.html\"\>italia<\/a\>\n\n";
	    $updateMsg .= "<p \/\>\n\n\n";
	    
	} 

	if ($MenuFORM{'tel_deutschland'}) {


	    `/usr/local/bin/perl /home/gartner/html/rt/getTeleconf.pl de`;
	    $updateMsg .= "<a href\=\"\/rt\/content\/emea\/de\/teleconf.html\"\>deutchland<\/a\>\n\n";
	    $updateMsg .= "<p \/\>\n\n\n";
	    
	}
    }



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

}

sub printInitialPage {


print <<EndofHTML;
Content-type: text/html

<html>
<head><title>update_menu.cgi</title></head>
<body>

<style>
    .head {background-color:#003399; font-family:verdana,arial,helvetica; color:#FFFFFF; font-size:11pt; font-weight:bold; text-decoration:none; font-style:normal; font-style:normal; }
    .selection {font-family: Verdana, Arial, Helvetica, sans-serif; font-weight: bold; font-size: 11px; color: #666666; text-decoration: none; cursor:default;}
    .listing {font-family:verdana,arial,helvetica; color:#3366CC; font-size:11px; font-weight:normal; font-style:normal; font-style:normal;}

</style>

<form method=get>

<table>

 <tr>
  <td colspan=2 class=head>Local Briefings</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=lb_europe></td>
  <td class=selection>europe</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=lb_italia></td>
  <td class=selection>italia</td>
 </tr>


 <tr>
  <td class=selection><input type=checkbox name=lb_deutschland></td>
  <td class=selection>deutschland</td>
 </tr>



 <tr>
  <td colspan=2 class=head>Teleconferences</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=tel_europe></td>
  <td class=selection>europe</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=tel_italia></td>
  <td class=selection>italia</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=tel_deutschland></td>
  <td class=selection>deutchland</td>
 </tr>

 <tr>
  <td colspan=2 class=head>Weblogs</td>
 </tr>

 <tr>
  <td colspan=2 class=selection> &nbsp; \-\- currently in the HC, MQ and VR section \-\-</td>
 </tr>

<!-- <tr>
  <td class=selection><input type=checkbox name=weblog_europe></td>
  <td class=selection>europe</td>
 </tr>
-->

 <tr>
  <td colspan=2 class=head>Focus Areas</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=focus_italia></td>
  <td class=selection>italia</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=focus_deutschland></td>
  <td class=selection>deutschland</td>
 </tr>



 <tr>
  <td colspan=2 class=head>Hype Cycles, MQs and Vendor Ratings</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=hc_italia></td>
  <td class=selection>italia</td>
 </tr>

 <tr>
  <td class=selection><input type=checkbox name=hc_deutschland></td>
  <td class=selection>deutschland</td>
 </tr>


 <tr>
  <td></td>
  <td class=selection><input type=submit></td>
 </tr>


</table>
<p />
<!-- <input type=checkbox name=intl value=true> use safe local version? -->
</form>

<hr size=1>
<span class=listing>
$updateMsg
</span>
<p />
</body>
</html>

EndofHTML


}
