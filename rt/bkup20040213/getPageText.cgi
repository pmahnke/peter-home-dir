#!/usr/local/bin/perl

require ("/home/gartner/cgi-bin/gNOlogin.pl");
use CGI_Lite;

# Variables
local $server = "regionals4";


# expects full url to doc
# i.e. http://www4.gartner.com/DisplayDocument?id=361453&acsFlg=accessBought

##############################################################
# Get the input from the HTML Form

if ($ENV{'CONTENT_LENGTH'}) {

    $cgi = new CGI_Lite;
    %FORM = $cgi->parse_form_data;
#    $FORM{'url'} = url_encode ($FORM{'url'});

} elsif ($ENV{'QUERY_STRING'}) {
    local $buffer = $ENV{'QUERY_STRING'};

# Split the name - value pairs
    @pairs = split(/&/, $buffer);
    foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ s/\+/ /g; # spaces
	$value =~ s/\&lt\;/\</g; # less thans
	$value =~ s/\&amp\;/\&/g; # ampersans
	$value =~ s/%(..)/pack("c",hex($1))/ge; # rest
	
	$FORM{$name} = $value;
    }
    
} else {

    &printForm;

    exit;

}


if ($FORM{'post'}) {
    
    if ($FORM{'post'} eq "jay") {

	&processJay;
	$msg = "<h3\>JAY OUTPUT<\/h3\>\n\n";
	&printForm;

    } else {

	# ftp meta data to the server
	
	$msg = "<h3\>OUTPUT<\/h3\>\n\n";
	
	&save;
	
	$msg .= "<p\>\n\n<hr size\=1\>\n\n";
	&printForm;
	
    }

} else {

    &getDoc($FORM{'url'});

    &printOutput;

}

exit;



####################################################
sub printForm {

    &readP2P;
    

    print <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>get meta data for site search</title>
</head>
<body>
<form method=GET>

$msg

URL: <input type=text size=60 name=url><p>
<select name=url>
$dropDown
</select><p>

<input type=submit>
</form>
</body>
</html>

EndofHTML


}


############################################################
sub getDoc {

    $msg .= time()." got request<br\>\n";
    local %Meta = &getMetaTags($_[0],$server);
    $msg .= time()." got data<br\>\n";
    if (!%Meta) {
	$msg .= "didn't get $_[0]<br\>\n";
    } else {
	
        @keysList = ('author', 'category', 'default', 'description', 'eventdate', 'eventlocation', 'eventtimezone', 'expirationdate', 'issearchable', 'keywords', 'language', 'mimetype', 'producername', 'publishdate', 'subject', 'title', 'windowheight', 'windowwidth');
	
	foreach $key (keys %Meta) {
	    
	    $list .= "$key \- $Meta{$key} <br\>";
	    
	    foreach (@keysList) {
		
		if ($key =~ /$_/i) {
		    next if ($key =~ /language/i);
		    if ($key =~ /title/i) {
			$title = $Meta{$key};
			next;
		    }

		    if ($key =~ /Description/i) {
			$desc = $Meta{$key};
		    } else {
			$line .= "\&lt\;meta name\=\"$key\" content\=\"$Meta{$key}\"\>\n";
		} 
    		}
	    }
	    
	}
    }
}



############################################################
sub printOutput {

    &readP2P;
    $outputFile = $1 if ($gcom2reg{$FORM{'url'}} =~ /(.[^\.]*)\./);
    $outputFile .= "_metadata.incl";

    $url = $1 if ($FORM{'url'} =~ /http:\/\/www4.gartner.com(.*)/i);

    $msg .= time()." printing<br\>\n";

    if (!$title) {
	$title = $Meta{'realTitle'};
    }

    # $title =~ s/^Gartner//; # used if prepending Gartner Europe (etc)

    print  <<EndofHTML;
Content-type:  text/html

<html>
<head>
<title>meta data</title>
</head>
<body>
<form method=POST>

<h1>meta data</h1>
<input type=hidden name=gcomUrl value=$FORM{'url'}>
<h4> from <a href=$FORM{'url'} target=viewpage>$FORM{'url'}</a></h4>
<!-- $msg -->
<p>
<pre>


output filename: <input type=text name=filename value="$outputFile" size=100>

Gartner Europe from <a href=http://regionals4.gartner.com/regionalization/content/emea/$gcom2reg{$FORM{'url'}} target=ge>$gcom2reg{$FORM{'url'}}</a>

<textarea name=emea rows=10 cols=70>
&lt;meta name="gcomPage" content="$url">
&lt;meta name="site" content="Gartner Europe">
&lt;meta name="language" content="English">
&lt;meta name="title" content="$title">
&lt;meta name="Summary" content="Gartner Europe &#151; $desc">
&lt;meta name="Description" content="Gartner Europe &#151; $desc">

$line
</textarea>

<hr size=1>

Gartner Italia from <a href=http://regionals4.gartner.com/regionalization/content/emea/it/$gcom2reg{$FORM{'url'}} target=gi>$gcom2reg{$FORM{'url'}}</a>

<textarea name=it rows=10 cols=70>
&lt;meta name="gcomPage" content="$url">
&lt;meta name="site" content="Gartner Italia">
&lt;meta name="language" content="Italiano">
&lt;meta name="title" content="$title">
&lt;meta name="Summary" content="Gartner Italia &#151; $desc">
&lt;meta name="Description" content="Gartner Italia &#151; $desc">
$line
</textarea>


<hr size=1>

Gartner Deutschland from <a href=http://regionals4.gartner.com/regionalization/content/emea/de/$gcom2reg{$FORM{'url'}} target=gd>$gcom2reg{$FORM{'url'}}</a>

<textarea name=de rows=10 cols=70>
&lt;meta name="gcomPage" content="$url">
&lt;meta name="site" content="Gartner Deutschland">
&lt;meta name="language" content="Deutsche">
&lt;meta name="title" content="$title">
&lt;meta name="Summary" content="Gartner Deutschland &#151; $desc">
&lt;meta name="Description" content="Gartner Deutschland &#151; $desc">
$line
</textarea>

<input type=submit name=post value=qa> <input type=submit name=post value=prod> <input type=submit name=post value=jay>

Raw Listing
$list 

To: Jay.Chiarito\@gartner.com

<textarea name=jay>
To: Peter.Mahnke\@gartner.com
From: Peter.Mahnke\@gartner.com
Subject: regional meta data [$title] - for your approval

regional web site meta data
$title

------------------------------------------------
Gartner.com
--
$FORM{'url'}
--
$line
--

------------------------------------------------
Gartner Europe Page
--
http://regionals4.gartner.com/regionalization/content/emea/$gcom2reg{$FORM{'url'}}
--
&lt;meta name="language" content="English">
&lt;meta name="title" content="$title">
$line
--

------------------------------------------------
<hr size=1>

Gartner Italia
--
http://regionals4.gartner.com/regionalization/content/emea/it/$gcom2reg{$FORM{'url'}}
--
&lt;meta name="language" content="Italiano">
&lt;meta name="title" content="$title">
$line
--

------------------------------------------------
Gartner Deutschland
--
http://regionals4.gartner.com/regionalization/content/emea/de/$gcom2reg{$FORM{'url'}}
--
&lt;meta name="language" content="Deutsche">
&lt;meta name="title" content="$title">
$line
----
</textarea>



</pre>
<p>
</form>
</body>
</html>

EndofHTML



}

sub save {

    if ($FORM{'post'} eq "qa") 
    {
	$passwd     = "pmahnke:hi11top";
	$server     = "kitkat.gartner.com/";
    } 
    elsif ($FORM{'post'} eq "prod") 
    {
	$passwd     = "pmahnke:hi11top";
	$server     = "twix.gartner.com/";
    } 

    $remoteFile = "regionalization/templates/emea/$FORM{'filename'}";
    $msg .= &ftp($FORM{'emea'});
    
    $remoteFile = "regionalization/templates/emea/it/$FORM{'filename'}";
    $msg .= &ftp($FORM{'it'});
    
    $remoteFile = "regionalization/templates/emea/de/$FORM{'filename'}";
    $msg .= &ftp($FORM{'de'});
    

    sub ftp {
	# include the necessary libraries
	use LWP::UserAgent;
	use HTTP::Request;
	
	# define the URL of the file to put ($u)
	$u = "ftp://".$passwd."\@".$server.$remoteFile;
	
	# create the user agent ($a)
	$a = new LWP::UserAgent;
	
	# create the request ($r)
	$r = new HTTP::Request 'PUT', "$u";
	$r->content($_[0]);
	
	# PUT it and save the output ($o)
	$o = $a->request($r);
	
	return($u);
    }
}


sub processJay {



    open (MAIL, "| /usr/sbin/sendmail -t >& /dev/null");
    print MAIL "$FORM{'jay'}\n.";
    close (MAIL);



}


############################################################
sub readP2P {

    # reads a file with a list of page to page comparison from gartner.com namespace to regionals

    open (P2P, "/home/gartner/html/rt/page2page.txt");
    while (<P2P>) {
	
	chop();

	local ($reg, $gcom) = split (/\t/);

	$gcom2reg{$gcom} = $reg;
	$reg2gcom{$reg}  = $gcom;

	$dropDown .= "<option value\=\"$gcom\"\> $gcom\n" if ($gcom ne "NA");

    }

    close (P2P);

}






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
