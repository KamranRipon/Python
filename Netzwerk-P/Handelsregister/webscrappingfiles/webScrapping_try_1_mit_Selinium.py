from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
from datetime import datetime
from selenium import webdriver
from fake_useragent import UserAgent
from ptpython import *

payloads = {
'suchTyp': 'e',
'registerArt': '',
'registerNummer': '',
'bundeslandBW': 'on',
'registergericht': '',
'schlagwoerter': 'Maler',
'schlagwortOptionen': '2',
'niederlassung': '',
'rechtsform': '',
'postleitzahl': '',
'ort': '',
'strasse': '',
'ergebnisseProSeite': '100',
'btnSuche': 'Suchen'}



ua = UserAgent()
headers = {'User-Agent': str(ua.chrome)}
url = 'https://www.handelsregister.de/rp_web/'
url1 = 'https://www.handelsregister.de/rp_web/mask.do?Typ=e'

driver = webdriver.Chrome('chromedriver_win32/chromedriver')

driver.get(url1)

bundeslander = driver.find_element_by_id('landBW').click()
keyword = driver.find_element_by_name('schlagwoerter')
keyword.clear()
keyword.send_keys('Maler')
seite = driver.find_element_by_name('ergebnisseProSeite')
seite.find_element_by_xpath('//*[@id="suchparameterForm"]/table/tbody/tr[22]/td[2]/select/option[4]').click()
find = driver.find_element_by_name('btnSuche').click()

#url3 = url + 'result.do?Page=2'
#html = requests.post(url1, data=payloads, headers=headers)
#tables = pd.read_html(html.text)
##table = pd.DataFrame(tables)
#tables.to_excel('xxxx.xlsx', index=False, header=False)
table = driver.find_element_by_class_name('RegPortErg')
tables = pd.read_html(table)
#driver.quit()