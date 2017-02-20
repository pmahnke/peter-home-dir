#!/usr/local/bin/perl


require ("/home/gartner/html/rt/SmartyPants.pl");
require ("/home/gartner/html/rt/replaceChars.pl");
require ("/home/gartner/html/rt/common.pl");
local $metaFile = "/home/gartner/html/deDocs/docs/metaDataIndex.db";
local $img = "/regionalization/img/content/emea/de/de_predicts_fp.gif";

&readDB;

my $c = 0;
foreach $key (reverse keys %results) {
    
#	if ($c < 1) {
    if ($key =~ /418584/) {
	# print fancy
	local $filename = "/home/gartner/html/rt/content/emea/de/de_fancy_"."$c".".incl";
	open (FP, ">$filename") || die "Can't open: $filename\n";
	print FP "$fancy{$key}\n\n";
	close (FP);
	
	$filename = "/home/gartner/html/rt/content/emea/de/home_de_fr_highlight_"."0$c".".incl";
	open (FP, ">$filename") || die "Can't open: $filename\n";
	print FP "$fancyHTML{$key}\n\n";
	close (FP);
	
    } elsif ($c % 2 != 0)  {
	
	$left  .= "$results{$key}\n\n";
	$html  .= "$simpleHTML{$key}\n\n" if ($c < 3);
	
    }  else {
	
	$right .= "$results{$key}\n\n";
	$html  .= "$simpleHTML{$key}\n\n" if ($c < 3);
	
    }
    $c++;
}


&saveHTML;

print "done.\n\n";
exit;


#########################################################################
sub saveHTML {

	# save rest
	open (FP, ">/home/gartner/html/rt/content/emea/de/de_rest.incl") || die "Can't open: de_rest.incl\n";

        print FP <<EOF;

        <tr bgcolor="#ffffff">
         <td colspan="3"><p class="head1">Weiterer Research auf Deutsch</p></td>
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


        close (FP);

	open (FP, ">/home/gartner/html/rt/content/emea/de/home_de_fr_headlines.incl") || die "Can't open: home_de_fr_headlines.incl\n";

        print FP $html;
        close (FP);
}


#########################################################################
sub readDB {


    use Text::Iconv;
    my $converter = Text::Iconv->new("utf-8", "iso-8859-1");
    my %meta;


	open (DB, "$metaFile") || die "Can't open db: $metaFile\n";

	while (<DB>) {

		chop();

    		my $converted = $converter->convert($_);

#    		$converted = &replaceCharacters($converted);

    		my @pairs = split (/\|/, $converted);


    		foreach (@pairs) {

    			my ($key, $value) = split (/\=/);
    			$meta{$key} = $value;

    		}

    		my @authors = split (/\&/, $meta{'AUTHOR'});
    		my $author = "";

    		foreach (@authors) {

    			# http://regionals4.gartner.com/AnalystBiography?authorId=9757

    			my ($name, $code) = split(/,/);
    			$author .= " <a href\=\"http:\/\/regionals4.gartner.com\/AnalystBiography?authorId\=$code\" class\=\"author\" \>$name<\/a> \|";

    		}
    		chop ($author); # remove trailing |

    		$key = "$meta{'LOCALEPUBDATE'}$meta{'GGRESID'}";
#    		$key = $key + 1 while { exists $results{$key} };


		my $hightitle = &noHang ($meta{'TITLE'}, 44);
		$hightitle    = &SmartyPants ($hightitle);
		$hightitle    = &replaceCharacters($hightitle);

		my $frtitle   = &noHang ($meta{'TITLE'}, 50);
		$frtitle      = &SmartyPants ($frtitle);
		$frtitle      = &replaceCharacters($frtitle);

		my $title     = &SmartyPants ($meta{'TITLE'});
		$title        = &replaceCharacters($title);


		my $summary   = &SmartyPants ($meta{'GGSUMMARY'}, 1);
		$summary      = &replaceCharacters($summary);

		$summary = substr ($summary, 0, index($summary, ".") + 1);


    		$results{$key} = <<EOF;
     <li>
      <p class="fpTitle"><a href="javascript:void(null)" onclick="openDocFromDoc('/regionalization/code/document.jsp?resId=$meta{'GGRESID'}&amp;ct=de&amp;gen=y')">$title</a></p>
      <p><span class="fpDate">$meta{'LOCALESERVICE'} -  $meta{'LOCALEPUBDATE'}</span></p>
      <p class="fpSummary">$summary</p>
     </li>

EOF

		$fancy{$key} =<<EOF;
<div class="focalpoint">
    <p><a href="javascript:void(null)" onclick="openDocFromDoc('/regionalization/code/document.jsp?resId=$meta{'GGRESID'}&amp;ct=de&amp;gen=y')"><img src="$img" width="100" height="68" alt="$title" border="0" align="text-left" hspace="5" /></a></p>
    <a href="javascript:void(null)" onclick="openDocFromDoc('/regionalization/code/document.jsp?resId=$meta{'GGRESID'}&amp;ct=de&amp;gen=y')">$title</a>
    <p><span class="date">$meta{'LOCALESERVICE'} -  $meta{'LOCALEPUBDATE'}</span><br />
       $summary</p>
</div>

EOF

#	$summarySmall = substr ($summary, 0, index($summary, ".") + 1);


		$fancyHTML{$key} =<<ENDofHTML;
<!-- start featured research highlight -->
<tr><td width="356" height="10" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="10" alt="" border="0"></td></tr>
<tr><td width="350" bgcolor="#FFFFFF" valign="top" colspan="2"><a href="javascript:void(null)" onclick="openDocFromDoc('/regionalization/code/document.jsp?resId=$meta{'GGRESID'}&amp;ct=de&amp;gen=y')"><img src="$img" width="100" height="68" hspace="6" align="left" alt="$title" border="0"></a><table border="0" cellspacing="0" cellpadding="0"><tr><td><a href="javascript:void(null)" onclick="openDocFromDoc('/regionalization/code/document.jsp?resId=$meta{'GGRESID'}&amp;ct=de&amp;gen=y')" class="largeBlueLink">$hightitle</a><br /><span class="smallGrayText">$summary</span><br /></td></tr></table></td><td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td></tr>
<!-- end featured research highlight 1 -->
ENDofHTML


		$simpleHTML{$key} =<<EndofHTML;
<!--start research  - $title $meta{'LOCALESERVICE'} -  $meta{'LOCALEPUBDATE'}  -->
    <tr><td width="356" height="8" colspan="3" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="356" height="8" alt="" border="0"></td></tr>
    <tr><td width="22" bgcolor="#FFFFFF" valign="top" align="center"><a href="javascript:void(null)" onclick="openDocFromDoc('/regionalization/code/document.jsp?resId=$meta{'GGRESID'}&amp;ct=de&amp;gen=y')" class="smallBlueLink"><img src="//img/homepage/reversed_orange_arrow.gif" width="9" height="9" vspace="2" alt="$title" border="0"></a></td>\n        <td width="328" valign="top" bgcolor="#FFFFFF"><a href="javascript:void(null)" onclick="openDocFromDoc('/regionalization/code/document.jsp?resId=$meta{'GGRESID'}&amp;ct=de&amp;gen=y')" class="smallBlueLink">$frtitle</a></td>\n        <td width="6" bgcolor="#FFFFFF"><img src="/images/trans_pixel.gif" width="6" height="1" alt="" border="0"></td>\n    </tr>
<!--end research - $title $meta{'LOCALESERVICE'} -  $meta{'LOCALEPUBDATE'} -->

EndofHTML

    	}




    	return();

}
