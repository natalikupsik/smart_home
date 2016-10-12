# coding=utf-8
from sms import *
import Queue
import time

class Receive:

    def __init__(self):
        self.queue_out = Queue.Queue()
        self.queue_in  = Queue.Queue()


    def work(self):
        sms_in = SMS()
        sms_out = SMS()

        while (True):
            time.sleep(1)
            if self.queue_in.empty() == False:
                get_sms(sms_in,self.queue_in.get())
                if sms_in.status == "unread":
                    get_sms(sms_out,sms_in)
                    self.queue_out.put(sms_out)

