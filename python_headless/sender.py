import cantools
import can
import time

db = cantools.database.load_file('nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')

speed_message = db.get_message_by_name('WHEEL_SPEEDS_REAR')
gearbox_message = db.get_message_by_name('GEARBOX')
doorlight_message = db.get_message_by_name('DOORS_LIGHTS')
blinker_message = db.get_message_by_name('LIGHTS')


def setSpeed(speed):
    speed = int(speed)
    data = speed_message.encode({'WHEEL_SPEED_RR': speed, 'WHEEL_SPEED_RL': speed})
    message = can.Message(arbitration_id=speed_message.frame_id, data=data)
    can_bus.send(message)

    print(message)

def setGear():
    gear = v.get()
    data = gearbox_message.encode({'GEAR_SHIFTER': gear})
    message = can.Message(arbitration_id=gearbox_message.frame_id, data=data)
    can_bus.send(message)

    print(message)

def setDoorStates():
    fl = door_fl.get()
    fr = door_fr.get()
    rr = door_rr.get()
    rl = door_rl.get()
    data = doorlight_message.encode({'DOOR_OPEN_FL': fl, 'DOOR_OPEN_FR': fr, 'DOOR_OPEN_RL': rl, 'DOOR_OPEN_RR': rr})
    message = can.Message(arbitration_id=doorlight_message.frame_id, data=data)
    can_bus.send(message)

    print(message)

def setBlinkerStates():
    l = left_blinker.get()
    r = right_blinker.get()
    data = blinker_message.encode({'LEFT_BLINKER': l, 'RIGHT_BLINKER': r})
    message = can.Message(arbitration_id=blinker_message.frame_id, data=data)
    can_bus.send(message)

    print(message)


values = {"P" : "1", 
          "R" : "2", 
          "N" : "3", 
          "D" : "4"}

num = input("test: ")
print(num)




