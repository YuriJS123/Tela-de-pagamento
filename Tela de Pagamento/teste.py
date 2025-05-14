from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

# Caminho absoluto para o novo arquivo HTML
caminho_html = 'file:///C:/Users/User/OneDrive/vs%20code/Tela%20de%20Pagamento/index.html'

# Iniciar o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Abrir o HTML local
driver.get(caminho_html)

# Esperar o usuário
input("Pressione ENTER para fechar o navegador...")

# Fechar o navegador
driver.quit()
