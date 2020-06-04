from tkinter import *
from pathlib import Path
from tkinter.filedialog import askopenfilename, asksaveasfile, askdirectory
 
 
class Window(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        self.open = Button(self, text='Open', command=self.open_file)
        self.save = Button(self, text='Save', command=self.save_file)
        self.ask_dir = Button(self, text='Folder', command=self.ask_folder)
        self.exit = Button(self, text='Exit', command=self.quit)
 
        for b in (self.open, self.save, self.ask_dir, self.exit):
            b.pack(side=LEFT, fill=BOTH)
 
        self.pack()
 
 
    def open_file(self):
        file = askopenfilename(filetypes=(("Python files", "*.py"),
                                           ("All files", "*.*")),
                               title='Open File',
                               initialdir=str(Path.home()))
        if file:
            print(file)
        else:
            print('Cancelled')
 
    def save_file(self):
        file = asksaveasfile(filetypes=(("Python files", "*.py"),
                                           ("All files", "*.*")),
                               title='Save File',
                               initialdir=str(Path.home()))
        if file:
            print(file)
        else:
            print('Cancelled')
 
    def ask_folder(self):
        folder = askdirectory(title='Pick a folder', initialdir=str(Path.home()))
 
        if folder:
            print(folder)
        else:
            print('Cancelled')
 
 
if __name__ == '__main__':
    win = Window(Tk())
    win.mainloop()