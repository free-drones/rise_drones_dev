#!/usr/bin/python3

import argparse
import serial
import sys
import time
import traceback

#--------------------------------------------------------------------#

__author__ = 'Lennart Ochel <lennart.ochel@ri.se>, Andreas Gising <andreas.gising@ri.se>, Kristoffer Bergman <kristoffer.bergman@ri.se>, Hanna Müller <hanna.muller@ri.se>'
__version__ = '0.1.0'
__copyright__ = 'Copyright (c) 2022, RISE'
__status__ = 'development'

#--------------------------------------------------------------------#

class MODEM:
    def __init__(self, tty_name):
        self.ser = serial.Serial()
        self.ser.port = tty_name
        self.ser.timeout = 0.01     # readline timeout in seconds
        self.ser.baudrate = 115200  # baudrate
        self.ser.open()
        self.ser.flushInput()
        self.ser.flushOutput()

        # AT command convenience table
        self._commands =   {
                            # Static info
                            'hardware':             'ATI',
                            'imsi':                 'AT+CIMI',
                            'imei':                 'AT+GSN',
                            'my_number':            'AT+CNUM',
                            'iccid':                 'AT+QCCID',
                            'current_operator':     'AT+COPS?',
                            'preferred_operator':   'AT+CPOL?',
                            'local_time':           'AT+CTZR?',
                            'config':               'AT+QCFG=?',

                            # Dynamic info
                            'signal_quality':       'AT+CSQ',
                            'band':                 'AT+QCFG="band"',
                            'network_info':         'AT+QNWINFO',
                            'network_reg_info':     'AT+CREG?',
                            'registered_network':   'AT+QSPN',
                            'service_profile':      'AT+CGQREQ=?',

                            # Setters
                            'network_reg_set_opt0': 'AT+CREG=0',
                            'network_reg_set_opt1': 'AT+CREG=1',
                            'network_reg_set_opt2': 'AT+CREG=2', # Req for cell id

                            # Not working..
                            'hsdpa':                'AT+QCFG="hsdpacat',
                            'hsupa':                'AT+QCFG="hsupacat'}
        # Set modem to provide to cell_ID
        if self.set_modem('network_reg_set_opt2'):
            print("Modem set to report Cell-ID on request")
        else:
            print("WARNING: Modem set to report Cell-ID on request FAILED")

    # Send specified AT command and return answer(s)
    def send_at_command(self, cmd_str):
        cmd = cmd_str + "\r\n"
        self.ser.write(cmd.encode())
        answers = []
        while True:
            answer = self.ser.readline()
            if self.is_timeout(answer):
                # This is a timeout
                break
            if self.is_empty_line(answer):
                # Discard empty line
                continue
            # Decode bytes to string
            decoded = answer.decode()
            # Clean trailing carriage return and newlines
            decoded = decoded.rstrip('\r\n')
            # Append to answer list
            answers.append(decoded)
        return answers

    # Send AT command to aquire info via look-up directory
    def get_info(self, key):
        # Look-up key
        if key in self._commands:
            cmd = self._commands[key] + "\r\n"
        else:
            # create exception..
            print("key not recognized:" , key)
            return []
        self.ser.write(cmd.encode())
        answers = []
        attempts = 1
        # Send command and read answer until timeout
        while True:
            answer = self.ser.readline()
            if self.is_timeout(answer):
                # This is a timeout
                if not answers and attempts < 5:
                    # time out and no received answers
                    if attempts == 5:
                        print("Warning, no answer recevied within 5 timeouts")
                        break
                    print("No response within timeout, try again. Attempts: ", attempts)
                    attempts += 1
                    continue
                # Complete response is already received
                break
            # Discard empty lines
            if self.is_empty_line(answer):
                continue
            # Print to stdout on receiving ERROR
            if self.is_error(answer):
                print("Received ERROR when sending ", self._commands[key])
            # Discart 'OK' from answer
            if self.is_ok(answer):
                # Dont log th 'OK'
                continue
            # Decode bytes to string
            decoded = answer.decode()
            # Clean trailing carriage return and newlines
            decoded = decoded.rstrip('\r\n')
            # Append to answer list
            answers.append(decoded)
        return answers

    # Send AT command from look-up directory
    def set_modem(self, key):
        # Look-up key
        if key in self._commands:
            cmd = self._commands[key] + "\r\n"
        else:
            # create exception..
            print("key not recognized:" , key)
            return False
        self.ser.write(cmd.encode())
        answers = []
        attempts = 1
        while True:
            answer = self.ser.readline()
            if self.is_timeout(answer):
                # This is a timeout
                if not answers and attempts < 5:
                    # time out and no received answers
                    if attempts == 5:
                        print("Warning, no answer recevied within 5 timeouts")
                        break
                    print("No response within timeout, try again. Attempts: ", attempts)
                    attempts += 1
                    continue
                # Complete response is already received
                break
            # Discard empty lines
            if self.is_empty_line(answer):
                continue
            # If 'ERROR'
            if self.is_error(answer):
                return False
            # If 'OK'
            elif self.is_ok(answer):
                return True
            else:
                return False

    # Test for timeout answer
    def is_timeout(self, bytes):
        return b'' == bytes

    # Test for carriage return and newline with no data
    def is_empty_line(self, bytes):
        return b'\r\n' == bytes

    # Test for 'ERROR'
    def is_error(self, bytes):
        return b'ERROR\r\n' == bytes

    # Test for 'OK'
    def is_ok(self, bytes):
        return b'OK\r\n' == bytes

    # Test AT command and print answer
    def test(self, cmd):
        answer = self.get_info(cmd)
        print(answer)

    def test_sequence(self):
        print("Static (?) information")
        self.test('hardware')
        print("imsi:")
        self.test('imsi')
        print("imei")
        self.test('imei')
        self.test('my_number')
        self.test('ccid')
        self.test('current_operator')
        #self.test('preferred_operator')
        self.test('icci')
        self.test('local_time')

        self.test('config')

        print("\nDynamic information")
        self.test('signal_quality')
        self.test('band')
        self.test('network_info')
        self.test('network_reg_info')
        #self.test('network_reg_info')
        # reg_info = self.get_info('network_reg_info')
        # data = reg_info[0].split(',')
        # location_area = data[2].replace("\"", "")
        # cell_id = data[3].replace("\"", "")
        # print("location area is: ", location_area, "cellID is : ", cell_id)
        self.test('registered_network')
        self.test('service_profile')

    # Setup serial, not used for now
    def serConf(self):
        self.ser.baudrate = 9600
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.timeout = 0 # Non-Block reading
        self.ser.xonxoff = False # Disable Software Flow Control
        self.ser.rtscts = False # Disable (RTS/CTS) flow Control
        self.ser.dsrdtr = False # Disable (DSR/DTR) flow Control
        self.ser.writeTimeout = 2

    # Close serial
    def close(self):
        self.ser.close()

    # Main
    def main(self):
        self.test_sequence()

        self.close()


#--------------------------------------------------------------------#
def _main():
  # parse command-line arguments
  parser = argparse.ArgumentParser(description='APP "app_noise"', allow_abbrev=False, add_help=False)
  parser.add_argument('-h', '--help', action='help', help=argparse.SUPPRESS)
  parser.add_argument('--tty', type=str, help='tty reference /etc/ttyXXX', required=True)
  args = parser.parse_args()


  # Initiate log file
  #dss.auxiliaries.logging.configure('app_noise', stdout=args.stdout, rotating=True, loglevel=args.log, subdir=subnet)

  # Create the MODEM class

  try:
    modem = MODEM(args.tty)
    modem.main()
  except:
    print("Something bad happened")
    print(traceback.format_exc())

#--------------------------------------------------------------------#
if __name__ == '__main__':
  _main()
