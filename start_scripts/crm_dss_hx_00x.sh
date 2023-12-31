#!/bin/bash
# Load the local variables for HX_IP and HX_NAME
source /home/pi/.hx_config
cd /home/pi/rise_drones_dev/
./start_scripts/performance_logger.sh &
cd /home/pi/rise_drones/src/app
/home/pi/.venv/rise_drones/bin/python3 crm_dss.py --drone=127.0.0.1:14555 --crm=10.44.160.10:16300  --dss_ip=$HX_IP  --descr=$HX_NAME --capabilities $HX_CAPABILITIES --stdout --log=info --without-midstick-check
