import pyautogui
import webbrowser
from time import sleep
from pyautogui import click, moveTo, typewrite

newtab = 2  # open in a new tab, if possible

url = "https://cadastro.vacinacuiaba.com.br/"
webbrowser.open(url, newtab)

botao_fechar = 'imagens/fechar.png'
botao_consultar = 'imagens/consultar.png'
texto_cpf = 'imagens/cpf.png'

sleep(2)  # carregar

pos_fechar = pyautogui.locateCenterOnScreen(botao_fechar, confidence=0.9)
moveTo(pos_fechar)
sleep(0.5)
click()
sleep(0.5)

pos_consultar = pyautogui.locateCenterOnScreen(botao_consultar, confidence=0.9)
moveTo(pos_consultar)
sleep(0.5)
click()
sleep(2)
pos_cpf = pyautogui.locateCenterOnScreen(texto_cpf)
moveTo(pos_cpf)
sleep(0.5)
click()
sleep(0.5)
cpf = '89409876168'
typewrite(cpf)
