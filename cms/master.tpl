$html = <<EndofHTML;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
  <title>gartner.com</title>
  <script src="$rootURI/js/search.js" language="javascript" type="text/javascript"></script>
  <link rel="stylesheet" type="text/css" href="$rootURI/css/basic.css"></link>
  <style type="text/css" media="all">\@import "$rootURI/css/sophisto.css";</style>
  $METAstyle
  $METAcharSet
  $METAlang

      $script

      <!-- start JavaScript Files to Reference -->
      $tmjsFile
      <!-- end JavaScript Files to Reference -->

      <!-- start JavaScript Files to Include -->
      <!--script-->
      $tmjsInclude
      <!-- /script-->
      <!-- end JavaScript Files to Include -->

  <title>Gartner $localeName{$COOKIE{locale}} - $tmTitle</title>
 </head>
  <body bgcolor="#bbbbbb">
<table width="766" cellpadding="0" cellspacing="0" align="center" summary="this table visually holds the page together for non-standards compliant browsers">
<tr>
 <td colspan="3" width="766" bgcolor="#ffffff">
<form method="post" name="frmSearch" onsubmit="submitSearch();return false;" action="http://regionals4.gartner.com/7_search/Search2Frame.jsp">
<!-- header start -->
$header
<!-- header end -->

<!-- navigation start -->
$navigation
<!-- navigation end -->

<!-- content start -->
$content
<!-- content end -->

<!-- footer start -->
$footer
<!-- footer end-->

</td></tr>

  </table>
 </body>
</html>
EndofHTML