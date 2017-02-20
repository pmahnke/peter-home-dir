#!/usr/bin/perl

open(SENDMAIL, "| /usr/lib/sendmail -f \"peter\@mahnke.net\" -t");
print SENDMAIL "To: $ARGV[0]\n";
print SENDMAIL "Subject: $ARGV[1]\n";
print SENDMAIL "$ARGV[2]\n\n";
close(SENDMAIL);
