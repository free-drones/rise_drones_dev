#!/bin/bash
app=../../../rise_drones/src/app/app_mission.py
mission=../../mission/missions/road_ref_skara.json
echo "app: $app"
echo "mission: $mission"
python3 $app --crm=10.44.160.10:16300 --app_ip=10.44.160.10 --mission=$mission --stdout --log=info --capabilities C0
#/home/droneadmin/.venv/rise_drones/bin/python3 $app --crm=10.44.160.10:16300 --app_ip=10.44.160.10 --mission=$mission --stdout --log=info --capabilities C0
