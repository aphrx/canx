import time
import sys
import cantools
import can
import socket

# code modified, tweaked and tailored from code by bertwert 
# on RPi forum thread topic 91796
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
 
# GPIO ports for the 7seg pins
segments =  (11,4,23,8,7,10,18,25)
# 7seg_segment_pins (11,7,4,2,1,10,5,3) +  100R inline
 
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)
 
# GPIO ports for the digit 0-3 pins 
digits = (22,27,17,24)
# 7seg_digit_pins (12,9,8,6) digits 0-3 respectively
 
for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)
 
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(0,1,0,1,1,1,1),
    '3':(0,1,1,1,0,1,1),
    '4':(1,1,1,0,0,0,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(0,1,1,0,0,1,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}

db = cantools.database.load_file('../nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')


fl = 0              # Front Left Door
fr = 0              # Front Right Door
rl = 0              # Rear Left Door
rr = 0              # Rear Right Door
l = 0               # Left Blinker
r = 0               # Right Blinker

while(True):
    message = can_bus.recv()

    if(message.arbitration_id == 645):
        speed = str(int(db.decode_message(message.arbitration_id, message.data)['WHEEL_SPEED_RR']))
        print("Speed: " + speed)
        s = speed.rjust(4)
        for digit in range(4):
            for loop in range(0,7):
                GPIO.output(segments[loop], num[s[digit]][loop])
                if (int(time.ctime()[18:19])%2 == 0) and (digit == 1):
                    GPIO.output(25, 1)
                else:
                    GPIO.output(25, 0)
            time.sleep(0.001)
 

    elif(message.arbitration_id == 1057):
        print("Gears: " + db.decode_message(message.arbitration_id, message.data)['GEAR_SHIFTER'])

    elif(message.arbitration_id == 1549):

        fl = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_FL']
        fr = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_FR']
        rl = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_RL']
        rr = db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_RR']
        

        temp = str(fl) + " " + str(fr) + " " + str(rl) + " " + str(rr)

        print("Doors: " + temp)

    elif(message.arbitration_id == 856):


        l = db.decode_message(message.arbitration_id, message.data)['LEFT_BLINKER']
        r = db.decode_message(message.arbitration_id, message.data)['RIGHT_BLINKER']

        temp = str(l) + " " + str(r)

        print("Blinkers: " + temp)
    #else:
    #    print(message.arbitration_id)






