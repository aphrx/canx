import time
import sys
import cantools
import can
from pprint import pprint

db = cantools.database.load_file('nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')

i = 1
g = 1
while True:
    message = can_bus.recv()

    if(message.arbitration_id == 645):
        i = db.decode_message(message.arbitration_id, message.data)['WHEEL_SPEED_RR']
        

    elif(message.arbitration_id == 1057):
        g = db.decode_message(message.arbitration_id, message.data)['GEAR_SHIFTER']
        
    CURSOR_UP_ONE = '\x1b[1A' 
    ERASE_LINE = '\x1b[2K'
    sys.stdout.write(CURSOR_UP_ONE+ERASE_LINE+'%s   %s%s \n' % ('Speed', i, ' kph'))
    sys.stdout.write('%s    %s%s \r' % ('Gear', g, ''))
    sys.stdout.flush()
    i = i+1
    i = i % 10
