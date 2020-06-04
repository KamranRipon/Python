import tkinter as tk
from ptpython import *
from tkinter import ttk


class PackGm:
    
    def __init__(self, master):
        
        
        self.label_1 = tk.Label(master,
                                text = 'this is label 1',
                                bg = 'yellow',
                                font = ('Times New Roman', 20, 'italic')).pack()
        self.label_2 = tk.Label(master,
                                text = 'this is label 2',
                                bg = 'white',
                                font = ('Times New Roman', 20, 'italic')).pack()
        self.label_3 = tk.Label(master,
                                text = 'this is label 3',
                                bg = 'light blue',
                                font = ('Times New Roman', 20, 'italic')).pack()
        self.label_4 = tk.Label(master,
                                text = 'this is label 4',
                                bg = 'olive',
                                font = ('Times New Roman', 20, 'italic')).pack()
        
        self.config_labels()
    
    def config_labels(self):
        for widget in master.pack_slaves():
            widget.pack_configure(
                    padx = 20, pady = 20,
                    ipadx = 60, ipady = 60
                    )
            
            if '1' in widget['text']:
                widget.pack_configure(anchor ='nw')
                
            elif '2' in widget['text']:
                widget.pack_configure(anchor ='s')
                
            else:
                widget.pack_configure(anchor = 'se')
            
#            print(widget.pack_info())
            
#            widget.pack_forget()
                print(str(widget))
        print(str(master))
#    
if __name__ == '__main__':
    master = tk.Tk()
    master.geometry('400x300')
    PackGm(master)
    master.mainloop()