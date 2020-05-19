import cantools
import can
import time
from pprint import pprint

db = cantools.database.load_file('../nissan_leaf_2018.dbc')
can_bus = can.interface.Bus('vcan0', bustype='socketcan')

speed_message = db.get_message_by_name('WHEEL_SPEEDS_REAR')
pprint(speed_message.signals)

i = 0;
while True:
	time.sleep(.1)
	data = speed_message.encode({'WHEEL_SPEED_RR': i, 'WHEEL_SPEED_RL': i})
	message = can.Message(arbitration_id=speed_message.frame_id, data=data)
	can_bus.send(message)
	i = i + 1
