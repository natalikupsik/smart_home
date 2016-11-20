# coding=utf-8
import threading
import time
from TYPES import *

def StartDevice(QueueInFromProtocol, QueueInFromIO, QueueOutToProtocol, QueueOutToIO):

    TelephonesList = ["None" , "None", "None", "None"]
    TempSensorsList = ["None" , "None", "None", "None"]
    MoveSensorsList = ["None" , "None", "None", "None"]

    InitSystemPhone = False

    CountPhones = 0
    CountTempSensors = 0
    CountMoveSensors = 0

    while True:

        #обработка команд от смс

        if QueueInFromProtocol.empty() == False:
            Cmd = Command()
            Cmd = QueueInFromProtocol.get()
            CmdResponse = Command()

            #проверка наличия номера в списке управляющих номеров
            if ((Cmd.recipient not in TelephonesList) and (InitSystemPhone == True)):
                CmdResponse.recipient = Cmd.recipient
                CmdResponse.type = Cmd.type
                CmdResponse.cmd = "cmd error"
                CmdResponse.data = "Your number is not in system"
                #QueueOutToProtocol.put(CmdResponse)
            else:

                if ((Cmd.cmd == "add system") and (Cmd.type == "number")):
                    if (CountPhones < 4):

                        if (Cmd.data in TelephonesList):
                            CmdResponse.recipient = Cmd.recipient
                            CmdResponse.cmd = "cmd error"
                            CmdResponse.type = Cmd.type
                            CmdResponse.data = "This phone exist."
                        else:
                            TelephonesList[CountPhones] = Cmd.data
                            InitSystemPhone = True
                            CountPhones = CountPhones + 1

                            CmdResponse.recipient = Cmd.recipient
                            CmdResponse.cmd = Cmd.cmd
                            CmdResponse.type = Cmd.type
                            CmdResponse.data = Cmd.data + "\nOperation success."
                    else:
                        CmdResponse.recipient = Cmd.recipient
                        CmdResponse.cmd = "cmd error"
                        CmdResponse.type = Cmd.type
                        CmdResponse.data = "Limit 4 phones. Delete phone."

                    #QueueOutToProtocol.put(CmdResponse)

                elif ((Cmd.cmd == "del system") and (Cmd.type == "number")):
                    if (Cmd.data not in TelephonesList):
                        CmdResponse.recipient = Cmd.recipient
                        CmdResponse.type = Cmd.type
                        CmdResponse.cmd = "cmd error"
                        CmdResponse.data = "This phone not exist in system"
                        #QueueOutToProtocol.put(CmdResponse)
                    else:
                        for phone in TelephonesList:
                            if phone == Cmd.data:
                                TelephonesList[TelephonesList.index(phone)] = "None"

                        CountPhones = CountPhones - 1
                        if (CountPhones == 0):
                            InitSystemPhone = False

                        CmdResponse.recipient = Cmd.recipient
                        CmdResponse.type = Cmd.type
                        CmdResponse.cmd = Cmd.cmd
                        CmdResponse.data = Cmd.data + "\nOperation success."
                        #QueueOutToProtocol.put(CmdResponse)

                elif (Cmd.cmd == "add sensor"):
                    if (Cmd.type == "temp"):

                        if (CountTempSensors < 4):
                            if (Cmd.data in TempSensorsList):
                                CmdResponse.recipient = Cmd.recipient
                                CmdResponse.cmd = "cmd error"
                                CmdResponse.type = Cmd.type
                                CmdResponse.data = "This sensor name exist."
                            else:
                                TempSensorsList[CountTempSensors] = Cmd.data
                                CountTempSensors = CountTempSensors + 1

                                CmdResponse.recipient = Cmd.recipient
                                CmdResponse.cmd = Cmd.cmd
                                CmdResponse.type = Cmd.type
                                CmdResponse.data = Cmd.data + "\nOperation success."
                        else:
                            CmdResponse.recipient = Cmd.recipient
                            CmdResponse.cmd = "cmd error"
                            CmdResponse.type = Cmd.type
                            CmdResponse.data = "Limit 4 temp sensors. Delete sensor."


                    if (Cmd.type == "move"):
                        if (CountMoveSensors < 4):
                            if (Cmd.data in MoveSensorsList):
                                CmdResponse.recipient = Cmd.recipient
                                CmdResponse.cmd = "cmd error"
                                CmdResponse.type = Cmd.type
                                CmdResponse.data = "This sensor name exist."
                            else:
                                MoveSensorsList[CountMoveSensors] = Cmd.data
                                CountMoveSensors = CountMoveSensors + 1

                                CmdResponse.recipient = Cmd.recipient
                                CmdResponse.cmd = Cmd.cmd
                                CmdResponse.type = Cmd.type
                                CmdResponse.data = Cmd.data + "\nOperation success."
                        else:
                            CmdResponse.recipient = Cmd.recipient
                            CmdResponse.cmd = "cmd error"
                            CmdResponse.type = Cmd.type
                            CmdResponse.data = "Limit 4 temp sensors. Delete sensor."

                elif (Cmd.cmd == "del sensor"):

                    if (Cmd.type == "temp"):

                        if (Cmd.data not in TempSensorsList):
                            CmdResponse.recipient = Cmd.recipient
                            CmdResponse.type = Cmd.type
                            CmdResponse.cmd = "cmd error"
                            CmdResponse.data = "This temp name not exist in system"
                            #QueueOutToProtocol.put(CmdResponse)
                        else:
                           for TempSensor in TempSensorsList:
                               if TempSensor == Cmd.data:
                                  TempSensorsList[TempSensorsList.index(TempSensor)] = "None"

                           CountTempSensors = CountTempSensors - 1


                           CmdResponse.recipient = Cmd.recipient
                           CmdResponse.type = Cmd.type
                           CmdResponse.cmd = Cmd.cmd
                           CmdResponse.data = Cmd.data + "\nOperation success."
                           #QueueOutToProtocol.put(CmdResponse)

                    if (Cmd.type == "move"):

                        if (Cmd.data not in MoveSensorsList):
                            CmdResponse.recipient = Cmd.recipient
                            CmdResponse.type = Cmd.type
                            CmdResponse.cmd = "cmd error"
                            CmdResponse.data = "This move name not exist in system"
                            #QueueOutToProtocol.put(CmdResponse)
                        else:
                           for MoveSensor in MoveSensorsList:
                               if MoveSensor == Cmd.data:
                                  MoveSensorsList[MoveSensorsList.index(MoveSensor)] = "None"

                           CountMoveSensors = CountMoveSensors - 1


                           CmdResponse.recipient = Cmd.recipient
                           CmdResponse.type = Cmd.type
                           CmdResponse.cmd = Cmd.cmd
                           CmdResponse.data = Cmd.data + "\nOperation success."
                           #QueueOutToProtocol.put(CmdResponse)

                elif (Cmd.cmd == "get sensor"):
                    if (Cmd.type == "temp"):
                        if Cmd.data in TempSensorsList:
                            for sensor in TempSensorsList:
                                if (sensor == Cmd.data):
                                    SensorCmd = CommandIO()
                                    SensorCmd.type = "temp"
                                    SensorCmd.cmd = "request"
                                    SensorCmd.number = TempSensorsList.index(sensor)

                                    QueueOutToIO.put(SensorCmd)

                                    CmdResponse.recipient = Cmd.recipient
                                    CmdResponse.type = Cmd.type
                                    CmdResponse.cmd = Cmd.cmd
                                    CmdResponse.data = "Request send"

                        else:
                            CmdResponse.recipient = Cmd.recipient
                            CmdResponse.type = Cmd.type
                            CmdResponse.cmd = "cmd error"
                            CmdResponse.data = "This sensor name not exist in system"


            QueueOutToProtocol.put(CmdResponse)






        #обработка команд от менеджера ввода вывода


        if QueueInFromIO.empty() == False:
            CmdIO = CommandIO()
            CmdIO = QueueInFromIO.get()
            CmdResponseInfo = Command()

            if CmdIO.type == "temp":
                CmdResponseInfo.cmd = "Request"
                CmdResponseInfo.type = CmdIO.type
                CmdResponseInfo.data = TempSensorsList[CmdIO.number] + " value is" + CmdIO.data

                for phone in TelephonesList:
                    if phone != "None":
                        CmdResponseInfo.recipient = phone
                        QueueOutToProtocol.put(CmdResponse)

            elif CmdIO.type == "move":
                if MoveSensorsList[CmdIO.number] != "None":
                    CmdResponseInfo.cmd = "Action"
                    CmdResponseInfo.type = CmdIO.type
                    CmdResponseInfo.data = MoveSensorsList[CmdIO.number] + "value is " + CmdIO.data

            for phone in TelephonesList:
                    if phone != "None":
                        CmdResponseInfo.recipient = phone
                        QueueOutToProtocol.put(CmdResponseInfo)