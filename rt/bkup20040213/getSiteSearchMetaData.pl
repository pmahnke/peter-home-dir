#!/usr/local/bin/perl

# getSiteSearchMetaData.pl
#
#    gets all the <meta name="" content=""> and puts it in a hash called %Meta

require ("/home/gartner/cgi-bin/gNOlogin.pl");


################################################
sub getMetaTags {


    # Variables
    local undef %Meta;

    local @output = split (/\>/,  &getGARTNERpage($_[0]));
    $msg .= time()." got page<br\>\n";
    foreach (@output) {

	$_ .= "\>";
	
	if ($titleFlag) {
	    $Meta{'realTitle'} = $1 if (/(.[^<\/]*)<\//i);
	    $titleFlag = 0;
	}
	$titleFlag = 1 if (/<title/i);


	$Meta{$1} = $2 if (/name\=\"(.[^\"]*)\" content\=\"(.[^\"]*)\"/i);

	last if (/<\/head\>/i);

    }

    $msg .= time()." processed page<br\>\n";
    return (%Meta);

}

1; # return true




