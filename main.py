import urllib.parse
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import pandas as pd
from selenium.webdriver.common.keys import Keys
options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
browser = Chrome(executable_path='C:\DRIVERS\chromedriver.exe',options=options)
browser.implicitly_wait(1)
telefones = pd.read_csv('TESTE_WHATSAPP.csv')
urlprincipal = 'https://web.whatsapp.com/'
browser.get(urlprincipal)
resposta = input('Você já escaneou o QRCODE?')
wppOn = []
wppOff = []
ddi= 55
cont = 0
try:
    while resposta == 'SIM':
        for i in telefones.index:
                fone = f'{telefones["DDD"][i]}{telefones["TELEFONE"][i]}'
                #mensagem = urllib.parse.quote('hello world')
                url = f'https://web.whatsapp.com/send?phone={ddi}{fone}&text='
                browser.get(url)
                cont += 1
                sleep(2)
                if len(browser.find_elements(By.CSS_SELECTOR,'div[title="Mensagem"]')) > 0:
                    wppOn.append(fone)
                    #browser.find_element(By.CSS_SELECTOR, 'div[role="gridcell"]').click()
                    #browser.find_element(By.CSS_SELECTOR, 'div[aria-label="Apagar conversa"]').click()
                    print(f'Total de {len(wppOn)} Validos.')
                elif len(browser.find_elements(By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')) > 0:
                    wppOff.append(fone)
                    print(f'Total de {len(wppOff)} invalidos.')
        if cont >= len(telefones['TELEFONE']):
            print(f'''
            Validação Finalizada:
            Numeros que contém WhatsAPP: {len(wppOn)}
            Numeros que não contém WhatsAPP: {len(wppOff)}
            Total de numeros analisados: {cont}''')
            break
except Exception as erro:
    print(erro)
finally:
    on = pd.DataFrame(wppOn)
    on.to_csv('TelefonesComWhatsapp')
    off = pd.DataFrame(wppOff)
    off.to_csv('TelefonesSemWhatsapp')

#'https://web.whatsapp.com/send?phone=+5511979529488&text=jesus%20me%20ajuda'

