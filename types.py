#! /usr/bin/env python
# coding: utf-8


class Message:
    # Инициализация полей сообщения
    def __init__(self):
        self.recipient = 0
        self.text = 0

    def PrintInfo(self):
        print('\n')
        print('Message')
        print('number: ' + str(self.recipient))
        print('text: ' + str(self.text))

    def CopyTo(self, msg):
        msg.number = self.recipient
        msg.text   = self.text

class Sensor:
    def __init__(self, type, number, value):
        self.type = type
        self.number = number
        self.value = value

class Command:
    def __init__(self):
        self.cmd = "None"
        self.type = "None"
        self.data = "None"
        self.number = 0

    def PrintInfo(self):
        print('\n')
        print('Command: ' + self.cmd + ' ' + self.type + ' ' + self.number)
