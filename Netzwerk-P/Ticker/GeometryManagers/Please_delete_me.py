import tkinter as tk

class application:
    def __init__(self,window):
        """ Initalize the Application """
        self.myentrybox = tk.Entry(window)
        self.myentrybox.pack()
        self.myentrybox.insert(0,"some default value")
        self.myentrybox.bind("<Return>",self.Enter)

    def Enter(self,event):
        """ Someone Pressed Enter """
        print ("You entered >> %s" % (self.myentrybox.get()))

root=tk.Tk()
root.geometry('200x200')
myapp = application(root)
root.mainloop()