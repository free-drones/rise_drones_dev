#!/bin/bash
# Set terminal type for screen
export TERM=vt100

/home/pi/rise_drones_dev/start_scripts/mobile-status.sh > /dev/null &
sleep 5
screen -r atcmd
