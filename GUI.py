# coding=utf-8
from Tkinter import *
import threading
import time
from TYPES import *

def UpdateTempValues(frame1, frame2, frame3, frame4, QueueIn, QueueOut):

        if QueueIn.empty() == False:
            temperature_sensor_request = QueueIn.get()
            if temperature_sensor_request.type == "temp":

                try:
                    if temperature_sensor_request.number == 0:
                        temperature_sensor_response = Sensor("temp", temperature_sensor_request.number,int(frame1.get()))
                    if temperature_sensor_request.number == 1:
                        temperature_sensor_response = Sensor("temp", temperature_sensor_request.number,int(frame2.get()))
                    if temperature_sensor_request.number == 2:
                        temperature_sensor_response = Sensor("temp", temperature_sensor_request.number,int(frame3.get()))
                    if temperature_sensor_request.number == 3:
                        temperature_sensor_response = Sensor("temp", temperature_sensor_request.number,int(frame4.get()))

                except Exception:
                    temperature_sensor_response = Sensor("temp", temperature_sensor_request.number,"None")
                    QueueOut.put(temperature_sensor_response)
                else:
                    QueueOut.put(temperature_sensor_response)





def StartTemperatureSensors(frame1, frame2, frame3, frame4,QueueIn, QueueOut):
    while True:
        UpdateTempValues(frame1, frame2, frame3, frame4,QueueIn, QueueOut)





def MoveEvent(QueueOut, MoveSensorId):
    move_sensor = Sensor("move",MoveSensorId,"on")
    QueueOut.put(move_sensor)

def StartGUI(QueueIn,QueueOut):

    root = Tk()
    root.title("GUI for SmartHome")
    root.geometry("{}x{}+200+100".format(600, 300))

    frame = Frame(root)
    frame.grid()

    #задание пустых ячеек для интервала между строками
    none = Label(frame, text="").grid(row=1,column=1,padx=(10,10))
    none = Label(frame, text="").grid(row=3,column=1,padx=(10,10))
    none = Label(frame, text="").grid(row=5,column=1,padx=(10,10))
    none = Label(frame, text="").grid(row=7,column=1,padx=(10,10))
    none = Label(frame, text="").grid(row=9,column=1,padx=(10,10))
    none = Label(frame, text="").grid(row=11,column=1,padx=(10,10))

    #инициализация полей для ввода температуры

    # данные температуры будут класться в выходную очередь по запросу из входной очереди

    temp1_label = Label(frame, text="Temperature #1").grid(row=2,column=1,padx=(50,10))
    temp1 = Entry(frame, width=3)
    temp1.grid(row=2,column=2,padx=(10,10))

    temp2_label = Label(frame, text="Temperature #2").grid(row=4,column=1,padx=(50,10))
    temp2 = Entry(frame, width=3)
    temp2.grid(row=4,column=2,padx=(10,10))

    temp3_label = Label(frame, text="Temperature #3").grid(row=6,column=1,padx=(50,10))
    temp3 = Entry(frame, width=3)
    temp3.grid(row=6,column=2,padx=(10,10))

    temp4_label = Label(frame, text="Temperature #4").grid(row=8,column=1,padx=(50,10))
    temp4 = Entry(frame, width=3)
    temp4.grid(row=8,column=2,padx=(10,10))


    #данные о датчике движения будут только класться в выходную очередь

    Move = Button(frame, text="Move sensor #1", command= lambda: MoveEvent(QueueOut,0)).grid(row=2, column=4, padx=(80, 0))
    Move = Button(frame, text="Move sensor #2", command= lambda: MoveEvent(QueueOut,1)).grid(row=4, column=4, padx=(80, 0))
    Move = Button(frame, text="Move sensor #3", command= lambda: MoveEvent(QueueOut,2)).grid(row=6, column=4, padx=(80, 0))
    Move = Button(frame, text="Move sensor #4", command= lambda: MoveEvent(QueueOut,3)).grid(row=8, column=4, padx=(80, 0))

    rf = threading.Thread(target=StartTemperatureSensors, args=(temp1, temp2, temp3, temp4,QueueIn, QueueOut,))
    rf.start()

    root.mainloop()




