import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--infile')
parser.add_argument('--outfile', default='Mission_lla.json')
parser.add_argument('--speed', type=float, default=0, help='Set to 0 to preserve Q-speed')
args = parser.parse_args()
q_file = args.infile
lla_file = args.outfile
speed = args.speed
print(speed)

with open(q_file,'r', encoding='utf-8') as infile:
  q_mission = json.load(infile)

#print(json.dumps(q_mission["mission"]["items"][0]["TransectStyleComplexItem"]["Items"], indent=4))
q_wp_list = q_mission["mission"]["items"]
q_hover_speed = q_mission["mission"]["hoverSpeed"]
print("Hover speed could be used in this script.. it is set to:", q_hover_speed)

# Allocate dss_mission
mission = {}
# j dss wp numbering
j = 0
# i Q ground control wp numbering
#i = -1
i=0
id = "id0"
for q_wp in q_wp_list:

  # Command == 178 -> condition_speed (belongs to previous wp)
  if q_wp["command"] == 178:
    if speed > 0:
      print("speed is bigger")
      mission[id].update({"speed": speed})
    else:
      mission[id].update({"speed": q_wp["params"][1]})

  # Command == 16 -> goto lat long
  if q_wp["command"] == 16:
    i +=1
    prev_id = id	# Speed is set after the wp in qGCS
    id = "id"+str(j)
    mission.update({id:{}})
    mission[id].update({"lat": q_wp["params"][4]})
    mission[id].update({"lon": q_wp["params"][5]})
    mission[id].update({"alt": q_wp["params"][6]})
    mission[id].update({"heading": "course"})
    mission[id].update({"alt_type": "relative"})
    if speed > 0:
      print("speed is bigger")
      mission[id].update({"speed": speed})
    else:
      mission[id].update({"speed": q_wp["params"][1]})



    j += 1

mission.update({"source_file": args.infile})

print(json.dumps(mission, indent=4))

# Write to file
with open(lla_file,'w',encoding='utf-8') as outfile:
  outfile.write(json.dumps(mission, indent=4))
