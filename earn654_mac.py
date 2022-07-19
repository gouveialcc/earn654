import webbrowser
import datetime
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
    keyboard.write('https://money-t2v3.beauty/310545056525')
    keyboard.press('enter')

#encerra chrome
def encerrar():
    keyboard.press_and_release('shift+Command+w')
 
# def countdown(h, m, s):
#     # Calculate the total number of seconds
#     total_seconds = h * 3600 + m * 60 + s
 
#     # While loop that checks if total_seconds reaches zero
#     # If not zero, decrement total time by one second
#     while total_seconds > 0:
 
#         # Timer represents time left on countdown
#         timer = datetime.timedelta(seconds = total_seconds)
        
#         # Prints the time left on the timer
#         print(timer, end="\r")
 
#         # Delays the program one second
#         time.sleep(1)
 
#         # Reduces total time by one second
#         total_seconds -= 1
 
#     print("Bzzzt! The countdown is at zero seconds!")
 
# # Inputs for hours, minutes, seconds on timer
# h = input("Enter the time in hours: ")
# m = input("Enter the time in minutes: ")
# s = input("Enter the time in seconds: ")
# countdown(int(h), int(m), int(s))

#roda script
def earn654():
    navegador()
    time.sleep(3)
    # fechaaba()
    # time.sleep(3)
    anonima()
    time.sleep(1)
    colaeroda()
    time.sleep(4)
    encerrar()
    time.sleep(1)
    fechaaba()

#laco para repetir script
while(True):
    earn654()
