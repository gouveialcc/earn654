import webbrowser
import keyboard
import time
from torch import true_divide

#abre o navegador
def navegador():
    # url = 'https://localhost:80'
    # webbrowser.get('chrome').open(url)
    webbrowser.open('https://localhost:80')

#fecha aba
def fechaaba():
    keyboard.press_and_release('Command+w')

# #abre aba anonima
def anonima():
    keyboard.press_and_release('shift+Command+n')

#cola link e roda
def colaeroda():
    keyboard.write('https://earn-654dfg.beauty/310545056525')
    keyboard.press('enter')

#encerra chrome
def encerrar():
    keyboard.press_and_release('shift+Command+w')

#roda script
def earn654():
    navegador()
    time.sleep(3)
    # fechaaba()
    # time.sleep(3)
    anonima()
    time.sleep(1)
    colaeroda()
    time.sleep(3)
    encerrar()
    time.sleep(1)
    fechaaba()
    
#laco para repetir script
while(True):
    earn654()
