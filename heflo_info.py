from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep

lista_error = "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR", "ERROR"

def pagamento(navegador):

    lista_aux = []

    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]')))
    wrapper = navegador.find_element(By.XPATH, '//*[@id="wrapper"]')

    lista_aux.append(navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[1]').text)

    #Enable reading the elements inside the HTML wraper / Permitir a leitura dos elementos dentro do wraper do HTML 
    elemento = navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr')
    actionChains = ActionChains(navegador)
    actionChains.double_click(elemento).perform()
    sleep(3)

    #Name / Nome
    try:
        WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[2]/input')))
        nome = (wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[2]/input').get_attribute('value'))
        print(nome)
        #lista_aux.append(nome)
    except:
        return lista_error

    #Conferência do e-mail para verificação da janela de alerta
    if(nome.split('@')[0] == nome):
        print("Nome")

        #Solicitation type
        lista_aux.append("Solicitação de Pagamento")

        #Nome
        lista_aux.append(nome)

        #Coligada 
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Coligada')

        #Unidade 
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Unidade')

        #Natureza orçamentária 
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[8]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Natureza')

        #Centro de custo
        try:                                                                           
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]')))                                          
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            lista_aux.append('Centro de custo')  

        #Cadastro
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

            try:                                                                          
                #Discription / Descrição                                                    
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
        print("Email")

        lista_aux.append("Solicitação de Pagamento")

        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[1]/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[1]/div[1]/input').get_attribute('value'))
        except:
            lista_aux.append('Nome')

        #Coligada
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Coligada')

        #Unidade filial
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Unidade/filial')

        #Natureza orçamentária 
        try:                                                     
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Natureza')

        #Centro de custo
         
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except:
            lista_aux.append('Centro de custo')

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

########################################################################################################################################
def reembolso(navegador):

    lista_aux = []

    WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]')))
    wrapper = navegador.find_element(By.XPATH, '//*[@id="wrapper"]')

    lista_aux.append(navegador.find_element(By.XPATH, '//*[@id="ui-id-2"]/tbody/tr/td[1]').text)

    #Enable reading the elements inside the HTML wraper / Permitir a leitura dos elementos dentro do wraper do HTML 
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

    #Conferência do e-mail para verificação da janela de alert: verificar se não existe @ no texto desse elemento
    if(nome.split('@')[0] == nome):
        print("Nome")

        lista_aux.append("Solicitação de Reembolso")

        #Name/nome
        lista_aux.append(nome)

        #Coligada
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[2]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[2]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Coligada')

        #Unidade
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[3]/div[1]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[3]/div[1]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Unidade')

        #Centro de Custo
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[3]/div[2]/div/span/span[1]/span/span[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[3]/div[2]/div/span/span[1]/span/span[1]').get_attribute('title'))
        except Exception as e:
            print (e)
            lista_aux.append('Centro de custo')

        
        #Natureza Orçamentária
        try:                                                                            
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[4]/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[1]')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[4]/div[2]/div/div[1]/div[2]/div[2]/table/tbody/tr/td[1]').text)
        except Exception as e:
            print (e)
            lista_aux.append('Natureza orçamentária')

        #Vencimento
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[6]/div[2]/div/input').get_attribute('value'))
        except Exception as e:
            print (e)
            lista_aux.append('Vencimento')

        #Valor
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[7]/div[2]/input').get_attribute('value'))
        except Exception as e:
            print (e)
            lista_aux.append('Valor')

        #Descrição
        try:
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/div')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[12]/div[1]/div').text)
        except Exception as e:
            print (e)
            lista_aux.append('Natureza orçamentária')

        try:
            #Fornecedor
            WebDriverWait(navegador,20).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[2]/input')))
            lista_aux.append(wrapper.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div[3]/div[3]/form/div[10]/div[2]/input').get_attribute('value'))
        except Exception as e:
            print (e)
            lista_aux.append('Fornecedor')

    
    else:
        print("A implementar")

    navegador.find_element(By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/div[1]/div[1]/div/button').click()

    return lista_aux