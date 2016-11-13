#! /usr/bin/env python
# coding: utf-8


class Message:
    # Инициализация полей сообщения
    def __init__(self):
        self.number = 0
        self.text = 0

    def Print_info(self):
        print('\n')
        print('Message')
        print('number: ' + str(self.number))
        print('text: ' + str(self.text))


def copy_msg(msg_destination, msg_source):
        msg_destination.number = msg_source.number
        msg_destination.text = msg_source.text
        msg_destination.token = msg_source.token