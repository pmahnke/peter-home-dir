#!/bin/sh
# dovecot-imapd/run
# daemontools run script for dovecot-imapd service
# wcm, 2004.01.22 - 2004.01.22
# ===
exec 2>&1
echo "*** Starting dovecot-imapd service..."
exec envuidgid dovecot \
    /usr/sbin/dovecot \
    -F \
    -c /etc/dovecot.conf
