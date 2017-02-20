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


<!-- content start -->
$content
<!-- content end -->

 </body>
</html>
EndofHTML