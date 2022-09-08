#!/bin/bash
#starting MavProxy for ttyACM0, one output for local host (DSS), and one for any ip (GCS)

/home/pi/.venv/rise_drones/bin/mavproxy.py --master=/dev/ttyACM1 --baud 921600 --load-module DGPS --out=tcpin:127.0.0.1:14555 --out=tcpin:0.0.0.0:14550
