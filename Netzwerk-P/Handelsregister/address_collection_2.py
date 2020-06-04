from ptpython import *
from fake_useragent import UserAgent
from selenium import webdriver
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd

df = pd.read_excel('Final_Table.xlsx')

url_1 = 'https://www.google.com/search?q='
url_2 = 'https://www.firmenwissen.de/index.html'

ua = UserAgent()
headers = {'User-Agent':str(ua.chrome)}

Com_address1 = []

com_list = ['Maler Jäggle GmbH']
keyword = 'site:www.unternehmen24.info/Firmeninformationen/'

driver = webdriver.Chrome('chromedriver_win32/chromedriver')
driver.get(url_1)

for company in :
	inputElement = driver.find_element_by_name("q")
	inputElement.clear()
	inputElement.send_keys(keyword+company)
	inputElement.submit()
	
	try:
        results = driver.find_elements_by_css_selector('div.TbwUpd')
        link = results[0].find_element_by_tag_name("a")
        href = link.get_attribute("href")
        driver.get(href)
        companyInfor = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]').text
        companyIndex = df.Beschreibung[df.Beschreibung==company].index.tolist()
        regNumber = df.loc[companyIndex[0], 'Firma/Name'].split()[-2:]
        regNumber = regNumber[0] + ' ' + regNumber[1]
        
        if regNumber in companyInfor:
            address = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[3]').text
            print(address)
            driver.get(url_1)
        
        else:
            driver.get(url_2)
            

    except:
        
        driver.get(url_2)