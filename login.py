from selenium import webdriver #importa o webdriver do selenium
from selenium.webdriver.common.by import By #importa o By do selenium
from selenium.webdriver.chrome.service import Service #importa o Service do Selenium
import time #importa a biblioteca de tempo

url = 'https://guiaodonto.com/home/dash' #endereço do site
driver = webdriver.Chrome() #define o navegador (no caso o nosso é o google)
driver.get(url) #vai para o endereço do site pelo navegador googel

driver.implicitly_wait(0.5) #espera

elemento_login = driver.find_element(by=By.XPATH, value='//*[@id="login_logar"]') #Busca o elemento via XPATH (no caso aqui é o login)
elemento_senha = driver.find_element(by=By.XPATH, value='//*[@id="senha_logar"]') #Busca o elemento via XPATH (no caso aqui é a senha)
login = "02205967606" #define o login
senha = "conzatti2001" #define a senha
elemento_login.send_keys(login) # digita o login no input do site
elemento_senha.send_keys(senha) # digita a senha no input do site

elemento_login.submit() # pressiona o enter para entrar no login
driver.implicitly_wait(1) # aguarda 1 segundo
