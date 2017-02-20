#!/usr/local/bin/perl

################################################################################
#
# footerIncl.pl
#
#   written:  01 Dec 2003 by Peter Mahnke
#   modified: 10 Jan 2005 by Peter Mahnke
#
#   DESCRIPTION
#   a CGI script to help create standard versions of the regional footers
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

	$regionalsrLocaleDir{'emea'} = "emea";
	$regionalsrLocaleDir{'it'}   = "emea/it";
	$regionalsrLocaleDir{'de'}   = "emea/de";
	$regionalsrLocaleDir{'at'}   = "emea/de/at";
	$regionalsrLocaleDir{'fr'}   = "emea/fr";

	$contactLink{'emea'}         = "/ContactUs?param=no";
	$contactLink{'it'}           = "/ContactUs?param=no";
	$contactLink{'de'}           = "/regionalization/content/emea/de/06_contactpopup.html";
	$contactLink{'at'}           = "/regionalization/content/emea/de/at/06_contactpopup.html";
	$contactLink{'fr'}           = "/ContactUs?param=no";

	$siteIndex =<<EOF;
<li><a href="/regionalization/content/$regionalsrLocaleDir{$region}/06_SiteIndexPopUp.html">Site Index</a></li>
EOF

$help =<<EOF;
<li><a href="/6_help/help_overview.html">Help</a></li>
EOF

	$contactUs =<<EOF;
<li><a href="$contactLink{$region}" onclick="openNewAdmin('$contactLink{$region}'); return false;">Contact Us</a></li>
EOF

	$signInOut =<<EOF;
		var regUCCookie          = GetCookie("regUC");
		if (regUCCookie == 'loggedin' || regUCCookie == 'EXPPrem' || regUCCookie == 'EXPClub')
		{
			document.write('<li><a href="/Terminate/doPost?locale=$region" onclick="regionalsignout(\\'$region\\'); return false;">Sign Off</a></li>');
		} else {
			document.write('<li><a href="/SignIn.jsp?call=homepage&amp;frm=reg">Sign-In</a></li>');
		}
EOF

	$signInOutTest =<<EOF;
<li><a href="/SignIn.jsp?call=homepage&amp;frm=reg">Sign-In</a></li>
EOF

	$AAA =<<EOF;
<li><a href="/Inquiry?pagenm=homepage" onclick="openNewAdminFooter('/Inquiry?pagenm=homepage'); return false;">Ask an Analyst</a></li>
EOF

	$about =<<EOF;
<li><a href="/regionalization/content/$regionalsrLocaleDir{$region}/05_z_about.html">About Gartner</a></li>
EOF

	$investor =<<EOF;
<li><a href="/5_about/investor_information/44a.html" target="_blank">Investor Relations</a></li>
EOF

	$vendor =<<EOF;
<li><a href="/5_about/our_business/vendor_relations.html">Vendor Relations</a></li>
EOF

	$media =<<EOF;
<li><a href="/media_relations/asset_61507_1575.jsp">Media Relations</a></li>
EOF


	$privacy =<<EOF;
<li><a href="/pages/story.php.id.2630.s.8.jsp">Privacy Policy</a></li>
EOF

	$terms =<<EOF;
<li><a href="/6_help/16.html" onclick="openNewAdminFooter('/6_help/16.html'); return false;">Terms of Use</a></li>
EOF

	$carrers =<<EOF;
<li><a href="/5_about/careers/45a.html">Careers</a></li>
EOF

	$copyright =<<EOF;
&nbsp;&copy;&nbsp;2005 Gartner, Inc. and/or its Affiliates.<br />All Rights Reserved.
EOF

	# format FOOTER
	$line .=<<EOF;
<table class="reg_footer" align="center" width="766" cellpadding="0" cellspacing="0" border="0"><tr><td width="400" rowspan="2"><ul class="reg_footerlist">$siteIndex $help $contactUs <script type="text/javascript">    document.open();$signInOut    document.close();</script></ul><ul class="reg_footerlist">$investor $vendor $media</ul><ul class="reg_footerlist">$about $AAA $carrers</ul><ul class="reg_footerlist">$privacy $terms</ul></td><td width="362"><img src="http://www.gartner.com/images/header/logo_footer.gif" width="98" height="26" border="0" alt="Gartner" class="reg_inline" align="right" hspace="10" /></td></tr><tr><td width="362"><p class="reg_copyright">$copyright</p></td></tr></table>
EOF

	$line =~ s/\n//g; # remove newlines

	# create escaped version for document write
	$jsline .=<<EOF;
		document.write[<table align="center" width="766" cellpadding="0" cellspacing="0" border="0"><tr><td><div id="reg_footercontainer"><table class="reg_footer" align="center" width="766" cellpadding="0" cellspacing="0" border="0"><tr><td width="400" rowspan="2"><ul class="reg_footerlist">$siteIndex $help $contactUs ]
		signInOut
		document.write[</ul><ul class="reg_footerlist">$investor $vendor $media</ul><ul class="reg_footerlist">$about $AAA $carrers</ul><ul class="reg_footerlist">$privacy $terms</ul></td><td width="362"><img src="http://www.gartner.com/images/header/logo_footer.gif" width="98" height="26" border="0" alt="Gartner" class="reg_inline" align="right" hspace="10" /></td></tr><tr><td width="362"><p class="reg_copyright">$copyright</p></td></tr></table></div></td></tr></table>]
EOF


	$jsline =~ s/\'/\\\'/g;
	$jsline =~ s/\\\\'/\\'/g;
	$jsline =~ s/\n//g;
	$jsline =~ s/\[/\(\'/g;
	$jsline =~ s/\]/\'\)\;\n/g;
	$jsline =~ s/signInOut/\n$signInOut\n/;

#	eval($jsline);

	# translate if required
	if ($region ne "emea") {

		# all austrian translations are german, except for above pop-ups
		$region = "de" if ($region eq "at");

		# provide a translation
		$line = &translateUIstring($line, 'eu', $region);
		$jsline = &translateUIstring($jsline, 'eu', $region);

	}

			$jsline =~ s/\</\&lt\;/g;

	$lineamped =$line;
	$lineamped =~ s/&(?!amp;)/&amp;/g;

	$jsline    =~ s/&(?!(amp|lt);)/&amp;/g;


	print <<EOF;
Content-type: text/html

<!DOCTYPE html PUBLIC "W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>footer $FORM{'region'} - $FORM{'from'} -> $FORM{'to'}</title>
<body>
<style type="text/css">
#reg_footercontainer    {  width: 766px; margin: auto; text-align: left;  }
.reg_footer	        {  margin: auto; padding: 0; padding-top: 5px; padding-bottom: 5px;  background-color: #DDE0E2;  background-image:url(http://www.gartner.com/images/header/footer_grad.gif);  background-repeat: repeat-y;  border: 2px solid #fff; margin: 0; padding: 0;  }
.reg_footerlist         {  margin: 0; padding: 1px 0 1px 5px;  }
.reg_footerlist ul      {  margin: 0; padding: 0; }
.reg_footerlist li      {  display: inline; list-style-type: none;  }
.reg_footerlist a       {  font-family: verdana, arial, helvetica, sans-serif; font-size: 10px; font-weight: bold; color: #4d4d4d; text-decoration: none;  }
.reg_footerlist a:hover {  color: #3088CC;  }
.reg_copyright          {  font-family: verdana, arial, helvetica, sans-serif; font-size: 10px; color: #4d4d4d; vertical-align: bottom; text-align: right; padding-right:3px;  }
.reg_inline             {  display: inline;  }
</style>
<table align="center" width="766" cellpadding="0" cellspacing="0" border="0"><tr><td>
<div id="reg_footercontainer">
$line
</div>
</td></tr></table>
<script type="text/javascript">
function regionalsignout(region) {

    var region = region;
    document.cookie="regUC=;domain=.gartner.com;path=/;expires=Sat, 16 Nov 2002 20:29:25 UTC";
    document.cookie="regQuery=;domain=.gartner.com;path=/;expires=Sat, 16 Nov 2002 20:29:25 UTC";
    document.cookie="idForRegionals=;domain=.gartner.com;path=/;expires=Sat, 16 Nov 2002 20:29:25 UTC";
    document.cookie="unForRegionals=loggedout;domain=.gartner.com;path=/;expires=Sat, 16 Nov 2002 20:29:25 UTC";
    window.location=("/Terminate/doPost?locale=" + region);
    return false;
}
</script>

<h4>HTML</h4>
<p>
<textarea cols="80" rows="10">
$lineamped
</textarea>
</p>


<h4>Javascript</h4>
<p>
<textarea cols="80" rows="10">
$jsline
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


