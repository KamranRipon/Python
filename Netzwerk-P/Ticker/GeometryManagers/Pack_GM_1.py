import tkinter as tk
from ptpython import *
from tkinter import ttk


class PackGm:
    
    def __init__(self, master):
        
        
        self.label_1 = tk.Label(master,
                                text = 'this is label 1',
                                bg = 'white',
                                font = ('Times New Roman', 20, 'italic')).pack(side ='top')
        self.label_2 = tk.Label(master,
                                text = 'this is label 2',
                                bg = 'yellow',
                                font = ('Times New Roman', 20, 'italic')).pack(side ='bottom')
        self.label_3 = tk.Label(master,
                                text = 'this is label 3',
                                bg = 'light blue',
                                font = ('Times New Roman', 20, 'italic')).pack(side ='right')
        self.label_4 = tk.Label(master,
                                text = 'this is label 4',
                                bg = 'olive',
                                font = ('Times New Roman', 20, 'italic')).pack(side ='left')
    
if __name__ == '__main__':
    master = tk.Tk()
    master.geometry('400x300')
    PackGm(master)
    master.mainloop()