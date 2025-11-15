
# ===== IMPORTACOES =====
#* Importacoes
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as p
import logging

#* Importacao das funcoes
from src.model.login_amazon import login_amazon

# ===== CONFIGURACOES GOOGLE CHROME E SELENIUM =====
#* Baixar versao correta do chromedrive e armazenar em cache
service = ChromeService(executable_path=ChromeDriverManager().install()) #* instalar chromedriver

# Configurar options para abrir o chrome no perfil do usuario
options = webdriver.ChromeOptions()
# options.add_argument(r'--user-data-dir=C:\Users\Usuário\AppData\Local\Google\Chrome\User Data') #* aponta para a pasta user data principal
# options.add_argument(r'--profile-directory=Profile 2') #* definicao do perfil a ser utilizado
options.add_experimental_option("detach", True) #* evita que o chrome feche sozinho

#* Iniciar instancia do chromedrive
driver = webdriver.Chrome(service=service, options=options)

# ===== CREDENCIAIS DE ACESSO =====
#* Ler arquivo de credenciais e salvar email e senha
arquivo_credenciais = open(r'C:\Users\Usuário\credenciais\login_amazon.txt', 'r')
credenciais = arquivo_credenciais.readlines()
arquivo_credenciais.close()

email = credenciais[0][:-1]
senha = credenciais[1]

# ===== CONFIGURACOES DO LOGGING
#* Configuracao de logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    datefmt='%d/%m/%Y %H:%M:%S',
    filename='mylog.log'
)

# ===== INICIO DO BOT =====
print('===== Bot de Coleta de Produtos da Amazon =====')
logging.info('===== Bot de Coleta de Produtos da Amazon =====')

#* Abrir site da amazon
print('Abrindo site da Amazon, aguarde')
driver.get('https://www.amazon.com.br')
driver.maximize_window()

#* Variavel para definir tempo de espera para carregamento de elementos
tempo_espera = 100

#* Execucao das funcoes
login_amazon(driver, tempo_espera, email, senha)