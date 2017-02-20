#!/bin/sh
# Start POP3
exec env - PATH="/var/qmail/bin" \
    /usr/bin/tcpserver -v -R 0 pop-3 \
    /var/qmail/bin/qmail-popup baby.internal.network \
    /usr/bin/checkvpw /usr/sbin/relay-ctrl-allow \
    /var/qmail/bin/qmail-pop3d Maildir 2>&1 | \
    /var/qmail/bin/splogger pop3d &


exec multilog t /var/log/qmail-pop3 &

#SMTPD
QMAILDUID=`id -u qmaild`
NOFILESGID=`id -g qmaild`
exec /usr/bin/softlimit -m 2000000 \
    /usr/bin/tcpserver -v -P -x /etc/smtp.cdb -u $QMAILDUID -g $NOFILESGID 0 smtp /var/qmail/bin/qmail-smtpd 2>&1 &

exec /usr/bin/setuidgid qmaill /usr/bin/multilog t s2500000 /var/log/qmail/smtpd &

#SEND
# Using qmail-local to deliver messages to ~/Mailbox by default.
exec env - PATH="/var/qmail/bin" \
    /var/qmail/bin/qmail-start ./Maildir \
    /var/qmail/bin/splogger qmail &

exec /usr/bin/setuidgid qmaill /usr/bin/multilog t s2500000 /var/log/qmail &
