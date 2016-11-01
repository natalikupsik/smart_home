# coding=utf-8
from Tkinter import *

def UpdateTempValues(frame1, frame2, frame3, frame4):

    #эти данные кладутся в выходную очередь по запросу из входной очереди (из модуля ввода вывода)
    global  temperature1
    global  temperature2
    global  temperature3
    global  temperature4

    try:
        temperature1 = int(frame1.get())
        temperature2 = int(frame2.get())
        temperature3 = int(frame3.get())
        temperature4 = int(frame4.get())

    except Exception:
            print("No value of temperature entered")

    else:
        print temperature1
        print temperature2
        print temperature3
        print temperature4


def MoveEvent(QueueOut, MoveSensorId):
    QueueOut.put(('Attention on move sensor #' + str(MoveSensorId)))

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



    UpdateTempValueButton = Button(frame, text="Update temperatures", command= lambda: UpdateTempValues(temp1, temp2, temp3, temp4)).grid(row=10, column=1, padx=(80, 0))


    #данные о датчике движения будут только класться в выходную очередь

    Move = Button(frame, text="Move sensor #1", command= lambda: MoveEvent(QueueOut,1)).grid(row=2, column=4, padx=(80, 0))
    Move = Button(frame, text="Move sensor #2", command= lambda: MoveEvent(QueueOut,2)).grid(row=4, column=4, padx=(80, 0))
    Move = Button(frame, text="Move sensor #3", command= lambda: MoveEvent(QueueOut,3)).grid(row=6, column=4, padx=(80, 0))
    Move = Button(frame, text="Move sensor #4", command= lambda: MoveEvent(QueueOut,4)).grid(row=8, column=4, padx=(80, 0))

    #данные будут только получаться из входной очереди
    Relay = Label(frame, text= ('Switch relay #1')).grid(row=10,column=4,padx=(100,10))

    root.mainloop()


