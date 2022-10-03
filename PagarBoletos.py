from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

# navegador = webdriver.Chrome()
navegador.get("https://auth.netcombo.com.br/web/login.html?client_id=MINHA_CLARO_RESIDENCIAL&redirect_uri=https%3A%2F%2Fminhaclaroresidencial.claro.com.br%2Flogin&response_type=code&scope=openid+minha_net&authMs=UP,EP,DOCP,OTP")
navegador.find_element(By.XPATH, '//*[@id="login"]').send_keys("USUARIO")
navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys("SENHA")
navegador.find_element(By.XPATH, '//*[@id="loginForm"]/fieldset/div[5]/button[1]').click()
'''
navegador.find_element(By.XPATH, '//*[@id="app"]/article/div/div[2]/div/div[2]/div[1]/div/div').Select.all_selected_options.setter
'''