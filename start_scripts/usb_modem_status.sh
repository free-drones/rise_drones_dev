#!/bin/bash
# root previligies are required, set no passwd for this script in /etc/sudoers file, add this line
# ALL ALL = (root) NOPASSWD: /home/pi/rise_drones_dev/start_scripts/usb_modem_status.sh
sudo qmicli -d /dev/cdc-wdm0 --dms-get-model | grep RM502Q-AE >> /dev/null && device=/dev/cdc-wdm0 || device=/dev/cdc-wdm1
sudo qmicli -d /dev/cdc-wdm0 --dms-get-model | grep RM502Q-AE >> /dev/null && iface=wwan0 || iface=wwan1


cmd="qmicli -d ${device} --nas-get-rf-band-info"
echo $cmd
$cmd
cmd="qmicli -d ${device} --nas-get-system-selection-preference"
echo $cmd
$cmd
cmd="qmicli -d ${device} --nas-get-serving-system"
echo $cmd
$cmd
cmd="qmicli -d ${device} --nas-get-system-info"
echo $cmd
$cmd
cmd="qmicli -d ${device} --nas-get-technology-preference"
echo $cmd
$cmd
cmd="qmicli -d ${device} --nas-get-signal-strength"
echo $cmd
$cmd
cmd="qmicli -d ${device} --nas-get-signal-info"
echo $cmd
$cmd
printf "\n\n"
route -n
