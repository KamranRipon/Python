import pandas as pd
from datetime import datetime

table1 = pd.read_excel('Table_from_Web_Maler_page1.xlsx')


table1.columns = ['Firma/Name', 'Beschreibung', 'Sitz', 'Status', 'Registerinhalt']


cols = ['Beschreibung','Sitz', 'Status', 'Registerinhalt']
for col in cols:
    table1[col].fillna(method='bfill',limit=1, inplace=True)

table_1 = table1.drop_duplicates(subset='Beschreibung', keep='first')


prep_table1 = table_1[table_1['Beschreibung'] != 'Historie']

prep_table1.dropna(inplace=True)


prep_table1.to_excel('{}_{}'.format('Final_Table_1',str(datetime.today().date()))+'.'+'xlsx')