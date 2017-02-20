# This file is auto-generated by the Perl DateTime Suite time zone
# code generator (0.07) This code generator comes with the
# DateTime::TimeZone module distribution in the tools/ directory

#
# Generated from /tmp/G45iu_6zbF/africa.  Olson data version 2013h
#
# Do not edit this file directly.
#
package DateTime::TimeZone::Indian::Antananarivo;
{
  $DateTime::TimeZone::Indian::Antananarivo::VERSION = '1.63';
}
BEGIN {
  $DateTime::TimeZone::Indian::Antananarivo::AUTHORITY = 'cpan:DROLSKY';
}

use strict;

use Class::Singleton 1.03;
use DateTime::TimeZone;
use DateTime::TimeZone::OlsonDB;

@DateTime::TimeZone::Indian::Antananarivo::ISA = ( 'Class::Singleton', 'DateTime::TimeZone' );

my $spans =
[
    [
DateTime::TimeZone::NEG_INFINITY, #    utc_start
60289390196, #      utc_end 1911-06-30 20:49:56 (Fri)
DateTime::TimeZone::NEG_INFINITY, #  local_start
60289401600, #    local_end 1911-07-01 00:00:00 (Sat)
11404,
0,
'LMT',
    ],
    [
60289390196, #    utc_start 1911-06-30 20:49:56 (Fri)
61635758400, #      utc_end 1954-02-27 20:00:00 (Sat)
60289400996, #  local_start 1911-06-30 23:49:56 (Fri)
61635769200, #    local_end 1954-02-27 23:00:00 (Sat)
10800,
0,
'EAT',
    ],
    [
61635758400, #    utc_start 1954-02-27 20:00:00 (Sat)
61643620800, #      utc_end 1954-05-29 20:00:00 (Sat)
61635772800, #  local_start 1954-02-28 00:00:00 (Sun)
61643635200, #    local_end 1954-05-30 00:00:00 (Sun)
14400,
1,
'EAST',
    ],
    [
61643620800, #    utc_start 1954-05-29 20:00:00 (Sat)
DateTime::TimeZone::INFINITY, #      utc_end
61643631600, #  local_start 1954-05-29 23:00:00 (Sat)
DateTime::TimeZone::INFINITY, #    local_end
10800,
0,
'EAT',
    ],
];

sub olson_version { '2013h' }

sub has_dst_changes { 1 }

sub _max_year { 2023 }

sub _new_instance
{
    return shift->_init( @_, spans => $spans );
}



1;

