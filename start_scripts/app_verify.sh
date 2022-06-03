#!/bin/bash
# Load the local variables for HX_IP
source /home/pi/.hx_config
cd /home/pi/companion_computer/
/home/pi/.venv/rise_drones/bin/python3 app_verify.py --crm 10.44.160.10:16300 --app_ip $HX_IP --stdout
