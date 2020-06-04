import tkinter as tk
from tkinter import ttk
from ptpython import *


master = tk.Tk()
master.geometry('750x600')   
  
        
label_1 = tk.Label(master,
                   text='Select Search Mode',
                   font=('Times New Romon', 15, 'normal')
                   )
label_2 = tk.Label(master,
                   text='Select States',
                   font=('Times New Romon', 15, 'normal')
                   )
label_3 = tk.Label(master,
                   text='Keywords',
                   font=('Times New Romon', 15, 'normal')
                   )


combo_1 = ttk.Combobox(master,
                       width=25,
                       font=('Times New Roman', 12, 'bold'))
combo_2 = ttk.Combobox(master,
                       width=25,
                       font=('Times New Roman', 12, 'bold'))

entry_1 = ttk.Entry(master,
                       width=28,
                       font=('Times New Roman', 12, 'bold'))

button_1 = ttk.Button(master,
                      text ='GO')
button_2 = ttk.Button(master,
                      text ='Exit',
                      command = master.destroy)

text_1 = tk.Text(master,
                 width=50,
                 height = 15)

label_1.grid(row=1,column=1,padx=10, pady=10,sticky='ne')
label_2.grid(row=2,
             column=1,
             padx=10, pady=10,
             sticky='ne')
label_3.grid(row=3,
             column=1,
             padx=10, pady=10,
             sticky='ne')

combo_1.grid(row=1,column=2,padx=10, pady=10,sticky='nw')
combo_2.grid(row=2,column=2,padx=10, pady=10,sticky='nw')

entry_1.grid(row=3,column=2,padx=10, pady=10,sticky='nw')

text_1.grid(row =4, column=2, padx=10, pady=10, sticky = 'nw')

button_1.grid(row=6,column=2,padx=10, pady=10,sticky='nw')
button_2.grid(row=7,column=2,padx=10, pady=10,sticky='w')

searchMode = ['Normal Search', 'Advance Search']
combo_1['values'] = tuple(searchMode)



    

master.mainloop()