# coding=utf-8
import threading
import time
from TYPES import *
import re

def ParseSMS(Msg):

        command = Command()
        command.recipient = Msg.recipient
        SMStext = str(Msg.text)
        SMSlist = re.split(" ",SMStext)
        if SMSlist.__len__() != 4:
            return command

        if SMSlist[0] == "add":
            if (SMSlist[1] == "system"):
                if (SMSlist[2] == "number"):
                    command.cmd = "add system"
                    command.type = "number"
                    command.data = SMSlist[3]
                    return command
            elif (SMSlist[1] == "sensor"):
                if ((SMSlist[2] == "temp") or (SMSlist[2] == "move")):
                    command.cmd = "add sensor"
                    command.type = SMSlist[2]
                    command.data = SMSlist[3]

        elif SMSlist[0] == "del":
            if (SMSlist[1] == "system"):
                if (SMSlist[2] == "number"):
                    command.cmd = "del system"
                    command.type = "number"
                    command.data = SMSlist[3]
                    return command
            elif (SMSlist[1] == "sensor"):
                if ((SMSlist[2] == "temp") or (SMSlist[2] == "move")):
                    command.cmd = "del sensor"
                    command.type = SMSlist[2]
                    command.data = SMSlist[3]

        elif SMSlist[0] == "get":
            if SMSlist[1] == "sensor":
                if ((SMSlist[2] == "temp") or (SMSlist[2] == "move")):
                    command.cmd = "get sensor"
                    command.type = SMSlist[2]
                    command.data = SMSlist[3]

        return command

def StartProtol(QueueInFromGSM, QueueOutToMainDevice,QueueInFromMainDevice, QueueOutToGSM):

    while True:
        if QueueInFromGSM.empty() == False:
            MSGgetfromGSM = Message()
            MSGgetfromGSM = QueueInFromGSM.get()
            cmd = ParseSMS(MSGgetfromGSM)

            if cmd.cmd != "None":
                QueueOutToMainDevice.put(cmd)
            else:
                ErrorMSG = Message()
                ErrorMSG.recipient = MSGgetfromGSM.recipient
                ErrorMSG.text = "Command not found"
                QueueOutToGSM.put(ErrorMSG)

        if QueueInFromMainDevice.empty() == False:
            MSGgetFromMainDevice = Command()
            MSGgetFromMainDevice = QueueInFromMainDevice.get()
            MSGtoGSM = Message()
            MSGtoGSM.recipient = MSGgetFromMainDevice.recipient
            if (MSGgetFromMainDevice.cmd != "cmd error"):
                MSGtoGSM.text = MSGgetFromMainDevice.cmd + ' ' + MSGgetFromMainDevice.type + ' ' + MSGgetFromMainDevice.data
            else:
                MSGtoGSM.text = MSGgetFromMainDevice.data
            QueueOutToGSM.put(MSGtoGSM)
