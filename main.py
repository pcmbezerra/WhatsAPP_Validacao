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
browser.implicitly_wait(2)
telefones = pd.read_csv('TESTE_WHATSAPP.csv')
urlprincipal = 'https://web.whatsapp.com/'
browser.get(urlprincipal)
resposta = input('Você já escaneou o QRCODE?')
wppOn = []
wppOff = []
ddi= 55
cont = 0
try:
    if resposta == 'SIM':
        for x in telefones['DDD']:
            for y in telefones['TELEFONE']:
                fone = f'{ddi}{x}{y}'
                mensagem = urllib.parse.quote('hello world')
                url = f'https://web.whatsapp.com/send?phone={fone}&text={mensagem}'
                browser.get(url)
                cont += 1
                print(cont)
                sleep(3.8)
                if len(browser.find_elements(By.CSS_SELECTOR, 'div[data-animate-modal-popup="true"]')) > 0:
                    wppOff.append(fone)
                else:
                    wppOn.append(fone)
                    if cont > len(telefones['TELEFONE']):
                        resposta = 'NAO'
    elif resposta == 'NAO':
        print('Processo Finalizado!')
except Exception as erro:
    print(erro)
finally:
    on = pd.DataFrame(wppOn)
    on.to_csv('TelefonesComWhatsapp')
    off = pd.DataFrame(wppOff)
    off.to_csv('TelefonesSemWhatsapp')

#'https://web.whatsapp.com/send?phone=+5511979529488&text=jesus%20me%20ajuda'

