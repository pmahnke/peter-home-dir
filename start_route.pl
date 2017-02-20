#!/usr/bin/perl

$i = 0; 
$j = 10; 

while ($i < 28)  {

    $ipAddr   = $i + 99;

    print "/sbin/ifconfig eth0:$i 209.219.93.$ipAddr netmask 255.255.255.224 broadcast 209.219.93.127
n";

    `/sbin/ifconfig eth0:$i 209.219.93.$ipAddr netmask 255.255.255.224 broadcast 209.219.93.127`;

print "/sbin/route add -host 209.219.93.$ipAddr dev eth0:$i\n";

    `/sbin/route add -host 209.219.93.$ipAddr dev eth0:$i`;
    $line .= "ipmasqadm portfw -a -P tcp -L 209.219.93.$i 80 -R 192.168.1.$j 80\n";

    $i++;
    $j = 10 * ($i+1);
}

open (FILE, ">/root/forward.txt");
print FILE $line;
close (FILE);

print "done.\n\n\n";
exit;





