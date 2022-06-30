#!/usr/bin/python3

import json
import argparse
import traceback

from modem import Modem


#--------------------------------------------------------------------#

__author__ = 'Lennart Ochel <lennart.ochel@ri.se>, Andreas Gising <andreas.gising@ri.se>, Kristoffer Bergman <kristoffer.bergman@ri.se>, Hanna Müller <hanna.muller@ri.se>'
__version__ = '0.1.0'
__copyright__ = 'Copyright (c) 2022, RISE'
__status__ = 'development'

#--------------------------------------------------------------------#

'''A script to print some informative modem info to script server'''

# Main
def main(modem):
    # Print mount point
    tty = {'tty': modem.ser.port}
    # Get static info
    static_info = modem.get_static_info()
    # Get signal quality
    signal_quality = modem.send_at_and_parse('sig_quality')
    # Merge into one dict
    modem_status = {**tty, **static_info, **signal_quality}

    # Print to scrren
    print(json.dumps(modem_status, indent=4))

    modem.close()


#--------------------------------------------------------------------#
def _main():
  # parse command-line arguments
  parser = argparse.ArgumentParser(description='APP "app_noise"', allow_abbrev=False, add_help=False)
  parser.add_argument('-h', '--help', action='help', help=argparse.SUPPRESS)
  parser.add_argument('--tty', type=str, default='/dev/ttyUSB3', help='tty reference /dev/ttyXXX', required=False)
  args = parser.parse_args()

  # Create the Modem class
# Try to create the Modem class, the correct path to modem is required

  if args.tty != '/dev/ttyUSB3':
    try:
      modem = Modem(args.tty)
    except:
      print(f'Could not connect to specified tty: {args.tty}')
      return
  # Else try what should work
  else:
    try:
      modem = Modem('/dev/ttyUSB2')
    except:
      print("Could not ocnnect to /dev/ttyUSB2")
      try:
        modem = Modem('/dev/ttyUSB3')
      except:
        print("Could not ocnnect to /dev/ttyUSB3")
        return
  # Finally try main
  try:
    main(modem)
  except:
    print("main(modem) in network_status failed somehow")
    print(traceback.format_exc())

#--------------------------------------------------------------------#
if __name__ == '__main__':
  _main()
