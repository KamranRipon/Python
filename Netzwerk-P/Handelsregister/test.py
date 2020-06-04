from bs4 import BeautifulSoup as BS
from selenium import webdriver
import requests
import pandas as pd
from fake_useragent import UserAgent
import datetime
import numpy as np

df = pd.read_excel('Final_Table.xlsx')

ua = UserAgent()
headers = {'User-Agent':str(ua.chrome)}

# Website Links
url_1 = 'https://www.google.com/search?q='
url_2 = 'https://www.firmenwissen.de/index.html'
url_3 = 'https://www.northdata.de/'

#search keyword
keyword = 'site:www.unternehmen24.info/Firmeninformationen/ '

driver = webdriver.Chrome('chromedriver_win32/chromedriver')
driver.get(url_1)

companyAddressList = []
companyTelefonList = []
registrationDateList = []

companyInformation = []

for company in df.Beschreibung:
    try:
        inputElement = driver.find_element_by_name("q")
        inputElement.clear()
        inputElement.send_keys(keyword+company)
        inputElement.submit()
        
        results = driver.find_elements_by_css_selector('div.bkWMgd')
        link = results[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")
        driver.get(href)
        
        #companyInfo = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]').text
        response = requests.get(href)
        soup = BS(response.content, 'html.parser')
        companyInfo = soup.find('div', class_='medium-8 columns').text.strip()
#        companyInfo = driver.find_element_by_css_selector('.medium-8.columns')
        
        regNumber = df.loc[df[df.Beschreibung == company].index.item(), 'Firma/Name'].split()[-2:]
        regNumber = regNumber[0] + ' ' + regNumber[1]

        try:
            ''' Try to Remove quote '''
            if regNumber in companyInfo:
                
                
#                companyAddress = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[3]').text
                companyAddress = soup.find('td', class_ = "infotbltd3 lh140").text.strip()
                companyAddressList.append(companyAddress)
                print(companyAddress)
                print()
                
#                try:                
#                    companyTelefon = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[3]').text
#                    companyTelefonList.append(companyTelefon)
#                    print('Telefon: ',companyTelefon)
#                    print()
#                    
#                except:
#                    companyTelefonList.append(np.nan)
                
                try: # if date not found
                    regtrationDate = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]').text
                
                except:
                    regtrationDate = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]').text
                    registrationDateList.append(regtrationDate)
                    print('Registration Data:', regtrationDate)
                    print()
                
            else:
                print('Registration Number Not in the page')

            driver.get(url_1)
                ##############################
            
        except:
            pass
        
        driver.get(url_1)

# first try and except
    except:
        pass