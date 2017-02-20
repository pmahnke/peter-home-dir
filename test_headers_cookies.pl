#!/usr/bin/perl


use LWP::Simple;

my $url = qq|http://www.ubuntu.com/download/desktop/questions?distro=desktop&bits=32&release=latest|;
#$url = qq|http://www.ubuntu.com/download/desktop/questions?distro=desktop&bits=32&release=lts|;

use LWP::UserAgent;
$ua = LWP::UserAgent->new;

$req = HTTP::Request->new(GET=>$url);

$res = $ua->request($req);

# check the outcome
if ($res->is_success) {
    print "\n\nCookie: " . $res->header( 'Set-Cookie' );
    print "\nCache: " . $res->header( 'X-Cache' );
    my $content = $res->content;
    @content = split(/\n/, $content);
    foreach (@content) {

	print "\nCode: $_\n\n" if (/066-EOV-335/);
    }

    print "\n\n";
}
else {
    print "Error: " . $res->status_line . "\n";
}
