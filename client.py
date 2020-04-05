import cantools
import can
import time
import tkinter as tk
from tkinter import ttk

db = cantools.database.load_file('nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')

speed_message = db.get_message_by_name('WHEEL_SPEEDS_REAR')
gearbox_message = db.get_message_by_name('GEARBOX')

def getSpeed(speed):
    speed = int(speed)
    data = speed_message.encode({'WHEEL_SPEED_RR': speed, 'WHEEL_SPEED_RL': speed})
    message = can.Message(arbitration_id=speed_message.frame_id, data=data)
    can_bus.send(message)

    print(message)

def getGear():
    gear = v.get()
    data = gearbox_message.encode({'GEAR_SHIFTER': gear})
    message = can.Message(arbitration_id=gearbox_message.frame_id, data=data)
    can_bus.send(message)

    print(message)

root = tk.Tk()
root.title("Canx Sender")

mainframe = ttk.Frame(root, padding="24 24 24 24")
mainframe.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'))

slider = tk.StringVar()
slider.set(0)

ttk.Scale(mainframe, from_=0, to_=100, length=300, 
    command=lambda s: [slider.set('%0.2d' % float(s)), getSpeed(int(float(s)))])

ttk.Label(mainframe, textvariable=slider).grid(column=1, columnspan=5)

v = tk.IntVar()

values = {"P" : "1", 
          "R" : "2", 
          "N" : "3", 
          "D" : "4"}

for (text, value) in values.items(): 
    ttk.Radiobutton(mainframe, text = text, variable = v, 
        value = value, command=getGear)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
