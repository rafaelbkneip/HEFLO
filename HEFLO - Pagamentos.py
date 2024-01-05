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
from selenium.webdriver.common.keys import Keys
import os.path
import heflo_info

options = webdriver.ChromeOptions()

options.add_experimental_option("detach", True)

options.add_argument("--start-maximized")


navegador = webdriver.Chrome(options = options)

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ""
SAMPLE_RANGE_NAME = ""

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")

except HttpError as err:
    print(err)


navegador.get("https://app.heflo.com/")

navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/div[2]/input').send_keys("")

sleep(3)

navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/div[3]/input').send_keys("")

sleep(60)

WebDriverWait(navegador,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/button[1]')))
navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/button[1]').click()

WebDriverWait(navegador,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainDiv"]/div/div/a[3]/div')))
navegador.find_element(By.XPATH, '//*[@id="mainDiv"]/div/div/a[3]/div').click()

chamados = len(values)
print('Número de chamados: ', chamados)

#Solicitation number from which the code starts to scrap the data / Número da solicitação da qual o programa começa a obter os dados
#chamado = int(values[-1][0])
chamado = 49501

print("Esse é a última solicitação na planilha "+ str(values[-1][0]) +". O programa começara a leitura a partir do chamado " + str(chamado) +"." )

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

                    chamados = chamados + 1

                    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A'+str(chamados)+":"+'L'+str(chamados), valueInputOption='USER_ENTERED', body={'values': lista }).execute()
                    
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
                    print(lista)
                    chamados = chamados + 1
                    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A'+str(chamados)+":"+'L'+str(chamados), valueInputOption='USER_ENTERED', body={'values': lista }).execute()
                    
                except Exception as e:
                    print(e)

            elif(solicitacao == 'Solicitação de Adiantamento'):
                print("Solicitação de Adiantamento")
                lista_aux=[]
                lista=[]
                lista_aux = heflo_info.adiantamento(navegador)
                print(lista_aux)
                lista.append(lista_aux)

                try: 
                        #Escrever os resultados na planilha / Write the results on the sheet
                    print(lista)

                    chamados = chamados + 1

                    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A'+str(chamados)+":"+'L'+str(chamados), valueInputOption='USER_ENTERED', body={'values': lista }).execute()
                    
                except Exception as e:
                    print(e)

            else:
                print("A implementar")

    except Exception as e:
        print('Não implementado ainda \n')