#!/bin/bash
# Script  runs as root
# Create log folder if not existing
dir=/home/pi/companion_computer/log/performance
if [ ! -d $dir ]
then
     echo "Creating performance log folder"
     mkdir $dir
     chown pi:pi $dir
fi

echo "Logging pi performance "$dir

cd $dir
filename="performance-"$(date +%Y%m%d-%H%M%S)".log"
touch $filename
chown pi:pi $filename

while sleep 0.1; do
    cpu=$((grep 'cpu ' /proc/stat;sleep 0.1;grep 'cpu ' /proc/stat)|awk -v RS="" '{print "CPU: "int(0.5+($13-$2+$15-$4)*100/($13-$2+$15-$4+$16-$5))"%"}')
    mem=$(awk '/MemTotal/{t=$2}/MemAvailable/{a=$2}END{print int(0.5+100-100*a/t)"%"}' /proc/meminfo)
    time_sec=$(date +%Y-%m-%d\ %H:%M:%S,%3N)
	  echo -e $time_sec" \t "$cpu" \t MEM: "$mem >> $filename
	  done
exit 0
