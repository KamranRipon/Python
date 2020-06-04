import tkinter as tk
from ptpython import *
from tkinter import ttk

master = tk.Tk()

check = ttk.Checkbutton(master, text='check')
check.pack(padx=150, pady=150)

checkvar = tk.BooleanVar()
check.config(variable=checkvar)

checkvar.set(True)

master.mainloop()