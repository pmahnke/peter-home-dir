#!/usr/local/bin/perl


require ("/home/gartner/html/rt/SmartyPants.pl");
require ("/home/gartner/html/rt/replaceChars.pl");
require ("/home/gartner/html/rt/common.pl");
local $metaFile = "/home/gartner/html/deDocs/docs/metaDataIndex.db";
local $img = "/regionalization/img/content/emea/de/de_predicts_fp.gif";

&readDEdb;

foreach $y (sort @years) {

    print "\nlooking at year: $y\n\n";

    # process a year at a time

    local $c = 1;
    local $left  = "";
    local $right = "";
    local $rest  = "";

    foreach $key (reverse sort @$y) {

		local $date = &proccessDate($key);

		# $m is the current month in MM format
		# $m{$m} is the german month
		print "$c: date: $date month: $m and title: $title{$key}\n";

		if ($m ne $previousMonth && $c > 2) {

		    # print "not equal: $c\n";
		    # new month, so print a heading....
		    &formatBYmonth($previousMonth);
		    $left  = "";
		    $right = "";
		    $c = 3;

		}

		if ($c < 3) {

		    # only format the first 2 "fancy"

		    # print fancy 2
		    local $filename = "/home/gartner/html/rt/content/emea/de/de_fancy_"."$y"."_"."$c".".incl";
		    open (FP, ">$filename") || die "Can't open: $filename\n";

		    print FP <<ENDofHTML;
<dl class="focalpoint">
    <dt><a href="$url{$key}"><img src="$img{$key}" width="100" height="68" alt="$title{$key}" border="0" /></dt>
    <dd><a href="$url{$key}">$title{$key}</a></dd>
    <dd><em>$date</em></dd>
    <dd>$desc{$key}</dd>
</dl>

ENDofHTML
            close (FP);

		} elsif ($c  % 2 == 0 ) {   # ($#$y + 4) / 2)  { # } elsif ($c % 2 != 0)  {

		    # print rest EVEN

		    $right .= <<ENDofHTML;
     <li><a href="$url{$key}">$title{$key}</a><br>$desc{$key}</li>
ENDofHTML

        } else {

	    	# print rest ODD

	    	$left .= <<ENDofHTML;
     <li><a href="$url{$key}">$title{$key}</a><br>$desc{$key}</li>
ENDofHTML
       	}


		$c++;
		$previousMonth = $m if ($c > 2); # store current month to see if its changed



    }

    &formatBYmonth($m);
    &saveRest;

}



sub formatBYmonth {

    return() if (!$left && !$right);

	$rest .= <<EOF;

        <tr bgcolor="#ffffff">
         <td colspan="3"><p class="head2">$m{$_[0]}</p></td>
        </tr>

        <tr bgcolor="#ffffff">
         <td valign="top">
<ul class="regionalFPlist">
$left
</ul>
  </td>
  <td></td>
  <td valign="top">
<ul class="regionalFPlist">
$right
</ul>
         </td>
        </tr>

EOF

}

sub saveRest {

	# save rest
	open (FP, ">/home/gartner/html/rt/content/emea/de/de_rest_$y.incl") || die "Can't open: fr_rest.incl\n";
	print FP <<EOF;
	<tr bgcolor="#ffffff">
          <td colspan="3"><p class="head1">Weitere Research Highlights</p></td>
        </tr>
EOF
	print FP $rest;
        close (FP);

}


####################################################################
sub readDEdb {

	local $fileDetail = "/home/gartner/html/rt/content/emea/de/FRde.csv";

	open (FP, "$fileDetail") || die "Can't open File Detail to read: $fileDetail\n";
	while (<FP>) {

		chop();
		local ($key, $resid, $t, $desc, $u, $i, $d) = split (/\t/);

		$msg .= "$frCodes match? $key<br />\n";

		next if ($_[0] !~ /$key/ && $_[0]); # skip if not in code list

		$msg .= "matched<br />\n";

		# one time date fix up for first set of research
		$key =~ s/20040309/20040229/;

		# CREATE DATE BASED KEYS
		local $y = substr ($key, 0, 4);
		$years{$y}++;
		push @$y, $key;



		push @key, $key;
		$resid{$key} = $resid;
		$title{$key} = &replaceCharacters($t);
		$desc{$key}  = &replaceCharacters($desc);
		$url{$key}   = $u;
		$img{$key}   = $i;
		$date{$key}  = $d;

	}
	close (FP);

    foreach $y (keys %years) {
		push @years, $y;
    }

}


########################################################################
sub proccessDate {

    local ($d, $y);
    $y = substr ($_[0], 0, 4);
    $m = substr ($_[0], 4, 2);
    $d = substr ($_[0], 6, 2);


    $m{'01'} = "Januar"; # = "01";
    $m{'02'} = "Februar"; # = "02";
    $m{'03'} = "M&auml;rz"; # = "03";
    $m{'04'} = "April"; # = "04";
    $m{'05'} = "Mai"; # = "05";
    $m{'06'} = "Juni"; # = "06";
    $m{'07'} = "Juli"; # = "07";
    $m{'08'} = "August"; # = "08";
    $m{'09'} = "September"; # = "09";
    $m{'10'} = "Oktober"; # = "10";
    $m{'11'} = "November"; # = "11";
    $m{'12'} = "Dezember"; # = "12";


    $d =~ s/^0//;

    local $newdate = "$m{$m} $y";
    return($newdate);

}
