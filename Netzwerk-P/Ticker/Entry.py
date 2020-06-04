import tkinter as tk
from ptpython import *
from tkinter import ttk


master = tk.Tk()
master.geometry('400x300')

entry_1 = tk.Entry(master,
                    width = 15)

entry_1.pack()

entry_2 = ttk.Entry(master,
                    width = 15,
                    font = 10)
entry_2.pack()

entry_2.config(show='*')
master.mainloop()