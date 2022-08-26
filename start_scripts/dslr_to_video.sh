#!/bin/bash
#ssh drone@jtx "cd /home/drone/video_streaming; ./dslr_to_video.sh"
ssh drone@jtx "cd /home/drone/video_streaming; python3 dslr_to_video.py"
