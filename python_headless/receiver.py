import time
import sys
import cantools
import can
import socket

db = cantools.database.load_file('../nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')


fl = 0              # Front Left Door
fr = 0              # Front Right Door
rl = 0              # Rear Left Door
rr = 0              # Rear Right Door
l = 0               # Left Blinker
r = 0               # Right Blinker

while(true):
    message = can_bus.recv()

    s.sendall(str(message) + "\n")

    if(message.arbitration_id == 645):
        i.set(db.decode_message(message.arbitration_id, message.data)['WHEEL_SPEED_RR'])

    elif(message.arbitration_id == 1057):
        g.set(db.decode_message(message.arbitration_id, message.data)['GEAR_SHIFTER'])

    elif(message.arbitration_id == 1549):

        global fl, fr, rl, rr

        fl = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_FL']
        fr = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_FR']
        rl = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_RL']
        rr = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_RR']
        

        temp = str(fl) + " " + str(fr) + " " + str(rl) + " " + str(rr)

        doorlights.set(temp)

    elif(message.arbitration_id == 856):

        global l, r

        l = db.decode_message(message.arbitration_id, message.data)['LEFT_BLINKER']
        r = db.decode_message(message.arbitration_id, message.data)['RIGHT_BLINKER']

        temp = str(l) + " " + str(r)

        blinkers.set(temp)
    else:
        print(message.arbitration_id)





