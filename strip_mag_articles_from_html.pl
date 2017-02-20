#!/usr/local/bin/perl

# writen by peter mahnke on 24 Sept 2009

use LWP::UserAgent;

if (!$ARGV[0]) {

	print qq |
	
strip_mag_articles_from_html.pl
	
	this will strip the non-article html from the mag articles and save
	
	usage is: strip_mag_articles_from_html.pl <file - list of URLS>
	
	|;
	exit;

}


my $log = "log_mag_articles.txt";
open (LOG, ">$log") || die "Can't open file : $log\n";

print STDERR "\n\nlog file running: tail -f $log\n";

open (DATA, "$ARGV[0]") || die "Can't open $ARGV[0]\n";
        
while (<DATA>) {

    chomp;
    
    next if (!$_);
    
    print LOG "looking at url: $_\n";
    
    # get filename ready
    # example url http://magazines.scholastic.co.uk/content/7227
    my @name = split (/\//, $_);
    my $filename = "mags\/".$name[$#name].".html.erb";
    
    my $page = &ConnectionGet($_);
    
    print LOG "got page: $_\n";
    
    $page = &processPage($page) if ($page);	
    
    print LOG "saving page at: $filename\n";
    
    open (PAGE, ">$filename") || die "Can't open $filename for saving\n";
    print PAGE $page;
    close (PAGE);
    
}
close (DATA);

print LOG "Done.\n\n";
close (LOG);

print "Done.\n\n";

exit;




sub processPage {

    my ($FLAGstart, $output, $lastline) = "";
    
    
    my @lines = split (/\n/, $_[0]);

    foreach (@lines) {

        # don't start until initial h1
        $FLAGstart = 1 if (/<h1>/);
        next if (!$FLAGstart);
        
	# end here
        return($output) if (/<div class\=\"clearfloat\"><\/div>/);
	
	next if ($lastline =~ /<br\/>/ && $_ =~ /<br\/>/);
	
	$lastline = $_;
	$output .= $_."\n";
        
    }
	return($output);
}





##########################################################
sub ConnectionGet {

    # Create a user agent object
    my $ua = new LWP::UserAgent;
    $ua->agent("$user_agent");

    # Create a request
    # parse URL to go to server we are authenticated on
    my $u = $_[0];
    my $req = new HTTP::Request('GET', $u);

    # Pass request to user agent and get response
    my $res = $ua->request($req);

    my $Output = $res->content;

    # Check output
    if ($res->is_success) {
		$res->status_line, "<p\>\n\n\n";
        return($Output);
    } else {
        return($Output, $_[0]); # return error info and url attempted
    }

}                        # end of sub Connection
