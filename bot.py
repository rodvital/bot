import pyautogui
from time import sleep
import sys


def Mensagem(tipo, texto, titulo, botao):
    if tipo == 'Alerta':
        pyautogui.alert(text=texto, title=titulo, button=botao)


def VerificarImagemExiste(imagem):
    try:
        pos = pyautogui.locateCenterOnScreen(imagem, confidence=0.9)
        return pos
    except Exception:
        return None


def Localizar_Click_Imagem(imagem, tempoPos, alterarvertical=0, alterarhorizontal=0):
    try:
        posicao = pyautogui.locateCenterOnScreen(imagem, confidence=0.9)
        # logging.debug('Localizando Imagem ' + imagem +' na posicao ' + str(posicao))
        pyautogui.moveTo(posicao)
        if alterarvertical != 0 or alterarhorizontal != 0:
            pyautogui.move(alterarhorizontal, alterarvertical)
        sleep(0.5)
        pyautogui.click()
        sleep(tempoPos)
    except Exception:
        pyautogui.alert(text='A Imagem ' + imagem + ' não foi encontrada.',
                        title='Imagem não encontrada', button='OK')
        sys.exit()


def ClickMesmoLugar(tempoPos):
    pyautogui.click()
    sleep(tempoPos)


def Preencher_Texto_Localizar_Imagem(imagem, tempoPos, texto_preencher, alterarvertical=0, alterarhorizontal=0):
    Localizar_Click_Imagem(
        imagem, tempoPos, alterarvertical=alterarvertical, alterarhorizontal=alterarhorizontal)
    sleep(tempoPos)
    pyautogui.typewrite(texto_preencher)


def pressionar_tecla(tecla, tempoAntes=0, tempoPos=0):
    if tempoAntes > 0:
        sleep(tempoAntes)
    pyautogui.press(tecla)
    if tempoPos > 0:
        sleep(tempoPos)


def Preencher_Texto(texto_preencher, tempoPos):
    pyautogui.typewrite(texto_preencher)
    sleep(tempoPos)


def pressionar_tecla_atalho(teclacontrole, letra, tempoAntes=0, tempoPos=0):
    if tempoAntes > 0:
        sleep(tempoAntes)
    with pyautogui.hold(teclacontrole):
        pyautogui.press(letra)
    if tempoPos > 0:
        sleep(tempoPos)
