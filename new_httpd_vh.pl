#!/usr/bin/perl

if (!@ARGV) {
    print "
CREATE A NEW VIRTUAL SERVER
This will add all the config options to the apache config files for another virtual server.\n
You must pass it 2 arguments, the name of the web site (i.e. mahnke.net if the site is going to be mahnke.net) and the final part of the IP (i.e. 120 for 192.168.1.120)\n\n";

    exit;
}

($name, $ext) = split (/\./, $ARGV[0]);
$name = "compclassifieds" if ($name eq "computerclassifieds");
print "
name $name
 ext $ext
  ip 192.168.1.$ARGV[1]\n";


open (FILE, ">>/usr/local/apache/conf/httpd.conf") || die;
print FILE <<endoflist;

################################################################
# start of of $ARGV[0] site listing
#
# $ARGV[0] site on port 80 for http
#
Listen 192.168.1.$ARGV[1]:80
#
<VirtualHost 192.168.1.$ARGV[1]:80>
  ServerName $ARGV[0]
  ServerAdmin webmaster\@$ARGV[0]
  DocumentRoot /home/$name/html
  ScriptAlias /cgi-bin/ /home/$name/cgi-bin/
  ScriptAlias /servlets/ /home/$name/servlets/
  ApJServMount /servlets /$name
  AddType text/html .shtml
  AddHandler server-parsed .shtml
  AddHandler cgi-script .cgi
  AddHandler cgi-script .pl
  AddHandler cgi-script .py
  ErrorLog /home/$name/logs/error_log
  TransferLog /home/$name/logs/access_log
  CustomLog /home/$name/logs/referer_log referer
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
# $ARGV[0] site on port 433 for https
#
Listen 192.168.1.$ARGV[1]:443
#
<VirtualHost 192.168.1.$ARGV[1]:443>
  SSLEnable
  ServerName $ARGV[0]
  ServerAdmin webmaster\@$ARGV[0]
  DocumentRoot /home/$name/html
  ScriptAlias /cgi-bin/ /home/$name/cgi-bin/
  ScriptAlias /servlets/ /home/$name/servlets/
  ApJServMount /servlets /$name
  AddType text/html .shtml
  AddHandler server-parsed .shtml
  AddHandler cgi-script .cgi
  AddHandler cgi-script .pl
  AddHandler cgi-script .py
  ErrorLog /home/$name/logs/error_log
  TransferLog /home/$name/logs/access_log
  CustomLog /home/$name/logs/referer_log referer
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
# end of $ARGV[0] site listing
################################################################


endoflist


    close (FILE);
print "Done with $ARGV[0] in httpd.conf\n\n";

sub dontrunthis { 
open (FILE, ">>/usr/local/apache/conf/access.conf") || die;
print  <<endoflist;

###############################
# $ARGV[0] site
###############################
# HTML Dir
<Directory /home/$ARGV[0]/html>
Options Indexes FollowSymLinks
AllowOverride None
allow from all
</Directory>

# CGI-BIN Dir
<Directory /home/$ARGV[0]/cgi-bin>
Options FollowSymLinks
AllowOverride None
order allow,deny
allow from all
</Directory>

# Includes Dir
<Directory /home/$ARGV[0]/includes>
Options Indexes FollowSymLinks
AllowOverride None
allow from all
</Directory>


endoflist


close (FILE);
print "Done with $ARGV[0] in access.conf\n\n";
}

exit;















