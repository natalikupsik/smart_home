# coding=utf-8
from sms import *
from receive_msg import *
from control_device import *
import threading
import time



receive_sms_thread = Receive()
main_device_thread = Control_device()

threading.Thread(target=start, args=(receive_sms_thread, main_device_thread)).start()
threading.Thread(target=receive_sms_thread.work, args=()).start()
threading.Thread(target=main_device_thread.work, args=()).start()
