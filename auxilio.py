import webbrowser
from time import sleep
import os
import re


def AbrirAba(url, tempoPos):
    newtab = 2  # Nova Tab
    webbrowser.open(url, newtab)
    sleep(tempoPos)


def NumLockLigado():
    import ctypes
    hllDll = ctypes.WinDLL("User32.dll")
    VK_NUMLOCK = 0x90
    if hllDll.GetKeyState(VK_NUMLOCK) == 1:
        return True
    else:
        return False


def ArquivosPastaemLista(diretorio, lista):
    texto = ''
    for entry in os.scandir(diretorio):
        if entry.is_file():
            if entry.name[:-4] in lista:
                if texto == '':
                    texto = "Arquivos com Ticket na pasta: "
                    texto = texto + entry.name
                else:
                    texto = texto + ', ' + entry.name
    return texto


def TextoemLista(texto):
    lista = [x.strip() for x in texto.split(',')]
    return lista
