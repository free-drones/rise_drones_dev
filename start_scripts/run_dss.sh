#!/bin/bash
cd /home/pi/rise_drones_dev/
./start_scripts/performance_logger.sh &
cd /home/pi/rise_drones/src/app
/home/pi/.venv/rise_drones/bin/python3 run_dss.py --connect 127.0.0.1:14555 --with-autogain
