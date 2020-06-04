import tkinter as tk
from ptpython import *
from tkinter import ttk


class GridGm:
    
    
    def __init__(self, master):
        
        master.title('pyMeet 2020')
        
        
        self.label_1 = ttk.Label(master,
                                 text = 'What\'s your name',
                                 font = ('Times New Roman',14, 'bold')).grid(padx = 5, pady = 5, row=0, sticky='e')
        self.label_2 = ttk.Label(master,
                                 text = 'Your Email',
                                 font = ('Times New Roman',14, 'bold')).grid(padx = 5,pady = 5, row=1, sticky='e')
        self.label_3 = ttk.Label(master,
                                 text = 'Programming Language',
                                 font = ('Times New Roman',14, 'bold')).grid(padx = 5,pady = 5, row=2, sticky='e')
        self.label_4 = ttk.Label(master,
                                 text = 'Comments',
                                 font = ('Times New Roman',14, 'bold')).grid(padx = 5,pady = 5, row=3, sticky='en')
        
        self.entry_1 = ttk.Entry(master,
                                 font = ('Times New Roman',14)).grid(padx=5,pady=5,row=0,column=1,sticky='ew',columnspan=5)
        self.entry_2 = ttk.Entry(master,
                                 font = ('Times New Roman',14)).grid(padx=5,pady=5,row=1,column=1,sticky='ew',columnspan=5)
        self.entry_3 = ttk.Entry(master,
                                 font = ('Times New Roman',14)).grid(padx=5,pady=5,row=2,column=1,sticky='ew',columnspan=5)
        
        self.text_1 = tk.Text(master,
                              width =30,
                              height=5).grid(padx=5, pady=5, row=3, column=1,sticky='ew',columnspan=5)
        
        self.button_1 = ttk.Button(master,
                                   text = 'Reserve').grid(row=4, column=1, sticky='w')
        
        self.check_1 = ttk.Checkbutton(master,
                                       text = 'Arriving early').grid(row=4, column=2, padx=5,pady=5)
        self.check_2 = ttk.Checkbutton(master,
                                       text = 'Need Breakfast').grid(row=4, column=3, padx=5,pady=5)
        
        
        
if __name__ == '__main__':
    
    master = tk.Tk()
    master.geometry('600x300+510+340')
    master.resizable(True, True)
    master.minsize(300,200)
    master.maxsize(2000,1000)
    GridGm(master)
    master.mainloop()