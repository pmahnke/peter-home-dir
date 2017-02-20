#!/usr/local/bin/perl
use gdchart;
use CGI_Lite;

# Variables
$thisScript = "http://intl.gartner.com/rt/chart.cgi";
$fileName   = "\/home\/gartner\/html\/rt\/chart.gif";
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
	    $xtitleSize = "verysmall";
	    $ytitleSize = "verysmall";
	} elsif ($FORM{'width'} < 400) {
	    $titleSize = "mediumbold";
	    $xtitleSize = "small";
	    $ytitleSize = "small";
	} else {
	    $titleSize = "mediumbold";
	    $xtitleSize = "mediumbold";
	    $ytitleSize = "mediumbold";
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
	$gdchart::GDC_YLabel2Color=hex $colours[1];
	$gdchart::GDC_grid=0;
	$gdchart::GDC_title_size=$titleSize;
	$gdchart::GDC_xtitle_size=$xtitleSize;
	$gdchart::GDC_ytitle_size=$ytitleSize;
	$gdchart::GDC_requested_ymin=$FORM{'y_min'};
	$gdchart::GDC_requested_ymax=$max;
	$gdchart::GDC_requested_yinterval=$FORM{'y_interval'};
	$gdchart::GDC_ylabel_density=100;
	$gdchart::GDC_ylabel_fmt=$FORM{'ylable_fmt'};
	$gdchart::GDC_BGColor= hex($FORM{'bgcolor'});
	$gdchart::GDC_GridColor= hex($FORM{'grid'});

	$gdchart::GDC_ytitle2=$FORM{'y_title2'};



	foreach (sort keys %FORM) {
	    $detail .= "<tr\><td\>$_<\/td\><td\>\|<b\>$FORM{$_}<\/b\>\|<\/td\><\/tr/>\n\n";
	}


	if ($FORM{'type'} eq "line" || $FORM{'type'} eq "bar") {
	    
	    if ($dsCount == 1) {
		
		$plotcolor = hex'00519C' if (!$plotcolor);
		
		if ($FORM{'type'} eq "bar") {
		    
		    
		    $msg .= <<Endoflist;
		    "<p\>\nbar_graph ( $FORM{'width'}, $FORM{'height'}, "\/home\/gartner\/html\/rt\/chart.gif", \@labels, \@dataset1, $plotcolor, $FORM{'title'}, $FORM{'x_axis'}, $FORM{'y_axis'} ); \n<p/>
Endoflist

    bar_graph ($FORM{'width'}, $FORM{'height'}, "\/home\/gartner\/html\/rt\/chart.gif", \@lables, \@dataset1, $plotcolor,"$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");


	    } else {
		

$gdchart::GDC_xtitle_size="small";

	$novalue = $gdchart::GDC_novalue;

		unshift @lables, "";
		    push @lables, "";
		unshift @dataset1, $novalue;
		    push @dataset1, $novalue;

		line_graph  ( $FORM{'width'}, $FORM{'height'}, "/home/gartner/html/rt/chart.gif",
			      \@labels, \@dataset1, $plotcolor, $FORM{'title'}, 
			      $FORM{'x_axis'}, $FORM{'y_axis'});
		
	    }

	                
	} elsif ($dsCount == 2) {
	    
	    double_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "/home/gartner/html/rt/chart.gif", \@lables, \@dataset1, \@dataset2, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	    
#	    $msg .= "type is double_stack<p\>\n\"$FORM{'type'}\", \"$FORM{'stack_type'}\", $FORM{'width'}, $FORM{'height'}, \"/home/gartner/html/rt/chart.gif\", \@lables, \@dataset1, \@dataset2, \@colours, \"$FORM{'title'}\", \"$FORM{'x_axis'}\", \"$FORM{'y_axis'}\"<p\>\n\n";
	
	} elsif ($dsCount == 3) {
	    triple_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	} elsif ($dsCount == 4) {
	    four_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@dataset4, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	} elsif ($dsCount == 5) {
	    five_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@dataset4, \@dataset5, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	} elsif ($dsCount == 6) {
	    six_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@dataset4, \@dataset5, \@dataset6, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	} elsif ($dsCount == 7) {
	    seven_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@dataset4, \@dataset5, \@dataset6, \@dataset7, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	} elsif ($dsCount == 8) {
	    eight_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@dataset4, \@dataset5, \@dataset6, \@dataset7, \@dataset8, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	} elsif ($dsCount == 9) {
	    nine_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@dataset4, \@dataset5, \@dataset6, \@dataset7, \@dataset8, \@dataset9, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	} elsif ($dsCount == 10) {
	    ten_stack ("$FORM{'type'}", "$FORM{'stack_type'}", $FORM{'width'}, $FORM{'height'}, "$fileName", \@lables, \@dataset1, \@dataset2, \@dataset3, \@dataset4, \@dataset5, \@dataset6, \@dataset7, \@dataset8, \@dataset9, \@dataset10, \@colours, "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	}

    } elsif ($FORM{'type'} eq "pie") {

	# pie charts

	if ($FORM{'width'} < 200) {
	    $titleSize = "verysmall";
	} elsif ($FORM{'width'} < 400) {
	    $titleSize = "small";
	} else {
	    $titleSize = "mediumbold";
	}
	$msg .= "<br\>\ntitleSize is: $titleSize<br/>\n";

	$gdchart::GDC_pie_title_size = $titleSize;
	$gdchart::GDC_pie_label_size = "small";
	$gdchart::GDC_pie_label_line = 1;
	$gdchart::GDC_pie_label_dist = 10;
	$gdchart::GDC_pct_placement = "right";

	$FORM{'bgcolor'} = "FFFFFF" if (!$FORM{'bgcolor'});
	
	$gdchart::GDC_pie_bgcolor= hex($FORM{'bgcolor'});
	$gdchart::GDC_GridColor= hex($FORM{'grid'});

	# explode
	#@explode= (0, 25, 0, 0, 40, 0);
	#$gdchart::GDC_pie_explode=\@explode;
  
	# missing chart
	#@missing= (0, 0, 1, 0, 0, 0);
	#$gdchart::GDC_pie_missing=\@missing;


local $count;
local $i = 0;
local $y = 1;
#undef @colours;
#foreach (@colors) {
#  $count++;
#  last if ($count > $#dataset1);
#  $msg .= "pie color is $colors[$i]  ";
#  $msg .= "i is $i and y is $y <br\>";
#  push @colours, hex $colors[$i];
#  $i = $i + 7;
#  if ($i > 24) {
#    $i = $y;
#    $y++;
#  }
#}

$msg .= "max elements is $count<p\>@colours<p\>\n\n";

	pie_chart       ($FORM{'width'}, $FORM{'height'}, "$fileName",
			 \@lables, \@dataset1, \@colours , "2d", "$FORM{'title'}");


    } elsif ($FORM{'type'} eq "combo_line_bar") {
	
	$FORM{'bgcolor'} = "FFFFFF" if (!$FORM{'bgcolor'});
 	

$gdchart::GDC_xaxis=1;
$gdchart::GDC_yaxis1=1;
$gdchart::GDC_yaxis2=1;
$gdchart::GDC_border=1;

	$novalue = $gdchart::GDC_novalue;

		unshift @lables, "";
		    push @lables, "";
		unshift @dataset1, $novalue;
		    push @dataset1, $novalue;
		unshift @dataset2, $novalue;
		    push @dataset2, $novalue;

	
#	$msg .= "type is $FORM{'type'} <br />\n\n datasetcount $dsCount <br\> ymin is $FORM{'y_min'} <br\> ymax is $max <br\> y interval $FORM{'y_interval'}<br/>lables @lables<p> dataset1 @dataset1<p\> dataset1 @dataset2<p\>";
	
	combo_line_bar ( $FORM{'width'}, $FORM{'height'},
			 "/home/gartner/html/rt/chart.gif", 
			 \@lables, \@dataset1, \@dataset2, 
			 $colours[0], $colours[1], 
			 "$FORM{'title'}", "$FORM{'x_axis'}", "$FORM{'y_axis'}");
	
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
&nbsp;&nbsp;<img src="chart.gif">&nbsp;&nbsp;
&nbsp;<br>
</td>
</tr>
$detail
</table> 
</body>
</html>
EndofHTML

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
line: <input type=radio name=type value=line>
pie:  <input type=radio name=type value=pie>
<br />
bar:  <input type=radio name=type value=bar>
line &amp; bar <input type=radio name=type value=combo_line_bar>
  </td>
 </tr>

 <tr>
  <td>
STACK TYPE
  </td>
  <td>
<select name=stack_type>
 <option> pie
 <option value=behind> behind
 <option value=above> above
 <option value-beside> beside
 <option value=layered> layered
</select>
  </td>
 </tr>

 <tr>
  <td>
DATA
  </td>
  <td>
<textarea cols=40 rows=30 name=data></textarea>
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
<input type=text name=width size=5 value=500>
  </td>
 </tr>

 <tr>
  <td>
HEIGHT
  </td>
  <td>
<input type=text name=height size=5 value=300>
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



sub lineChart {


    @dataset = (10, 20, 30, 40, 50);
    @labels = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday");
    $plotcolor=hex'0000cd';
    
    line_graph ( 400, 400, "/home/gartner/html/uot/line_graph.gif",
		 \@labels, \@dataset, $plotcolor, "The Graph", "X Axis",
		 "Y axis");
}



##############################################################
sub barChart {


    undef local @Clables;
    undef local @Cdata;
    undef local @Ctitle;
    undef local $data;
    undef local $date;
    undef local $Cdate;
    undef local $Cn;
    undef local $max;
    local $xaxis     = "chart updated through $CONFIG{Updated}";

    foreach $date (sort @dates) {
	
	
	if (!$$date{$usrId}) {
	    $data = 0;
	} else {
	    $data = $$date{$usrId};
	}

	$Cdate = &niceDatemmyy($date);

	push @Clables, $Cdate;
	push @Cdata, $data;

	$max = $data if ($data > $max);
	
    }
    
    if ($FORM{'y_max'}) {
	$max = $FORM{'y_max'};
    } else {
	$max = $max * 1.2;
    }

    $barcolor  = hex 'ffcccc'; # dark red hex 'ff0000'; # blue hex '0000cd'; # purple hex 'ccccff';
    $Cn = "$_[0]"."$date"."_chart.gif";
    $Cn =~ s/\%20/_/g;
    $Cn =~ s/\,/_/g;
    $Cn =~ s/ö/o/g;
    $Cn =~ s/Å/A/g;

    $Ctitle = $_[0];
    $Ctitle =~ s/\%20/ /g;

    return ($Cn) if (-e "\/tmp\/uotuserimg\/$Cn"); # file exists
    return ($Cn) if (!$max);  # no data
    
    $gdchart::GDC_title_size="mediumbold";
    $gdchart::GDC_xtitle_size="verysmall";
    $gdchart::GDC_ytitle_size="verysmall";
    $gdchart::GDC_requested_ymin=$FORM{'y_min'};
    $gdchart::GDC_requested_ymax=$max;
    $gdchart::GDC_ylabel_fmt="%.0f%";
    
    bar_graph (300, 150, "\/tmp\/uotuserimg\/$Cn", \@Clables, \@Cdata, $barcolor,"$Ctitle", $xaxis, "Docs Read");

    
    
    return($Cn);
    

}


sub pieChart {

    $legend = "<table class\=legend\>\n\n\n";
    
    @colors=( "\#FF9999", "\#FFCC99", "\#FFFF99", "\#CCFF99", "\#CC99FF", "\#9999FF", "\#99CCFF", "\#CC6666", "\#993333", "\#339999");

    foreach $color (@colors) {
	local $colour = substr($color,1,6);
	push @piecolors, hex $colour;
    }
    foreach $key (sort {$kmap{$b} <=> $kmap{$a} }keys %kmap) {
	
	next if ($counter > 9);

	push @kmap, $lable;
	push @dataset, $kmap{$key};

	local $colour = substr($colors[$counter],1,6);
	local $image = "\/uot\/img\/"."$colour".".gif";
	$legend .= "<tr\><td width\=5\><img src\=$image\><\/td\><td nowrap\>$key<\/td\><\/tr\>\n\n";
	$counter++;	
    }
    $legend .= "<tr\><td colspan\=2><i\>pie chart is for current month \($niceDate\) only<\/td\><\/tr\>\n\n<\/table\>\n\n\n";


    use gdchart;


    $gdchart::GDC_pie_title_size = "mediumbold";
    $gdchart::GDC_pie_label_size = "verysmall";
    $gdchart::GDC_pie_label_line = 0;
#    $gdchart::GDC_pie_label_dist = 10;
    $gdchart::GDC_pct_placement = "above";
  


    pie_chart       (200, 200, "\/tmp\/uotuserimg\/$_[0]",
		     \@kmapw, \@dataset, \@piecolors , "2d", "Top KMAP Nodes");

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
