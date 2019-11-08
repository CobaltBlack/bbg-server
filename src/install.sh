#!/bin/sh

echo "Installing Essence Personal Server..."

echo "Install pip requirements..."
pip3 install -r requirements.txt

echo "Set permissions..."
chmod +x gunicornStart.sh

echo "Configure Essence service..."
if [ -f /etc/systemd/system/essence.service ]; then
        systemctl stop essence.service
fi
cp scripts/essence.service /etc/systemd/system/
systemctl enable essence.service
