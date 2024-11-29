from login import *
from Funções_em_diretórios import Criacao_de_diretorio_e_pastas_do_Programa, Limpeza_da_pasta_do_programa, Limpeza_de_downloads_antigos, Mover_arquivos_para_Diretorio_do_programa
import time
import os

#Verificando se existe a pasta que o programa vai utilizar
if 'guiaOrto' in os.listdir('C:\\'):
    print('Diretorio já criado')
else:
    #Criando o diretório que nosso programa irá utilizar
    Criacao_de_diretorio_e_pastas_do_Programa()

#Chamando função que tira todos as planilhas que nossa automação gerou do diretório de DOWNLOADS
Limpeza_de_downloads_antigos() 

#Chamando função que tira todos as planilhas que nossa automação gerou na ultima vez que rodou!
Limpeza_da_pasta_do_programa()

driver.switch_to.new_window('tab')
driver.get("https://guiaodonto.com/home/dash")


driver.find_element(by=By.CLASS_NAME, value='pe-7s-users').click()
time.sleep(3)

driver.find_element(by=By.XPATH, value='//*[@id="excel"]/span').click()
time.sleep(3)

driver.close()

driver.switch_to.window(original_window)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/button').click()

lista_filtro = driver.find_element(By.ID, 'lista-consulta')
lista_filtro.click()

driver.find_element(By.XPATH, '//*[@id="filtro"]/form/div[4]/div/div[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="filtro"]/form/div[4]/div/div[2]/div/div[4]').click()
driver.find_element(By.XPATH, '//*[@id="filtro"]/form/div[14]/button').click()
time.sleep(1)

driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div/button').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[6]/div/div/ul/li[2]/a').click()
time.sleep(5)
    
#Chamando função que move todas as planilhas baixadas para pasta do programa
Mover_arquivos_para_Diretorio_do_programa()