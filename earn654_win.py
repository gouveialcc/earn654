import webbrowser
import keyboard
import time
from torch import true_divide

#abre o navegador
def navegador():
    #url = 'https://localhost:80'
    #webbrowser.get('chrome').open(url)
    webbrowser.open('https://localhost:80')
    
#nova aba
def abreaba():
    keyboard.press_and_release('ctrl+t')
    
#fecha aba
def fechaaba():
    keyboard.press_and_release('ctrl+w')

#abre aba anonima
def anonima():
    keyboard.press_and_release('ctrl+shift+n')

#cola link e roda
def colaeroda():
    keyboard.write('https://earn-a8gn2.beauty/567636693945')
    keyboard.press('enter')

#encerra chrome
def encerrar():
    keyboard.press_and_release('ctrl+w')

#roda script
def earn654():
    navegador()
    time.sleep(4)
    #abreaba()
    #time.sleep(2)
    #fechaaba()
    #time.sleep(2)
    anonima()
    time.sleep(3)
    colaeroda()
    time.sleep(5)
    encerrar()
    time.sleep(2)
    fechaaba()

#laco para repetir script
while(True):
    earn654()
