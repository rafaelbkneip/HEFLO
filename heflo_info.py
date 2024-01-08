#Selenium installations / Instalações para o selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver import ActionChains

from time import sleep

#Error list / Lista de error
lista_error = "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"

#Payment solicitation / Solciitação de pagamento
def pagamento(navegador):
    lista_aux = []

    #Solicitation number / Número da solicitação
    lista_aux.append(navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[1]').text)

    #Enable reading the elements inside the HTML wraper / Permitir a leitura dos elementos dentro do wraper do HTML
    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]')))
    wrapper = navegador.find_element(By.XPATH, '//*[@id="wrapper"]')     
    elemento = navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr')
    actionChains = ActionChains(navegador)
    actionChains.double_click(elemento).perform()
    sleep(3)

    #Name / Nome
    try:
        WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[2]/input')))
        nome = (wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[2]/input').get_attribute('value'))
    except:
        return lista_error

    #Depending on the location of the 'Name' field, the rest of the information can be located at different positions. Make sure that it is 'Name' field
    #Dependendo da localização do campo de 'Nome', o resto das informações podem ser localizadas em diferentes posiçõe. Garantir que esse é o campo de 'Nome'.
    #Conferência do e-mail para verificação da janela de alerta: verificar se não existe @ no texto desse elemento
    if(nome.split('@')[0] == nome):
        print("Nome")

        #Solicitation type / Tipo de solicitação
        lista_aux.append("Solicitação de Pagamento")

        #Name / Nome
        lista_aux.append(nome)

        #Related Company / Coligada 
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Coligada')

        #Branch / Unidade/Filial
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Unidade')

        #Budgetary nature / Natrureza orçamentária
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Natureza')

        #Center of cost / Centro de custo 
        try:                                                                           
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]')))                                          
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            lista_aux.append('Centro de custo')  

        #Make sure the supplier is registered / Garantir que o fornecedor está cadastrado
        try:                                                                           
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[9]/div[1]/div/span/span[1]/span/span[1]')))                                          
            cadastro =wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[9]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title')
        except Exception as e:
            cadastro = 'Erro' 
            
        if (cadastro == 'Cadastrado'):

            #Fornecedor
            try:                                                                            
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[1]/div/span/span[1]/span/span[1]')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
            except Exception as e:
                lista_aux.append('Fornecedor')

            #Charged amount / Valor
            try:                                                                                                                                               
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/input')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/input').get_attribute('value'))
            except Exception as e:
                print(e)
                lista_aux.append('Valor')

            #Discription / Descrição
            try:                                                                                                                             
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[17]/div[1]/div')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[17]/div[1]/div').text)
            except:
                lista_aux.append('Descrição')

            #Payment date / Data
            try:                                                                            
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[2]/div/input')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[2]/div/input').get_attribute('value'))
            except Exception as e:
                print(e)
                lista_aux.append('Data')
        
    else:
        lista_aux.append("Solicitação de Pagamento")

        #Name / Nome
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[1]/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[1]/input').get_attribute('value'))
        except:
            lista_aux.append('Nome')

        #Coligada / Related Company
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Coligada')

        #Unidade/Filial / Branch 
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Unidade/filial')

        #Budget / Natureza orçamentária 
        try:                                                     
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Natureza')

        #Center of cost / Centro de custo
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Centro de custo')

        #Make sure the supplier is registered / Garantir que o fornecedor está cadastrado
        try:
            cadastro = wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title')
        except:
            cadastro = "Erro"
        
        if (cadastro == 'Cadastrado'):

            try:                                                                                                                                      
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[9]/div[1]/div/span/span[1]/span/span[1]')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[9]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
            except:
                try:
                    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[1]/div/span/span[1]/span/span[1]')))
                    lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
                except:    
                    lista_aux.append('Valor')


            #Charged amount / Valor
            try:                                                                             
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[2]/input')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[2]/input').get_attribute('value'))
            except:
                try:
                    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[2]/input')))
                    lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[2]/input').get_attribute('value'))
                except:                                            
                    lista_aux.append('Valor')
                
            
            #Discription / Descrição
            try:                                                                             
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[15]/div[2]/div')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[15]/div[2]/div').text)
            except:
                try:
                    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[16]/div[2]/div')))
                    lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[16]/div[2]/div').text)
                except:    
                    lista_aux.append('Descrição')

            #Payment date / Data
            try:                                                                           
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[1]/div/input')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[1]/div/input').get_attribute('value'))
            except:
                try:
                    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/div/input')))
                    lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/div/input').get_attribute('value'))
                except:    
                    lista_aux.append('Valor')
                
    navegador.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/div[1]/div[1]/div/button').click()

    return lista_aux

################################################################################################################
#Refund solicitation / Solicitação de reembolso
def reembolso(navegador):

    lista_aux = []

    #Enable reading the elements inside the HTML wraper / Permitir a leitura dos elementos dentro do wraper do HTML 
    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]')))
    wrapper = navegador.find_element(By.XPATH, '//*[@id="wrapper"]')
    elemento = navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr')
    actionChains = ActionChains(navegador)
    actionChains.double_click(elemento).perform()
    sleep(3)

    #Solicitation number / Número da solicitação
    lista_aux.append(navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[1]').text)

    #Name / Nome
    try:                                                                           
        WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[2]/input')))
        nome = (wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[2]/input').get_attribute('value'))
        print(nome)
    except:
        return lista_error
    
    #Depending on the location of the 'Name' field, the rest of the information can be located at different positions. Make sure that it is 'Name' field
    #Dependendo da localização do campo de 'Nome', o resto das informações podem ser localizadas em diferentes posiçõe. Garantir que esse é o campo de 'Nome'.
    #Conferência do e-mail para verificação da janela de alerta: verificar se não existe @ no texto desse elemento
    if(nome.split('@')[0] == nome):
        lista_aux.append("Solicitação de Reembolso")

        #Name / nome
        lista_aux.append(nome)

        #Related company / Coligada
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[2]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[2]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Coligada')

        #Branch / Unidade/Filial
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[3]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[3]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Unidade')

        #Budget / Natrureza orçamentária
        try:                                                                 
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[4]/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[4]/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[1]').text)
        except Exception as e:
            print (e)
            lista_aux.append('Natureza orçamentária')   

        #Center of cost / Centro de Custo 
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[3]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[3]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Centro de custo')

        #Supplier / Fornecedor 
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[2]/input')))
            fornecedor = (wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[2]/input').get_attribute('value'))
            print(fornecedor)
            try:
                int(fornecedor.split("-")[0])
                print(fornecedor.split(".")[0])
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[1]/input')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[1]/input').get_attribute('value'))
            except:
                lista_aux.append(fornecedor)

        except Exception as e:
            print (e)
            lista_aux.append('Fornecedor')    

        #Charged amount / Valor 
        try:                                                                                           
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/input').get_attribute('value'))
        except:
            try:
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[1]/input')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[1]/input').get_attribute('value'))
            except Exception as e:
                print(e)
                lista_aux.append('Valor')

        #Description / Descrição
        try:                                                                 
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/div')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/div').text)
        except:
            try:
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[2]/div')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[2]/div').text)
            except Exception as e:
                print(e)
                lista_aux.append('Descrição')

        #Due date / Vencimento                                                                   
        try:                                                                    
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/input').get_attribute('value'))
        except:
            try:
                WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/input')))
                lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/input').get_attribute('value'))
            except Exception as e:
                print(e)
                lista_aux.append('Vencimento')

    else:
        print("A implementar")

    navegador.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/div[1]/div[1]/div/button').click()

    return lista_aux

################################################################################################################
#Advance solicitation / Solicitação de adiantamento
def adiantamento(navegador):

    lista_aux = []

    #Solicitation number / Número da solicitação
    lista_aux.append(navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[1]').text)

    #Enable reading the elements inside the HTML wraper / Permitir a leitura dos elementos dentro do wraper do HTML
    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]')))
    wrapper = navegador.find_element(By.XPATH, '//*[@id="wrapper"]')
    elemento = navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr')
    actionChains = ActionChains(navegador)
    actionChains.double_click(elemento).perform()
    sleep(3)

    #Name / Nome
    try:                                                                          
        WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[2]/input')))
        nome = (wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[2]/input').get_attribute('value'))
        print(nome)
    except:
        return lista_error

    #Depending on the location of the 'Name' field, the rest of the information can be located at different positions. Make sure that it is 'Name' field
    #Dependendo da localização do campo de 'Nome', o resto das informações podem ser localizadas em diferentes posiçõe. Garantir que esse é o campo de 'Nome'.
    #Conferência do e-mail para verificação da janela de alerta: verificar se não existe @ no texto desse elemento
    if(nome.split('@')[0] == nome):
        lista_aux.append("Solicitação de Adiantamento")

        #Name / nome
        lista_aux.append(nome)

        #Related company / Coligada
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Coligada')

        #Branch / Unidade/Filial
        try:    
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Unidade')

        #Center of cost / Centro de Custo
        try: 
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Centro de custo')

        #Budget / Natureza Orçamentária
        try:                                                                           
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[1]/div/span/span[1]/span/span[1]').text)
        except Exception as e:
            print (e)
            lista_aux.append('Natureza orçamentária')

        #Supplier / Fornecedor
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
                try:
                    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[9]/div[2]/div/span/span[1]/span/span[1]')))
                    lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[9]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
                except Exception as e:
                    print (e)
                    lista_aux.append('Fornecedor') 
      
        #Charged amount / Valor
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/input').get_attribute('value'))
        except:
                try:
                    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[1]/input')))
                    lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[1]/input').get_attribute('value'))
                except Exception as e:
                    print (e)
                    lista_aux.append('Valor')

        #Description / Descrição
        try:                
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[17]/div[1]/div')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[17]/div[1]/div').text)
        except:
                try:
                    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[16]/div[1]/div')))
                    lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[16]/div[1]/div').text)
                except Exception as e:
                    print (e)
                    lista_aux.append('Descrição')

        #Due date / Vencimento
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[2]/div/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[2]/div/input').get_attribute('value'))
        except:
                try:
                    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[2]/div/input')))
                    lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[11]/div[2]/div/input').get_attribute('value'))
                except Exception as e:
                    print (e)
                    lista_aux.append('Vencimento')
    else:
        print("A implementar")

    navegador.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/div[1]/div[1]/div/button').click()

    return lista_aux