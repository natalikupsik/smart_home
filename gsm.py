#! /usr/bin/env python
# coding: utf-8
import time

import serial


def InitModem(PortName):
    global SerialPort
    SerialPort = serial.Serial(PortName, 9600, timeout=5)

def SendMsg (recipient, message):
    SerialPort.write('AT+CMGF=1\r')
    time.sleep(1)
    SerialPort.write('''AT+CMGS="''' + recipient + '''"\r''')
    time.sleep(1)
    SerialPort.write(message + "\r")
    time.sleep(1)
    SerialPort.write(chr(26))
