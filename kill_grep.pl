#!/usr/bin/perl


if (!@ARGV) {

    print "\nUSAGE: kill_grep.pl <regex1> <regex2> ....\n
PURPOSE: kills all process that follow the regex patterns\n\n";
    exit;
}

foreach $regex (@ARGV) {
    $ps .= `ps ax | grep $regex`;
}


@ps = split (/\n/, $ps);

foreach $pid (@ps) {

    print "\nkill: $pid (y/n/q)? ";
    $yesno = <STDIN>;
    
    if ($yesno =~ /q/i) {
	print "\nQuiting!\n";
	exit;
    } elsif ($yesno !~ /y/i) {
	print "Skipping...\n";
	next;
    }
    
    $pid = substr($pid,0,5);
    `kill -9 $pid`;
    print "\nKilling: $pid\n";
    $i++;
}


print "Killed $i processes!\ndone!\n\n";
