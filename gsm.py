#! /usr/bin/env python
# coding: utf-8
import re
import time
import sys
import serial
from TYPES import *

#обработка входящих смс
class ModemToReceive:

    def __init__(self, QueuePortIn,QueueOut):
        global  SerialPortIN
        SerialPortIN = serial.Serial('/dev/cu.HUAWEIMobile-Pcui', 9600, timeout=0)
        SerialPortIN.write('AT+CMGF=1\r')
        time.sleep(2)
        SerialPortIN.write('AT+CNMI=1,2,2,1,0\r')
        time.sleep(2)

    def ReceiveMsg(self):
             ReceivedMsg = Message()
             NumberOfCharactersReadyToRead = SerialPortIN.inWaiting()  # Get the number of characters ready to be read
             ReceivedData = SerialPortIN.read(NumberOfCharactersReadyToRead)
             String = str(ReceivedData)
             String = String.replace('"',',')
             ListOfReceivedData = re.split("\\r|,| |\n",String)
             ReceivedMsg.number = 0
             ReceivedMsg.text = 0
             for element in ListOfReceivedData:
                 if element == '+CMT:':
                     ReceivedMsg.number = ListOfReceivedData[(ListOfReceivedData.index(element)) + 2]
                     ReceivedMsg.text = ListOfReceivedData[(ListOfReceivedData.index(element)) + 10]
                     ReceivedMsg.Print_info()


             return ReceivedMsg

class ModemToSend:

    def __init__(self, QueueIn,QueuePortOut):
        global  SerialPortOUT
        SerialPortOUT = serial.Serial(QueuePortOut, 9600, timeout=5)
        SerialPortOUT.write('ATZ\r')
        time.sleep(1)
        SerialPortOUT.write('AT+CMGF=1\r')
        time.sleep(1)

    def SendMsg (self, recipient, message):
        SerialPortOUT.write('AT+CMGS="''' + recipient + '''"\r''')
        time.sleep(1)
        SerialPortOUT.write(message + "\r")
        time.sleep(1)
        SerialPortOUT.write(chr(26))


def StartModem(QueueIn,QueueOut,QueuePortIN,QueuePortOUT):
    ModemSend = ModemToSend(QueueIn,QueuePortOUT)
    ModemReceive = ModemToReceive(QueuePortIN,QueueOut)

    while 1:
        if QueueIn.empty() == False:
            MsgToSend = QueueIn.get()
            ModemSend.SendMsg(MsgToSend.recipient,MsgToSend.text)


        MsgReceived = Message()
        MsgReceived = ModemReceive.ReceiveMsg()
        if MsgReceived.number != 0:
            QueueOut.put(MsgReceived)




