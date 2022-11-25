#!/bin/bash
app=../../../rise_drones/src/app/app_monitor.py
printf "app: $app"
printf "\n\nThis is a new screen session named app_monitor\n"
printf "Detach screen:        ctrl + a, d\n"
printf "Resume screen:        screen -r app_monitor\n"
printf "Quit app_monitor:     ctrl + c\n"
printf "Quit screen session   ctrl + d\n\n"
/home/droneadmin/.venv/rise_drones/bin/python3 $app --crm=10.44.160.10:16300 --app_ip=10.44.163.34 --stdout --log=info --mqtt_agent
