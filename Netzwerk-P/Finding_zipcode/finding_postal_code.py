#import pgeocode as pg
#
#de_zip = pg.GeoDistance('de')
#zip_code_DB = [70180, 75305, 89077, 40223, 10559, 52477, 76229, 79104, 70195]
#
#all_zip = []
#
#def find_zipcode(current, dist):
#    for x in zip_code_DB:
#        cal_dist = de_zip.query_postal_code(current, x)
#        
#        if cal_dist < dist + 10:
#            all_zip.append(x)
#    return all_zip 
#
#print(find_zipcode(78054, 50))
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
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
headers = {'User-Agent':str(ua.chrome)}
driver = webdriver.Chrome('C:/Users/Prisma/Documents/Netzwerk-P/chromedriver_win32/chromedriver')
driver.get(url)

companylist = ['ARTA Management für das Handwerk GmbH + Co.', "aktive Stuttgarter", 'ABEX Dachdecker Handwerks-GmbH',
'Academie für Kunst und Handwerk e.V.', 'AHA Agentur fürs Handwerk GmbH']

com_list = ["Arbeitskreis  Unternehmerfrauen im Handwerk Böblingen-Leonberg e. V."]

#for url in search(com, tld='de', lang='de', stop=10):
#    print(url)

Com_address1 = []
Com_address2 = []
count = 0
error = []
#df.Beschreibung_2
'''
for x in df.Beschreibung_2:    
    if "\"" in x:
        print(x)
    else:
        print(False)
'''

for company in df.Beschreibung_2:
#    company = company
    inputElement = driver.find_element_by_name("q")
    inputElement.clear()
    inputElement.send_keys(company)
    inputElement.submit()
    response = requests.get(url+company)
    soup = BS(response.content, 'html.parser')
#    if soup.find('span', class_= 'A1t5ne') != None:
#        count += 1
#        print(count)
#    soup = BS(response.text, 'html.parser')
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
                #    print()
                #    print(add_str1)
                #    print()
            #        print('Com_address1 %s' %len(Com_address1))
            #        print(company, add_str1)
                    driver.get(url)
                    
                else:
                    add_str = soup.find('span', class_= 'A1t5ne').text.strip()
    #               print(add_str)
                    Com_address2.append(add_str)
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
        #    print()
        #    print(add_str1)
        #    print()
    #        print('Com_address1 %s' %len(Com_address1))
    #        print(company, add_str1)
            driver.get(url)
                    
        
#    elif soup.find('span', class_= 'A1t5ne') == None:
#        
#        driver.get(url2)
#        inputElement = driver.find_element_by_id("searchPhrase0")
#        inputElement.clear()
#        inputElement.send_keys(company)
#        inputElement.submit()
#    
#        soup = BS(driver.page_source, 'html.parser')
#    
#        link = soup.find('span',{'class':'company--name'})
#        a_link = link.find('a')['href']
#        item = 'https://www.firmenwissen.de' + a_link + '?showEmail=true'
#    
#        response = requests.get('https://www.firmenwissen.de' + a_link + '?showEmail=true', headers=headers)
#        alpha_soup = BS(response.text, 'html.parser')
#    
#    
#        try:
#            phone = alpha_soup.find('span', {'class':'yp_phoneNumber'}).text.strip()
#        except:
#            phone = ''
#    
#        try:
#            email = alpha_soup.find('span', {'class':'yp_email'}).text.strip()
#        except:
#            email = ''
#    
#        try:
#            website = alpha_soup.find('span', {'class':'yp_website'}).text.strip()
#        except:
#            webiste = ''
#    
#        try:
#    #        contact = soup.find('div', {'class':'company--info'})
#    #        address = contact.find_all('p')[-1].text.strip()
#            driver.get(item)
#            str_addr = driver.find_element_by_css_selector('.yp_address')
#    #        print(str_addr.text)
#        except:
#            print ('Could not locate %s company info' %(company))
#            error.append(company)
#        
#        add_str1 = '{} {} {} {}'.format(str_addr.text.strip(), phone, email, website)
#        Com_address2.append(add_str1)
#    #    print()
#    #    print(add_str1)
#    #    print()
##        print('Com_address1 %s' %len(Com_address1))
##        print(company, add_str1)
#        driver.get(url)
    
        
    else:
        add_str = soup.find('span', class_= 'A1t5ne').text.strip()
#        print(add_str)
        Com_address2.append(add_str)
#        print(company,'\n{}'.format(soup.find('span', class_= 'A1t5ne').text),'\n')
#        count += 1
#        print(count)
   
driver.quit()
#response = requests.get(url)

#soup = BS(response.text, 'html.parser')