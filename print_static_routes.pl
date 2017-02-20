#!/usr/bin/perl

$i = 0; 


open (FILE, ">/home/peter/static-routes.txt");
while ($i < 20)  {

    $ipAddr   = 10 * ($i+1);


    print FILE "eth0:$i host 192.168.1.$ipAddr\n";

    $i++;

}



close (FILE);

print "done.\n\n\n";
exit;





