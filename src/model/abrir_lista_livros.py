
#* Importacoes
import logging
import traceback
import pyautogui as p

#* Importacoes do selenium
from selenium.common.exceptions import TimeoutException #* exceção para quando o tempo de espera for esgotado
from selenium.webdriver.common.by import By #* usada para definir como o elemento será selecionado
from selenium.webdriver.support.wait import WebDriverWait #* usada para definir uma espera até algo acontecer
from selenium.webdriver.support import expected_conditions as EC

#* Dicionario de XPATH's
dict_xpath = {
    'menu_suspenso' : '/html/body/div[1]/header/div/div[1]/div[3]/div/div/a',
    'caixa_minhas_listas' : '/html/body/div[1]/div[1]/div/ul[4]/li[1]/span/span/a',
    'lista_livros' : '/html/body/div[2]/div[1]/div/div/div/div/div/div[1]/div/div[3]/a',
}

def abrir_lista_livros(navegador, tempo_espera):
    try:
        print('\nProcesso Atual: Acessar lista e Coletar Livros')
        logging.info('Processo Atual: Acessar lista e Coletar Livros')
        
    except TimeoutException as toe:
        msg_error = traceback.format_exc()
        print(f'-- Tempo de espera esgotado.\nDetalhes: {toe}')
        logging.error(f'-- Tempo de espera esgotado.\nDetalhes: {toe}')
        logging.error(msg_error)
        
    except Exception as e:
        msg_error = traceback.format_exc()
        print(f'-- Ocorreu um erro ao realizar o login: {e}\n{msg_error}')
        logging.error(f'-- Ocorreu um erro ao realizar o login: {e}\n{msg_error}')