#!/usr/bin/perl

# variables
$ip = 10; # first IP

open (LIST, "/home/peter/zone_list") || die ;
open (HOMENET, ">/home/peter/zone_files") || die "Can not open zone file for writin\n";
open (FILEIP, ">/home/peter/zone_files_ip") || die "Can not open zone file for writin\n";
open (HTTPD, ">/home/peter/apache/httpd.conf") || die;
#open (HTTPD, ">>/usr/local/apache/conf/httpd.conf") || die;

while (<LIST>) {
    
    chop();
    $name = $_;
    $ip++;
    $intIP = 5 * $i + 10;
    $devIP = $intIP + 1;
    
    print FILEIP "$name\|64.232.146.$ip\|192.169.1.$intIP\n";


################################################################
#
# write httpd.conf
#
################################################################


($acct, $ext) = split (/\./, $name);
$acct = "compclassifieds" if ($acct eq "computerclassifieds");
$acct = "digalli" if ($acct eq "digitalalliances");
$acct = "mkwsoft" if ($acct eq "mwksoftware");

print "
name $acct
 ext $ext
  ip 192.168.1.$ARGV[1]\n";



print HTTPD <<endoflist;

################################################################
# start of of $name site listing
#
# $name site on port 80 for http
#
Listen 192.168.1.$intIP:80
#
<VirtualHost 192.168.1.$intIP:80>
  ServerName $name
  ServerAdmin webmaster\@$name]
  DocumentRoot /home/$acct/html
  ScriptAlias /cgi-bin/ /home/$acct/cgi-bin/
  ScriptAlias /servlets/ /home/$acct/servlets/
  ApJServMount /servlets /$acct
  AddType text/html .shtml
  AddHandler server-parsed .shtml
  AddHandler cgi-script .cgi
  AddHandler cgi-script .pl
  AddHandler cgi-script .py
  ErrorLog /home/$acct/logs/error_log
  TransferLog /home/$acct/logs/access_log
  CustomLog /home/$acct/logs/referer_log referer
 <Location />
  Options Indexes FollowSymLinks ExecCGI Includes
  AllowOverride None
  allow from all
 </Location>
 <Location /cgi-bin/>
  Options FollowSymLinks
  AllowOverride None
  order allow,deny
  allow from all
 </Location>
</VirtualHost>
#
# $name site on port 433 for https
#
Listen 192.168.1.$intIP:443
#
<VirtualHost 192.168.1.$intIP:443>
  SSLEnable
  ServerName $name
  ServerAdmin webmaster\@$name
  DocumentRoot /home/$acct/html
  ScriptAlias /cgi-bin/ /home/$acct/cgi-bin/
  ScriptAlias /servlets/ /home/$acct/servlets/
  ApJServMount /servlets /$name
  AddType text/html .shtml
  AddHandler server-parsed .shtml
  AddHandler cgi-script .cgi
  AddHandler cgi-script .pl
  AddHandler cgi-script .py
  ErrorLog /home/$acct/logs/error_log
  TransferLog /home/$acct/logs/access_log
  CustomLog /home/$acct/logs/referer_log referer
 <Location />
  Options Indexes FollowSymLinks ExecCGI Includes
  AllowOverride None
  allow from all
 </Location>
 <Location /cgi-bin/>
  Options FollowSymLinks
  AllowOverride None
  order allow,deny
  allow from all
 </Location>
</VirtualHost>
#
# end of $name site listing
################################################################


endoflist


print "Done with $name in httpd.conf\n\n";




#################################################################
#
# write a Zone File
#
#################################################################


#open (FILE, ">/home/peter/named/$name") || die "Can not open zone file for writin\n";
open (FILE, ">/var/named/pz/$name") || die "Can not open zone file for writin\n";
print FILE <<EndofListing;
;
; ZONE FILE for $name
;
;
@               IN      SOA     baby.internal.network. peter.internal.network. (
                                20000921        ; Serial, today's date 
                                8H      	; Refresh, seconds
                                2H     		; Retry, seconds
                                1W      	; Expire, seconds
                                1D)     	; Minimum TTL, setconds
                        NS      baby		; name server
			MX	10 baby  	; Primary Mail Exchanger
;
$name.		A	192.168.1.$intIP
www			A	192.168.1.$intIP
ftp			A	192.168.1.$intIP 
mail			A	192.168.1.$intIP 
pop			A	192.168.1.$intIP 
dev			A	192.168.1.$devIP

EndofListing

close (FILE);

print "\nCreated zone file for $name at $intIP!\n\n";

#################################################################
#
# add Zone information to named.conf
#
#################################################################
#open (FILE, ">>/home/peter/named/named.conf") || die "Can not open named.conf to append zone information\n";
open (FILE, ">>/etc/named.conf") || die "Can not open named.conf to append zone information\n";

print FILE <<EndofListing;

zone "$name" {
	notify no;
	type master;
	file "pz/$name";
};

EndofListing

close (FILE);

print "Added zone information to named.conf!\n\n";


#################################################################
#
# add reverse lookup to 192.198.1 Zone file
#
#################################################################

#open (FILE, ">>/home/peter/named/192.168.1") || die "Can not open 192.168.1 to append reverse name lookup zone information\n";
open (FILE, ">>/var/named/pz/192.168.1") || die "Can not open 192.168.1 to append reverse name lookup zone information\n";

print FILE <<EndofListing;
$intIP			PTR	$name
$devIP			PTR	dev.$name
EndofListing
close (FILE);

print "Appended reverse name lookup zone information to 192.168.1\n";



#################################################################
#
# write home.net zone files
#################################################################


print HOMENET <<EndofListing;
; 
; $name (Peter Mahnke) 
; 
@ IN SOA wns1.home.net. hostmaster.home.net. ( 
					       2000051400 ; serial 
					       10800 ; refresh (3 hours) 
					       3600 ; retry (1 hour) 
					       604800 ; expire (7 days) 
					       86400 ) ; minimum (1 day) 
A 64.232.146.$ip 
; 
; Nameservers 
NS NS1.HOME.NET. 
NS NS2.HOME.NET. 
; 
; MX Records 
; 
MX 10 mail.$name. 
MX 100 mx1.home.com. 
MX 100 mx2.home.com. 
; 
; Host Records 
; 
www IN A 64.232.146.$ip
mail IN A 64.232.146.$ip
ftp IN A 64.232.146.$ip
pop IN A 64.232.146.$ip
; 
; CNAMES 
---------------------------------------------------------------------------------------- 
EndofListing

$i++;

}
close (FILE);
close (HOMENET);
close (LIST);
close (HTTPD);



print "Done!\n\n";

exit















