import time
import sys
import cantools
import can
import tkinter as tk
from tkinter import ttk
from threading import Thread
from pprint import pprint

db = cantools.database.load_file('nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')

def fetch():
    global i, g
    message = can_bus.recv()

    if(message.arbitration_id == 645):
        i.set(db.decode_message(message.arbitration_id, message.data)['WHEEL_SPEED_RR'])

    elif(message.arbitration_id == 1057):
        g.set(db.decode_message(message.arbitration_id, message.data)['GEAR_SHIFTER'])
    
    elif(message.arbitration_id == 1549):
        temp =  (str(db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_FL']) + " " +
                str(db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_FR']) + " " +
                str(db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_RL']) + " " +
                str(db.decode_message(message.arbitration_id, message.data)['DOOR_OPEN_RR']) + " ")
        doorlights.set(temp)
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

print(i)

root.after(5, fetch)
root.mainloop()




