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

