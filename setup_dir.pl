#!/usr/bin/perl

if (!@ARGV) {
    print "

Uaage:  username


";
    exit;
}


$dir = "/home/".$ARGV[0];
`mkdir -p $dir`;
`mkdir -p $dir/logs`;
`mkdir -p $dir/html`;
`mkdir -p $dir/cgi-bin`;
`chown -R $ARGV[0].users $dir`;

print "Done.\n\n";
