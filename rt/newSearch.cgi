#!/usr/local/bin/perl


#
#
#  ToDo
#   -  clean up special results like events
#
#
#
#

use Carp;
no Carp::Assert;


require ('/home/gartner/html/rt/commonSearch.pl');


# Variables
$server = "www4";
local $pageOneFlag = "";
local $URL = "http:\/\/$server.gartner.com\/Search";
local $thisScript = "http://intl.gartner.com/rt/newSearch.cgi";


##############################################################
# Get the input from the HTML Form
##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {
    
    
    # something submitted
    
    use CGI_Lite;
    $cgi = new CGI_Lite;
    
    %FORM = $cgi->parse_form_data;
    
    foreach $key (keys %FORM) {
	
	# not required?
	next if ($key eq "PRM");
	$buffer .= "$key\=$FORM{$key}\&";
	
    }
    
        
} else {
    
    $inputs = "<p\>Username: <input type\=\"text\" name\=\"username\"\ \/\><\/p\>\n";
    &printSearchForm;
    exit;
    
}


##################################################################################
# MAIN
#
#

#################################
# What to do


if ($FORM{'rss'}) {
    
    &runQuery;
    &printRSS;
    exit;
    
} elsif ($FORM{'action'} eq "edit") {
    
    $inputs = "<input type\=\"hidden\" name\=\"username\" value\=\"$FORM{'username'}\" \>\n<input type\=\"hidden\" name\=\"oldname\" value\=\"$FORM{'name'}\" \>  $FORM{'username'}\n";
    &printEditForm;
    exit;


} elsif ($FORM{'action'} eq "save") {

    $inputs = "<input type\=\"hidden\" name\=\"username\" value\=\"$FORM{'username'}\" \>\n";

    if ($FORM{'oldname'}) {
	
	# actually saving over an old one
	&saveDB(&readDB($FORM{'username'}, 'edit', $FORM{'oldname'}));

    } else {

	# saving a new one
	&saveDB(&readDB($FORM{'username'}, 'all'));

    }
    
    $info   = &readDB($FORM{'username'}, 'get');
    &printSearchForm;
    exit;

} elsif ($FORM{'action'} eq "savenew") {
    
    $inputs = "<input type\=\"hidden\" name\=\"username\" value\=\"$FORM{'username'}\" \>\n $FORM{'username'}\n";
    &printEditForm;
    exit;
    
} elsif ($FORM{'action'} eq "delete") {

    $inputs = "<input type\=\"hidden\" name\=\"username\" value\=\"$FORM{'username'}\" \>\n";
    &saveDB(&readDB($FORM{'username'}, 'edit', $FORM{'name'}));
    $info   = &readDB($FORM{'username'}, 'get');
    &printSearchForm;
    exit;
    

} else {
    
    &runQuery if ($FORM{'keywords'});
    &prepareHTML;
    &printSearchForm;
    exit;
    
}
    
    exit;
    


################################################################################
sub runQuery {



    # Run initial search and get all documents
    local $query = "keywords\=".$FORM{'keywords'};
    $query .= "\&op\=73" if ($FORM{'sort'} eq "date");
    $query .= "\&op\=72" if ($FORM{'sort'} eq "relavancy");
    $query .= "\&op\=1"  if (!$FORM{'sort'});
    
    &getSearchResults($query);


}

##################################################################################
sub prepareHTML {

    $line = "";

    # get username, or make it hidden
    if (!$FORM{'username'}) {
	
	$inputs = "<p\>Username: <input type\=\"text\" name\=\"username\"\><\/p\>\n";
	# turn on BUY flag
	$buy = " \- <a href\=\"\#\"\>buy<\/a\>";
	
    } else {
	
	$inputs = "<input type\=\"hidden\" name\=\"username\" value\=\"$FORM{'username'}\" \>\n";
	$info   = &readDB($FORM{'username'}, 'get');
	
#	$info  .= "\n <li\><a href\=\"$thisScript?action\=savenew\&amp\;username=$FORM{'username'}\&amp\;keywords\=$FORM{'keywords'}\&amp\;terse\=$FORM{'terse'}\"\>save this search<\/a\><\/li\>\n" if ($FORM{'action'} ne "savedsearch" && @url);

	
    }
    
    local $terse   = "checked\=\"checked\"" if ($FORM{'terse'} eq "true");
    local $ck_rel  = "checked\=\"checked\"" if ($FORM{'sort'}  eq "relavancy");
    local $ck_date = "checked\=\"checked\"" if ($FORM{'sort'}  eq "date");
    local $st_date = "";
    if ($FORM{'datesortdirection'} eq "up" || $FORM{'sort'} eq "relavancy"  || !$FORM{'sort'}) {
        $st_date = "date <strong\>\&darr\;<\/strong\> <input type\=\"hidden\" name\=\"datesortdirection\" value\=\"down\" \/\>\n";
    } else {
        $st_date = "date <strong\>\&uarr\;<\/strong\> <input type\=\"hidden\" name\=\"datesortdirection\" value\=\"up\" \/\>\n";
    }
    

    $resultsDetail =<<EndofHTML if (@url);
<div id="resultsdetail">
  <h2>Current Results</h2>
  <ul>
    <li>Found $results{'total'} results</li>
    <li><input type="checkbox" name="terse" value="true" $terse />simple listings</li>
    <li>sort by <input type="radio" name="sort" value="relavancy" $ck_rel />relavancy <input type="radio" name="sort" value="date" $ck_date />$st_date</li>
    <li><a href="$thisScript?action=savenew&amp;username=$FORM{'username'}&amp;keywords=$FORM{'keywords'}&amp;terse=$FORM{'terse'}&amp;sort=$FORM{'sort'}">Save this search</a></li>
  </ul>
</div>
EndofHTML

    $keywordsDetail =<<EndofHTML if ($results{'keywords'});
<div id="keywordsdetail">
 <h2>Keywords</h2>
 <p>You might also like to try...</p>
 <ul>
  $results{'keywords'}
 </ul>
</div>

EndofHTML

    
    foreach $url (@url) {
    
	# alternate class on each list to allow alternating colors
	if ($c eq "even") {
	    $c = "odd";
	} else {
	    $c = "even";
	}
    
	if ($results{'topic'}{$url} !~ /Events/) {
	
	    # NOT an EVENT
	    $line .= <<EndofLine;
  <li class="$c">
<a href="$url" class="title"><strong>$results{'title'}{$url}</strong></a><br />
$results{'summary'}{$url}<br />

EndofLine

    if (!$FORM{'terse'}) {
	$line .= <<EndofLine;
<div class="detail">
$results{'topic'}{$url} - $results{'date'}{$url} - $results{'pages'}{$url} pages $buy<br />
Written by $results{'authors'}{$url}<br />
Browse Similar Research: $results{'browse'}{$url}
</div>
EndofLine
    
    } else {
    
    # terse
    $line .= <<EndofLine;
<div class="detail">
$results{'topic'}{$url} - $results{'date'}{$url} - $results{'pages'}{$url} pages - $results{'tersebrowse'}{$url} $buy<br />
</div>
EndofLine

}
	$line .= <<EndofLine;
</li>

EndofLine


} else {

    # an EVENT
	$eventsDetail .= <<EndofLine;
<div id="eventsdetail">
<h2>$results{'topic'}{$url}</h2>
<ul>
  <li>
<a href="$url"><strong>$results{'title'}{$url}</strong></a><br />
$results{'summary'}{$url}<br />
$results{'date'}{$url}<br />
  </li>
</ul>
</div>
EndofLine

	# undo the alternating cells thingy
	if ($c eq "even") {
	    $c = "odd";
	} else {
	    $c = "even";
	}

}

    }

    
}



##########################################################################
sub printRSS {

        # put dates into proper RSS 2.0 format
        use DateTime::Format::HTTP;
        my $dt = 'DateTime::Format::HTTP';

	foreach $url (@url) {
	    
	    local ($d, $m, $y) = split(/ /, $results{'date'}{$url});
	    $m = substr($m, 0, 3);
	    
	    local $pubdate = "$d $m $y";
	    
	    local $datestring = $dt->parse_datetime($pubdate, 'GMT');
	    local $dateStr = $dt->format_datetime($datestring);
	    
	    $rss .= "<item>\n  <title><![CDATA[$results{'title'}{$url}]]></title>\n  <description><![CDATA[$results{'summary'}{$url}]]></description>\n  <pubDate>$dateStr</pubDate>\n  <link><![CDATA[http://www.gartner.com$url]]></link>\n</item>\n";
	    
	#    $rss =~ s/\&(?!amp)/\&amp\;/g;
	}
	
	$date          = `date +'%a, %d %b %Y %T GMT'`;
	
	print <<EndofText;
Content-type: text/plain

<?xml version="1.0" ?>
  <rss version="2.0" xmlns:blogChannel="http://backend.userland.com/blogChannelModule">
  <channel>
  <title>Gartner Search -- $FORM{'keywords'}</title>
  <link>http://www.gartner.com/</link>
  <description>Dynamic search of gartner.com based on $FORM{'keywords'} -- there were $results{'total'} results -- brought to you by Gartner, the world's leading IT research and advisory firm.</description>
  <language>en-us</language>
  <copyright>Copyright 2004 Gartner, Inc. and/or its Affiliates. All Rights Reserved. </copyright>
  <lastBuildDate>$date</lastBuildDate>
  <webMaster>peter.mahnke\@gartner.com</webMaster>
  <image>
    <url><![CDATA[http://regionals4.gartner.com/pages/docs/exp/images/dbd/gartner_logo.gif]]></url>
    <width>76</width>
    <height>19</height>
    <link><![CDATA[http://www.gartner.com]]></link>
    <title>Gartner</title>
  </image>
  <ttl>120</ttl>
  <skipDays><day>Saturday</day><day>Sunday</day></skipDays>
  <skipHours><hour>1</hour><hour>2</hour><hour>3</hour><hour>4</hour><hour>5</hour><hour>6</hour><hour>19</hour><hour>20</hour><hour>21</hour><hour>22</hour><hour>23</hour><hour>24</hour></skipHours>
<item>
  <title>Gartner Security Summit</title>
  <description>Learn how to protect your datacenter from inside and out.</description>
  <pubDate>$date</pubDate>
  <link><![CDATA[http://gartner.com/events/secuity.html]]></link>
</item>
$rss
 </channel>
</rss>
EndofText

	

}    

##############################################################################
sub printSearchForm {

    print <<EndofHTML;
Content-type: text/html

<html>
 <head>
<title>Peter's Simple Search</title>

<link rel="stylesheet" href="/css/newSearch.css" type="text/css">

<style type="text/css">
</style>

<script type="text/javascript">

</script>

</head>

<body>
    <form method="post" name="frmSearch">
<div id="container">

  <div id="searchform">

    $inputs 
    <p><img src="http://regionals4.gartner.com/pages/docs/exp/images/dbd/gartner_logo.gif" hspace="20" vspace=""width="76" height="19" alt="Gartner Logo" />
    <input type="text" size="27" maxlength="400" name="keywords" value="$FORM{'keywords'}" />
    <input type="submit" value="search" class="submit" /><br />
    </p>
  
  </div><!-- END div search form -->


  <div id="sidebar">

    $resultsDetail

    <div id="info">
      $infoTitle
       <ul>
        $info
        $savethissearch
       </ul>
    </div><!-- END div info -->
    
    $keywordsDetail
    
    $eventsDetail

  </div><!-- END div sidebar -->

  <div id="content">
    <ul>
      $line
    </ul>
  </div><!-- END div content -->
  
  <div id="footer">
<!--
    <p><img src="http://regionals4.gartner.com/pages/docs/exp/images/dbd/gartner_logo.gif" hspace="20" vspace=""width="76" height="19" alt="Gartner Logo" />
    <input type="text" size="27" maxlength="400" name="keywords" value="$FORM{'keywords'}" />
    <input type="submit" style="position:relative;top:2;font:9pt;" value="search" /><br />
    </p>
-->
  </div><!-- END div footer -->

  
  <p class="buffer">$buffer</p>
  
</div><!-- END div container -->
  </form>
</body>
</html>
EndofHTML

}



############################################################################################
sub readDB {
    
    local $info;

    open(FILE, "/home/gartner/html/rt/content/newSearch.db") || die "Can't open db";
    
    while (<FILE>) {

	chop();
	
	local ($u, $n, $q) = split(/\t/);
	
	if ($_[1] eq "get") {
	    
	    # display mode
	    
	    $info .= "<li\>$n :: 
<a href\=\"$thisScript?$q\&amp\;username=$FORM{'username'}\&amp\;action=savedsearch\"\>search<\/a\> : 
<a href\=\"$thisScript?$q\&amp\;username=$FORM{'username'}\&amp\;rss\=true\"\>rss<\/a\> : 
<a href\=\"$thisScript?$q\&amp\;name\=$n\&amp\;username=$FORM{'username'}\&amp\;action\=edit\"\>edit<\/a\> :
<a href\=\"$thisScript?$q\&amp\;name\=$n\&amp\;username=$FORM{'username'}\&amp\;action\=delete\"\>delete<\/a\>
<\/li\>\n" if ($_[1] eq "get" && $u eq $_[0] && $_[0]);
	
	} elsif ($_[1] eq "edit") {
	    
	    # edit mode -- grab everyting except the one you are editing
	    if ($u eq $_[0] && $n eq $_[2] && ($FORM{'oldname'} || $FORM{'action'} eq "delete")) {
		
		# this is the one you are editing, so ignor
		next;
		
	    } else {
		
		$info .= "$_\n"; 

	    }
	    
	} else {
	    
	    # get all
	    $info .= "$_\n";

	}
    }
    
    close(FILE);
    
    $infoTitle = "<h2\>Saved Searches<\/h2\>" if ($_[1] eq "get");


    return($info);

}


##################################################################################
sub saveDB {

    # saves the database
    # input is the old database, without the edited listing
    # uses Form inputs for rest
    
    local $terse = "\&amp\;terse\=true"        if ($FORM{'terse'} eq "true");
    local $sort  = "\&amp\;sort=$FORM{'sort'}" if ($FORM{'sort'});

    open(FILE, ">/home/gartner/html/rt/content/newSearch.db") || die "Can't open db";
    
    print FILE $_[0];
    print FILE "$FORM{'username'}\t$FORM{'name'}\tkeywords\=$FORM{'keywords'}$terse$sort\n" if ($FORM{'action'} eq "save"); # don't save deleted information
    
    close(FILE);

    return();

}




##############################################################################
sub printEditForm {

    local $terse = "checked\=\"checked\""   if ($FORM{'terse'} eq "true");
    local $ck_rel  = "checked\=\"checked\"" if ($FORM{'sort'}  eq "relavancy" || !$FORM{'sort'});
    local $ck_date = "checked\=\"checked\"" if ($FORM{'sort'}  eq "date");

    print <<EndofHTML;
Content-type: text/html

<html>
 <head>
<title>Peter's Simple Search</title>

<link rel="stylesheet" href="/css/newSearch.css" type="text/css">

<style type="text/css">

</style>

<script type="text/javascript">

</script>

</head>

<body>
<div class="searchform">
<form method="post" name="frmSearch">
$inputs 
<p><img src="http://regionals4.gartner.com/pages/docs/exp/images/dbd/gartner_logo.gif" hspace="20" vspace=""width="76" height="19" alt="Gartner Logo" /></p>
<p>Name: <input type="text" size="27" maxlength="400" name="name" value="$FORM{'name'}" /></p>
<p>Search Term: <input type="text" size="27" maxlength="400" name="keywords" value="$FORM{'keywords'}" /></p>
<p>Terse Listings: <input type="checkbox" name="terse" value="true" $terse /> yes</p>
<p>Sort Listings: <input type="radio" name="sort" value="relavancy" $ck_rel />relavancy <input type="radio" name="sort" value="date" $ck_date />date</p>
<p><input type="submit" style="position:relative;top:2;font:9pt;" name="action" value="save" /></p>
</form>
</div>

<div id="info">
$info
</div>

<p class="buffer">$buffer</p>

</body>
</html>
EndofHTML

}
