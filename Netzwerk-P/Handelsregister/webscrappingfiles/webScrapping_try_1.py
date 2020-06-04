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

html = requests.post(url, data=payloads, headers=headers)

soup = BS(html.content, 'html.parser')

tables = pd.read_html(html.text)

table1 = tables[1]

############################## 
'''                     Data Preparation                    '''

table1.columns = ['Firma/Name', 'Beschreibung', 'Sitz', 'Status', 'Registerinhalt']


cols = ['Beschreibung','Sitz', 'Status', 'Registerinhalt']
for col in cols:
    table1[col].fillna(method='bfill',limit=1, inplace=True)

table_1 = table1.drop_duplicates(subset='Beschreibung', keep='first')


prep_table1 = table_1[table_1['Beschreibung'] != 'Historie']

prep_table1.dropna(inplace=True)


prep_table1.to_excel('{}_{}'.format('Final_Table_1',str(datetime.today().date()))+'.'+'xlsx')

#############################
