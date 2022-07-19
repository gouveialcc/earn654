from fileinput import close
import webbrowser
import pyautogui
import time
#from torch import true_divide

#abre o navegador
def navegador():
    #url = 'https://localhost:80'
    #webbrowser.get('chrome').open(url)
    webbrowser.open('https://localhost:80')
    
#nova aba
def abreaba():
    pyautogui.hotkey('ctrl', 't')
    
#fecha aba
def fechaaba():
    pyautogui.hotkey('ctrl', 'w')

#abre aba anonima
def anonima():
    pyautogui.hotkey('ctrl', 'shift', 'n')

#cola link e roda
def colaeroda():
    pyautogui.write('https://earn-654dfg.beauty/310545056525')
    pyautogui.press('enter')

#encerra chrome
def encerrar():
    pyautogui.hotkey('ctrl', 'w')

#roda script
def earn654():
    navegador()
    time.sleep(2)
    #abreaba()
    #time.sleep(2)
    #fechaaba()
    #time.sleep(2)
    anonima()
    time.sleep(3)
    colaeroda()
    time.sleep(3)
    encerrar()
    time.sleep(2)
    fechaaba()
    
#laco para repetir script
while(True):
    earn654()
