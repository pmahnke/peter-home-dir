#!/usr/bin/perl

if (!@ARGV) {
    print "This will build a zone file for you for a new virtual domain.\n\nYou must pass it 2 arguments, the name of the web site (i.e. mahnke.net if the site is going to be mahnke.net) and the final part of the IP (i.e. 120)\n\n";

    exit;
}

$zone = "$ARGV[0]"."\."; # create a domain name with an extra . at the end 
$webip = $ARGV[1]+1;
#################################################################
#
# write a Zone File
#
#################################################################


open (FILE, ">/var/named/pz/$ARGV[0]") || die "Can not open zone file for writin\n";
print FILE <<EndofListing;
;
; ZONE FILE for $ARGV[0]
;
;
@               IN      SOA     baby.internal.network. peter.internal.network. (
                                200101171       ; Serial, today's date 
                                8H      	; Refresh, seconds
                                2H     		; Retry, seconds
                                1W      	; Expire, seconds
                                1D)     	; Minimum TTL, setconds
                        NS      baby		; name server
			MX	10 baby  	; Primary Mail Exchanger
;
;
; HOST RECORDS
;
$zone		A	192.168.1.$ARGV[1]
www		A	192.168.1.$webip
;
; CNAMES
;
pop			CNAME	$zone
mail			CNAME	$zone
ftp			CNAME	$zone
dev			CNAME	$zone

EndofListing

close (FILE);

print "\nCreated zone file for $ARGV[0] at $ARGV[1] and $webip!\n\n";

#################################################################
#
# add Zone information to named.conf
#
#################################################################
open (FILE, ">>/etc/named.conf") || die "Can not open named.conf to append zone information\n";

print FILE <<EndofListing;

zone "$ARGV[0]" {
	notify no;
	type master;
	file "pz/$ARGV[0]";
};

EndofListing

close (FILE);

print "Added zone information to named.conf!\n\n";


#################################################################
#
# add reverse lookup to 192.198.1 Zone file
#
#################################################################

open (FILE, ">>/var/named/pz/192.168.1") || die "Can not open 192.168.1 to append reverse name lookup zone information\n";

print FILE <<EndofListing;
$ARGV[1]	IN	PTR	$zone
$webip		IN	PTR	www.$zone
EndofListing
close (FILE);

print "Appended reverse name lookup zone information to 192.168.1\n";

print "Done!\n\n";

exit

















