#!/bin/bash
cd /home/pi/companion_computer/
./start_scripts/performance_logger.sh &
/home/pi/.venv/rise_drones/bin/python3 crm_dss.py --drone=127.0.0.1:14555 --crm=10.44.160.10:16300  --dss_ip=10.44.163.54  --descr=HX_004 --stdout
