from ptpython import *
from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd

#df = pd.read_excel('')

url_1 = 'https://www.google.com/search?q='
url_2 = 'https://www.firmenwissen.de/index.html'


Com_address1 = []

error = []
n = 0

ua = UserAgent()

headers = {'User-Agent':str(ua.chrome)}

driver = webdriver.Chrome('chromedriver_win32/chromedriver')
driver.get(url)
for company in df.Beschreibung_2:

			inputElement = driver.find_element_by_name("q")
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
