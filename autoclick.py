import keyboard
import mouse
import time

isClicking = False

def set_clicker():
    global isClicking
    isClicking = not isClicking
    print("Включено" if isClicking else "Отключено")

keyboard.add_hotkey("Alt + Z", set_clicker)

while True:
    if isClicking:
        mouse.click(button= "left")
        time.sleep(1)