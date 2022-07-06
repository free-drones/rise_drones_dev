#!/bin/bash
#Run application app geopoint
# Load the local variables for HX_IP
source /home/pi/.hx_config
cd /home/pi/rise_drones/src/app
/home/pi/.venv/rise_drones/bin/python3 ./app_geopoint.py --crm=10.44.160.10:16300 --app_ip=$HX_IP --stdout --log=info
