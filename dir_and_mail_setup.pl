#!/usr/bin/perl

print "\nRun this as the shell of the web account in the root of the web account with one argument, the name of the web account!\n\n\tapache_setup.pl webacct (i.e. mahnke if the site is mahnke.net)

It will setup the virtual mail files for the virtual domain as well as all the web directories.

You still have to add the account to \/var\/qmail\/control rcpthosts and virtualdomains file control lists\n\n" if (!$ARGV[0]);

open (FILE, ">/home/$ARGV[0]/.qmail") || die;
print FILE "./Maildir/\n";
close (FILE);
`mkdir html`;
`mkdir cgi\-bin`;
`mkdir logs`;
`mkdir include`;
`mkdir servlets`;
`chgrp users *`;
`chown  $ARGV[0] *`;
`chown  $ARGV[0] .qmail`;
`chgrp users .qmail`;
`vsetup`;

print "done setting up $ARGV[0] !\n\n";
exit;
