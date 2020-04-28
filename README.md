# CANX
## Overview
This project was developed initially as a way to showcase how CAN works. It illustrates the powers of a DBC file. The CAN messanges sent in this project use the Nissan Leaf 2018 as a template, however I am hopefully planning on making this non-vehicle specific.

This project only works on Linux machines as canutils is only available on Linux.

## Scripts
`vcan.sh` - This script sets up the Virtual CAN 

## Python
### Overview
The Python components of this project interact with the CANbus directly. Below are some of the components and their functionalities.

### CANX Sender
This is the file that sends the actual CAN messages. Once you open the file by using `python sender.py`, you can adjust any of the parameters. Keep in mind that the virtual CAN bus must be initialized first.

### CANX Speed
This file is a simple file which simply increments the speeds and sends it through the CAN bus. It will loop this forever and is a great way to test if everything is performing as expected.

### CANX Receiver
This is the file that mimics the behavior of the listeners on a vehicle. It will listen to the CAN messages on the virtual bus and display them accordingly.

### CANX Trigger
This is the file that triggers behaviour based off CAN messages. Currently, it is hardcoded to turn the blinkers on if a door is open, however there are plans to make this modular soon.

## Java
To communicate with the Java web server, the CANX Receiver code will communicate to the Java Reciever via sockets.

## Dumps
Dumps are a great way to log the CAN messages outputted by CANX as well as real car data such as the `nissan_leaf_candump.log`.

## Starter Commands
Convert CAN messages using provided DBC file - `candump vcan0 | cantools decode nissan_leaf_2018.dbc`
Sniff CAN messages - `cansniffer vcan0`
Play back CAN messages from a log dump (Real CAN log source) - `cat nissan_leaf_candump.log | canplayer vcan0=slcan0`
Play back CAN messages from a log dump (Virtual source) - `cat demo_meet.log | canplayer`
Send a single CAN message - `cansend vcan0 1F334455#1122334455667788`
Dump CAN messages - `candump -L vcan0 > dump.log`
