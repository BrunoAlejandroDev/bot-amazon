
#* Importacoes
import logging
import traceback
import pyautogui as p
import time
import unicodedata

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
    'lista_completa_livros' : 'li[data-itemid]'
}

dados_dos_livros = []

def remover_acentos(texto):
    return ''.join(
    char for char in unicodedata.normalize('NFD', texto)
    if not unicodedata.combining(char)
)

def abrir_lista_livros(navegador, tempo_espera):
    try:
        print('\nProcesso Atual: Acessar lista e Coletar Livros')
        logging.info('Processo Atual: Acessar lista e Coletar Livros')
        
        time.sleep(1)
        
        #* Abrir menu suspenso 
        menu_suspenso = WebDriverWait(navegador, tempo_espera).until(
            EC.element_to_be_clickable((By.XPATH, dict_xpath['menu_suspenso']))
        )
        menu_suspenso.click()
        
        time.sleep(1)
        
        #* Clicar na opcao "minhas listas"
        minhas_listas = WebDriverWait(navegador, tempo_espera).until(
            EC.element_to_be_clickable((By.XPATH, dict_xpath['caixa_minhas_listas']))
        )
        minhas_listas.click()
        
        time.sleep(1)
        
        #* Selecionar lista "livros" 
        lista_livros = WebDriverWait(navegador, tempo_espera).until(
            EC.element_to_be_clickable((By.XPATH, dict_xpath['lista_livros']))
        )
        lista_livros.click()
        
        time.sleep(2)
        
        print('-- iniciando rolagem para carregar todos os itens')
        
        #* rolar a pagina
        ultima_altura = navegador.execute_script('return document.body.scrollHeight')
        
        while True:
            #* Ir ate o fim da pagina
            navegador.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            
            time.sleep(2)
            
            nova_altura = navegador.execute_script("return document.body.scrollHeight")
            
            if nova_altura == ultima_altura:
                break
            
            ultima_altura = nova_altura
            
        time.sleep(1)
        
        print('-- pagina completamente carregada')
        
        lista_de_livros = WebDriverWait(navegador, tempo_espera).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'li[data-itemid]'))
        )
        print(f'-- Quantidade de livros encontrados: {len(lista_de_livros)}')
        
        #* Percorrer todos os livros e pegar dados de cada um
        for livro in lista_de_livros:
            #* Extrair titulo
            elemento_titulo_livro = livro.find_element(By.CSS_SELECTOR, "a[id^='itemName_']")
            titulo_livro = elemento_titulo_livro.get_attribute('title')
            titulo_livro_formatado = remover_acentos(titulo_livro)
            print(titulo_livro_formatado)
        
        p.alert('oi')
        
    except TimeoutException as toe:
        msg_error = traceback.format_exc()
        print(f'-- Tempo de espera esgotado.\nDetalhes: {toe}')
        logging.error(f'-- Tempo de espera esgotado.\nDetalhes: {toe}')
        logging.error(msg_error)
        
    except Exception as e:
        msg_error = traceback.format_exc()
        print(f'-- Ocorreu um erro ao realizar o login: {e}\n{msg_error}')
        logging.error(f'-- Ocorreu um erro ao realizar o login: {e}\n{msg_error}')