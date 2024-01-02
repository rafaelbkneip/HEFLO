from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path
import heflo_info

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_argument("--start-maximized")


navegador = webdriver.Chrome(options = options)


navegador.get("https://app.heflo.com/")

navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/div[2]/input').send_keys("")

sleep(3)

navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/div[3]/input').send_keys("")

sleep(60)

WebDriverWait(navegador,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/button[1]')))
navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/button[1]').click()

WebDriverWait(navegador,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainDiv"]/div/div/a[3]/div')))
navegador.find_element(By.XPATH, '//*[@id="mainDiv"]/div/div/a[3]/div').click()

#Solicitation number from which the code starts to scrap the data / Número da solicitação da qual o programa começa a obter os dados
chamado = 45900

while (True):

    navegador.get('https://app.heflo.com/Portal/List')

    chamado = chamado + 1

    print(chamado)

    WebDriverWait(navegador,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerSearchControl"]/div/div[1]/input')))

    navegador.find_element(By.XPATH, '//*[@id="headerSearchControl"]/div/div[1]/input').send_keys(str(chamado))

    navegador.find_element(By.XPATH, '//*[@id="headerSearchControl"]/div/div[1]/input').send_keys(Keys.ENTER)

    sleep(10)

    lista_aux = []

    try:
        navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[4]/i')
        controle = (navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[4]/i').get_attribute('title'))
        print(controle)

        if(controle != 'Rascunho'):

            sleep(5)
            #Solicitation type / Tipo de solicitação 
            solicitacao = (navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[3]').text)

            print(solicitacao)

            if (solicitacao == 'Solicitação de Pagamento'):
                        
                lista_aux=[]
                lista=[]
                lista_aux = heflo_info.pagamento(navegador)
                        
                print(lista_aux)

                lista.append(lista_aux)

                try: 
                        #Escrever os resultados na planilha / Write the results on the sheet
                    print(lista)
                    print("\n")
                    
                except Exception as e:
                    print(e) 

            elif(solicitacao == 'Financeiro - Solicitação de Reembolso'):
                print("Solicitação de Reembolso")
                lista_aux=[]
                lista=[]
                lista_aux = heflo_info.reembolso(navegador)

                print(lista_aux)

                lista.append(lista_aux)

                try: 
                        #Escrever os resultados na planilha / Write the results on the sheet
                    print("essa é a lista")
                    print(lista)
                    print("\n")
                    
                except Exception as e:
                    print(e)

            else:
                print("A implementar")

    except Exception as e:
        print('Não implementado ainda')