import tkinter as tk
import threading as td
import queue as Q
from time import sleep
import random
from ptpython import *
from tkinter import ttk




def run():
    count = 0
    while True:
        count += 1
        thread_0_update(count)
        sleep(random.random()/100)
            


def thread_0_update(val):
    q.put(val)
    master.event_generate("<<Thread_0_Label_Update>>", when='tail')

def thread_0_update_e(e):
    while q.qsize():
        try:
            val = q.get()
            label_1.config(text = str(val))
        except Q.Empty:
            pass


master = tk.Tk()
master.geometry('400x400+1+1')

frame_1 = ttk.Frame(master,height = 100, width = 100)
frame_1.pack()
#frame_1.grid(row=1, column=1, padx=20,pady = 20)

label_1 = ttk.Label(frame_1)
label_1.pack()
#label_1.grid(row=1, column=1, padx=5,pady=5)

#button_1 = ttk.Button(master, text='Go')
#button_1.grid(row=3, column=3)

q = Q.Queue()

master.bind("<<Thread_0_Label_Update>>", thread_0_update_e)

master.mainloop()