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
        
        
        
        companyInfo = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]').text
        #companyInfo = driver.find_element_by_css_selector('div.full-width').text
        
        regNumber = df.loc[df[df.Beschreibung == company].index.item(), 'Firma/Name'].split()[-2:]
        regNumber = regNumber[0] + ' ' + regNumber[1]

        try:
            ''' Try to Remove quote '''
            if regNumber in companyInfo:
                
                companyAddress = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[3]').text
                companyAddressList.append(companyAddress)
                print(companyAddress)
                print()
                
                try:                
                    companyTelefon = driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[3]').text
                    companyTelefonList.append(companyTelefon)
                    print('Telefon: ',companyTelefon)
                    print()
                    
                except:
                    companyTelefonList.append(np.nan)
                
                try: # if date not found
                    regtrationDate = driver.find_element_by_xpath('/html/body/div[7]/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[1]').text
                    registrationDateList.append(regtrationDate)
                    print('Registration Data:',regtrationDate)
                    print()
                except:
                    registrationDateList.append(np.nan)
                
            else:
                driver.get(url_2)
                
                inputElement = driver.find_element_by_id("searchPhrase0")
                inputElement.clear()
                inputElement.send_keys(company)
                inputElement.submit()
                
                soup = BS(driver.page_source, 'html.parser')
                content_del = requests.get(url_2+company)
                soup_del = BS(content_del.content, 'html.parser')
                link = soup.find('span',{'class':'company--name'})
                a_link = link.find('a')['href']
                item = 'https://www.firmenwissen.de' + a_link + '?showEmail=true'
                
                driver.get(item)
                
                try:
                    companyInfo = driver.find_element_by_xpath('//*[@id="Firmenauskunft"]/div[3]/div[1]/div').text
                    
                    regNumber = df.loc[df[df.Beschreibung == company].index.item(), 'Firma/Name'].split()[-2:]
                    regNumber = regNumber[0] + ' ' + regNumber[1]
                    
                    '''Try to Remove quote '''
                    if regNumber in companyInfo:
                        companyAddress = driver.find_element_by_css_selector('div.yp_address').text
                        companyAddressList.append(companyAddress)
                        print(companyAddress)
                        print()

                        allCompanyInfo = companyInfo.split()
                        
                        for x in allCompanyInfo:
                            try:
                                regdate = datetime.datetime.strptime(x, '%d.%m.%Y')
                                
                                regtrationDate = str(regdate.day) + '.'+str(regdate.month)+'.'+ str(regdate.year)
                                registrationDateList.append(regtrationDate)
                                print('Registration Data:',regtrationDate)
                                print()
                                
                            except:
                                #registrationDateList.append(np.nan)
                                pass
                            
                        try:
                            companyTelefon = driver.find_element_by_css_selector('.yp_phoneNumber').text
                            companyTelefonList.append(companyTelefon)
                            print('Telefon: ',companyTelefon)
                            print()
                        except:
                            companyTelefonList.append(np.nan)
                    else:
                        companyAddressList.append(np.nan)
                        registrationDateList.append(np.nan)
                        companyTelefonList.append(np.nan)
                        print('Information Not found for:')
                        print(company)

                except:
                    pass

            driver.get(url_1)
                ##############################
            
        except:
            pass
        
        driver.get(url_1)

# first try and except
    except:
        driver.get(url_2)
        
        inputElement = driver.find_element_by_id("searchPhrase0")
        inputElement.clear()
        inputElement.send_keys(company)
        inputElement.submit()
        
        soup = BS(driver.page_source, 'html.parser')
        content_del = requests.get(url_2+company)
        soup_del = BS(content_del.content, 'html.parser')
        link = soup.find('span',{'class':'company--name'})
        a_link = link.find('a')['href']
        item = 'https://www.firmenwissen.de' + a_link + '?showEmail=true'
        
        driver.get(item)
        
        try:
            companyInfo = driver.find_element_by_xpath('//*[@id="Firmenauskunft"]/div[3]/div[1]/div').text
            
            regNumber = df.loc[df[df.Beschreibung == company].index.item(), 'Firma/Name'].split()[-2:]
            regNumber = regNumber[0] + ' ' + regNumber[1]
            
            '''Try to Remove quote '''
            if regNumber in companyInfo:
                companyAddress = driver.find_element_by_css_selector('div.yp_address').text
                companyAddressList.append(companyAddress)
                print(companyAddress)
                print()
                
                allCompanyInfo = companyInfo.split()
                
                for x in allCompanyInfo:
                    try:
                        regdate = datetime.datetime.strptime(x, '%d.%m.%Y')
                        regtrationDate = str(regdate.day) + '.'+str(regdate.month)+'.'+ str(regdate.year)
                        registrationDateList.append(regtrationDate)
                        print('Regtration Date: ',regtrationDate)
                        print()
                    except:
                        pass
                
                try:
                    companyTelefon = driver.find_element_by_css_selector('.yp_phoneNumber').text
                    companyTelefonList.append(companyTelefon)
                    print('Telefone: ',companyTelefon)
                    print()

                except:
                    companyTelefonList.append(np.nan)

            else:
                companyAddressList.append(np.nan)
                registrationDateList.append(np.nan)
                companyTelefonList.append(np.nan)

                print('Information Not found for:')
                print(company)
                print()     

        except:
            pass
        
        driver.get(url_1)

driver.quit()

#d = {'Addfress': companyAddressList, 'Telefone': companyTelefonList, 'Date of Registration': registrationDateList}
#df = pd.concat([pd.Series(v, name=k) for k, v in d.items()], axis=1)
#print(df)


#df.style.apply(lambda x: ["background: red" if x not in df.date2 else "" for x in df.A], axis = 1)