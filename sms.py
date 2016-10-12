# coding=utf-8
import json

class SMS:
    # Чтение сообщения из файла
    def __init__(self):
        self.status = None
        self.type = None
        self.device = None
        self.device_id = None
        self.data = None

    def update(self):
        sms = json.load(open("sms.json"))
        self.status = sms["status"]
        self.type = sms["type"]
        self.device = sms["device"]
        self.device_id = sms["device_id"]
        self.data = sms["data"]


        sms_update = {}
        sms_update["status"] = "read"
        sms_update["type"] = self.type
        sms_update["device"] = self.device
        sms_update["device_id"] = self.device_id
        sms_update["data"] = self.data
        with open("sms.json", 'w') as fp:
            json.dump(sms_update, fp)



def get_sms(sms_destination, msg_source):
        sms_destination.status = msg_source.status
        sms_destination.type = msg_source.type
        sms_destination.device = msg_source.device
        sms_destination.device_id = msg_source.device_id
        sms_destination.data = msg_source.data