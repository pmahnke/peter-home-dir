#!/usr/bin/perl

`/etc/rc.d/init.d/qmail stop`;

$ps = `ps ax | grep qmail`;
$ps .= `ps ax | grep vmail`;
$ps .= `ps ax | grep vdeliver`;
$ps .= `ps ax | grep smtp`;


@ps = split (/\n/, $ps);

foreach $pid (@ps) {

    $pid = substr($pid,0,5);
    `kill -9 $pid`;
#    print "kill -9 $pid\n";
    $i++;
}


print "killed $i processes!\ndone!\n\n";
