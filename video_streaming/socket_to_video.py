import time
from subprocess import Popen, PIPE
from datetime import datetime
import socket

HOST = "192.168.2.3"
PORT = 13330


ffmpeg = Popen(['ffmpeg', '-i', '-', '-vcodec', 'rawvideo', '-pix_fmt', 'yuv420p', '-f', 'v4l2', '/dev/video0'],stdin=PIPE)
fps = 25

read_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
read_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
read_sock.bind((HOST, PORT))
read_sock.setblocking(0)
print(f"binded to port complete")

while True:
   try:
      data = read_sock.recv(32768)
      #print(f"data received with length {len(data)}")
      ffmpeg.stdin.write(data)
   except socket.error as e:
      pass
