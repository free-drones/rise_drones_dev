#!/bin/bash
source /home/pi/.hx_config
/home/pi/.venv/rise_drones/bin/python3 /home/pi/companion_computer/ntripclient-py/ntrip_client.py --user $NTRIP_USER --password $NTRIP_PWD --server $NTRIP_SERVER --mountpoint $NTRIP_MOUNTPOINT --description "$NTRIP_MNTP_DESCR" --verbose
echo "STREAMING RTCM DATA FROM SWEPOS"
exit
