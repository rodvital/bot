import webbrowser
from time import sleep


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
