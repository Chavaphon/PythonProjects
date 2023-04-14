import pyautogui
from time import sleep
import keyboard

MatchCounter = 0
WinCounter = 0
try:
    print(f"Initiating...")
    sleep(3)
    while not keyboard.is_pressed("q"):
        if pyautogui.locateOnScreen("Play.PNG", confidence=0.8):
            pyautogui.click(963, 853)
            MatchCounter += 1
            print(f"Started!")
            sleep(1)
        else:
            print(f"Playing...")
            if pyautogui.locateOnScreen("Victory.PNG", confidence=0.8):
                WinCounter += 1
            pyautogui.click(1281, 1002)
            sleep(1)
    print(f"Played {MatchCounter} matches\n Win rate: {(WinCounter / MatchCounter) * 100}%")
    print(f"Terminated!")
except KeyboardInterrupt:
    print(f"Played {MatchCounter} matches\n Win rate: {(WinCounter / MatchCounter) * 100}%")
    print(f"Terminated!")