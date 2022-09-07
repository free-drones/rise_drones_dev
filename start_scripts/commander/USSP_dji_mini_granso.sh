#!/bin/bash
app=../../../rise_drones/src/app/app_lmd_granso.py
mission=../../mission/missions/USSP_Granso_LMD.json
echo "app: $app"
echo "mission: $mission"
cd /home/droneadmin/tyra/rise_drones/app
/home/droneadmin/.venv/rise_drones/bin/python3 $app --crm=10.44.160.10:16300 --app_ip=10.44.160.10 --mission=$mission --stdout --log=info
