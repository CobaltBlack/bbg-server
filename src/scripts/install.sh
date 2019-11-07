#!/bin/sh

echo "Installing Essence Personal Server..."

if [ -f /etc/systemd/system/essence.service ]; then
        systemctl stop essence.service
fi

cp ../gunicornStart.sh /root/essence
cp essence.service /etc/systemd/system

systemctl enable essence.service
