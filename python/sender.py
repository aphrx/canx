import cantools
import can
import time
import tkinter as tk
from tkinter import ttk

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

root = tk.Tk()
root.title("Canx Sender")

mainframe = ttk.Frame(root, padding="24 24 24 24")
mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))

slider = tk.StringVar()
slider.set(0)

values = {"P" : "1", 
          "R" : "2", 
          "N" : "3", 
          "D" : "4"}

v = tk.IntVar()
door_fl = tk.IntVar()
door_fr = tk.IntVar()
door_rl = tk.IntVar()
door_rr = tk.IntVar()

left_blinker = tk.IntVar()
right_blinker = tk.IntVar()

ttk.Label(mainframe, text="Speed Slider:  ").grid(row=1, column=0)
ttk.Scale(mainframe, from_=0, to_=100, length=300, command=lambda s: [slider.set('%0.2d' % float(s)), setSpeed(int(float(s)))]).grid(row=1, column=1, columnspan = 4, sticky = tk.W+tk.E)
ttk.Label(mainframe, text="Gear Shifter:  ").grid(row=3, column=0)
for (text, value) in values.items(): 
    ttk.Radiobutton(mainframe, text = text, variable = v, 
        value = value, command=setGear).grid(row=3, column=value)
ttk.Label(mainframe, text="Open Doors:  ").grid(row=5, column=0)
ttk.Checkbutton(mainframe, text="FL", variable=door_fl, command=setDoorStates).grid(row=5, column=1)
ttk.Checkbutton(mainframe, text="FR", variable=door_fr, command=setDoorStates).grid(row=5, column=2)
ttk.Checkbutton(mainframe, text="RL", variable=door_rl, command=setDoorStates).grid(row=5, column=3)
ttk.Checkbutton(mainframe, text="RR", variable=door_rr, command=setDoorStates).grid(row=5, column=4)

ttk.Label(mainframe, text="Blinkers:  ").grid(row=6, column=0)
ttk.Checkbutton(mainframe, text="L", variable=left_blinker, command=setBlinkerStates).grid(row=6, column=1)
ttk.Checkbutton(mainframe, text="R", variable=right_blinker, command=setBlinkerStates).grid(row=6, column=2)

root.mainloop()
