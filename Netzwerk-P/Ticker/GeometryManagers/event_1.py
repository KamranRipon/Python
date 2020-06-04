from tkinter import *
from tkinter import ttk


master = Tk()
master.geometry('600x350+200+200')

frame_1 = ttk.Frame(master,
                    width=500,
                    height=200,
                    relief = 'groove')

frame_1.pack()

label_1 = ttk.Label(master,
                    width = 40,
                    background = 'light blue',
                    anchor=CENTER,
                    font=('helvetica', 14)
                    )
label_1.pack()

def coords(event):
    
    temp = 'x:{} , y:{}'.format(event.x, event.y)
    
    label_1.config(text=temp)

frame_1.bind('<Button-1>', coords)


master.mainloop()