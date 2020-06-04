from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
 
d = webdriver.Chrome('C:/Users/Prisma/Documents/Netzwerk-P/chromedriver_win32/chromedriver')
#companyList = ['aktive Stuttgarter','ABEX Dachdecker Handwerks-GmbH', "BIH e.K."]
companyList = ["Filz"]
 
url = 'https://www.firmenwissen.de/ergebnis.html'
baseUrl = 'https://www.firmenwissen.de'
headers = {'User-Agent': 'Mozilla/5.0'}
 
finalLinks = []
 
## searches section; add to list
 
with requests.Session() as s:
    for company in companyList:
        payloads = {
        'searchform': 'UFT-8',
        'phrase':company,
        "mainSearchField__button":'submit'
        }
 
        html = s.post(url, data=payloads, headers=headers)
        soup = BS(html.content, 'lxml')
 
        companyLinks = baseUrl + soup.select_one("[href*='firmeneintrag/']")['href']
        finalLinks.append(companyLinks)
 
for item in set(finalLinks):
    d.get(item)
    info  = d.find_element_by_css_selector('.yp_abstract_narrow')
    address =  d.find_element_by_css_selector('.yp_address')
    print(info.text, address.text)
    
d.quit()