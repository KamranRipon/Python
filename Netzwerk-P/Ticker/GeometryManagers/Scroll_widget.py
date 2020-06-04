import tkinter as tk
from ptpython import *
from tkinter import ttk

class Frame:
    
    def __init__(self, master):
        
        self.frame_1 = ttk.Frame(master,
                                height = 200,
                                width = 300,
                                relief = 'solid' ## flat, raised, groove, ridge
                                )
        self.frame_2 = ttk.Frame(master,
                                 height = 200,
                                 width = 300,
                                 relief = 'sunken')
#        
        self.labe_1 = ttk.Label(self.frame_1,
                                text = 'This is Label 1')
        self.labe_2 = ttk.Label(self.frame_2,
                                text = 'This is Label 2')
        
        self.button_1 = ttk.Button(self.frame_1,
                                   text = 'Submit')
        self.button_2 = ttk.Button(self.frame_2,
                                   text = 'EXIT',
                                   command = master.destroy)
        
        
        self.checkbutton = ttk.Checkbutton(master,
                                           text = 'show me the money')
        self.checkbutton.grid(row=2,
                              column = 1,
                              padx=10,
                              pady = 10,
                              sticky='w')
        
        self.checkvar = tk.BooleanVar()
        self.checkvar.set(True)
        self.checkbutton.config(variable = self.checkvar)
        
        
     
        
        
        
        self.frame_1.grid(row = 1,
                          column = 1,
                          padx = 20,
                          pady = 20)
        self.frame_2.grid(row = 1,
                          column = 2, 
                          padx = 20,
                          pady = 20)
        
        self.labe_1.grid(row = 1,
                         column=1,
                         padx = 20,
                         pady = 20)
        self.labe_2.grid(row = 1,
                         column=1,
                         padx = 20,
                         pady = 20)
        
        self.button_1.grid(row = 1,
                         column=2,
                         padx = 20,
                         pady = 20)
        self.button_2.grid(row = 1,
                         column=2,
                         padx = 20,
                         pady = 20)
        


if __name__ == '__main__':
    master = tk.Tk()
#    master.geometry('400x500')
    Frame(master)
    master.mainloop()