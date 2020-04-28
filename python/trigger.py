import time
import sys
import cantools
import can
import csv

arb_id = 645
trigger = 'WHEEL_SPEED_RR'
trig_threshold = 50
result_arb = 'GEARBOX'
result_mess = 'GEAR_SHIFTER'
result_data = 'D'
message_type = 0



db = cantools.database.load_file('nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')

blinker_message = db.get_message_by_name('LIGHTS')

while(True):
    message = can_bus.recv()
    if(message.arbitration_id == 1549):
   
        fl = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_FL']
        fr = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_FR']
        rl = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_RL']
        rr = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_RR']
        
        if (fl or fr or rl or rr == 1):
            data = blinker_message.encode({'LEFT_BLINKER': 1, 'RIGHT_BLINKER': 1})
            message = can.Message(arbitration_id=blinker_message.frame_id, data=data)
            can_bus.send(message)
        
