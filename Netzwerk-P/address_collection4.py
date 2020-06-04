from bs4 import BeautifulSoup as BS
from selenium import webdriver

url = 'https://www.firmenwissen.de/index.html'

driver = webdriver.Chrome('C:/Users/Prisma/Documents/Netzwerk-P/chromedriver_win32/chromedriver')
driver.get(url)

companylist = ['ARTA Management für das Handwerk GmbH + Co.',   "aktive Stuttgarter", 'ABEX Dachdecker Handwerks-GmbH',
'Academie für Kunst und Handwerk e.V.', 'AHA Agentur fürs Handwerk GmbH']

error = []
for company in companylist:
    inputElement = driver.find_element_by_id("searchPhrase0")
    inputElement.clear()
    inputElement.send_keys(company)
    inputElement.submit() 

    soup = BS(driver.page_source, 'html.parser')

    try:
        contact = soup.find('div', {'class':'company--info'})
        address = contact.find_all('p')[-1].text.strip()
    except:
        print ('Could not locate %s company info' %(company))
        error.append(company)

    print(address)

driver.quit()