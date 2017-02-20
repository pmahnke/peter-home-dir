#!/usr/local/bin/perl

use CGI_Lite;

# variables
$rootDir = "/home/gartner/html/rt/content/";
$fileMQ = "$rootDir"."MQ.csv";
$fileHC = "$rootDir"."HC.csv";
$fileVR = "$rootDir"."VR.csv";



&openFile ($fileMQ);
print $line;
exit;


##############################################################
# Get the input from the HTML Form
if ($ENV{'CONTENT_LENGTH'}) {

    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;

} else {

    &printForm;

}











sub openFile {

    # 113833	20 March 2003	Noninvasive Legacy Web Enablement Is Still Viable

    open (FILE, "$_[0]") || die "can't open file: $_[0]\n";
    while (<FILE>) {
	chop();
	local ($code, $date, $title) = split (/\t/);
	
	$line .= "$title \- $date \- $code\n";

    }
    close(FILE);

}

sub writeIncludes {



    print OUT <<EndofHTML;


<!--  start mq_vr inc -->
<!-- begin magic quadrant and vendor rating section -->

<script src="/pages/docs/gartner/hc/scripts/utils.js"></script>
<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="360" height="2" bgcolor="#BBBBBB"><img src="/images/trans_pixel.gif" width="360" height="2" alt="" border="0"></td>
</tr>
</table>

<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td rowspan="100" width="2" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
   <td width="10"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
   <td width="336"><img src="/images/trans_pixel.gif" width="336" height="1" alt="" border="0"></td>
   <td width="10"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
   <td rowspan="100" width="2" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
</tr>

<!-- mq's -->
<tr>
  <td width="10" height="2" bgcolor="#F5F5F5"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
   <td width="336" height="2" bgcolor="#F5F5F5"><div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div>
<a href="/mq/asset_6590.jsp"><img src="/images/homepage/promo_02/mquadrants_logo.gif" width="175" height="21" border="0" alt=""></a>
   <div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div>
    <span class="smallGrayText">Find out which vendors are leaders, visionaries, challengers or niche players.<br></span>
    <div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div>
    <img src="/images/homepage/arrow_trans_k.gif" width="10" height="10" alt="" border="0"><a href="/mq/asset_6590.jsp" class="smallThinBlueLink">View All Magic Quadrants</a><br>
   <div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div>
   </td>
   <td width="10" height="2" bgcolor="#F5F5F5"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
</tr>
<tr>
  <td width="10" height="2" bgcolor="#E3E9EC"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
  <td width="336" height="2" bgcolor="#E3E9EC">
  <div><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></div>
  <span class="focusAreaLink"><b>Latest Magic Quadrant:&nbsp;</b><br></span>
  &nbsp;&nbsp;&nbsp;<a href="javascript:void(null)" onclick="popUpQuadrant(117832)" class="smallThinBlueLink"><b>Corporate Performance Management Suites</b></a><br>
 <div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div></td>
  <td width="10" height="2" bgcolor="#E3E9EC"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
</tr>

<!-- hc's -->
<tr>
   <td colspan="3" width="356" height="2"><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></td>
</tr>
<tr>
  <td width="10" height="2" bgcolor="#F5F5F5"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
  <td width="336" height="2" bgcolor="#F5F5F5"><div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div>
   <a href="/hc/asset_8989.jsp"><img src="/images/homepage/promo_02/hypecycles_logo.gif" width="130" height="21" border="0" alt=""></a>
   <div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div>
   <span class="smallGrayText">Gartner Hype Cycles clearly explain the difference between hype and the future of technology.<br></span>
<div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div>
  <img src="/images/homepage/arrow_trans_k.gif" width="10" height="10" alt="" border="0"><a href="/hc/asset_8989.jsp" class="smallThinBlueLink">View All Hype Cycles</a><br>
   <div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div>
   </td>
   <td width="10" height="2" bgcolor="#F5F5F5"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
</tr>
<tr>
  <td width="10" height="2" bgcolor="#E3E9EC"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
  <td width="336" height="2" bgcolor="#E3E9EC">
  <div><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></div>
  <span class="focusAreaLink"><b>Latest Hype Cycle:&nbsp;</b></span>
  <a href="javascript:void(null)" onclick="popUpHypeCycle(117446)" class="smallThinBlueLink"><b>Business Activity Monitoring</b></a><br><div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div>
   </td>
   <td width="10" height="2" bgcolor="#E3E9EC"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
</tr>

<!-- vendor ratings -->
<tr>
  <td width="356" height="2" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="2" alt="" border="0"></td>
</tr>
<tr>
  <td width="10" height="2" bgcolor="#F5F5F5"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
  <td width="336" height="2" bgcolor="#F5F5F5"><div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div>
  <a href="/1_researchanalysis/vendor_rating/vr_main.html"><img src="/images/homepage/promo_02/vendorratings_logo.gif" width="125" height="21" border="0" alt=""></a>
  <div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div>
  <span class="smallGrayText">Gartner's latest ratings of leading vendors.<br></span>
  <div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div>
  <img src="/images/homepage/arrow_trans_k.gif" width="10" height="10" alt="" border="0"><a href="/1_researchanalysis/vendor_rating/vr_main.html" class="smallThinBlueLink">View All Vendor Ratings</a><br>
   <div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div>
  </td>
  <td width="10" height="2" bgcolor="#F5F5F5"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
</tr>
<tr>
  <td width="10" height="2" bgcolor="#E3E9EC"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
  <td width="336" height="2" bgcolor="#E3E9EC" valign="top">
   <div><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></div>
      <table width="336">
      <tr>
          <td width="100" valign="top">
          <span class="focusAreaLink"><b>Latest Ratings: </b></span>
          </td>
          <td width="236" valign="top">
          <img src="/images/homepage/arrow_trans_k.gif" width="10" height="10" alt="" border="0"><a href="/1_researchanalysis/vendor_rating/vr_hitachi.html" class="smallThinBlueLink"><b>Hitachi Data Systems</b></a><br>

          <img src="/images/homepage/arrow_trans_k.gif" width="10" height="10" alt="" border="0"><a href="/1_researchanalysis/vendor_rating/vr_veritassoftware.html" class="smallThinBlueLink"><b>Veritas</b></a><br>
          <img src="/images/homepage/arrow_trans_k.gif" width="10" height="10" alt="" border="0"><a href="/1_researchanalysis/vendor_rating/vr_bmcsoftware.html" class="smallThinBlueLink"><b>BMC Software</b></a><br>
      <div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div>
          </td>
       </tr>
      </table>

   </td>
   <td width="10" height="2" bgcolor="#E3E9EC"><img src="/images/trans_pixel.gif" width="10" height="2" alt="" border="0"></td>
</tr>
<tr>
   <td width="356" height="2" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="2" alt="" border="0"></td>
</tr>
</table>

<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="360" height="2" bgcolor="#BBBBBB"><img src="/images/trans_pixel.gif" width="360" height="2" alt="" border="0"></td>
</tr>
</table>


<!-- whiteline -->
<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td bgcolor="#ffffff"><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></td>
</tr>
</table>


<!-- Gartner Weblogs -->
<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="2" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
   <td width="356" height="20" bgcolor="#ADB5C6"><a href="http://weblog.gartner.com/weblog/weblogIndex.php" class="sectionHead">&nbsp;Gartner Weblogs</a></td>
   <td width="2" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
</tr>
</table>

<table width="360" border="0" cellspacing="0" cellpadding="0">


<tr>
   <td width="340" bgcolor="#FFFFff" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><span class="smallGrayText">Find out what Gartner analysts are thinking about current business & technology issues &#133;<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div>
         </td>
      </tr>

      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
      </table>
   </td>
</tr>



<!-- Unconventional Thinking -->
<tr>
   <td width="340" bgcolor="#FFFFff" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><a href="http://fellows.blog.gartner.com/weblog/index.php?blogid=2" class="smallBlueLink">Unconventional Thinking</a><br>
         <span class="smallGrayText">Gartner's leading analysts discuss new approaches and new ideas.<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="3" alt="" border="0"></div>
         </td>
      </tr>
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="4" height="16" alt="" border="0" align="left"><img src="/images/arrowBlue.gif" width="13" height="8" alt="" hspace="0" vspace="2" border="0" align="left"><a href="http://fellows.blog.gartner.com/weblog/index.php?blogid=2" class="smallThinBlueLink">Latest Topic:
      <img src="/images/trans_pixel.gif" width="13" height="1" alt="" hspace="0" vspace="0" border="0" align="left">Outsmarting the Real-Time Government</a><div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div></td>
      </tr>
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
   </table>
   </td>
</tr>



<!-- Sarbanes-Oxley Act -->
<tr>
   <td width="340" bgcolor="#FFFFff" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><a href="http://sox.weblog.gartner.com/weblog/index.php?blogid=11" class="smallBlueLink">Sarbanes-Oxley Act</a><br>
         <span class="smallGrayText">The U.S. Sarbanes-Oxley Act has changed the rules of business. Learn how this will affect your IS organization.<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="3" alt="" border="0"></div>
         </td>
      </tr>
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="4" height="16" alt="" border="0" align="left"><img src="/images/arrowBlue.gif" width="13" height="8" alt="" hspace="0" vspace="2" border="0" align="left"><a href="http://sox.weblog.gartner.com/weblog/index.php?blogid=11" class="smallThinBlueLink">Latest Topic:<br>
      <img src="/images/trans_pixel.gif" width="13" height="1" alt="" hspace="0" vspace="0" border="0" align="left">Use Smart Cards or Biometrics to Prevent Fraud</a><div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div></td>
      </tr>
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
   </table>
   </td>
</tr>



<!-- outsourcing -->
<tr>
   <td width="340" bgcolor="#FFFFff" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><a href="http://outsourcing.weblog.gartner.com/weblog/index.php?blogid=9" class="smallBlueLink">Outsourcing</a><br>
         <span class="smallGrayText">Separate the myths from the reality about outsourcing and share best practices.<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="3" alt="" border="0"></div>
         </td>
      </tr>
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="4" height="16" alt="" border="0" align="left"><img src="/images/arrowBlue.gif" width="13" height="8" alt="" hspace="0" vspace="2" border="0" align="left"><a href="http://outsourcing.weblog.gartner.com/weblog/index.php?blogid=9" class="smallThinBlueLink">Latest Topic:<br>
      <img src="/images/trans_pixel.gif" width="13" height="1" alt="" hspace="0" vspace="0" border="0" align="left">Outsourcing Leads to Fewer Consumers, Fewer Jobs</a><div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div></td>
      </tr>
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
      </table>
   </td>
</tr>


<!-- Does IT matter -->
<tr>
   <td width="340" bgcolor="#FFFFFF" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></td>
         <td><a href="http://itmatters.weblog.gartner.com/weblog/index.php?blogid=10" class="smallBlueLink">Does IT Matter?</a><br>
         <span class="smallGrayText">Join the discussion about the future of IT and how it will affect your business.<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="3" alt="" border="0"></div>
         </td>
      </tr>

      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="4" height="16" alt="" border="0" align="left"><img src="/images/arrowBlue.gif" width="13" height="8" alt="" hspace="0" vspace="2" border="0" align="left"><a href="http://itmatters.weblog.gartner.com/weblog/index.php?blogid=10" class="smallThinBlueLink">Latest Topic: <br><img src="/images/trans_pixel.gif" width="13" height="1" alt="" hspace="0" vspace="0" border="0" align="left">More About IT for Business Results</a><div><img src="/images/trans_pixel.gif" width="1" height="8" alt="" border="0"></div></td>
      </tr>
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
      </table>
   </td>
</tr>

<tr>
   <td width="356" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="8" alt="" border="0"></td>
</tr>
</table>


<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="28" bgcolor="#FFFFFF" valign="top" align="center"><img src="/images/trans_pixel.gif" width="4" height="1" alt="" border="0"><img src="/images/homepage/gray_arrow.gif" width="10" height="10" vspace="2" hspace="0" alt="" border="0"></td>
   <td width="330" valign="top" bgcolor="#FFFFFF"><a href="http://weblog.gartner.com/weblog/weblogIndex.php" class="smallGreenLink">View All Gartner Weblogs</a><div><img src="/images/trans_pixel.gif" width="318" height="10" alt="" border="0"></div></td>
</tr>
</table>
<!-- End Gartner Weblogs -->


<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="360" height="2" bgcolor="#BBBBBB"><img src="/images/trans_pixel.gif" width="360" height="2" alt="" border="0"></td>
</tr>
</table>

























<!-- whiteline -->
<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td bgcolor="#ffffff"><img src="/images/trans_pixel.gif" width="1" height="2" alt="" border="0"></td>
</tr>
</table>


<!-- Start Research Collections -->
<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="2" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
   <td width="356" height="20" bgcolor="#ADB5C6"><a href="/pages/story.php.id.3021.s.8.jsp" class="sectionHead">&nbsp;Research Collections</a></td>
   <td width="2" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
</tr>
<tr>
   <td width="2" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
   <td width="356" height="5" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="5" alt="" border="0"></td>
   <td width="2" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="2" height="1" alt="" border="0"></td>
</tr>

</table>

<table width="360" border="0" cellspacing="0" cellpadding="0">

<tr>
   <td width="340" bgcolor="#FFFFff" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><span class="headFootGrayBold">Get research articles, tools and other resources.<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div>
         </td>
      </tr>

      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
      </table>
   </td>
</tr>





<!-- Outsourcing -->
<tr>
   <td width="340" bgcolor="#FFFFff" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><a href="/pages/section.php.id.2215.s.8.jsp" class="smallBlueLink">Outsourcing</a><br>
         <span class="smallGrayText">Find out how to choose the right vendors and negotiate the best deals.<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div>
         </td>
      </tr>

      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
      </table>
   </td>
</tr>







<!-- The Business Value of IT -->
<tr>
   <td width="340" bgcolor="#FFFFff" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><a href="http://rte.gartner.com/section.php.id.2159.s.15.jsp" class="smallBlueLink" target="_blank">The Business Value of IT</a><br>
         <span class="smallGrayText">Learn why IT investments succeed or fail &#151; and what it really takes to determine value.<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div>
         </td>
      </tr>

      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
      </table>
   </td>
</tr>











<!-- The New Executive Reports -->
<tr>
   <td width="340" bgcolor="#FFFFff" valign="top" colspan="2">
   <div><img src="/images/trans_pixel.gif" width="1" height="4" alt="" border="0"></div>
      <table border="0" cellspacing="0" cellpadding="0">
      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><a href="/5_about/news/exec_reports.jsp" class="smallBlueLink">Gartner Executive Reports</a><br>
         <span class="smallGrayText">Five comprehensive reports about CRM, web services, security, outsourcing and asset management.<br></span>
         <div><img src="/images/trans_pixel.gif" width="1" height="6" alt="" border="0"></div>
         </td>
      </tr>

      <tr>
         <td width="10" height="1"><img src="/images/trans_pixel.gif" width="10" height="1" alt="" border="0"></td>
         <td><img src="/images/trans_pixel.gif" width="330" height="1" alt="" border="0" class="dottedLine"><div><img src="/images/trans_pixel.gif" width="1" height="1" alt="" border="0"></div></td>
      </tr>
      </table>
   </td>
</tr>





<tr>
   <td width="356" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="8" alt="" border="0"></td>
</tr>
</table>


<table width="360" border="0" cellspacing="0" cellpadding="0">
<tr>
   <td width="28" bgcolor="#FFFFFF" valign="top" align="center"><img src="/images/trans_pixel.gif" width="4" height="1" alt="" border="0"><img src="/images/homepage/gray_arrow.gif" width="10" height="10" vspace="2" hspace="0" alt="" border="0"></td>
   <td width="330" valign="top" bgcolor="#FFFFFF"><a href="/pages/story.php.id.3021.s.8.jsp" class="smallGreenLink">View All Research Collections</a><div><img src="/images/trans_pixel.gif" width="318" height="10" alt="" border="0"></div></td>
</tr>
</table>
<!-- End Research Collections -->


<table width="360" border="0" cellspacing="0" cellpadding="0">
<!-- <tr>
   <td width="360" height="2" bgcolor="#BBBBBB"><img src="/images/trans_pixel.gif" width="360" height="2" alt="" border="0"></td>
</tr> -->
<tr>
   <td width="360" height="2" bgcolor="#ffffff"><img src="/images/trans_pixel.gif" width="360" height="10" alt="" border="0"></td>
</tr>
</table>
<!--  end mq_vr inc -->


EndofHTML




















}



sub processDate {

    local ($d, $m, $y) = split(/ /, $_[0]);


    $m{'January'} = "01";
    $m{'February'} = "02";
    $m{'March'} = "03";
    $m{'April'} = "04";
    $m{'May'} = "05";
    $m{'June'} = "06";
    $m{'July'} = "07";
    $m{'August'} = "08";
    $m{'September'} = "09";
    $m{'October'} = "10";
    $m{'November'} = "11";
    $m{'December'} = "12";

    if ($locale eq "it") {
        $mn{'January'} = "gennaio";
        $mn{'February'} = "febbraio";
        $mn{'March'} = "marzo";
        $mn{'April'} = "aprile";
        $mn{'May'} = "maggio";
        $mn{'June'} = "giugno";
        $mn{'July'} = "luglio";
        $mn{'August'} = "agosto";
        $mn{'September'} = "settembre";
        $mn{'October'} = "ottobre";
        $mn{'November'} = "novembre";
        $mn{'December'} = "dicembre";
    } elsif ($locale eq "de") {
        $mn{'January'} = "Januar";
        $mn{'February'} = "Februar";
        $mn{'March'} = "M&amp;auml;rz";
        $mn{'April'} = "April";
        $mn{'May'} = "Mai";
        $mn{'June'} = "Juni";
        $mn{'July'} = "Juli";
        $mn{'August'} = "August";
        $mn{'September'} = "September";
        $mn{'October'} = "Oktober";
        $mn{'November'} = "November";
        $mn{'December'} = "Dezember";
    } else {
	$mn{'January'} = "January";
	$mn{'February'} = "February";
	$mn{'March'} = "March";
	$mn{'April'} = "April";
	$mn{'May'} = "May";
	$mn{'June'} = "June";
	$mn{'July'} = "July";
	$mn{'August'} = "August";
	$mn{'September'} = "September";
	$mn{'October'} = "October";
	$mn{'November'} = "November";
	$mn{'December'} = "December";

    }
    if ($d < 10) {
	$dO = "0"."$d";
    } else {
	$dO = $d;
    }
    local $key = "$y"."$m{$m}"."$dO";

    local $newdate;

    if ($locale eq "de") {
	$newdate = "$d\. $mn{$m} $y";
    } else {
	$newdate = "$d $mn{$m} $y";
    }

    return($newdate);

}
