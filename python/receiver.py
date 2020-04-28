import time
import sys
import cantools
import can
import socket
import tkinter as tk
from tkinter import ttk

db = cantools.database.load_file('nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

fl = 0
fr = 0
rl = 0
rr = 0
l = 0
r = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def fetch():
    global i, g, s
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
    root.after(5, fetch)
    print(message)


root = tk.Tk()
root.title("Canx Receiver")

mainframe = ttk.Frame(root, padding="24 24 24 24")
mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))

i = tk.IntVar()
g = tk.IntVar()
doorlights = tk.StringVar()
blinkers = tk.StringVar()
i.set(0)
g.set("P")
doorlights.set("0 0 0 0")
blinkers.set("0 0")

ttk.Label(mainframe, text="Speed:  ").grid(row=1, column=1)
ttk.Label(mainframe, textvariable=i).grid(row=1, column=2)
ttk.Label(mainframe, text="  kph").grid(row=1, column=3)

ttk.Label(mainframe, text="Gear:  ").grid(row=2, column=1)
ttk.Label(mainframe, textvariable=g).grid(row=2, column=2)

ttk.Label(mainframe, text="Doors:  ").grid(row=3, column=1)
ttk.Label(mainframe, textvariable=doorlights).grid(row=3, column=2)

ttk.Label(mainframe, text="Blinkers:  ").grid(row=4, column=1)
ttk.Label(mainframe, textvariable=blinkers).grid(row=4, column=2)

print(i)

root.after(5, fetch)
root.mainloop()




