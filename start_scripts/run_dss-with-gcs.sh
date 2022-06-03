#!/bin/bash
cd /home/pi/companion_computer/
./start_scripts/performance_logger.sh &
/home/pi/.venv/rise_drones/bin/python3 run_dss.py --connect 127.0.0.1:14555 --with-gcs
