#!/bin/bash
# Set terminal type for screen
export TERM=vt100

/home/pi/companion_computer/start_scripts/mobile-status.sh > /dev/null &
sleep 5
screen -r atcmd
