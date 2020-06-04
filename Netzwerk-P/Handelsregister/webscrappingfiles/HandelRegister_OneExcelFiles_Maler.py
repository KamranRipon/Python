from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
from datetime import datetime

url = "https://www.handelsregister.de/rp_web/mask.do?Typ=e"

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

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}


results_df = pd.DataFrame()
with requests.Session() as s:
    html = s.post(url, data=payloads, headers=headers)
    jsesID = s.cookies.items()[0][1]
    
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,en-GB;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'language=en; JSESSIONID=' + jsesID,
    'Host': 'www.handelsregister.de',
    'Upgrade-Insecure-Requests': '1'}
    
    for page in range(1,101):    
        try:
            request_url = 'https://www.handelsregister.de/rp_web/result.do?Page=%s' %page
        
            html2 = s.get(request_url, headers=headers)
            tables = pd.read_html(html2.text)
            table = tables[1]
            
            if page != 1:
                if table.equals(prev_table) == True:
                    print ('No more pages')
                    break
            
            prev_table = table.copy()
            results_df = results_df.append(table)
            print ('Proccessed page %s' %page)
        except:
            print ('No more pages')
            break
        
results_df = results_df.reset_index(drop=True)
results_df.to_excel('Table_from_Web_Maler.xlsx', index=False, header=False)