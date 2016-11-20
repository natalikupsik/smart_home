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
        self.recipient = 0

    def PrintInfo(self):
        print('\n')
        print('Command: ' + self.cmd + ' ' + self.type + ' ' + self.recipient)

class CommandIO:
    def __init__(self):
        self.cmd = "None" #request/response
        self.type = "None"
        self.number = "None"
        self.data = "None"

    def PrintInfo(self):
        print('\n')
        print('CommandIO: ' + self.cmd + ' ' + self.type + ' ' + str(self.number) + ' ' + self.data)