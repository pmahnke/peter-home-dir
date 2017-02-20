#!/usr/bin/perl

$file = "/etc/sysconfig/network-scripts/ifcfg-eth0:$ARGV[0]";

if (!@ARGV) {
    print "This will build a if-cfg:0:XX file for you for a new virtual domain.\n\nYou must pass it 2 arguments, the name of the ifcfg-eth0:XX file to create, and the final part of the IP (i.e. 120)\n\n";

    exit;

} elsif (-e $file) {
    print "$file already exists\n";
    exit;
}


open (FILE, ">$file") || die "Can not open $file for writing\n";
print FILE <<EndofListing;
DEVICE=eth0:$ARGV[0]
USERCTL=no
ONBOOT=yes
BOOTPROTO=none
BROADCAST=192.168.1.255
NETWORK=192.168.1.0
NETMASK=255.255.255.0
IPADDR=192.168.1.$ARGV[1]

EndofListing
close (FILE);

print "\nCreated \n\y $file\n\t\t for 192.168.1.$ARGV[1]!\n\n";


`/sbin/route add -host 192.168.1.$ARGV[1] dev eth0:$ARGV[0]`;



print "\nCreated route for 192.168.1.$ARGV[1]!\n\n";

exit;
