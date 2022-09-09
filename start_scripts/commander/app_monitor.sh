#!/bin/bash

# Use screen to be able to run app_monitor in background
screen -S app_monitor bash -c "bash app_monitor_screen.sh"
printf "Re-attach to to screen: screen -r app_monitor\n"
