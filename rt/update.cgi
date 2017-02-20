#!/usr/local/bin/perl

$msg = "<h4\>Gartner Europe Local Briefings<\/h4\><pre\>\n\n";
$msg .= `/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl`;
$msg .= "<\/pre\><h4\>Gartner Europe Italia Briefings<\/h4\><pre\>\n\n";
$msg .= `/usr/local/bin/perl /home/gartner/html/rt/getLocalBriefings.pl italia`;
$msg .= "<\/pre\><h4\>Gartner Europe Teleconf<\/h4\><pre\>\n\n";
$msg .= `/usr/local/bin/perl /home/gartner/html/rt/getTeleconf.pl`;

$msg .= "<\/pre\><h4\>Gartner Italia Teleconf<\/h4\><pre\>\n\n";
$msg .= `/usr/local/bin/perl /home/gartner/html/rt/getTeleconf.pl italia`;


# WEBLOGS
$msg .= "<\/pre\><h4\><a href\=\/rt\/content\/weblog.inc\>WEBLOGS Updated<\/a\><\/h4\><pre\>\n\n";
$weblog = `/usr/local/bin/perl /home/gartner/cgi\-bin/urlIncl.cgi \/featured_research.inc`;

open (WEBLOG, ">\/home\/gartner\/html\/rt\/content\/weblog.inc");
print WEBLOG $weblog;
close (WEBLOG);


# focus areas for italia
$msg .= "<\/pre\><h4\>italia <a href\=\/rt\/content\/emea\/it\/focus_areas.inc\>focus_areas.inc<\/a\> Updated<\/h4\><pre\>\n\n";
$fa = `/usr/local/bin/perl /home/gartner/cgi\-bin/urlIncl.cgi \/focus_areas.inc`;

open (FA, ">\/home\/gartner\/html\/rt\/content\/emea\/it\/focus_areas.inc");
print FA $fa;
close (FA);

# /mq_vr.inc
$msg .= "<\/pre\><h4\>italia <a href\=\/rt\/content\/emea\/it\/mq_vr.inc\>hype cycle, mq and vr mq_vr.inc<\/a\> Updated<\/h4\><pre\>\n\n";
$mq = `/usr/local/bin/perl /home/gartner/cgi\-bin/urlIncl.cgi \/mq_vr.inc`;

open (MQ, ">\/home\/gartner\/html\/rt\/content\/emea\/it\/mq_vr.inc");
print MQ $mq;
print MQ "\n<\/table\>\n\n";
close (MQ);


print <<EndofHTML;
Content-type: text/html

<html>
<body>
$msg
</pre>
</body>
</html>

EndofHTML
