import tkinter as tk
from tkinter import filedialog
import threading as td
import queue as Q
from time import sleep
import random
from ptpython import *
from tkinter import ttk
#import urllib.request
from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import requests
import re 
import pandas as pd
import os


webAddress = {
	'WebSite 1': 'https://www.google.com/search?q=',
	'WebSite 2': 'https://www.firmenwissen.de/index.html'
}

Com_address1 = []

error = []
n = 0

class Thread_0(td.Thread):

	def __init__(self):
		td.Thread.__init__(self)


	def run(self):
		df = pd.read_excel(hmi.entry_1.get())
		#print(df.head())
		df.dropna(axis=0, inplace=True)
		# print(df.head())
		self.ua = UserAgent()
		url = webAddress[hmi.combo_1.get()]
		url2 = webAddress[hmi.combo_2.get()]
		headers = {'User-Agent':str(self.ua.chrome)}
		#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
		self.driver = webdriver.Chrome('C:/Users/Prisma/Documents/Netzwerk-P/chromedriver_win32/chromedriver')
		self.driver.get(url)
		for company in df.Beschreibung_2:
			global n
			print(n)
			n = n + 1
			inputElement = self.driver.find_element_by_name("q")
			inputElement.clear()
			inputElement.send_keys(company)
			inputElement.submit()
			response = requests.get(url+company)
			soup = BS(response.content, 'html.parser')
			if soup.find('span', class_= 'A1t5ne') == None:
				if "\"" in company:
					quoted = re.compile('"[^"]*"')
					for value in quoted.findall(company):
						inputElement = self.driver.find_element_by_name("q")
						inputElement.clear()
						inputElement.send_keys(value)
						inputElement.submit()
						response = requests.get(url+value)
						soup = BS(response.content, 'html.parser')
						if soup.find('span', class_= 'A1t5ne') == None:
							self.driver.get(url2)
							inputElement = self.driver.find_element_by_id("searchPhrase0")
							inputElement.clear()
							inputElement.send_keys(company)
							inputElement.submit()
							soup = BS(self.driver.page_source, 'html.parser')
							link = soup.find('span',{'class':'company--name'})
							a_link = link.find('a')['href']
							item = 'https://www.firmenwissen.de' + a_link + '?showEmail=true'
							response = requests.get('https://www.firmenwissen.de' + a_link + '?showEmail=true', headers=headers)

							alpha_soup = BS(response.text, 'html.parser')

							try:
								phone = alpha_soup.find('span', {'class':'yp_phoneNumber'}).text.strip()

							except:
								phone = ''
							try:
								email = alpha_soup.find('span', {'class':'yp_email'}).text.strip()

							except:
								email = ''

							try:
								website = alpha_soup.find('span', {'class':'yp_website'}).text.strip()

							except:
								webiste = ''

							try:
								self.driver.get(item)
								str_addr = self.driver.find_element_by_css_selector('.yp_address')

							except:
								print ('Could not locate %s company info' %(company))
								error.append(company)
							add_str1 = '{} {} {} {}'.format(str_addr.text.strip(), phone, email, website)
							hmi.thread_0_update(company+'\n'+add_str1+'\n')
							sleep(random.random()/100)
							Com_address1.append(add_str1)
							#print(add_str1)
							#print()
							#received_html = add_str1
							self.driver.get(url)

							if n >= len(df.Beschreibung_2):
								Address = pd.DataFrame(Com_address1)
								df['address'] = Address
								df.to_excel('Final_Table'+str(n)+'.xlsx', index=False, header=False)
							if n > 80:
								Address = pd.DataFrame(Com_address1)
								#df['address'] = Address
								Address.to_excel('Final_Table.xlsx', index=False, header=False)

						else:
							add_str = soup.find('span', class_= 'A1t5ne').text.strip()
							hmi.thread_0_update(company+'\n'+add_str+'\n')
							sleep(random.random()/100)
							Com_address1.append(add_str)
							#print(add_str)
							#print()
							#received_html = add_str

							if n >= len(df.Beschreibung_2):
								Address = pd.DataFrame(Com_address1)
								df['address'] = Address
								df.to_excel('Final_Table'+str(n)+'.xlsx', index=False, header=False)

							if n > 80:
								Address = pd.DataFrame(Com_address1)
								#df['address'] = Address
								Address.to_excel('Final_Table.xlsx', index=False, header=False)

				else:
					self.driver.get(url2)
					inputElement = self.driver.find_element_by_id("searchPhrase0")
					inputElement.clear()
					inputElement.send_keys(company)
					inputElement.submit()

					soup = BS(self.driver.page_source, 'html.parser')

					link = soup.find('span',{'class':'company--name'})

					a_link = link.find('a')['href']
					item = 'https://www.firmenwissen.de' + a_link + '?showEmail=true'

					response = requests.get('https://www.firmenwissen.de' + a_link + '?showEmail=true', headers=headers)
					alpha_soup = BS(response.text, 'html.parser')

					try:
						phone = alpha_soup.find('span', {'class':'yp_phoneNumber'}).text.strip()
					except:
						phone = ''

					try:
						email = alpha_soup.find('span', {'class':'yp_email'}).text.strip()
					except:
						email = ''
					try:
						website = alpha_soup.find('span', {'class':'yp_website'}).text.strip()
					except:
						webiste = ''

					try:
						self.driver.get(item)
						str_addr = self.driver.find_element_by_css_selector('.yp_address')
					except:
						print ('Could not locate %s company info' %(company))
						error.append(company)

					add_str1 = '{} {} {} {}'.format(str_addr.text.strip(), phone, email, website)
					hmi.thread_0_update(company+'\n'+add_str1+'\n\n')
					sleep(random.random()/100)
					Com_address1.append(add_str1)
					#received_html = add_str1
					#text.insert(tk.END, received_html)
					print(add_str1)
					print()
					self.driver.get(url)

					if n >= len(df.Beschreibung_2):
						Address = pd.DataFrame(Com_address1)
						df['address'] = Address
						df.to_excel('Final_Table'+str(n)+'.xlsx', index=False, header=False)

					if n > 80:
						Address = pd.DataFrame(Com_address1)
						#df['address'] = Address
						Address.to_excel('Final_Table.xlsx', index=False, header=False)

			else:
				add_str = soup.find('span', class_= 'A1t5ne').text.strip()
				hmi.thread_0_update(company+'\n'+add_str+'\n\n')
				sleep(random.random()/100)
				Com_address1.append(add_str)
				#print(add_str)
				#print()
				#received_html = add_str

				if n >= len(df.Beschreibung_2):
					Address = pd.DataFrame(Com_address1)
					df['address'] = Address
					df.to_excel('Final_Table'+str(n)+'.xlsx', index=False, header=False)

				if n > 80:
					Address = pd.DataFrame(Com_address1)
					#df['address'] = Address
					Address.to_excel('Final_Table.xlsx', index=False, header=False)

		#n = 0
		#hmi.thread_0_update(Com_address1[0])
		#sleep(random.random()/100)

		
		self.driver.quit()
        #self.driver.quit()
		
		#n = 0
		#while True:
			#for x in companylist:
				#count += 1
				#hmi.thread_0_update(Com_address1[0])
				#sleep(random.random()/100)
	    #self.driver.quit()

class HMI:
	
	def __init__(self):

		self.master = tk.Tk()
		self.master.geometry('500x320+50+50')
		self.master.title('GUI for Address Collection')

		self.label_1 = tk.Label(self.master, text= "Website 1", font =('Times New Roman', 14))
		self.label_1.grid(row=1, column=1, padx =10, pady=5, sticky='ne')

		self.combo_1 = ttk.Combobox(self.master, width=15, values = ["WebSite 1"], font=('Times New Roman', 12))
		self.combo_1.grid(row=1, column=2, padx = 10, pady=5, sticky='nw')

		self.label_2 = tk.Label(self.master, text= "Website 2", font =('Times New Roman', 14))
		self.label_2.grid(row=2, column=1, padx =10, pady=5, sticky='ne')

		self.combo_2 = ttk.Combobox(self.master, width=15, values = ["WebSite 2"], font=('Times New Roman', 12))
		self.combo_2.grid(row=2, column=2, padx = 10, pady=10, sticky='nw')


		self.label_3 = tk.Label(self.master, text= "Select file", font =('Times New Roman', 14))
		self.label_3.grid(row=3, column=1, padx =10, pady=5, sticky='ne')

		self.entry_1 = tk.StringVar()

		self.entry_1 = ttk.Entry(self.master, width=15)
		self.entry_1.grid(row=3, column=2, padx=10,pady=10, sticky='ew')

		self.button_1 = ttk.Button(self.master, text='Path', command = self.open_file)
		self.button_1.grid(row=3, column=3, padx=5, pady=5)

		self.label_4 = tk.Label(self.master, text= "Save as", font =('Times New Roman', 14))
		self.label_4.grid(row=4, column=1, padx =10, pady=5, sticky='ne')

		self.entry_2 = tk.StringVar()

		self.entry_2 = ttk.Entry(self.master, width=15)
		self.entry_2.grid(row=4, column=2, padx=10,pady=10, sticky='ew')

		#self.dirname = filedialog.askdirectory(parent=self.master, initialdir="/", title='Please select a path')
		#os.chdir(self.dirname)

		self.button_2 = ttk.Button(self.master, text='Path', command=self.select_folder)
		self.button_2.grid(row=4, column=3, padx=5, pady=5)

		self.label_5 = tk.Label(self.master, text= "Address", font =('Times New Roman', 14))
		self.label_5.grid(row=5, column=1, padx =10, pady=10, sticky='ne')

		self.text_1 = tk.Text(self.master, height=5, width=10)
		self.text_1.grid(row=5, column=2, padx = 10, pady=10, sticky='e'+'w'+'n'+'s', columnspan=5)
		#self.text_1.grid(row=4, column=2, padx = 10, pady=10, sticky='ew', columnspan=15)

		#self.scroll_1 = ttk.Scrollbar(self.text_1, orient ='vertical', command=self.text_1.yview)
		#self.scroll_1.grid(row=3,column=15, sticky='nw')
		#self.scroll_1.grid(row=3, column=15, sticky='ns')

		n = 3
		self.label = ttk.Label(self.text_1)
		self.label.grid(row=3, column=2, padx=10,pady=5, columnspan=5)
		n += 1

		##########################################
		#self.label_3 = tk.Label(self.master, text= " ", font =('Times New Roman', 14))
		#self.label_3.grid(row=4, column=1, padx =10, pady=5, sticky='ne')
		##########################################

		self.button_3 = ttk.Button(self.master, text='Go', command = t0.start)
		self.button_3.grid(row=10, column=2, padx=5, pady=5, sticky='w')

		self.button_4 = ttk.Button(self.master, text='Exit',command = self.master.destroy)
		self.button_4.grid(row=10, column=3, padx=5, pady=5)

		#self.text_1.config(yscrollcommand=self.scroll_1.set)
		#self.text_1.config(xscrollcommand=self.scroll_1.set)

		self.q = Q.Queue()

		self.master.bind("<<Thread_0_Label_Update>>", self.thread_0_update_e)

	def open_file(self):
		self.open_dirname = filedialog.askopenfilename(filetypes = (('Excel files','*.xlsx'),("All files", "*.*")), initialdir="/", title='Open file')
		if self.open_dirname:
			self.entry_1.delete(0,'end')
			#os.chdir(self.open_dirname)
			self.entry_1.insert(tk.END, self.open_dirname)

	def select_folder(self):
		self.dirname = filedialog.askdirectory(parent=self.master, initialdir="/", title='Please select a path')
		if self.dirname:
			self.entry_2.delete(0,'end')
			os.chdir(self.dirname)
			self.entry_2.insert(tk.END, self.dirname)


	def start(self):
		self.master.mainloop()
		self.master.destroy()
		

	def thread_0_update(self, val):
		self.q.put(val)
		self.master.event_generate("<<Thread_0_Label_Update>>", when='tail')
		

	def thread_0_update_e(self, e):
		while self.q.qsize():
			try:
				val = self.q.get()
				self.label.config(text = str(val), font =('Times New Roman', 13))
				#self.label.config(text=self.label.cget("text")+ str(val), font =('Times New Roman', 12))
			except Q.Empty:
				pass


if __name__ == '__main__':
    t0 = Thread_0()
    hmi = HMI()
    #hmi.path()
    hmi.start()