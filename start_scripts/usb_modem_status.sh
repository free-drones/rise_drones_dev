#!/bin/bash 
# root previligies are required, set no passwd for this script in /etc/sudoers file, add this line
# ALL ALL = (root) NOPASSWD: /home/pi/rise_drones_dev/start_scripts/usb_modem_status.sh
cmd="qmicli -d /dev/cdc-wdm1 --nas-get-rf-band-info"
echo $cmd
$cmd
cmd="qmicli -d /dev/cdc-wdm1 --nas-get-system-selection-preference"
echo $cmd
$cmd
cmd="qmicli -d /dev/cdc-wdm1 --nas-get-serving-system"
echo $cmd
$cmd
cmd="qmicli -d /dev/cdc-wdm1 --nas-get-system-info"
echo $cmd
$cmd
cmd="qmicli -d /dev/cdc-wdm1 --nas-get-technology-preference"
echo $cmd
$cmd
cmd="qmicli -d /dev/cdc-wdm1 --nas-get-signal-strength"
echo $cmd
$cmd
cmd="qmicli -d /dev/cdc-wdm1 --nas-get-signal-info"
echo $cmd
$cmd
printf "\n\n"
route -n
