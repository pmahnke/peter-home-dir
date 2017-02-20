#!/usr/bin/perl

$i = 0; 

while ($i < 22)  {

    $ipAddr   = 10 * ($i+1);

    print "/sbin/ifconfig eth0:$i 192.168.1.$ipAddr netmask 255.255.255.0\n";

    `/sbin/ifconfig eth0:$i 192.168.1.$ipAddr netmask 255.255.255.0`;

    print "/sbin/route add -host 192.168.1.$ipAddr dev eth0:$i\n";

    `/sbin/route add -host 192.168.1.$ipAddr dev eth0:$i`;
#    $line .= "ipmasqadm portfw -a -P tcp -L 209.219.93.$i 80 -R 192.168.1.$j 80\n";

    $i++;

}

#open (FILE, ">/root/forward.txt");
#print FILE $line;
#close (FILE);

print "done.\n\n\n";
exit;






