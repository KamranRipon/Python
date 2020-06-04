'''
from bs4 import BeautifulSoup as BS
import requests
from googlesearch import search
from googleapiclient.discovery import build
import re


companylist = ['aktive Stuttgarter','ARTA Management für das Handwerk GmbH + Co.',  
'ABEX Dachdecker Handwerks-GmbH', 'Academie für Kunst und Handwerk e.V.', 
'AHA Agentur fürs Handwerk GmbH']


companylist = ['ABEX Dachdecker Handwerks-GmbH']

url = 'https://www.firmenwissen.de/index.html'

payloads = {
        'searchform': 'UFT-8',
        'phrase':'ABEX Dachdecker Handwerks-GmbH',
        "mainSearchField__button":'submit'
        }

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

html = requests.post(url, data=payloads, headers=headers)
soup = BS(html.content, 'html.parser')
link_list= []

links = soup.findAll('a')

for li in links:
    link_list.append(li.get('href'))
print(link_list)

#tables = pd.read_html(html.text)

'''

from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver

d = webdriver.Chrome('C:/Users/Prisma/Documents/Netzwerk-P/chromedriver_win32/chromedriver')
#companyList = ['ABEX Dachdecker Handwerks-GmbH','SUCHMEISTEREI GmbH']
companyList = ['aktive Stuttgarter']

url = 'https://www.firmenwissen.de/ergebnis.html'
baseUrl = 'https://www.firmenwissen.de'
headers = {'User-Agent': 'Mozilla/5.0'}

finalLinks = set()


## searches section; gather into set

with requests.Session() as s:
    for company in companyList:
        payloads = {
        'searchform': 'UFT-8',
        'phrase':company,
        "mainSearchField__button":'submit'
        }

        html = s.post(url, data=payloads, headers=headers)
        soup = BS(html.content, 'lxml')
        
        div = soup.find('div', class_ = 'toggleBox' )
        link_list = []
        hlink = div.findAll('a')
        for li in hlink:
            link_list.append(li.get('href'))
        companyLinks = {baseUrl + item['href'] for item in soup.select("[href*='firmeneintrag/']")}
#        companyLinks = baseUrl + soup.select_one("[href*='firmeneintrag/']")['href'] 
        # print(soup.select_one('.fp-result').text)
        finalLinks = finalLinks.union(companyLinks)

for item in finalLinks:
    d.get(item)
    info  = d.find_element_by_css_selector('.yp_white_box')
    print(info.text)

d.quit()
