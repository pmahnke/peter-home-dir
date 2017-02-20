#!/usr/bin/perl

# Dynamically create firewall rules
#
# eth1 is on the internal.network
#
# eth0 is on the external network
#
# reads virtual server ips and phyical ips from files
#
#

# VARIABLES
$rootDir = "\/root\/";
$vList = $rootDir."virtual.list";
$pList = $rootDir."physical.list";
$NAMESERVER_1 = "24.2.128.33"; # @home DNS 1
$NAMESERVER_2 = "24.2.128.34"; # @home DNS 2

# ACTION
&makeGeneralRules;
&readList($vList);
&makeVrules;
&readList($pList);
&makePrules;
#`ipmasqadm portfw -l`;
&makeAntiSpamRules;


print "\nDone.\n\n";
exit;

######################################################################
sub readList {

    # empty the list from the last load
    splice (@dnsName,0, $#dnsName);
    splice (@extIP, 0, $#extIP);
    splice (@intIP, 0, $#intIP);
    
    open (LIST, "$_[0]") || die "Can't read $_[0]\n";
    while (<LIST>) {
	
	local ($dnsName, $extIP, $intIP) = "";
	chomp();
	next if ($_ eq "");

	($dnsName, $extIP, $intIP) = split(/\|/);
	push @dnsName, $dnsName;
	push @extIP, $extIP;
	push @intIP, $intIP;
	print "$dnsName, $extIP, $intIP\n";

    }
    close (LIST);
    return();

} # end sub readList


######################################################################
sub makeGeneralRules {

    print "FLUSH ALL EXISTING RULES\n";
    `ipchains -F input`;
    `ipchains -F output`;
    `ipchains -F forward`;
    `ipchains -F eth0-out`;
    `ipchains -X eth0-out`;
    `ipmasqadm portfw -f`;

    print "default Policy DENY\n";
    `ipchains -P input ACCEPT`;
    `ipchains -P output ACCEPT`;
    `ipchains -P forward ACCEPT`;

    print "local packets are freed\n";
    `ipchains -A input  -i lo   -j ACCEPT`;
    `ipchains -A output -i lo   -j ACCEPT`;
    `ipchains -A input  -i eth1 -j ACCEPT`;
    `ipchains -A output -i eth1 -j ACCEPT`;
#    `ipchains -A input  -i eth0 -j DENY`;
    `ipchains -A input  -i eth0 -j ACCEPT`;
    `ipchains -A output -i eth0 -j ACCEPT`;


    print "masq rules \n";
    `ipchains -A forward -j MASQ -s 192.168.1.0/24`; 

    print "Create eth0-out chain\n";
    `ipchains -N eth0-out`;
    print "putting all eth0 output on the eth0-out chain\n";
    `ipchains -A output -i eth0 -j eth0-out`;

    print "setting TOS Type of Service\n";
    `ipchains -A eth0-out -p TCP -d 0.0.0.0 www      -t 0x01 0x10`;
    `ipchains -A eth0-out -p TCP -d 0.0.0.0 telnet   -t 0x01 0x10`;
    `ipchains -A eth0-out -p TCP -d 0.0.0.0 ftp      -t 0x01 0x10`;
    `ipchains -A eth0-out -p TCP -d 0.0.0.0 nntp     -t 0x01 0x02`;
    `ipchains -A eth0-out -p TCP -d 0.0.0.0 pop-3    -t 0x01 0x02`;
    `ipchains -A eth0-out -p TCP -d 0.0.0.0 ftp-data -t 0x01 0x08`;
    `ipchains -A eth0-out -p TCP -d 0.0.0.0 smtp     -t 0x01 0x04`;

    `ipchains -A eth0-out -p udp -s $NAMESERVER_1 53 -d 192.168.1.1 53 -j ACCEPT`;
    `ipchains -A eth0-out -p udp -s $NAMESERVER_2 53 -d 192.168.1.1 53 -j ACCEPT`;

    `ipchains -A input  -i eth1 -p udp -s $NAMESERVER_1 53 -d 192.168.1.1 53  -j ACCEPT`;
    `ipchains -A input  -i eth1 -p udp -s $NAMESERVER_2 53 -d 192.168.1.1 53  -j ACCEPT`;


}


######################################################################
sub makeVrules {

    local $i = 0;

    foreach $dnsName (@dnsName) {

	local $last = substr ($intIP[$i],  10);
	$last = $last + 1;
	local $devIP = "192.168.1."."$last";
	
	print "\nSTART RULES FOR $dnsName \t $extIP[$i] \=\> $intIP[$i]\n";
	print "opening WWW 80...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 80 -R $intIP[$i] 80`;
	print "443 for ssl...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 443 -R $intIP[$i] 443`;
	print "25 for smtp...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 25 -R $intIP[$i] 25`;
	`ipmasqadm portfw -a -P udp -L $extIP[$i] 25 -R $intIP[$i] 25`;
	print "TCP 110 for pop...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 110 -R $intIP[$i] 110`;
	print "UDP 110 for pop\n";
	`ipmasqadm portfw -a -P udp -L $extIP[$i] 110 -R $intIP[$i] 110`;
	print "opening up development servers\n";
	print " 8080 \=\> 80 for http..."; 
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 8080 -R $devIP 80`;
	print "8443 \=\> 443 for ssl http\n";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i]  8443 -R $devIP 443`;
	
	$i++;
    }
    print "done with virtual domains\n";
    return();
} # end sub makeVrules 

######################################################################
sub makePrules {

    local $i = 0;
    
    foreach $dnsName (@dnsName) {

	print "\nSTART RULES FOR PHYSICAL SYSTEM $dnsName\n";
	print "80 for http...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 80 -R $intIP[$i] 80`;
#	`ipmasqadm portfw -a -P upd -L $extIP[$i] 80 -R $intIP[$i] 80`;
	print "443 for ssl...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 443 -R $intIP[$i] 443`;
#	`ipmasqadm portfw -a -P upd -L $extIP[$i] 443 -R $intIP[$i] 443`;
	print "20 and 21 for ftp and ftp_data...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 20 -R $intIP[$i] 20`;
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 21 -R $intIP[$i] 21`;
	`ipmasqadm portfw -a -P udp -L $extIP[$i] 20 -R $intIP[$i] 20`;
	`ipmasqadm portfw -a -P udp -L $extIP[$i] 21 -R $intIP[$i] 21`;
	print "23 for telnet...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 23 -R $intIP[$i] 23`;
	print "TCP and UDP 110 for pop...";
	`ipmasqadm portfw -a -P tcp -L $extIP[$i] 110 -R $intIP[$i] 110`;
	`ipmasqadm portfw -a -P udp -L $extIP[$i] 110 -R $intIP[$i] 110`;
	if ($dnsName eq "baby" || $dnsName eq "wife") {
	    print "rsh and rexec 6000 and 60001...";
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 512 -R $intIP[$i] 512`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 514 -R $intIP[$i] 514`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 6000 -R $intIP[$i] 6000`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 6001 -R $intIP[$i] 6001`;
	}
	if ($dnsName eq "wife") {
	    print "ports on wife for John Cook 8001-8003 and 8081-8083...";
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 8001 -R $intIP[$i] 8001`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 8002 -R $intIP[$i] 8002`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 8003 -R $intIP[$i] 8003`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 8081 -R $intIP[$i] 8081`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 8082 -R $intIP[$i] 8082`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 8083 -R $intIP[$i] 8083`;
	}
	if ($dnsName eq "pc") {
	    print "pc anywhere on 5631 5632 ...";
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 5631 -R $intIP[$i] 5631`;
	    `ipmasqadm portfw -a -P tcp -L $extIP[$i] 5632 -R $intIP[$i] 5632`;
	    `ipmasqadm portfw -a -P udp -L $extIP[$i] 5631 -R $intIP[$i] 5631`;
	    `ipmasqadm portfw -a -P udp -L $extIP[$i] 5632 -R $intIP[$i] 5632`;
	}

	print "\n";

	$i++;
    }
    print "done with physical systems\n";
    return();
} # end sub makePrules



######################################################################
sub makeAntiSpamRules {
    print "\nAnti Spam stuff\n";
#    print "REJECTING from BOOK.COM\n";
#    `ipchains -A input -s 208.237.178.0/24 -j DENY`; 
#    to test type    `ipchains -C input -s 208.237.178.0/24 smtp -d 209.219.93.109 smtp -p TCP -i eth0:20`;
}









