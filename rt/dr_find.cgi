#!/usr/local/bin/perl



use lib '/usr/local/lib/perl5/site_perl/5.6.1/';


use Carp;
no Carp::Assert;

##############################################################
# Get the input from the HTML Form
##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {


	# something submitted

	use CGI_Lite;
	$cgi = new CGI_Lite;

	%FORM = $cgi->parse_form_data;


} else {

	# nothing submitted
	print <<EndofHTML;
Content-Type: text/html

<html>
    <head>
    </head>
    <body>
<form method="get">
<input type="text" name="resId" />
<input type="submit" name="page" value="getDoc" />
</form>
<p><a href="?page=search&amp;catagory=Asset+Management">Asset Management - search layout (node 7090 - 7019 for software?)</a></p>
<p><a href="?page=search&amp;catagory=Business+Intelligence">Bus Intel - search layout (node 6764)</a></p>
<p><a href="?page=search&amp;catagory=CRM">CRM - search layout (node 3826)</a></p>
<p><a href="?page=search&amp;catagory=Data+Center">Data Center - search layout (node 6823)</a></p>
<p><a href="?page=search&amp;catagory=Mobile+&amp;+Wireless">Mobile &amp; Wireless - search layout (node 7259)</a></p>
<p><a href="?page=search&amp;catagory=Security">Security - search layout (node 6899 - strat 6753?)</a></p>
<p><a href="?page=search&amp;catagory=Sourcing">Sourcing - search layout (node 6708)</a></p>
<p><a href="?page=search&amp;catagory=Web+Services">Web Services - search layout (node 7189)</a></p>

    </body>
</html>
EndofHTML

	exit;
}


#############################################
# what to do
#
if ($FORM{'page'} eq "getDoc") {
	&findDB($FORM{'resId'});
	&format;
	&printOutput;
	exit;
} elsif ($FORM{'page'} eq "search") {
	&readDB;
	&formatSearch;
	&printSearchOutput;
	exit;
} elsif ($FORM{'page'} eq "detail") {
	&findDB($FORM{'resId'});
	&formatDetail;
	&printDetailOutput;
	exit;
} elsif ($FORM{'page'} eq "package") {
	&printPackage;
	exit;
} elsif ($FORM{'page'} eq "special") {
	&printSpecial;
	exit;
} elsif ($FORM{'search'}) {
	local $found;
	local %search;
	local @results = &searchDB($FORM{'search'});
	if (!@results) {
		# nothing returned
		$searchLayout .= "<h3>Search: Nothing Returned<\/h3>\n\n";
	} else {
		foreach (@results) {
			local $rId = $1 if (/resId\=(\d\d\d\d\d\d)/);
			$search{$rId} = 1;
		}
		foreach $rId (keys %search) {
			carp "dr_find: finding search result: $rId\n";
			&findDB($rId);
			$found++;
		}
		$searchLayout .= "<h2>Search: $FORM{'search'} [$found docs]<\/h2>\n\n";
		&formatSearch;
	}
	&printSearchOutput;
	exit;
}

exit;

#############################################
sub searchDB {

	carp "dr_find: searchDB: string: $_[0]\n";

	local @results = `grep \-i \"$_[0]\" /home/gartner/html/rt/content/dr.csv`;

	carp "dr_find: searchDB: results: $#results\n";

	return(0) if (!@results);
	return (@results);
}

#############################################
sub formatSearch {

	local $c  = 1;
	local $fc = 1;
	foreach $resId ( sort {$docType{$a} cmp $docType{$b} } keys %docType) {

		if ($docType{$resId} ne $prevDocType && $c) {

			&printSearchSection($c);
			$searchLayoutLeft  = "";
			$searchLayoutRight = "";
			$c = 0;

		}
		$c++;
		$fc++;

		if ($c % 2 != 0) {

			$searchLayoutLeft .=<<EOF;

	<p class="department">In $catagory{$resId}</p>
	<p class="type">$docType{$resId}</p>
	<p class="title">$title{$resId}</p>
	<p class="summary">$summary{$resId}</p>
	<p class="price">PRICE: \$$price{$resId}</p>
        <p class="cartLink"><a href="http://www4.gartner.com/DisplayDocument?id=$resId&amp;ref=g_search" target="_blank">ADD TO CART</a> | <a href="?page=detail&resId=$resId">REPORT DETAIL</a></p>

EOF
		} else {

			$searchLayoutRight .=<<EOF;

	<p class="department">In $catagory{$resId}</p>
	<p class="type">$docType{$resId}</p>
	<p class="title">$title{$resId}</p>
	<p class="summary">$summary{$resId}</p>
	<p class="price">PRICE: \$$price{$resId}</p>
        <p class="cartLink"><a href="http://www4.gartner.com/DisplayDocument?id=$resId&amp;ref=g_search" target="_blank">ADD TO CART</a> | <a href="?page=detail&resId=$resId">REPORT DETAIL</a></p>

EOF
		}
		$prevDocType = $docType{$resId};
		$catagory = $catagory{$resId};
	}
	$fc--;
	&printSearchSection($c);
	$searchLayout .=<<EOF;
  <tr><td colspan="3"><h3>[total $fc docs]</h3></td></tr>
EOF
}

sub printSearchSection {

	return() if (!$searchLayoutRight && !$searchLayoutLeft);

	# new doctype, add line
	$searchLayout .=<<EOF;
  <tr><td colspan="3"><h3>$prevDocType [$_[0] docs]</h3></td></tr>
  <tr>
    <td width="250" valign="top">

      <div id="left">$searchLayoutLeft</div>

    </td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">

      <div id="right">$searchLayoutRight</div>

    </td>
  </tr>
  <tr><td colspan="3" class="morelink"><a href="?page=search&amp;catagory=$catagory&amp;docType=$prevDocType">See all $prevDocType documents in $catagory</a><br /></td></tr>
EOF
}

#############################################
sub formatDetail {

	$detailLayout .=<<EOF;

	<p class="type">$docType{$FORM{'resId'}}</p>
	<p class="title">$title{$FORM{'resId'}}</p>
	<p class="summary">$summary{$FORM{'resId'}}</p>
	<p class="authors">Written by $author{$FORM{'resId'}}</p>
	<p class="date">Published on $date{$FORM{'resId'}}</p>
	<p class="pages">$pages{$FORM{'resId'}} pages</p>
	<p class="price">PRICE: \$$price{$FORM{'resId'}}</p>
	<p class="cartLink"><a href="http://www4.gartner.com/DisplayDocument?id=$FORM{'resId'}&amp;ref=g_search" target="_blank">ADD TO CART</a></p>
        $toc{$FORM{'resId'}}

EOF

}

#############################################
sub format {

	$searchLayout .=<<EOF;

	<p class="department">In $catagory{$FORM{'resId'}}</p>
	<p class="type">$docType{$FORM{'resId'}}</p>
	<p class="title">$title{$FORM{'resId'}}</p>
	<p class="summary">$summary{$FORM{'resId'}}</p>
	<p class="price">PRICE: \$$price{$FORM{'resId'}}</p>
        <p class="cartLink"><a href="http://www4.gartner.com/DisplayDocument?id=$FORM{'resId'}&amp;ref=g_search" target="_blank">ADD TO CART</a></p>

EOF

	$packageLayout .=<<EOF;

	<p class="type">$docType{$FORM{'resId'}}</p>
	<p class="title">$title{$FORM{'resId'}}</p>
	<p class="summary">$summary{$FORM{'resId'}}</p>
	<p class="authors">Written by $author{$FORM{'resId'}}</p>
	<p class="date">Published on $date{$FORM{'resId'}}</p>
	<p class="pages">$pages{$FORM{'resId'}} pages</p>
	<p class="price">PRICE: \$$price{$FORM{'resId'}}</p>
	<p class="cartLink"><a href="http://www4.gartner.com/DisplayDocument?id=$FORM{'resId'}&amp;ref=g_search" target="_blank">ADD TO CART</a></p>

EOF

	$detailLayout .=<<EOF;

	<p class="type">$docType{$FORM{'resId'}}</p>
	<p class="title">$title{$FORM{'resId'}}</p>
	<p class="summary">$summary{$FORM{'resId'}}</p>
	<p class="authors">Written by $author{$FORM{'resId'}}</p>
	<p class="date">Published on $date{$FORM{'resId'}}</p>
	<p class="pages">$pages{$FORM{'resId'}} pages</p>
	<p class="price">PRICE: \$$price{$FORM{'resId'}}</p>
	<p class="cartLink"><a href="http://www4.gartner.com/DisplayDocument?id=$FORM{'resId'}&amp;ref=g_search" target="_blank">ADD TO CART</a></p>
        $toc{$FORM{'resId'}}

EOF


}

#############################################
sub printDetailOutput {

	&printTop($catagory{$FORM{resId}});

	if ($docType{$FORM{'resId'}} eq "Magic Quadrant") {
		print <<EOF;
<div class="marketing">
  <h3>$docType{$FORM{'resId'}}</h3>
  <img src="http://regionals.gartner.com/regionalization/img/gpress/mq_icon.gif" width="229" height="240" alt="" align="left" />
  <p>Gartner Magic Quadrants provide a snapshot of how vendors are performing in a market segment and highlight the leaders to show how others compare.</p>
  <p>Magic Quadrants help you make better informed decisions on companies you are looking to partner with, or whose services or products you want to buy.</p>
</div>
EOF
		$toc{$FORM{resId}} =<<EOF;
  <div class="toc">
    <p>Typical Table of Contents </p>
    <ul>
      <li>Market Overview &amp; Trends</li>

      <li>Magic Quadrant Criteria</li>

      <ul>
         <li>Leaders</li>
           <ul>
             <li><i>Vendors in the Leaders segment are most likely to have high revenue in this market, high market share and products that are of interest to a wide audience.</i></li>
           </ul>

         <li>Challengers</li>
           <ul>
             <li><i>Challengers have focused significant resources on this market, but they have a narrower understanding of the market and a less-impressive product strategy, or they have deliberately chosen to limit the scope of their product lines.</i></li>
           </ul>

         <li>Visionaries</li>
           <ul>
             <li><i>Visionaries understand the market and customer requirements well, but have fewer assets committed to the pursuit of this particular market than the leaders.</i></li>
           </ul>

         <li>Niche Players</li>
           <ul>
             <li><i>Niche Players are limited to a particular geographical or industry segment, or have a smaller range of features or resources that, taken together, preclude them from competing across the board in many major segments of the integration market.</i></li>
           </ul>
       </ul>
    </ul>
</div>

EOF

	} elsif ($docType{$FORM{'resId'}} eq "Hype Cycle") {
		print <<EOF;
<div class="marketing">
  <h3>$docType{$FORM{'resId'}}</h3>
  <img src="http://www4.gartner.com/hc/images/graph_hc.gif" width="168" height="93" alt="" align="left" />
  <p>A Hype Cycle is a graphic representation of the maturity, adoption and business application of specific technologies.</p>
  <p>Since 1995, Gartner has used Hype Cycles to characterize the over-enthusiasm or "hype" and subsequent disappointment that typically happens with the introduction of new technologies. Hype Cycles also show how and when technologies move beyond the hype, offer practical benefits and become widely accepted.</p>
</div>
EOF
		$toc{$FORM{resId}} =<<EOF;
  <div class="toc">
   <p>What are the 5 phases of a Hype Cycle?</p>
    <ul>
      <li>Technology Trigger</li>
      <ul>
        <li>The first phase of a Hype Cycle is the "technology trigger" or breakthrough, product launch or other event that generates significant press and interest.</li>
      </ul>

      <li>Peak of Inflated Expectations</li>
      <ul>
        <li>In the next phase, a frenzy of publicity typically generates over-enthusiasm and unrealistic expectations. There may be some successful applications of a technology, but there are typically more failures.</li>
      </ul>

      <li>Trough of Disillusionment</li>
      <ul>
        <li>Technologies enter the "trough of disillusionment" because they fail to meet expectations and quickly become unfashionable. Consequently, the press usually abandons the topic and the technology.</li>
      </ul>

      <li>Slope of Enlightenment</li>
      <ul>
        <li>Although the press may have stopped covering the technology, some businesses continue through the "slope of enlightenment" and experiment to understand the benefits and practical application of the technology.</li>
      </ul>

      <li>Plateau of Productivity</li>
      <ul>
        <li>A technology reaches the "plateau of productivity" as the benefits of it become widely demonstrated and accepted. The technology becomes increasingly stable and evolves in second and third generations. The final height of the plateau varies according to whether the technology is broadly applicable or benefits only a niche market.</li>
      </ul>
    </ul>

  </div>
EOF

	} elsif ($docType{$FORM{'resId'}} eq "Vendor Rating") {
		print <<EOF;
<div class="marketing">
  <h3>Vendor Rating</h3>
  <img src="http://intl.gartner.com/img/vendorrating_icon.gif" width="220" height="213" alt="" align="left" />
  <p>Gartner Vendor Ratings provide clear, concise indicators of each vendor's overall status and the status of such initiatives as strategy, organization, products, technology, marketing, financials and support.</p>
  <p>Gartner's vendor ratings focus on the vendor as a whole, not just on its position within a single market. Gartner's vendor ratings provide: end-user organizations with a holistic view of vendors from which they are purchasing products and services, financial investors with an independent and complete view of a vendor's strengths and challenges areas, and vendors with a total view of their potential partners, competitors and suppliers.</p>
</div>
EOF

	$toc{$FORM{resId}} =<<EOF;

  <div class="toc">
   <p>Vendor Rating Coverage Catagories</p>
<ul>
<li>Corporate Viability
<ul>
<li>Strategy </li>
<li>Financial</li>
<li>Marketing </li>
<li>Organization </li>
</ul>
</li>
<li>Product/Services/Technologies
<ul>
<li>Product/Service </li>
<li>Technology </li>
<li>Pricing </li>
</ul>
</li>
<li>Customer Service/Product Support
<ul>
<li>Sales/Distribution</li>
<li>Support Services</li>
</ul>
</li>
</ul>

    <p>Ratings Definitions</p>
<ul>
<li>Strong positive
<ul>
<li><i>Proves itself as a solid provider of strategic products, services or solutions. Gartner advises IT users to continue investing in that vendor&#8217;s products and solutions; potential users of the vendor&#8217;s products and technology should consider this vendor a strong strategic choice. For investors, the vendor represents a low-risk investment opportunity, from a technology standpoint.</i></li>
</ul>
</li>
<li>Positive
<ul>
<li><i>Demonstrates strength in specific areas, but is largely opportunistic. Gartner advises IT users to continue incremental investments; potential users of the vendor&#8217;s products and technology should put this vendor on a shortlist of tactical alternatives. Investors should consider the opportunity as short-term, focusing on exit scenarios.</i></li>
</ul>
</li>
<li>Promising
<ul>
<li><i>Shows potential in specific areas; however, the initiative or vendor has not fully evolved or matured. Gartner cautions users to watch for a change in status and consider scenarios for short- and long-term impact; potential users of the vendor&#8217;s products and technology should plan for, and be aware of, issues and opportunities that are related to the evolution and maturity of this initiative or vendor. For investors, this represents niche opportunities or medium- or high-risk investments.</i></li>
</ul>
</li>
<li>Caution
<ul>
<li><i>Faces challenges in one or more areas. Gartner advises IT users to understand challenges in relevant areas and assess short- and long-term benefits and risks to determine if contingency plans are needed. Potential users of the vendor&#8217;s products and technology &#8212; and investors &#8212; should note the vendor&#8217;s challenges as part of due diligence. The vendor faces challenges in one or more areas.</i></li>
</ul>
</li>
<li>Strong negative
<ul>
<li><i>Indicates difficulty in responding to problems in multiple areas. Gartner advises users to exit immediately; potential users of the vendor&#8217;s products and technology should consider this vendor only if there are no alternatives. Investors are advised to stay away.</i></li>
</ul>
</li>
</ul>


  </div>


EOF


	} elsif ($docType{$FORM{'resId'}} =~ /(Market|Dataquest|Focus Report)/) {
		print <<EOF;
<div class="marketing">
  <h3>$docType{$FORM{'resId'}}</h3>
  <img src="http://regionals4.gartner.com/regionalization/img/content/20031219_fp_header_left.jpg" width="262" height="195" alt="" align="left" />
  <p>Gartner $docType{$FORM{'resId'}} documents provide detailed Vendor information.</p>
  <p>You can expect to find that Analysts are free with their use of industry buzzwords and are quiet willing to leave questions unanswered.</p>
</div>
EOF

	} elsif ($docType{$FORM{'resId'}} eq "") {
		print <<EOF;
<div class="marketing">
  <h3>Product Details</h3>
  <img src="http://www4.gartner.com/regionalization/img/content/20040220_fp_header_left.jpg" width="175" height="175" alt="" align="left" />
  <p>Gartner Market Analysis documents provide strategic information.</p>
  <p>You can expect to find that Analysts are free with their use of industry buzzwords and are quiet willing to leave questions unanswered.</p>
</div>
EOF

	} elsif ($docType{$FORM{'resId'}} eq "") {
		print <<EOF;
<div class="marketing">
  <h3>Product Details</h3>
  <img src="http://www4.gartner.com/regionalization/img/content/20040220_fp_header_left.jpg" width="175" height="175" alt="" align="left" />
  <p>Gartner Market Analysis documents provide strategic information.</p>
  <p>You can expect to find that Analysts are free with their use of industry buzzwords and are quiet willing to leave questions unanswered.</p>
</div>
EOF

	} else {
		print <<EOF;
<div class="marketing">
  <h3>$docType{$FORM{'resId'}}</h3>
  <img src="http://regionals4.gartner.com/regionalization/img/content/20031306_fp_header_left.jpg" width="262" height="195" alt="" align="left" />
  <p>Gartner Research and Analysis documents provide strategic information.</p>
  <p>You can expect to find that Analysts are free with their use of industry buzzwords and are quiet willing to leave questions unanswered.</p>
</div>
EOF

	}

	print <<EOF;
 <div class="package">
	<p class="title">$title{$FORM{'resId'}}</p>
	<p class="summary">$summary{$FORM{'resId'}}</p>
	<p class="authors">Written by $author{$FORM{'resId'}}</p>
	<p class="date">Published on $date{$FORM{'resId'}}</p>
	<p class="pages">$pages{$FORM{'resId'}} pages</p>
	<p class="price">PRICE: \$$price{$FORM{'resId'}}</p>
	<p class="cartLink"><a href="http://www4.gartner.com/DisplayDocument?id=$FORM{'resId'}&amp;ref=g_search" target="_blank">ADD TO CART</a></p>
        $toc{$FORM{'resId'}}
 </div>
EOF

	&printBottom;
}

#############################################
sub printSearchOutput {

	local $topAction = "Search Results: $FORM{'search'}" if ($FORM{'search'});
	local $topAction = "Catagory: $FORM{'catagory'} \[$FORM{'docType'}\]";

	&printTop($topAction);

	print <<EOF;
 <div class="searchpackage">
 <table width="505">
    $searchLayout
    <!--
     <td width="250" valign="top">

      <div id="left">$searchLayoutLeft</div>

    </td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">

      <div id="right">$searchLayoutRight</div>

    </td>
  </tr>
  -->
  </table>
  </div>
EOF
	&printBottom;
}



#############################################
sub printOutput {

    print <<EndofHTML;
Content-Type: text/html

<html>
<head>
  <title>DR Output Test - $resId</title>
  <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
  <link href="http://intl.gartner.com/css/dr.css" rel="stylesheet" type="text/css">
</head>
<body>

 <h1>Research Collection Search Results</h1>

<p>$msg</p>

<h3>search layouts</h3>

$searchLayout


<h3>package layouts</h3>
$packageLayout


<h3>detail layouts</h3>
$detailLayout

</body>
</html>
EndofHTML


}






##################################################################################
sub findDB {

	local $line = `grep $_[0] /home/gartner/html/rt/content/dr.csv`;

	return(0) if (!$line);

	# catagory=$FORM{'PRM'}|resid=$resId{$FORM{'resId'}}|notenumber=$noteNumber{$FORM{'resId'}}|title=$title{$FORM{'resId'}}|date=$date{$FORM{'resId'}}|author=$author{$FORM{'resId'}}|summary=$summary{$FORM{'resId'}}|price=$price{$FORM{'resId'}}|pages=$pages{$FORM{'resId'}}|type=$docType{$FORM{'resId'}}|toc=$toc{$FORM{'resId'}}\n

	$line = $1 if ($line =~ /(.[^\n]*)/);

	local @pairs = split (/\|/, $line, 11);

	local $rId = $1 if ($line =~ /resId\=(\d\d\d\d\d\d)/);

	foreach (@pairs) {
		local ($name, $value) = split("\=", $_, 2);
		$$name{$rId} = "$value";
	}

	return(1);

}









##################################################################################
sub readDB {

	open (DB, "/home/gartner/html/rt/content/dr.csv");

	while (<DB>) {

		chop();

		# catagory=$FORM{'PRM'}|resid=$resId{$FORM{'resId'}}|notenumber=$noteNumber{$FORM{'resId'}}|title=$title{$FORM{'resId'}}|date=$date{$FORM{'resId'}}|author=$author{$FORM{'resId'}}|summary=$summary{$FORM{'resId'}}|price=$price{$FORM{'resId'}}|pages=$pages{$FORM{'resId'}}|type=$docType{$FORM{'resId'}}|toc=$toc{$FORM{'resId'}}\n

		next if ($_ !~ /catagory\=$FORM{'catagory'}/ && $FORM{'catagory'});
		next if ($_ !~ /docType\=$FORM{'docType'}/ && $FORM{'docType'});

		local @pairs = split (/\|/);

		local $rId = $1 if (/resId\=(\d\d\d\d\d\d)/);

		foreach (@pairs) {
			local ($name, $value) = split("\=", $_, 2);
			$$name{$rId} = $value;

		}
	}

	close(DB);

	return();

}



#############################################
sub printTop {


    print <<EOF;
Content-Type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<title>Untitled Document</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="/css/digital_home.css" rel="stylesheet" type="text/css">
<link href="/css/dr_IAN.css" rel="stylesheet" type="text/css">
</head>

<body>
<form method="get">
<!-- start start main table -->
<div id="maintableframe">
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
  <tr>
    <td valign="top">
	<!-- end start of main table -->


	<!-- start header -->

	<div id="welcometop">
	<table width="100%" border="0" cellspacing="0" cellpadding="0">

  <tr>
    <!-- start nav title -->
    <td valign="top" width="45%">

    <div class="logo"><img src="/images/glogo_bg.gif" alt="" width="125" height="29" /></div>

    <!-- div class="topnavpackagelgtitle">Welcome to the Gartner Store</div -->

    </td>
	<!-- end nav title -->



	<!-- start search text -->
	<td valign="top" width="20%" align="right">

	 <div class="searchboxtext">Search Store</div>


	</td>
	<!-- end search text-->


	<!-- start search -->
	<td valign="top" width="25%">


	<div id="searchbox"><input type="text" name="search" value="$FORM{'search'}" size="35" /></div>

	</td>
	<!-- end search -->


	<!-- start search go-->
	<td valign="top" width="10%">


	<div class="searchboxtext"><input type="submit" name="page" value="GO" /></div>

	</td>
	<!-- end search go -->

  </tr>

</table>
        </div>


	<!-- end header -->




	<!-- start banner-->
		<table width="100%" border="0" cellspacing="0" cellpadding="0">

  <tr>

   <td valign="top">
	<div id="bannerleft"><img src="/images/bannertext.gif" alt="" width="284" height="185" /></div>
	</td>

    <td valign="top">
	<div id="bannerright"><img src="/images/keyboard.jpg" alt="" width="423" height="185" /></div>
	</td>



  </tr>
</table>
	 <!-- end banner -->







 <!-- start vspacing box -->


	<!-- <div class="vspacing"> </div> -->


	  <!-- end vspacing box -->



<div class="maintablebgcolour">


	<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
  <!-- start sign in-->
    <td valign="top" width="100%">

	<ul class="signinbackground">
	<li class="signin"><a href="" class="signinlink">Sign In</a></li>
	<li class="signin"><a href="" class="signinlink">Register</a></li>
	<li class="signin"><a href="" class="signinlink">View Privacy Policy</a></li>
	</ul>

	</td>
    <!-- end sign in -->


  </tr>
</table>



 <!-- start vspacing box -->


	<div class="vspacing"> </div>


	  <!-- end vspacing box -->




	<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>
 <!-- start shopping cart/breadcrumb -->
	<td valign="top">

	<div class="crumbleft">SHOPPING CART: 0 items | Customer Service</div>

	</td>
	<!-- end shopping cart/breadcrumb -->


	<!-- start main breadcrumb/title -->
	<td valign="top" align="right"><div class="crumbright">Gartner Store | $_[0]</div></td>
	<!-- start main breadcrumb/title -->
  </tr>
</table>



 <!-- start vspacing box -->


	<div class="vspacing"> </div>


	  <!-- end vspacing box -->




<table width="100%" border="0" cellspacing="0" cellpadding="0">
  <tr>

    <td valign="top">



	<div class="navbgcolour">

	<!--div class="navtoptitle">BROWSE DEPARTMENTS</div-->

	 <!-- start nav box -->

	<div class="navlgtitle">Key Topics:</div>


	<div class="pod">

	<ul class="nav-pod">
          <li class="nav1"><a href="?page=search&amp;catagory=Asset+Management">Asset Management</a></li>
          <li class="nav2"><a href="?page=search&amp;catagory=Business+Intelligence">Business Intelligence</a></li>
          <li class="nav3"><a href="?page=search&amp;catagory=CRM">CRM</a></li>
          <li class="nav4"><a href="?page=search&amp;catagory=Data+Center">Data Center</a></li>
          <li class="nav5"><a href="?page=search&amp;catagory=Mobile+&amp;+Wireless">Mobile &amp; Wireless</a></li>
          <li class="nav6"><a href="?page=search&amp;catagory=Security">Security</a></li>
          <li class="nav7"><a href="?page=search&amp;catagory=Sourcing">Sourcing</a></li>
          <li class="nav8"><a href="?page=search&amp;catagory=Web+Services">Web Services</a></li>
	</ul>
	</div>

	</div>

<!--	<div class="navbgcolour">

	<div class="navlgtitle">Search:</div>
        <div class="pod">

	<ul class="nav-pod">
          <li class="nav1"><input type="text" name="search" /><li>
          <li class="nav2"><input type="submit" name="page" value="Search" /><li>
	</ul>
	</div>

	</div>
-->
		<div class="navbgcolour">

	 <!-- start nav box -->
	<div class="navlgtitle">Market Analysis:</div>



	<div class="pod">

	<ul class="nav-pod">
	<li class="nav1"><a href="">Magic Quadrants</a></li>
	<li class="nav2"><a href="">Hype Cycles</a></li>
	<li class="nav3"><a href="">Vendor Ratings</a></li>
	</ul>
	</div>

	</div>



		<div class="navbgcolour">

	 <!-- start nav box -->
	<div class="navlgtitle">Market Statistics:</div>


	<div class="pod">

	<ul class="nav-pod">
	<li class="nav1"><a href="">Vertical Industry 1</a></li>
	<li class="nav2"><a href="">Vertical Industry 2</a></li>
	<li class="nav3"><a href="">Vertical Industry 3</a></li>
	<li class="nav4"><a href="">Vertical Industry 4</a></li>
	<li class="nav5"><a href="">Vertical Industry 5</a></li>
	<li class="nav6"><a href="">Vertical Industry 6</a></li>
	</ul>
	</div>

	</div>




	</td>
	<!-- end nav box -->


	<!-- start content area -->
    <td valign="top" width="100%">

EOF

}

#############################################
sub printBottom {



    print <<EOF;
	<!-- end content area -->



  </tr>
</table>



<!-- start footer -->


	<div id="footer">
	<table width="100%" border="0" cellspacing="0" cellpadding="0">

  <tr>
    <!-- start footer title -->
    <td valign="top" width="60%">

    <div class="logo"> </div>



    </td>
	<!-- end footer title -->



	<!-- start footerlink -->
	<td valign="top" width="20%">

	 <div class="footerposition"><a class="footerlink" href="">Privacy Policy</a></div>


	</td>
	<!-- end footerlink -->


	<!-- start footerlink -->
	<td valign="top" width="20%">


	<div class="footerposition"><span class="footertext">back to </span><a class="footerlink" href="">Gartner.com</a></div>

	</td>
	<!-- end footerlink -->




  </tr>

</table>
        </div>

<!-- end footer -->




	</div>


	<!-- start end of main table -->
	</td>
  </tr>
</table>
</div>
<!-- end end of main table -->
</form>
</body>
</html>

EOF

}

########################################
sub printPackage {

	&printTop('Sourcing');

	print <<EOF;
<div class="marketing">
  <h3>Successful IT Outsourcing</h3>
  <img src="http://regionals4.gartner.com/regionalization/img/gpress/03_cover_out.jpg" width="160" height="160" alt="" align="left" />

<p>Your complete guide to creating an <strong>Effective Sourcing Strategy</strong></p>
<p>Successful IT Outsourcing can help your organization build effective sourcing and relationship management strategies and avoid costly mistakes.</p>
<p>Gartner&#8217;s latest Executive Report has almost 300 pages containing all the research, tips and techniques needed to develop a best-in-class IT outsourcing strategy and avoid costly mistakes.</p>
<p class="price">PRICE: \$1,000</p>
<p class="cartLink"><a href="buy?id=$_[0]">ADD TO CART</a> | <a href="?page=detail&resId=$_[0]">REPORT DETAIL</a></p>
</div>

<div class="marketing">
<h3>Gartner March Sourcing Special</h3>

<table><tr><td valign="top"><img src="/img/20030718_fp_header_left-thumb.jpg" width="100" height="72" alt="two women drinking coffee ;-)" /></td><td>The desire to control and cut IT costs has driven many enterprises across Europe to outsource. However, Gartner research reveals that the total cost of IT outsourcing is often underestimated, and initial cost reductions do not always lead to lower costs over the length of the contract. As a result&#8230;</td></tr></table>
<p class="summary"><strong>We have selected the most important documents to start you on your way.</strong></p>
<p class="summary"><strong>Get 4 reports for the price of 3!</strong></p>
<p class="price">PRICE: \$1,495</p>
<p class="cartLink"><a href="buy?id=$_[0]">ADD TO CART</a> | <a href="?page=detail&resId=$_[0]">REPORT DETAIL</a></p>
</div>

EOF
	($ras1, $rasLink) = &formatPackage('420377');
	($ras2, $rasLink) = &formatPackage('420081');
	($mq1, $mqLink)   = &formatPackage('417394');
	($mq2, $mqLink)   = &formatPackage('408319');
	($hc1, $hcLink)   = &formatPackage('407577');
	($hc2, $hcLink)   = &formatPackage('424786');
	($vr1, $vrLink)   = &formatPackage('416088');
	($vr2, $vrLink)   = &formatPackage('418486');
	($dq1, $dqLink)   = &formatPackage('417680');
	($dq2, $dqLink)   = &formatPackage('423480');


	print <<EOF;
	<div class="package">
<table width="505">
  <tr><td colspan="3"><h3>Strategy and Analysis</h3></td></tr>
  <tr><td colspan="3"><p class="summary">Gartner Strategy and Analysis reports will help guide you through the business and technical issues around an IT subject, it helps decision-makers capitalise on information technologies
and markets.  These reports are written for project heads, consultants, IT decision makers and C-level executives.</p></td></tr>
  <tr>
     <td width="250" valign="top">$ras1</td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">$ras2</td>
  </tr>
  $rasLink

  <tr><td colspan="3"><h3>Magic Quadrants</h3></td></tr>
  <tr><td colspan="3"><p class="summary">Gartner Magic Quadrants provide a graphical snapshot of how vendors are performing in a market segment and highlight the leaders to show how others compare.</p></td></tr>
  <tr>
     <td width="250" valign="top">$mq1</td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">$mq2</td>
  </tr>
  $mqLink

  <tr><td colspan="3"><h3>Hype Cycles</h3></td></tr>
  <tr><td colspan="3"><p class="summary">A Hype Cycle is a graphic representation of the maturity, adoption and business application of specific technologies.  Hype Cycles show how and when technologies move beyond the hype, offer practical benefits and become widely accepted.</p></td></tr>
  <tr>
     <td width="250" valign="top">$hc1</td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">$hc2</td>
  </tr>
  $hcLink

  <tr><td colspan="3"><h3>Vendor Ratings</h3></td></tr>
  <tr><td colspan="3"><p class="summary">Gartner Vendor Ratings provide clear, concise indicators of each vendor's overall status and the status of such initiatives as strategy, organization, products, technology, marketing, financials and support.</p></td></tr>
  <tr>
     <td width="250" valign="top">$vr1</td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">$vr2</td>
  </tr>
  $vrLink

  <tr><td colspan="3"><h3>Market Trends and Statistics</h3></td></tr>
  <tr><td colspan="3"><p class="summary">Gartner Market Trends and Statistics documents provide detailed information on Hardware and Systems, IT Services, Software, Semiconductors, Telecommunications market share and forecast data.  Gartner gives clear explanations of how changing market opportunities, industry events and end-user wants and needs are likely to affect your business.</p></td></tr>
  <tr>
     <td width="250" valign="top">$dq1</td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">$dq2</td>
  </tr>
  $dqLink

</table>

	</div>
EOF

	&printBottom;
}

sub formatPackage {

	&findDB($_[0]);

	local $packageLayout .=<<EOF;

	<p class="title">$title{$_[0]}</p>
	<p class="summary">$summary{$_[0]}</p>
	<!-- <p class="authors">Written by $author{$_[0]}</p> -->
	<p class="date">Published on $date{$_[0]}</p>
	<p class="pages">$pages{$_[0]} pages</p>
	<p class="price">PRICE: \$$price{$_[0]}</p>
	<p class="cartLink"><a href="buy?id=$_[0]">ADD TO CART</a> | <a href="?page=detail&resId=$_[0]">REPORT DETAIL</a></p>

EOF

	local $packageLink .=<<EOF;
  <tr><td colspan="3" class="morelink"><a href="?page=search&amp;catagory=$catagory{$_[0]}&amp;docType=$docType{$_[0]}">See all $docType{$_[0]} documents in $catagory{$_[0]}</a><br /></td></tr>

EOF
	return($packageLayout, $packageLink);

}



########################################
sub printSpecial {

	&printTop('Sourcing Package');

	print <<EOF;
<div class="marketing">
  <h3>Gartner March Sourcing Special</h3>

<table><tr><td><img src="/img/dr_package.jpg" width="150" height="112" alt="two women drinking coffee ;-)" vspace="10" hspace="3"/></td><td><h3>The Economics of IT Services and Outsourcing in Europe</h3></td></tr></table>
<p> </p>
<p class="summary">The desire to control and cut IT costs has driven many enterprises across Europe to outsource. However, Gartner research reveals that the total cost of IT outsourcing is often underestimated, and initial cost reductions do not always lead to lower costs over the length of the contract. As a result, although service providers usually meet contracted service levels and often exceed them because buyers are unable to realize their vision of sustained and continual cost reduction throughout the deal, many buyers are left feeling that service providers overcharge for a sometimes inadequate service. The mistaken view that the sole value of outsourcing is cost reduction can have negative consequences for buyers. It sets unrealistic expectations, leads them to feel dissatisfied even when delivery requirements have been met, and causes them to overlook additional business value that outsourcers can provide.</p>

<p>Moreover, outsourcing deals that are based solely on reducing costs throughout the contract term can compromise the vendor&#8217;s ability to deliver quality services to the required service-level standards. In extreme situations, these types of deals can erode profit margins to the point that the deal is no longer sustainable for the vendor.</p>

<p>Therefore, it is to both parties&#8217; advantage to recognize that the value of an outsourcing deal derives both from improved quality as well as from cost management. Both enterprises and suppliers can start laying the groundwork now to establish the high level of trust required to develop a payment structure that is based, in part, on delivering business value instead of solely on cutting costs and meeting IT service levels.</p>


<p class="summary"><strong>We have selected the most important documents to start you on your way.</strong></p>
<p class="summary"><strong>Get 4 reports for the price of 3!</strong></p>
<p class="price">PRICE: \$1,495</p>
<p class="cartLink"><a href="buy?id=$_[0]">ADD TO CART</a> | <a href="?page=detail&resId=$_[0]">REPORT DETAIL</a></p>
</div>

EOF
	($special1) = &formatSpecial('420081');
	($special2)   = &formatSpecial('417394');
	($special3)   = &formatSpecial('407577');
	($special4)   = &formatSpecial('416088');


	print <<EOF;
	<div class="package">
<table width="505">
  <tr>
    <td width="250" valign="top">$special1</td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">$special2</td>
  </tr>
  <tr>
    <td width="250" valign="top">$special3</td>
    <td width="5">&nbsp;</td>
    <td width="250" valign="top">$special4</td>
  </tr>

</table>

	</div>
EOF

	&printBottom;
}

sub formatSpecial {

	&findDB($_[0]);

	local $packageLayout .=<<EOF;

	<p class="title">$title{$_[0]}</p>
	<p class="summary">$summary{$_[0]}</p>
	<p class="date">Published on $date{$_[0]}</p>
	<p class="pages">$pages{$_[0]} pages</p>
	<p class="cartLink"><a href="?page=detail&resId=$_[0]">REPORT DETAIL</a></p>

EOF

	return($packageLayout);

}
