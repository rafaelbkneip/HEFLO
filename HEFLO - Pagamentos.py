from __future__ import print_function

#Selenium installations / Instalações para o selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

#Google API installations / Instalações do Google API
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from selenium.webdriver.common.keys import Keys

from time import sleep
import os.path

#Solicitation information function / Função de informação das solicitações
import heflo_info

#Set up configurations for the driver / Configurações do driver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--start-maximized")
navegador = webdriver.Chrome(options = options)

#Scopes to use the Google Spreadsheets API / Escopo para usar a API do Google Spreadsheet
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

#The ID and range of the spreadsheet / O ID e a intervalo da planilha
SAMPLE_SPREADSHEET_ID = ""
SAMPLE_RANGE_NAME = ""

#Acess the token file / Acessar o arquivo de token
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

#Number of solicitations / Número de chamados
chamados = len(values)
print('Número de chamados: ', chamados)

#Log into HEFLO/Logar no HEFLO
navegador.get("https://app.heflo.com/")
navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/div[2]/input').send_keys("")
sleep(3)
navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/form/div[3]/input').send_keys("")
sleep(60)

#Acess the page with all the solicitations / Acessar a página com todas as solicitações
WebDriverWait(navegador,20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/button[1]')))
navegador.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[1]/button[1]').click()
WebDriverWait(navegador,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainDiv"]/div/div/a[3]/div')))
navegador.find_element(By.XPATH, '//*[@id="mainDiv"]/div/div/a[3]/div').click()

#Solicitation number from which the code starts to scrap the data / Número da solicitação da qual o programa começa a obter os dados
#chamado = int(values[-1][0])
chamado = 49501
print("Esse é a última solicitação na planilha "+ str(values[-1][0]) +". O programa começara a leitura a partir do chamado " + str(chamado) +"." )

while (True):

    navegador.get('https://app.heflo.com/Portal/List')

    #Acess the next solicitation / Acessar a próxima solicitação
    chamado = chamado + 1
    print(chamado)

    #Search for the solicitation / Pesquisar a solicitação
    WebDriverWait(navegador,20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="headerSearchControl"]/div/div[1]/input')))
    navegador.find_element(By.XPATH, '//*[@id="headerSearchControl"]/div/div[1]/input').send_keys(str(chamado))
    navegador.find_element(By.XPATH, '//*[@id="headerSearchControl"]/div/div[1]/input').send_keys(Keys.ENTER)

    sleep(10)

    lista_aux = []

    #Try to click on the solicitation window / Tentar clicar na janela da solicitação
    try:
        navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[4]/i')
        controle = (navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[4]/i').get_attribute('title'))
        print(controle)

        #Make sure the solcitation is not a draft / Assegurar que a solicitação não é um rascunho
        if(controle != 'Rascunho'):

            sleep(5)

            #Solicitation type / Tipo de solicitação 
            solicitacao = (navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[3]').text)
            print(solicitacao)

            if (solicitacao == 'Solicitação de Pagamento'):
                #Define the auxiliary lists / Definir as listas auxiliares        
                lista_aux=[]
                lista=[]

                #Call the specific function / Chamar a função específica
                lista_aux = heflo_info.pagamento(navegador)

                print(lista_aux)
                lista.append(lista_aux)

                #Escrever os resultados na planilha / Write the results on the sheet
                try:
                    #Define the spreadsheet row the solicitation info will be written / Definir a linha da planilha an qual as informações da planilha serão escritas
                    chamados = chamados + 1

                    #Write the info / Escrever as informações
                    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A'+str(chamados)+":"+'L'+str(chamados), valueInputOption='USER_ENTERED', body={'values': lista }).execute()
                    
                except Exception as e:
                    print(e) 

            elif(solicitacao == 'Financeiro - Solicitação de Reembolso'):
                #Define the auxiliary lists / Definir as listas auxiliares
                lista_aux=[]
                lista=[]

                #Call the specific function / Chamar a função específica
                lista_aux = heflo_info.reembolso(navegador)
                print(lista_aux)
                lista.append(lista_aux)

                #Escrever os resultados na planilha / Write the results on the sheet
                try: 
                    #Define the spreadsheet row the solicitation info will be written / Definir a linha da planilha an qual as informações da planilha serão escritas
                    chamados = chamados + 1

                    #Write the info / Escrever as informações
                    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A'+str(chamados)+":"+'L'+str(chamados), valueInputOption='USER_ENTERED', body={'values': lista }).execute()
                    
                except Exception as e:
                    print(e)

            elif(solicitacao == 'Solicitação de Adiantamento'):
                #Define the auxiliary lists / Definir as listas auxiliares
                lista_aux=[]
                lista=[]

                #Call the specific function / Chamar a função específica
                lista_aux = heflo_info.adiantamento(navegador)
                print(lista_aux)
                lista.append(lista_aux)

                #Escrever os resultados na planilha / Write the results on the sheet
                try: 
                    #Define the spreadsheet row the solicitation info will be written / Definir a linha da planilha an qual as informações da planilha serão escritas
                    chamados = chamados + 1

                    #Write the info / Escrever as informações
                    result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range='A'+str(chamados)+":"+'L'+str(chamados), valueInputOption='USER_ENTERED', body={'values': lista }).execute()
                    
                except Exception as e:
                    print(e)

            else:
                print("A implementar")

    #If the search does not show any results, the solicitation does not exist / Se a busca não mostra nenhum resultado, a solicitação não existe
    except Exception as e:
        print('Chamado não existe \n')