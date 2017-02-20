#!/usr/local/bin/perl
use gdchart;
use CGI_Lite;

# Variables
$thisScript = "http://intl.gartner.com/rt/hlcChart.cgi";
$fileName   = "\/home\/gartner\/html\/rt\/hlcchart.gif";
@colors=( "ff9600", "294d39", "638663", "6b6d18", "ce3400",
	  "ffb642", "637d6b", "8c9ead", "8c8e52", "d66542",
	  "ffc784", "94a69c", "adbece", "b5b68c", "e79e84",
	  "ffe7bd", "c6d7ce", "d6dfde", "d6d7c6", "efcfbd",
	  "00559C", "427db5", "7ba6ce", "bdd7e7",  
	  ); # gartner secondary colours for charts and graphs


#    print <<EndofHTML;
#Content-type: text/html;

#EndofHTML

###############################################################
# was something POSTED
if ($ENV{'CONTENT_LENGTH'} || $ENV{'QUERY_STRING'}) {

    # something submitted
    &parsePage;
    &parseDataTable;
    &parseColourData;
    
    &buildWhichChart;

    &printOutput;

    exit;

} else {

    # nothing submitted
    &printInputPage;
    exit;
}



#################################################################
sub parsePage {

    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;
    #$FORM{'text'} = escape_dangerous_chars ($FORM{text});

}

#################################################################
sub buildWhichChart {

	if ($FORM{'width'} < 200) {
	    $titleSize = "small"; # verysmallbold";
	} elsif ($FORM{'width'} < 400) {
	    $titleSize = "mediumbold";
	} else {
	    $titleSize = "mediumbold";
	}
	$msg .= "<br\>\ntitleSize is: $titleSize<br/>\n";


	if (!$FORM{'colours'}) {
	    
	    local $count = 0;
	    foreach $color (@colors) {
		$count++;
		last if ($count > $dsCount);
		push @colours, hex $color;
	    }
	    $msg .= "<br\>\ngot no color info, using defaults<p>\n";
	}
	


	$FORM{'ylable_fmt'} = "%.0f%" if (!$FORM{'ylable_fmt'});

	$FORM{'bgcolor'} = "FFFFFF" if (!$FORM{'bgcolor'});
 	
	$gdchart::GDC_TitleColor= hex '336699';
	$gdchart::GDC_XTitleColor=hex '336699';
	$gdchart::GDC_YTitleColor=hex '336699';
	$gdchart::GDC_YTitle2Color=hex $colours[1];
	$gdchart::GDC_XLabelColor=hex '336699';
	$gdchart::GDC_YLabelColor=hex '336699';
#	$gdchart::GDC_YLabel2Color=hex $colours[1];
	$gdchart::GDC_grid=0;
	$gdchart::GDC_title_size=$titleSize;
	$gdchart::GDC_xtitle_size="verysmall";
	$gdchart::GDC_ytitle_size="verysmall";
	$gdchart::GDC_requested_ymin=$FORM{'y_min'};
	$gdchart::GDC_requested_ymax=$max;
	$gdchart::GDC_requested_yinterval=$FORM{'y_interval'};
	$gdchart::GDC_ylabel_density=100;
	$gdchart::GDC_ylabel_fmt=$FORM{'ylable_fmt'};
	$gdchart::GDC_BGColor= hex($FORM{'bgcolor'});
	$gdchart::GDC_GridColor= hex($FORM{'grid'});


	$novalue = $gdchart::GDC_novalue;
	
	unshift @lables, "";
	push @lables, "";
	unshift @dataset1, $novalue;
	push @dataset1, $novalue;
	unshift @dataset2, $novalue;
	push @dataset2, $novalue;
	unshift @dataset3, $novalue;
	push @dataset3, $novalue;



#	@high = (62, 71, 71, 52, 55);
#	@low = (42, 62, 52, 37, 52);
#	@close = (50, 66, 59, 45, 53);
#	@labels = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday");
#	@plotcolors=(hex'0000cd', hex'cd0000', hex'9c9c9c');
#	@hlc_style=("diamond", "connecting", "i_cap");
#	$gdchart::GDC_HLC_cap_width=40;

	# hiloclose ( 400, 400, "/usr/local/etc/httpd/htdocs/gdchart/hiloclose_option.gif", \@labels, \@high, \@low, \@close, \@plotcolors, \@hlc_style, "HiLoClose Graph", "X axis", "Y axis" ); 
	# ("diamond", "close_connected", "connecting","i_cap");

	@hlc_style = ("diamond", "connecting", "i_cap");
	
	hiloclose ( $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@colours, \@hlc_style, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}" );

    }



#################################################################
sub printInputPage {



	@colors=( "ff9600", "294d39", "638663", "6b6d18", "ce3400",
		  "ffb642", "637d6b", "8c9ead", "8c8e52", "d66542",
		  "ffc784", "94a69c", "adbece", "b5b68c", "e79e84",
		  "ffe7bd", "c6d7ce", "d6dfde", "d6d7c6", "efcfbd",
		  "00559C", "427db5", "7ba6ce", "bdd7e7",  
		  ); # gartner secondary colours for charts and graphs

	local $count;
	foreach $color (@colors) {
	    $count++;
	    $cTable .= "\n <\/tr\>\n <tr\>\n" if (($count%5) == 1);
	    $cTable .= "  <td bgcolor\=$color\>$count $color<\/td\>\n";
	}
	
    print <<EndofHTML;
Content-type: text/html;

<html>
<head>
<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
</head>
<body>
<form action=$thisScript method=POST  target=grid>

<table>
 <tr>
  <td>
CHART TYPE
  </td>
  <td>
hiloclose
  </td>
 </tr>

 <tr>
  <td>
DATA
  </td>
  <td>
<textarea cols=40 rows=10 name=data></textarea>
  </td>
 </tr>


 <tr>
  <td>
Y VALUE MIN/MAX/INTERVAL
  </td>
  <td>
<input type=text name=y_min size=5 value="0">
<input type=text name=y_max size=5 value="max">
<input type=text name=y_interval size=5 value="int">
<select name=ylable_fmt>
 <option value="%.0f%"> no decimal
 <option value="%.1f%"> .0
 <option value="%.2f%"> .00
 <option value="%.3f%"> .000
 <option value="%.4f%"> .0000
</select>
  </td>
 </tr>

 <tr>
  <td>

  </td>
  <td>
<table>$cTable</table>
  </td>
 </tr>


 <tr>
  <td>
COLOURS
  </td>
  <td>
<input type=text name=colours size=50 value="00519C C6D3DE 3f963f 5f5fa0 336699">
  </td>
 </tr>

 <tr>
  <td>
BACKGROUND COLOUR
  </td>
  <td>
<input type=text name=bgcolor size=50 value=FFFFFF>
  </td>
 </tr>

 <tr>
  <td>
GRID COLOUR
  </td>
  <td>
<input type=text name=grid size=50 value=000000>
  </td>
 </tr>


 <tr>
  <td>
WIDTH
  </td>
  <td>
<input type=text name=width size=5 value=160>
  </td>
 </tr>

 <tr>
  <td>
HEIGHT
  </td>
  <td>
<input type=text name=height size=5 value=116>
  </td>
 </tr>

 <tr>
  <td>
TITLE
  </td>
  <td>
<input type=text name=title size=50>
  </td>
 </tr>

 <tr>
  <td>
X-AXIS TEXT
  </td>
  <td>
<input type=text name=x_axis size=50>
  </td>
 </tr>

 <tr>
  <td>
Y-AXIS TEXT
  </td>
  <td>
left:  <input type=text name=y_axis size=50> <br />
right: <input type=text name=y_title2 size=50>
  </td>
 </tr>



 <tr>
  <td> </td>
  <td>
<input type=submit name=page value=draw>
  </td>
</tr>

</table>
</body>
</html>
EndofHTML

}


sub parseDataTable {
    
    local $x = 0;
    local @cells;
   
    local @rows = split (/\n/, $FORM{'data'});
    foreach (@rows) {
	chop();
	if ($x == 0) {
	    $arrayName = "lables";
	} else {
	    $arrayName = "dataset$x";
	    $dataSets .= "\\\@dataset$x, ";
	    $dsCount++;
	}
	$msg .= "<br\>$arrayName cells:";
        @cells = split (/\t/);
	foreach (@cells) {
	    #chop(); # if ($arrayName ne "lables");
	    #$_ = substr ($_, 0, index($_, ".")) if ($arrayName ne "lables");
	    #$_ =~ s/ //g if ($arrayName ne "lables");
	    push @$arrayName, "$_";
	    $msg .= " \|$_\| ";
	    $max = $_ if ($_ > $max);
	}
	$x++;
    }

   
    if ($FORM{'y_max'}) {
	$max = $FORM{'y_max'};
    } else {
	$max = int ($max * 1.2);
    }

    $FORM{'y_interval'} = int (($max-$FORM{'y_min'})/5) if (!$FORM{'y_interval'});

}

sub parseColourData {
    
    local @TEMPcolours = split (/ /, $FORM{'colours'});
    foreach (@TEMPcolours) {
	local $TEMP = hex($_);
	$colour .= "$_ [ $TEMP ]";
	push @colours, $TEMP;
    }
    
}


#################################################################
sub printOutput {

	
    print <<EndofHTML;
Content-type: text/html;

<html>
<head>
<meta HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=ISO-8859-1">
</head>
<body>
$msg <p>
colours $colour<p>
$FORM{'type'}<p>

<table>
<tr>
<td bgcolor=EEEEEE>
&nbsp;<br>
&nbsp;&nbsp;<img src="hlcchart.gif">&nbsp;&nbsp;
&nbsp;<br>
</td>
</tr>
$detail
</table> 
</body>
</html>
EndofHTML

}
