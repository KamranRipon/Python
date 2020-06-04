import tkinter as tk
from ptpython import *
from tkinter import ttk


master = tk.Tk()

def displayPicture():
    global img_gif
    label_1 = tk.Label(master,
                       text = 'Here comes the Rockman',
                       font = ('Mv Boli', 15, 'bold')
                       )
    img_gif = tk.PhotoImage(file='pic1.gif')
    label_1.config(image = img_gif, compound = 'left')
    label_1.pack()
    
displayPicture()

master.mainloop()