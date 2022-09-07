#!/bin/bash
take_pic_dir=/home/drone/Lumenera/lumenera_camera_sdk_linux_v2_3_for_64bit_arm_systems/examples/takeAPicture
www_dir=/var/www/html
ssh drone@jxt "cd $take_pic_dir; ./takeAPicture"
scp drone@jxt:/$take_pic_dir/captured_image.bmp $www_dir
echo "Resizing the image for display..."
convert -resize 1024X768  $www_dir/captured_image.bmp $www_dir/captured_image_small.jpg
echo "Go to http://25.35.105.129/ so see picture"
exit

