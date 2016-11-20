# coding=utf-8

from GUI import *
from gsm import  *
import Queue
import threading
from protocol import  *
from IOmanager import  *
from TYPES import *
from device import *

#данный модуль запускает все процессы и сопоставляет очереди
'''def work(QueueIn,QueueOut):
    a = 0
    while True:
        if QueueIn.empty() == False:
           cmd = CommandIO()
           cmd = QueueIn.get()
           cmd.PrintInfo()

        if (a==0):
            time.sleep(15)
            a = 1
            c = CommandIO()
            c.cmd = "request"
            c.type = "temp"
            c.number = 0
            c.data = "NULL"
            c.PrintInfo()
            QueueOut.put(c)

'''

'''
rf = threading.Thread(target=work, args=(QueueIn,QueueOut))
rf.start()
StartGUI(QueueIn,QueueOut)
'''

'''
QueueIn = Queue.Queue()
QueueOut = Queue.Queue()

StartModem(QueueIn,QueueOut,'/dev/cu.HUAWEIMobile-Pcui','/dev/cu.HUAWEIMobile-Modem')

'''


'''
QueueInMainDeviceFromProtocol = Queue.Queue()
QueueOutMainDeviceToProtocol = Queue.Queue()

QueueInProtocolFromGSM = Queue.Queue()
QueueOutProtocolToGSM = Queue.Queue()


threadProtocol = threading.Thread(target=StartProtol, args=(QueueInProtocolFromGSM, QueueInMainDeviceFromProtocol,QueueOutMainDeviceToProtocol, QueueOutProtocolToGSM,))
threadProtocol.start()

threadGSM= threading.Thread(target=StartModem, args=(QueueOutProtocolToGSM,QueueInProtocolFromGSM,))
threadGSM.start()

test = threading.Thread(target=work, args=(QueueInMainDeviceFromProtocol,))
test.start()

'''

'''
QueueInFromGUI = Queue.Queue()
QueueInFromMainDevice = Queue.Queue()
QueueOutToGUI = Queue.Queue()
QueueOutToMainDevice = Queue.Queue()

threadIO = threading.Thread(target=StartIOmanager, args=(QueueInFromGUI, QueueInFromMainDevice, QueueOutToGUI, QueueOutToMainDevice,))
threadIO.start()

test = threading.Thread(target=work, args=(QueueOutToMainDevice,QueueInFromMainDevice))
test.start()

StartGUI(QueueOutToGUI,QueueInFromGUI)

'''

QueueFromGUIToIO = Queue.Queue()
QueueFromIOToGUI = Queue.Queue()

QueueFromIOtoDevice = Queue.Queue()
QueueFromDeviceToIO = Queue.Queue()

QueueFromDeviceToProtocol = Queue.Queue()
QueueFromProtocolToDevice = Queue.Queue()

QueueFromGSMToProtocol = Queue.Queue()
QueueFromProtocolToGSM = Queue.Queue()


GSMModemThread = threading.Thread(target=StartModem, args=(QueueFromProtocolToGSM,QueueFromGSMToProtocol,))
GSMModemThread.start()

ProtocolThread = threading.Thread(target=StartProtol, args=(QueueFromGSMToProtocol, QueueFromProtocolToDevice,QueueFromDeviceToProtocol, QueueFromProtocolToGSM,))
ProtocolThread.start()

DeviceThread = threading.Thread(target=StartDevice, args=(QueueFromProtocolToDevice,QueueFromIOtoDevice,QueueFromDeviceToProtocol,QueueFromDeviceToIO,))
DeviceThread.start()

IOThread = threading.Thread(target=StartIOmanager, args=(QueueFromGUIToIO,QueueFromDeviceToIO,QueueFromIOToGUI,QueueFromIOtoDevice,))
IOThread.start()

StartGUI(QueueFromIOToGUI,QueueFromGUIToIO)

