from bs4 import BeautifulSoup as BS
from selenium import webdriver
import requests
import pandas as pd
from datetime import datetime
from fake_useragent import UserAgent

df = pd.read_excel('Final_Table_2019-04-24.xlsx')
df.dropna(axis=0, inplace=True)

ua = UserAgent()

headers = {'User-Agent':str(ua.chrome)}

url1 = 'https://www.firmenwissen.de/index.html'
url2 = 'https://www.northdata.de/'
url3 = 'https://www.google.com/search?q='


driver = webdriver.Chrome('chromedriver_win32/chromedriver')
driver.get(url1)

Com_address1 = []

Company_information = []

companylist = ['"Maler Jäggle GmbH"']

count = 0
for company in df.Beschreibung_2:
#    inputElement = driver.find_element_by_name("q")
    inputElement = driver.find_element_by_id("searchPhrase0")
    inputElement.clear()
    inputElement.send_keys(company)
    inputElement.submit()

    soup = BS(driver.page_source, 'html.parser')
    content_del = requests.get(url1+company)
    soup_del = BS(content_del.content, 'html.parser')
    link = soup.find('span',{'class':'company--name'})
    a_link = link.find('a')['href']
    item = 'https://www.firmenwissen.de' + a_link + '?showEmail=true'

    response = requests.get('https://www.firmenwissen.de' + a_link + '?showEmail=true', headers=headers)
    alpha_soup = BS(response.text, 'html.parser')

    
    try:
        driver.get(item)
#        com_info = alpha_soup.find('div', {'class': 'yp_abstract_narrow'})
        com_info = info  = driver.find_element_by_css_selector('.yp_abstract_narrow')
        com_info = com_info.text
        for registration in df['Firma/Name']:
            uni_nm = registration.split()[-2:]
            reg_num = uni_nm[0]+' '+ uni_nm[1]
            if reg_num in com_info:
                count += 1
                print(count)
                com_status = driver.find_element_by_css_selector('.yp_general_data_row')
                com_status = com_status.text.split()[:2]
                com_status = com_status[0]+com_status[1]
                print()
                print()
                print(company)
                print(com_status)
                print(reg_num)
                com_age = driver.find_element_by_xpath('//*[@id="Firmenauskunft"]/div[4]/ul[1]/li[1]/div/a')
                print(com_age.text)
                com_age = com_age.text[:2]
                com_inin = com_info.split()
                for string in com_inin:
                    try:
                        datetime.strptime(string, '%d.%m.%Y')
                        print('Last Modified:', string)
                    except:
                        pass
                    company_info = '{} {} {} {} {}'.format(company,reg_num,com_status, com_age,string)
                    Company_information.append(company_info)
    
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
#                    contact = soup.find('div', {'class':'company--info'})
#                   address = contact.find_all('p')[-1].text.strip()
                    driver.get(item)
                    str_addr = driver.find_element_by_css_selector('.yp_address')
                except:
                    print ('Could not locate %s company info' %(company))
                    error.append(company)
    
                add_str1 = '{} {} {} {}'.format(str_addr.text.strip(), phone, email, website)
                Com_address1.append(add_str1)
            
            elif:
                driver.get(url2+company)
                