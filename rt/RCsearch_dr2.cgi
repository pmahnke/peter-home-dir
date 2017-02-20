#!/usr/local/bin/perl

use CGI_Lite;
require ("/home/gartner/html/rt/getNODocument3.pl");

##############################################################
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    # something submitted
    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;

    &getNoteNumber($FORM{'doc'});
    &printPage;
    exit;


} else {

    print <<EOF;
Content-type: text/html

<html>
<body>
<form method="get">

Resid: <input type="text" name="doc" />
<input type="submit" />

</form>
</body>
</html>
EOF


    exit;

}




sub getNoteNumber {


    $FORM{URL} = "http:\/\/www4.gartner.com\/DisplayDocument\?id\=$_[0]\&ref\=g_search";

    local ($title, $pubDate, $summary, $resId, $auth, $body, $noteNumber, $toc, $price, $pages, $docType, $contentType, $folderType) = &getResearchDetail($FORM{URL});


    $title{$resId}       = $title;
    $summary{$resId}     = $summary;
    $noteNumber{$resId}  = $noteNumber;
    $date{$resId}        = $pubDate;
    $author{$resId}      = $auth;
    $toc{$resId}         = $toc;
    $price{$resId}       = $price;
    $pages{$resId}       = $pages;
    $resId{$resId}       = $resId;
    $docType{$resId}     = $docType;
    $contentType{$resId} = $contentType;
    $folderType{$resId}  = $folderType;
    return();

}



sub printPage {

    local $i = 1;
    foreach $resId (reverse sort keys %title) {

	chop ($author{$resId}); # remove last comma

	$date{$resId} =~ s/\&nbsp\;/ /gi;

	$listing .=<<EOF;
<tr>
 <td rowspan="12" valign="top" bgcolor="lightblue">$i</td>
 <td>title</td>
 <td>$title{$resId}</td>
</tr>

<tr>
 <td>summary</td>
 <td>$summary{$resId}</td>
</tr>

<tr>
 <td>author</td>
 <td>$author{$resId}</td>
</tr>

<tr>
 <td>date</td>
 <td>$date{$resId}</td>
</tr>

<tr>
 <td>ResId</td>
 <td>$resId{$resId}</td>
</tr>

<tr>
 <td>NN</td>
 <td>$noteNumber{$resId}</td>
</tr>

<tr>
 <td>Doc Type</td>
 <td>$docType{$resId}</td>
</tr>

<tr>
 <td>Folder Type</td>
 <td>$folderType{$resId}</td>
</tr>

<tr>
 <td>Content Type</td>
 <td>$contentType{$resId}</td>
</tr>

<tr>
 <td>price</td>
 <td>$price{$resId}</td>
</tr>

<tr>
 <td>pages</td>
 <td>$pages{$resId}</td>
</tr>

<tr>
 <td>Table of Contents</td>
 <td>$toc{$resId}</td>
</tr>

EOF

	$searchLayout .=<<EOF;

	<p class="department">In $folderType{$resId}</p>
	<p class="title">$title{$resId}</p>
	<p class="summary">$summary{$resId}</p>
	<p class="price">PRICE: \$$price{$resId}</p>
	<p class="cartLink"><a href="buy?id=$resId{$resId}">ADD TO CART</a></p>

EOF

	$packageLayout .=<<EOF;

	<p class="title">$title{$resId}</p>
	<p class="date">$date{$resId}</p>
	<p class="summary">$summary{$resId}</p>
	<p class="pages">PAGES: $pages{$resId}</p>
	<p class="price">PRICE: \$$price{$resId}</p>
	<p class="cartLink"><a href="buy?id=$resId{$resId}">ADD TO CART</a></p>

EOF

	$detailLayout .=<<EOF;
 <div class="package">
	<p class="type">$contentType{$resId}</p>
	<p class="title">$title{$resId}</p>
	<p class="summary">$summary{$resId}</p>
	<p class="authors">Written by $author{$resId}</p>
	<p class="date">Published on $date{$resId}</p>
	<p class="pages">$pages{$resId} pages</p>
	<p class="price">PRICE: \$$price{$resId}</p>
	<p class="cartLink"><a href="buy?id=$resId{$resId}">ADD TO CART</a></p>
	$toc{$resId}
 </div>

EOF

	$i++;
    }

    chop ($date = `date '+%d %b %Y'`);
    $outputFilename = "RCoutput_".time().".xls";

	$getGARTNERmsg =~ s/</\&lt\;/g;
	$msg =~ s/</\&lt\;/g;

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

<p>$FORM{keywords}</p>
<p>$date</p>
<h2>messages</h2>
<p>getGARTNERmsg</p>
<p>$msg</p>
<p>getNOdocmsg</p>

<table>
$listing
</table>


<h2>Search</h2>
$searchLayout


<h2>Package</h2>
$packageLayout


<h2>Detail</h2>
$detailLayout


</body>
</html>
EndofHTML


}
