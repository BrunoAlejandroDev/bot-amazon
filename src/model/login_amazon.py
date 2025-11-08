
#* Importacoes
import logging
import traceback
import pyautogui as p

from selenium.common.exceptions import TimeoutException #* exceção para quando o tempo de espera for esgotado
from selenium.webdriver.common.by import By #* usada para definir como o elemento será selecionado
from selenium.webdriver.support.wait import WebDriverWait #* usada para definir uma espera até algo acontecer
from selenium.webdriver.support import expected_conditions as EC

#* Dicionario de XPATH's
dict_xpath = {
    'seta_menu_suspenso' : '/html/body/div[1]/header/div/div[1]/div[3]/div/div/button',
    'btn_login' : '/html/body/div[1]/header/div/div[3]/div[2]/div[2]/div/div[1]/div/a',
    'campo_email' : '/html/body/div[1]/div[1]/div[2]/div/div/div/div/span/form/div[1]/input',
    'campo_senha' : '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/input',
    'btn_continuar' : '/html/body/div[1]/div[1]/div[2]/div/div/div/div/span/form/span/span/input',
    'bnt_fazer_login' : '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/span/span/input'
}

def login_amazon(navegador, tempo_espera, email, senha):
    try:
        print('\nProcesso Atual: Fazer Login na Amazon')
        logging.info('Processo Atual: Fazer Login na Amazon')

        #* Clicar na seta para abrir o menu suspenso 
        seta_menu_suspenso = WebDriverWait(navegador, tempo_espera).until(
            EC.visibility_of_element_located((By.XPATH, dict_xpath['seta_menu_suspenso']))
        )
        seta_menu_suspenso.click()
        
        p.sleep(1)
        
        #* Apos menu suspenso abrir, clicar no botao de login
        fazer_login = WebDriverWait(navegador, tempo_espera).until(
            EC.visibility_of_element_located((By.XPATH, dict_xpath['btn_login']))
        )
        fazer_login.click()
        
        p.sleep(1.5)
        
        #* Quando o campo de email aparecer, preencher o campo com o email do usuario
        campo_email = WebDriverWait(navegador, tempo_espera).until(
            EC.element_to_be_clickable((By.XPATH, dict_xpath['campo_email']))
        )
        campo_email.send_keys(email)
        
        p.sleep(1)
        
        #* Clicar em continuar para seguir para o proximo campo
        btn_continuar = WebDriverWait(navegador, tempo_espera).until(
            EC.visibility_of_element_located((By.XPATH, dict_xpath['btn_continuar']))
        )
        btn_continuar.click()
        
        p.sleep(1.5)
        
        #* Inserir a senha no campo de senha 
        campo_senha = WebDriverWait(navegador, tempo_espera).until(
            EC.element_to_be_clickable((By.XPATH, dict_xpath['campo_senha']))
        )
        campo_senha.send_keys(senha)
        
        p.sleep(1)
        
        btn_fazer_login = WebDriverWait(navegador, tempo_espera).until(
            EC.visibility_of_element_located((By.XPATH, dict_xpath['bnt_fazer_login']))
        )
        btn_fazer_login.click()
        
        p.sleep(1.5)
        
        print('-- Login efetuado com sucesso!')
        logging.info('-- Login efetuado com sucesso!')
        
    except TimeoutException as toe:
        msg_error = traceback.format_exc()
        print(f'-- Tempo de espera esgotado.\nDetalhes: {toe}')
        logging.error(f'-- Tempo de espera esgotado.\nDetalhes: {toe}')
        logging.error(msg_error)
        
    except Exception as e:
        msg_error = traceback.format_exc()
        print(f'-- Ocorreu um erro ao realizar o login: {e}\n{msg_error}')
        logging.error(f'-- Ocorreu um erro ao realizar o login: {e}\n{msg_error}')