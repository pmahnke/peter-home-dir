#!/bin/sh

echo Stoping Servers
/etc/rc.d/init.d/qmail.init       stop
/etc/rc.d/init.d/qmail-smtpd.init stop
/etc/rc.d/init.d/qmail-pop3d.init stop
/etc/rc.d/init.d/qmail-qmqpd.init stop
/etc/rc.d/init.d/qmail-qmtpd.init stop
/etc/rc.d/init.d/vmailmgrd        stop

wait 10

echo Restarting Servers
/etc/rc.d/init.d/qmail.init       start
/etc/rc.d/init.d/qmail-smtpd.init start
/etc/rc.d/init.d/qmail-pop3d.init start
/etc/rc.d/init.d/qmail-qmqpd.init start
/etc/rc.d/init.d/qmail-qmtpd.init start
/etc/rc.d/init.d/vmailmgrd        start

