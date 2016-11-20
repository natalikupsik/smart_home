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
                QueueOutToProtocol.put(CmdResponse)
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

                    QueueOutToProtocol.put(CmdResponse)

                elif ((Cmd.cmd == "del system") and (Cmd.type == "number")):
                    if (Cmd.data not in TelephonesList):
                        CmdResponse.recipient = Cmd.recipient
                        CmdResponse.type = Cmd.type
                        CmdResponse.cmd = "cmd error"
                        CmdResponse.data = "This phone not exist in system"
                        QueueOutToProtocol.put(CmdResponse)
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
                        QueueOutToProtocol.put(CmdResponse)








        #обработка команд от менеджера ввода вывода



