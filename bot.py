import pyautogui
from pyautogui import click, moveTo, typewrite
from time import sleep


def Localizar_Click_Imagem(imagem, tempoPos):
    posicao = pyautogui.locateCenterOnScreen(imagem, confidence=0.9)
    moveTo(posicao)
    sleep(0.5)
    click()
    sleep(tempoPos)


def Preencher_Texto_Localizar_Imagem(imagem, tempoPos, texto_preencher):
    Localizar_Click_Imagem(imagem, tempoPos)
    sleep(0.5)
    typewrite(texto_preencher)
