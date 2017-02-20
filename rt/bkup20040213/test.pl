#!/usr/local/bin/perl



    use DateTime::Format::HTTP;
    my $dt = 'DateTime::Format::HTTP';
    $datestring = $dt->parse_datetime($ARGV[0], 'GMT');
print "$datestring\n";
    $dateStr = $dt->format_datetime($datestring);
print "$dateStr\n";

