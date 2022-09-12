import time
import gphoto2 as gp
from subprocess import Popen, PIPE
from datetime import datetime

camera = gp.Camera()
camera.init()
ffmpeg = Popen(['ffmpeg', '-i', '-', '-vcodec', 'rawvideo', '-pix_fmt', 'yuv420p', '-f', 'v4l2', '/dev/video0'],stdin=PIPE)
fps = 25
while True:
   start_t = datetime.timestamp(datetime.now())
   capture = camera.capture_preview()
   filedata = capture.get_data_and_size()
   data = memoryview(filedata)
   ffmpeg.stdin.write(data.tobytes())
   end_t = datetime.timestamp(datetime.now())
   time.sleep(max(1/fps - (end_t-start_t), 0))

