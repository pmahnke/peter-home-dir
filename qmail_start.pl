#!/usr/bin/perl

#SMTPD
# print "getting ids\n";
# $QMAILDUID=`id -u qmaild`;
# $NOFILESGID=`id -g qmaild`;

print "starting smtpd\n";
`/usr/bin/softlimit -m 2000000  /usr/bin/tcpserver -v -P -x /etc/smtp.cdb -u 504 -g 503 25 /var/qmail/bin/qmail-smtpd 2>&1`;

print "starting smtpd log\n";
`usr/bin/setuidgid qmaill /usr/bin/multilog t s2500000 /var/log/qmail/smtpd`;

#SEND
# Using qmail-local to deliver messages to ~/Mailbox by default.
print "starting qmail\n";
`/var/qmail/bin/qmail-start ./Maildir /var/qmail/bin/splogger qmail`;

print "starting qmail log\n";
#`/usr/bin/setuidgid qmaill /usr/bin/multilog t s2500000 /var/log/qmail`; 



# Start POP3
print "starting pop\n";
`/usr/bin/tcpserver -v -R 0 110 /var/qmail/bin/qmail-popup baby.internal.network /usr/bin/checkvpw /usr/sbin/relay-ctrl-allow  /var/qmail/bin/qmail-pop3d Maildir 2>&1 | /var/qmail/bin/splogger pop3d`;

print " starting pop log\n";
`multilog t /var/log/qmail-pop3`;





