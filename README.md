# CANX
## Overview
This project was developed initially as a way to showcase how CAN works. It illustrates the powers of a DBC file. The CAN messanges sent in this project use the Nissan Leaf 2018 as a template, however I am hopefully planning on making this non-vehicle specific.

This project only works on Linux machines as canutils is only available on Linux.

## CANX Sender
This is the file that sends the actual can messages. Once you open the file by using `python sender.py`, you can adjust any of the parameters. Keep in mind that the virtual CAN bus must be initialized first.

## CANX Receiver
This is the file that mimics the behavior of the listeners on a vehicle. It will listen to the CAN messages on the virtual bus and display them accordingly.