from login import * #importa tudo do codigo login (tudo == *)
import pandas as pd #importa pandas como pd(nomeclatura)

time.sleep(5) # aguarda 3 segundos
driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[1]/button').click() # fecha o popup de avaliação do guiaodonto

button_mes = driver.find_element(by=By.XPATH, value='//*[@id="calendar"]/div[1]/div[2]/div/button[1]') # Busca o elemento do botão mês via XPATH
button_mes.click() # Clica no botão mês
time.sleep(3) # aguarda 3 segundos

nomes_pacientes = []
status = []

for nomes in driver.find_elements(by=By.CLASS_NAME, value='fc-title'): #um loop que procura todos os elementos EXISTENTES por uma classe de valor fc-title
    nomes.click() #clica no elemento que mostra a tela de status e informações em relação a agenda do paciente
    time.sleep(1) #aguarda 1 segundo

    if driver.find_element(by=By.CLASS_NAME, value='selectize-control.demo-default.select-status.single').text != '': # compara o texto do elemento pelo valor de sua classe com o texto de status (no caso é o 'Não confirmado')
        nomes_pacientes.append(f'{nomes.text}') # da um append e adiciona na lista o nome do elemento fc-title
        status.append(driver.find_element(by=By.CLASS_NAME, value='selectize-control.demo-default.select-status.single').text)
    driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div/div[1]/button').click() # acha o elemento de fechar a tela de status

dados = { # organização dos dados por dicionario
    'Paciente' : nomes_pacientes,
    'Status' : status
}

df = pd.DataFrame.from_dict(dados, orient='index') # organização dos dados (obs: index um paramentro que sera utilizado na proxima linha)
df = df.transpose() # vai ignorar se as listas possui tamanhos diferentes e não vai dar erro
df.to_excel('projeto_final.xlsx', index=False) # tranforma tudo para xlsx (excel)
