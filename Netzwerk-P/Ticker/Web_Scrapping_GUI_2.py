import tkinter as tk
import threading as td
import queue as Q
from time import sleep
import random
from ptpython import *
from tkinter import ttk

class Thread_0(td.Thread):

	def __init__(self):
		td.Thread.__init__(self)

	def run(self):
		count = 0
		while True:
			count += 1
			hmi.thread_0_update(count)
			sleep(random.random()/100)


class HMI:
	
	def __init__(self):

		self.master = tk.Tk()
		self.master.geometry('400x400+1+1')

		#self.frame_1 = ttk.Frame(self.master,height = 100, width = 100,  relief = 'groove')
		frame_1 = tk.Frame(self.master)
		frame_1.pack()
		#self.frame_1.grid(row=1, column=1, padx=20,pady = 20)

		self.label_1 = tk.Label(frame_1)
		self.label_1.pack()
		#self.label_1.grid(row=1, column=1, padx=5,pady=5)

		self.q = Q.Queue()

		self.master.bind("<<Thread_0_Label_Update>>", self.thread_0_update_e)

	def start(self):
		self.master.mainloop()
		self.master.destroy()

	def thread_0update(self, val):
		self.q.put(val)
		self.master.event_generate("<<Thread_0_Label_Update>>", when='tail')

	def thread_0_update_e(self, e):
		while self.q.qsize():
			try:
				val = self.q.get()
				self.label_1.config(text = str(val))
			except Q.Empty:
				pass



if __name__ == '__main__':
	hmi = HMI()
	t0 = Thread_0()
	t0.start()
	hmi.start()