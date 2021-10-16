import pyautogui
from pyautogui import click, moveTo, typewrite
from time import sleep


def Localizar_Click_Imagem(imagem, tempoPos, alterarvertical=0, alterarhorizontal=0):
    posicao = pyautogui.locateCenterOnScreen(imagem, confidence=0.9)
    moveTo(posicao)

    if alterarvertical != 0 or alterarhorizontal != 0:
        sleep(1)
        # print(str(posicao.x) + str(posicao.y))
        pyautogui.move(alterarhorizontal, alterarvertical)
        # posicao = pyautogui.position()
        # print(str(posicao.x) + str(posicao.y))

    sleep(0.5)
    click()
    sleep(tempoPos)


def ClickMesmoLugar(tempoPos):
    click()
    sleep(tempoPos)


def Preencher_Texto_Localizar_Imagem(imagem, tempoPos, texto_preencher, alterarvertical=0, alterarhorizontal=0):
    Localizar_Click_Imagem(
        imagem, tempoPos, alterarvertical=alterarvertical, alterarhorizontal=alterarhorizontal)
    sleep(0.5)
    typewrite(texto_preencher)


def pressionar_tecla(tecla, tempoAntes=0, tempoPos=0):
    if tempoAntes > 0:
        sleep(tempoAntes)
    pyautogui.press(tecla)
    if tempoPos > 0:
        sleep(tempoPos)


def Preencher_Texto(texto_preencher, tempoPos):
    typewrite(texto_preencher)
    sleep(tempoPos)


def pressionar_tecla_atalho(teclacontrole, letra, tempoAntes=0, tempoPos=0):
    if tempoAntes > 0:
        sleep(tempoAntes)
    with pyautogui.hold(teclacontrole):
        pyautogui.press(letra)
    if tempoPos > 0:
        sleep(tempoPos)
