#!/bin/bash
# Load the local variables for HX_IP
source /home/pi/.hx_config
cd /home/pi/rise_drones/src/app
/home/pi/.venv/rise_drones/bin/python3 app_ussp_lmd_granso.py --crm=10.44.160.10:16300 --app_ip=$HX_IP --mission=Mission_lla.json --stdout --log=info
