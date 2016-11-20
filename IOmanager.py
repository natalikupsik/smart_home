# coding=utf-8
import threading
import time
from TYPES import *

def StartIOmanager(QueueInFromGUI, QueueInFromMainDevice, QueueOutToGUI, QueueOutToMainDevice):

    SensorsTempValues = ["None","None","None","None"]

    while True:

        if (QueueInFromGUI.empty() == False):
            #print SensorsTempValues
            sensor = QueueInFromGUI.get()
            if (sensor.type == "move"):
                CmdAction = CommandIO()
                CmdAction.cmd = "response"
                CmdAction.type = "move"
                CmdAction.number = sensor.number
                CmdAction.data = "action"
                QueueOutToMainDevice.put(CmdAction)
            elif (sensor.type == "temp"):
                SensorsTempValues[sensor.number] = sensor.value

        if (QueueInFromMainDevice.empty() == False):
            CmdRequest = QueueInFromMainDevice.get()
            CmdResponse = CommandIO()
            if (CmdRequest.cmd == "request"):
                CmdResponse.cmd = "response"
                CmdResponse.type = CmdRequest.type
                CmdResponse.number = CmdRequest.number
                CmdResponse.data =  str(SensorsTempValues[CmdRequest.number])
                QueueOutToMainDevice.put(CmdResponse)


        SensorCount = 0
        while (SensorCount < 4):
            QueueOutToGUI.put(Sensor("temp", SensorCount,"None"))
            SensorCount = SensorCount + 1

