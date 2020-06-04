from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver

d = webdriver.Chrome('C:/Users/Prisma/Documents/Netzwerk-P/chromedriver_win32/chromedriver')

companyList = ['aktive Stuttgarter',"BiH e.K. Betriebsvermittlung im Handwerk" ,'ARTA Management für das Handwerk GmbH + Co.',  
'ABEX Dachdecker Handwerks-GmbH', 'Academie für Kunst und Handwerk e.V.', 
'AHA Agentur fürs Handwerk GmbH']



url = 'https://www.firmenwissen.de/ergebnis.html'
baseUrl = 'https://www.firmenwissen.de'
headers = {'User-Agent': 'Mozilla/5.0'}

finalLinks = []
finalLinks2 = []

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
#    info  = d.find_element_by_css_selector('.yp_abstract_narrow')
    print()
    address =  d.find_element_by_css_selector('.yp_address')
    print(address.text)
#    print(info.text, address.text)

d.quit()