
#* Importacoes
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as p
import logging

#* Importacao das funcoes
from src.model.login_amazon import login_amazon

#* Baixar versao correta do chromedrive e armazenar em cache
service = ChromeService(executable_path=ChromeDriverManager().install()) #* instalar chromedriver

#* Inicar instancia do chromedriver
navegador = webdriver.Chrome(service=service)

#* Ler arquivo de credenciais e salvar email e senha
arquivo_credenciais = open(r'C:\Users\Usuário\credenciais\login_amazon.txt', 'r')
credenciais = arquivo_credenciais.readlines()
arquivo_credenciais.close()

email = credenciais[0][:-1]
senha = credenciais[1]

#* Configuracao de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%d/%m/%Y %H:%M:%S',
    filename='mylog.log'
)

print('===== Bot de Coleta de Produtos da Amazon =====')
logging.info('===== Bot de Coleta de Produtos da Amazon =====')

#* Abrir site da amazon
print('Abrindo site da Amazon, aguarde...')
navegador.get('https://www.amazon.com.br')
navegador.maximize_window()

#* Variavel para definir tempo de espera para carregamento de elementos
tempo_espera = 100

#* Execucao das funcoes
login_amazon(navegador, tempo_espera, email, senha)
p.alert('oi')