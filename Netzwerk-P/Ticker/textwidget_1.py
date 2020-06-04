import tkinter as tk
from ptpython import *
from tkinter import ttk


master = tk.Tk()
master.geometry('400x300')

text_1 = tk.Text(master,
                 width = 70,
                 height=20,
                 font = ('Times New Roman', 20, 'italic'))

text_1.pack()
text_1.config(wrap = 'word')

text_1.config(wrap = 'word')

text_1.config(padx = 30)

text_1.pack()

text = '''It is not an error to specify line numbers beyond the last line, 
or column numbers beyond the last column on a line. Such numbers correspond 
to the line beyond the last, or the newline character ending a line.

Note that line/column indexes may look like floating point values, but it’s 
seldom possible to treat them as such (consider position 1.25 vs. 1.3, for example). 
I sometimes use 1.0 instead of “1.0” to save a few keystrokes when referring to the 
first character in the buffer, but that’s about it. '''

text_1.insert('1.0 + 1 lines', text, '\n')
              
master.mainloop()