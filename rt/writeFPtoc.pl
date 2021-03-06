#!/usr/local/bin/perl

########################################################################
#
#    writeFPtoc.pl
#
#        writen:    18 Feb 2004 by Peter Mahnke
#
#        run from command line, or cron
#
#        script creates the three includes required to produce the
#        regionals sites Focal Point archives for each year
#
#        it reads /home/gartner/html/rt/content/fp.csv for the
#        list of all the FPs and then creates the various include files
#
#        all the text is made 'nice' with SmartyPants.pl
#
#        OUTPUTS
#        FP w/ picture 1:  /home/gartner/html/rt/content/emea/fp_fancy_<yyyy>_1.incl
#        FP w/ picture 2:  /home/gartner/html/rt/content/emea/fp_fancy_<yyyy>_2.incl
#        FP List:          /home/gartner/html//rt/content/emea/fp_rest_<yyyy>.incl
#
#
########################################################################

require ("/home/gartner/html/rt/SmartyPants.pl");
local $fileFP = "/home/gartner/html/rt/content/fp.csv";



&readFP;


foreach $y (sort @years) {

    # process a year at a time

    local $c = 1;
    local $left = "";
    local $right = "";
    foreach $key (reverse sort @$y) {

	print "$y\t$key\t$title{$key}\n";

	local $date = &proccessDate($key);

	if ($c < 3) {

	    # print fancy 2
	    local $filename = "/home/gartner/html/rt/content/emea/fp_fancy_"."$y"."_"."$c".".incl";
	    open (FP, ">$filename") || die "Can't open: $filename\n";

	    print FP <<ENDofHTML;
<div class="focalpoint">
    <p><a href="$url{$key}"><img src="http://www.gartner.com/$img{$key}" width="100" height="68" alt="$title{$key}" border="0" align="text-left" hspace="5" /></a></p>
    <a href="$url{$key}">$title{$key}</a>
    <p><span class="date">$date</span><br />
       $desc{$key}</p>
</div>

ENDofHTML
            close (FP);

	} elsif ($c < ($#$y + 4) / 2)  { # } elsif ($c % 2 != 0)  {

	    # print rest EVEN

	    $left .= <<ENDofHTML;

     <li>
      <p class="fpTitle"><a href="$url{$key}">$title{$key}</a></p>
      <p><span class="fpDate">$date</span></p>
      <p class="fpSummary">$desc{$key}</p>
     </li>

ENDofHTML

        } else {

	    # print rest ODD

	    $right .= <<ENDofHTML;

     <li>
      <p class="fpTitle"><a href="$url{$key}">$title{$key}</a></p>
      <p><span class="fpDate">$date</span></p>
      <p class="fpSummary">$desc{$key}</p>
     </li>

ENDofHTML
       }


	$c++;

	# save rest
	open (FP, ">/home/gartner/html/rt/content/emea/fp_rest_$y.incl") || die "Can't open: fp_rest.incl\n";

	if ($left) {

	    print FP <<EOF;

        <tr bgcolor="#ffffff">
         <td colspan="3"><p class="head1">More European Research Highlights</p></td>
        </tr>

        <tr bgcolor="#ffffff">
         <td valign="top">
<ul class="fpList">
$left
</ul>
  </td>
  <td></td>
  <td valign="top">
<ul class="fpList">
$right
</ul>
         </td>
        </tr>

EOF
       } else {
	   print FP " ";
       }

        close (FP);


    }
}






####################################################################
sub readFP {

    open (FP, "$fileFP") || die "Can't open FP: $fileFP\n";
    while (<FP>) {

	chop();
	local ($key, $t, $desc, $u, $i, $d) = split (/\t/);

	local $y = substr ($key, 0, 4);
	$years{$y}++;
	push @$y, $key;

	$title{$key} =  &SmartyPants ($t, 1);
	$desc{$key}  =  &SmartyPants ($desc, 1);
	$url{$key}   = $u;
	$img{$key}   = $i;
	$date{$key}  = $d;


    }
    close (FP);


    foreach $y (keys %years) {
	push @years, $y;
    }


}

####################################################################
sub saveFP {

	&readFP;

	open (FP, ">$fileFP") || die "Can't open FP: $fileFP\n";

        print FP "$FORM{'key1'}\t$FORM{'title1'}\t$FORM{'desc1'}\t$FORM{'url1'}\t$FORM{'img1'}\t$FORM{'date1'}\n";
        print FP "$FORM{'key2'}\t$FORM{'title2'}\t$FORM{'desc2'}\t$FORM{'url2'}\t$FORM{'img2'}\t$FORM{'date2'}\n";

	foreach $key (reverse sort @key) {

		next if ($key =~ /$FORM{'key1'}/ && $FORM{'updated1'});
		next if ($key =~ /$FORM{'key2'}/ && $FORM{'updated2'});


		print FP "$key\t$title{$key}\t$desc{$key}\t$url{$key}\t$img{$key}\t$date{$key}\n";

	}

	close (FP);

}


########################################################################
sub proccessDate {

    local ($d, $m, $y);
    $y = substr ($_[0], 0, 4);
    $m = substr ($_[0], 4, 2);
    $d = substr ($_[0], 6, 2);


    $m{'01'} = "January"; # = "01";
    $m{'02'} = "February"; # = "02";
    $m{'03'} = "March"; # = "03";
    $m{'04'} = "April"; # = "04";
    $m{'05'} = "May"; # = "05";
    $m{'06'} = "June"; # = "06";
    $m{'07'} = "July"; # = "07";
    $m{'08'} = "August"; # = "08";
    $m{'09'} = "September"; # = "09";
    $m{'10'} = "October"; # = "10";
    $m{'11'} = "November"; # = "11";
    $m{'12'} = "December"; # = "12";

    $d =~ s/^0//;

    local $newdate = "$d $m{$m} $y";
    return($newdate);

}
