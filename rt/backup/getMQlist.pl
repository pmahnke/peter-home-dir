#!/usr/local/bin/perl

require ("/home/gartner/cgi-bin/glogin_regionals.pl");

# MQs
$URL = "http:\/\/regionals4.gartner.com/mq/asset_50486.jsp";
&getList;
&save('MQ');
undef %output;

# HCs
@URL = ("http:\/\/regionals4.gartner.com\/hc\/asset_50595.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50597.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50598.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50602.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50599.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50601.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50604.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50635.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50605.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50607.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50609.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50625.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50628.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50629.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50631.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50611.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50613.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50615.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50616.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_51279.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50618.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50633.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50620.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50632.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50621.jsp", "http:\/\/regionals4.gartner.com\/hc\/asset_50623.jsp");
foreach $URL (@URL) {
    print "getting $URL\n\n";
    &getList;
}
&save('HC');
undef %output;




print "\n\nDone.\n\n";

exit;

##########################################################
sub save {

    $file = "/home/gartner/html/rt/content/$_[0]"."\.csv";
    open (FILE, ">$file") || die "Can't open file: $file\n\n";
    foreach (values %output) {    
	print FILE $_;
    }
    close (FILE);

    return;

}

##########################################################
sub getList {

    
    $msg .=  "\nurlIncl: GETTING URL $URL\n";
    
    local $document = &getGARTNERpage($URL, $ARGV[1]);
    
    
    undef local $link;
    undef local $title;
    undef local $date;
	
    
    #process document
    local @doc = split (/\n/, $document); # split on newlines
       
    foreach (@doc) {
	$c++;
	print "$c $_ \n\n" if (/popUpQuadrant\(\d\d\d\d\d\d\)\;\" class\=\"BoldBlueLink\"\>(.[^<\/]*)<\//);


	$start = 1 if (/popUpQuadrant/);
	next if (!$start);
    
	if (/javascript:popUpQuadrant\((\d\d\d\d\d\d)\)\;\" class\=\"BoldBlueLink\"\>(.[^<]*)</) {
	    print "found at $_\n   title $2    link  $1\n";
	    $link  = $1;
	    $title = $2;
	}
	
	if (/<span class\=\"mqGrayText\"\>(\d.[^<\/]*)<\//) {
	    $date = $1;
	    print "   date  $1\n\n";

	    $output{$link} = "$link\t$date\t$title\n";

            undef $link;
	    undef $title;
	    undef $date;
	}

    }
}

1;
