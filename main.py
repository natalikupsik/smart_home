# coding=utf-8

from GUI import *
from gsm import  *
import Queue

#данный модуль запускает все процессы и сопоставляет очереди

'''
def work(Queue):
    while (1):
        if (Queue.empty != False):
            print QueueOut.get()

QueueIn = Queue.Queue()
QueueOut = Queue.Queue()
threading.Thread(target=work, args=(QueueOut,)).start()
StartGUI(QueueIn,QueueOut)
'''

QueueIn = Queue.Queue()
QueueOut = Queue.Queue()

StartModem(QueueIn,QueueOut,'/dev/cu.HUAWEIMobile-Pcui','/dev/cu.HUAWEIMobile-Modem')




