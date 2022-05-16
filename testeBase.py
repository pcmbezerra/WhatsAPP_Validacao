import pandas as pd
from pprint import pprint
df = pd.read_csv('TESTE_WHATSAPP_30.csv')
cont = 0
for i in df.index:
    fone = f'{df["DDD"][i]}{df["TELEFONE"][i]}'
    print(fone)