import tkinter as tk
from requests import get
#import urllib.request
from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import requests
#from googlesearch import search
#from googleapiclient.discovery import build
import re 
import pandas as pd
import tkinter.ttk as k
#import ttk

df = pd.read_excel('../Table3_.xlsx')
df.dropna(axis=0, inplace=True)
ur1 = 'https://www.google.com/search?q='
ur2 ='https://www.firmenwissen.de/index.html'
companylist = ['ARTA Management für das Handwerk GmbH + Co.']

Com_address1 = []
Com_address2 = []
count = 0
error = []

def go():
    text.delete(1.0, tk.END)
    url = entry1.get()
    url2 = entry2.get()
    ua = UserAgent()
    headers = {'User-Agent':str(ua.chrome)}
    driver = webdriver.Chrome('C:/Users/Prisma/Documents/Netzwerk-P/chromedriver_win32/chromedriver')
    driver.get(url)
    for n, company in enumerate(df.Beschreibung_2):
#        print('compay NO', n)
#        text_1.config(text = 'compay NO'+ str(n))
#        text_1.update()
#        brows_window.after(10, lambda:go(text_1))
#        text.insert(tk.END, n)
#        text.pack()
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
                    inputElement = driver.find_element_by_name("q")
                    inputElement.clear()
                    inputElement.send_keys(value)
                    inputElement.submit()
                    response = requests.get(url+value)
                    soup = BS(response.content, 'html.parser')
                    if soup.find('span', class_= 'A1t5ne') == None:
                        driver.get(url2)
                        inputElement = driver.find_element_by_id("searchPhrase0")
                        inputElement.clear()
                        inputElement.send_keys(company)
                        inputElement.submit()
                        soup = BS(driver.page_source, 'html.parser')
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
                            driver.get(item)
                            str_addr = driver.find_element_by_css_selector('.yp_address')
                        except:
                            print ('Could not locate %s company info' %(company))
                            error.append(company)
            
                        add_str1 = '{} {} {} {}'.format(str_addr.text.strip(), phone, email, website)
                        Com_address2.append(add_str1)
                        print(add_str1)
                        print()
                        received_html = add_str1
#                        text.insert(1.0, received_html)
                        #text.insert(tk.END, received_html)
                        driver.get(url)
                    else:
                        add_str = soup.find('span', class_= 'A1t5ne').text.strip()
                        Com_address2.append(add_str)
                        print(add_str)
                        print()
                        received_html = add_str
#                        text.insert(1.0, received_html)
                        text.insert(tk.END, received_html)
            else:
                driver.get(url2)
                inputElement = driver.find_element_by_id("searchPhrase0")
                inputElement.clear()
                inputElement.send_keys(company)
                inputElement.submit()
        
                soup = BS(driver.page_source, 'html.parser')
        
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
        #        contact = soup.find('div', {'class':'company--info'})
        #        address = contact.find_all('p')[-1].text.strip()
                    driver.get(item)
                    str_addr = driver.find_element_by_css_selector('.yp_address')
        #        print(str_addr.text)
                except:
                    print ('Could not locate %s company info' %(company))
                    error.append(company)
            
                add_str1 = '{} {} {} {}'.format(str_addr.text.strip(), phone, email, website)
                Com_address2.append(add_str1)
                received_html = add_str1
#                text.insert(1.0, received_html)
                text.insert(tk.END, received_html)
                print(add_str1)
                print()
                driver.get(url)
                    
        
        else:
            add_str = soup.find('span', class_= 'A1t5ne').text.strip()
#                print(add_str)
            Com_address2.append(add_str)
            print(add_str)
            print()
            received_html = add_str
#            text.insert(1.0, received_html)
#            text.insert(END, received_html)
            text.insert(tk.END, received_html)
   
    driver.quit()
    

brows_window = tk.Tk()
#brows_window.geometry('600x350')
brows_window.title('Test GUI')
label1 = tk.Label(brows_window, text = 'Enter Url 1').grid(row=1,sticky = tk.W)
label2 = tk.Label(brows_window, text = 'Enter Url 2').grid(row=2, sticky = tk.W)
entry1 = tk.Entry(brows_window)
entry2 = tk.Entry(brows_window)
button = tk.Button(brows_window, text='Go', command = go)
#entry = Entry(brows_window)
entry1.insert(tk.END, ur1)
entry2.insert(tk.END, ur2)

text = tk.Text(brows_window)
#label.grid(column = 0,row=0)
#entry.pack(side=RIGHT)
button.grid(column=0, row=3)
text.grid(column=0, row=5)
entry1.grid(row=0, column = 0)
entry2.grid(row=1, column = 0)



#driver.quit()
brows_window.mainloop()