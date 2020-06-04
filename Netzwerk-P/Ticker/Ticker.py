import tkinter as tk
from ptpython import *
import random
from tkinter import ttk

master = tk.Tk()
master.geometry('500x500')

#spells = ['avada kedevra!', 'sectumsempra', 'riddikulus', 'lumos','expelliarmus']
#colors = ['orange', '#FFFFFF', '#54BAD8', '#0093C6', 'magenta','lightblue','orange']
#i = 0
#def spelBound():
#    global i
#    label = tk.Label(root,
#             text=random.choice(spells),
#             bg=random.choice(colors),
#             font=('Times New Roman',18,'bold'))
#    i = i + 1
#    label.grid(row=5+i, column=15)
#
#button = tk.Button(root,
#                  text='Reveal a Spell',
#                  command = spelBound)
#button.grid(row=0,column=2)
#
#button2 = ttk.Button(root,
#                     text ='push',command=spelBound)
#button2.grid(padx = 10,row =2,column=2)
i = 0
def clickThatButton():
    global i
    i += 1
    print('click'+str(i))

button = ttk.Button(master,
                    text = 'submit',
                    command = clickThatButton)
button.pack()
master.mainloop()