from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://guiaodonto.com/home/dash' 

options = webdriver.ChromeOptions() 
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get(url) 

driver.implicitly_wait(0.5) 

elemento_login = driver.find_element(by=By.XPATH, value='//*[@id="login_logar"]') 
elemento_senha = driver.find_element(by=By.XPATH, value='//*[@id="senha_logar"]') 

login = "02205967606" 
senha = "conzatti2001" 

elemento_login.send_keys(login) 
elemento_senha.send_keys(senha) 

elemento_login.submit() 
driver.implicitly_wait(1) 

original_window = driver.current_window_handle