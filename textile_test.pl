#!/usr/bin/perl
#use strict;

use Text::Textile;

my $textile = new Text::Textile;
my $str = <<EOTEXTILE;
  This is a *test*!
EOTEXTILE

    print $textile->process($str);
