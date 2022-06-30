#!/bin/bash
# Export terminal type for screen
export TERM=vt100

# Check if a screen is already started, if not start a screen and log to file
if ! screen -list | grep -q "atcmd"; then
    # Create log dir of not existing
    dir=/home/pi/rise_drones_dev/log/mobile_data
    if [ ! -d $dir ]
    then
        echo "Creating mobile_data log folder"
        mkdir $dir
        chown pi:pi $dir
    fi

    echo "Logging mobile data to "$dir
    cd $dir

    # Get current date time and create a file for logging
    cur_date_time=`date +%Y%m%d_%H%M%S`
    filename=mobile_data_$cur_date_time.log
    touch $filename

    # Open a screen in background, log input/output, attach to ttyUSB and write to filename
    screen -dmS atcmd -L -Logfile $filename /dev/ttyUSB3 115200 # to create the screen
fi

# Collect device information (once)
screen -S atcmd -X stuff 'AT+CGMI\r\n' # String representation of manufacturer
screen -S atcmd -X stuff 'AT+CGMM\r\n' # Model of modem
screen -S atcmd -X stuff 'AT+CGMR\r\n' # Firmware version
screen -S atcmd -X stuff 'AT+GSN\r\n'  # International Mobile Equipment Identity
screen -S atcmd -X stuff 'AT+CIMI\r\n' # IMSI number
screen -S atcmd -X stuff 'AT+CCID\r\n' # ICCID of the SIM
screen -S atcmd -X stuff 'AT+CNUM\r\n' # Phone number / MSISDN of the device

# Send AT commands in a loop
while true; do
  screen -S atcmd -X stuff 'AT+CSQ\r\n'     # to get signal quality
  screen -S atcmd -X stuff 'AT+QNWINFO\r\n' # to get info about the connected network
  sleep 5
done
