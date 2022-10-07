#!/bin/bash
#Process will live until abort is sent from script server

ffmpeg -f v4l2 -i /dev/video0 -c libx264 -pix_fmt yuv420p -preset ultrafast -f flv -b:v 0 -g 1 -tune zerolatency -crf 18 rtmp://ome.waraps.org/app/RISE-HX-003
