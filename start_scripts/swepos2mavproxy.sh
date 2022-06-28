#!/bin/bash
source /home/pi/.hx_config
/home/pi/.venv/rise_drones/bin/python3 /home/pi/rise_drones/src/app/ntripclient-py/ntrip_client.py --user $NTRIP_USER --password $NTRIP_PWD --server $NTRIP_SERVER --mountpoint $NTRIP_MOUNTPOINT --description "$NTRIP_MNTP_DESCR" --port $NTRIP_PORT --verbose
echo "STREAMING RTCM DATA FROM SWEPOS"
exit
