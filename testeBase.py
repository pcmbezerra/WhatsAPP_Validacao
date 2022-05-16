import pandas as pd
from pprint import pprint
df = pd.read_csv('TESTE_WHATSAPP.csv')
for x in df['DDD']:
    for y in df['TELEFONE']:
        fone = f'{x}{y}'
        print(fone)
#print(df[['DDD','TELEFONE']])