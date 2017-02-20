# This file is auto-generated by the Perl DateTime Suite time zone
# code generator (0.07) This code generator comes with the
# DateTime::TimeZone module distribution in the tools/ directory

#
# Generated from /tmp/G45iu_6zbF/australasia.  Olson data version 2013h
#
# Do not edit this file directly.
#
package DateTime::TimeZone::Pacific::Midway;
{
  $DateTime::TimeZone::Pacific::Midway::VERSION = '1.63';
}
BEGIN {
  $DateTime::TimeZone::Pacific::Midway::AUTHORITY = 'cpan:DROLSKY';
}

use strict;

use Class::Singleton 1.03;
use DateTime::TimeZone;
use DateTime::TimeZone::OlsonDB;

@DateTime::TimeZone::Pacific::Midway::ISA = ( 'Class::Singleton', 'DateTime::TimeZone' );

my $spans =
[
    [
DateTime::TimeZone::NEG_INFINITY, #    utc_start
59958272968, #      utc_end 1901-01-01 11:49:28 (Tue)
DateTime::TimeZone::NEG_INFINITY, #  local_start
59958230400, #    local_end 1901-01-01 00:00:00 (Tue)
-42568,
0,
'LMT',
    ],
    [
59958272968, #    utc_start 1901-01-01 11:49:28 (Tue)
61707178800, #      utc_end 1956-06-03 11:00:00 (Sun)
59958233368, #  local_start 1901-01-01 00:49:28 (Tue)
61707139200, #    local_end 1956-06-03 00:00:00 (Sun)
-39600,
0,
'NST',
    ],
    [
61707178800, #    utc_start 1956-06-03 11:00:00 (Sun)
61715037600, #      utc_end 1956-09-02 10:00:00 (Sun)
61707142800, #  local_start 1956-06-03 01:00:00 (Sun)
61715001600, #    local_end 1956-09-02 00:00:00 (Sun)
-36000,
1,
'NDT',
    ],
    [
61715037600, #    utc_start 1956-09-02 10:00:00 (Sun)
62048804400, #      utc_end 1967-04-01 11:00:00 (Sat)
61714998000, #  local_start 1956-09-01 23:00:00 (Sat)
62048764800, #    local_end 1967-04-01 00:00:00 (Sat)
-39600,
0,
'NST',
    ],
    [
62048804400, #    utc_start 1967-04-01 11:00:00 (Sat)
62574721200, #      utc_end 1983-11-30 11:00:00 (Wed)
62048764800, #  local_start 1967-04-01 00:00:00 (Sat)
62574681600, #    local_end 1983-11-30 00:00:00 (Wed)
-39600,
0,
'BST',
    ],
    [
62574721200, #    utc_start 1983-11-30 11:00:00 (Wed)
DateTime::TimeZone::INFINITY, #      utc_end
62574681600, #  local_start 1983-11-30 00:00:00 (Wed)
DateTime::TimeZone::INFINITY, #    local_end
-39600,
0,
'SST',
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
