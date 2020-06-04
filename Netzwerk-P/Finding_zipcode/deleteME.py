from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import requests
from googlesearch import search
from googleapiclient.discovery import build
import re 
import pandas as pd


df = pd.read_excel('Table3_.xlsx')
df.dropna(axis=0, inplace=True)

ua = UserAgent()

url = 'https://www.google.com/search?q='
url2 ='https://www.firmenwissen.de/index.html'

headers = {'User-Agent':str(ua.chrome)}
driver = webdriver.Chrome('C:/Users/Prisma/Documents/Netzwerk-P/chromedriver_win32/chromedriver')
driver.get(url)

Com_address1 = []

error = []

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
                    Com_address1.append(add_str1)
                    driver.get(url)
                    
                else:
                    add_str = soup.find('span', class_= 'A1t5ne').text.strip()
                    Com_address1.append(add_str)
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
                driver.get(item)
                str_addr = driver.find_element_by_css_selector('.yp_address')
            except:
                print ('Could not locate %s company info' %(company))
                error.append(company)
            
            add_str1 = '{} {} {} {}'.format(str_addr.text.strip(), phone, email, website)
            Com_address1.append(add_str1)
            driver.get(url)
    
        
    else:
        add_str = soup.find('span', class_= 'A1t5ne').text.strip()
        Com_address1.append(add_str)
   
driver.quit()