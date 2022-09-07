#!/bin/bash
app=../../../rise_drones/src/app/app_monitor.py
echo "app: $app"
/home/droneadmin/.venv/rise_drones/bin/python3 $app --crm=10.44.160.10:16300 --app_ip=10.44.160.10 --stdout --log=info
