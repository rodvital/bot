import webbrowser
from time import sleep
import pyautogui
from pyautogui import click, moveTo
from time import sleep
import bot


def Localizar_Click_Imagem(imagem, tempoPos):
    posicao = pyautogui.locateCenterOnScreen(imagem, confidence=0.9)
    moveTo(posicao)
    sleep(0.5)
    click()
    sleep(tempoPos)


newtab = 2  # Nova Tab
webbrowser.open('https://cadastro.vacinacuiaba.com.br', newtab)
sleep(2)

botao_fechar = 'static/img_vacina/fechar.png'
botao_consultar = 'static/img_vacina/consultar.png'
texto_cpf = 'static/img_vacina/cpf.png'

bot.Localizar_Click_Imagem(botao_fechar, 0.5)
# Localizar_Click_Imagem(botao_fechar, 0.5)
# Localizar_Click_Imagem(botao_consultar, 2)
