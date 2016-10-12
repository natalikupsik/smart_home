# coding=utf-8
from sms import *
import Queue
import time

class Control_device:

    def __init__(self):
        self.queue_out = Queue.Queue()
        self.queue_in  = Queue.Queue()


    def work(self):
        sms = SMS()

        while (True):
            time.sleep(6)
            if self.queue_in.empty() == False:
                get_sms(sms,self.queue_in.get())
                if sms.status == "unread":
                    if sms.type == "configuration":
                        print sms.device, '#', sms.device_id, ' ',sms.data

                    if sms.type == "get status":
                        print sms.device, '#', sms.device_id, ' ',sms.data

                    if sms.type == "control":
                        print sms.device, '#', sms.device_id, ' ',sms.data



def start(sms_thread_in,sms_thread_main_device):
    parse_sms = SMS()
    while (True):
       #print '1'
       parse_sms.update()
       sms_thread_in.queue_in.put(parse_sms)
       if sms_thread_in.queue_out.empty() == False:
         sms_thread_main_device.queue_in.put(sms_thread_in.queue_out.get())
       time.sleep(6) # 1s