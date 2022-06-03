import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--infile')
parser.add_argument('--outfile', default='Mission_lla.json')
parser.add_argument('--speed', default=1)
parser.add_argument('--heading', default="course")
parser.add_argument('--alt', default=8)
parser.add_argument('--alt_offset', default=0)
parser.add_argument('--tracking_precision', default=5)
args = parser.parse_args()
q_file = args.infile
lla_file = args.outfile
speed = float(args.speed)
alt = float(args.alt)
alt_offset = float(args.alt_offset)
tracking_precision = int(args.tracking_precision)

if args.heading != "course":
  heading = float(args.heading)
else:
  heading = args.heading

with open(q_file,'r', encoding='utf-8') as infile:
  q_mission = json.load(infile)

# Depending on how the mission is saved, the list index may have to be altered (0 or 1 so far..)
q_wp_list = q_mission["mission"]["items"][1]["TransectStyleComplexItem"]["Items"]



# Allocate dss_mission
mission = {}
# j dss wp numbering
j = 0
# i Q ground control wp numbering
#i = -1
i=0
for q_wp in q_wp_list:

  # Use frame == 0 if terrain follow, use ==3 if not. This sorts out camera trigger wps
  # 1, 4,5 ,8,9  12,13
  #if q_wp["frame"] == 3:
  if q_wp["command"] == 16:
    i +=1
    #if i%6 == 0 or (i+1)%6==0:
    if i%4 == 0 or i%4 == 1:
      id = "id"+str(j)
      mission.update({id:{}})
      mission[id].update({"tracking_precision": tracking_precision})
      mission[id].update({"lat": q_wp["params"][4]})
      mission[id].update({"lon": q_wp["params"][5]})
      #mission[id].update({"alt": q_wp["params"][6]})
      mission[id].update({"heading": heading})
      mission[id].update({"speed": speed})
      if (j+1)%4 == 0 or j%4 == 0:
        # Entry side of pattern
        mission[id].update({"alt":alt})
      else:
        #Opposite entry side of pattern
        mission[id].update({"alt":alt+alt_offset})
      j += 1

mission["id0"]["speed"] = 5
print(json.dumps(mission, indent=4))

# Write to file
with open(lla_file,'w',encoding='utf-8') as outfile:
  outfile.write(json.dumps(mission, indent=4))
