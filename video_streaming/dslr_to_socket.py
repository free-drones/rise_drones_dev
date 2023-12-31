import time
import gphoto2 as gp
from subprocess import Popen, PIPE
import socket
from datetime import datetime

HOST = "192.168.2.3"
PORT = 13330
send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"trying to connect to {HOST}:{PORT}")
send_sock.connect((HOST, PORT))
print(f"Connected to {HOST}:{PORT}")

camera = gp.Camera()
camera.init()
fps = 25
while True:
   start_t = datetime.timestamp(datetime.now())
   capture = camera.capture_preview()
   filedata = capture.get_data_and_size()
   data = memoryview(filedata)
   send_sock.sendall(data.tobytes())
   end_t = datetime.timestamp(datetime.now())
   time.sleep(max(1/fps - (end_t-start_t), 0))
