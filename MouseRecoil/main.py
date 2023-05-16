from time import sleep
import pyautogui as pag
import win32api, win32con
from keyboard import is_pressed
from random import randint
Spread = {
    0 : 0,
    1 : 5,
    2 : -5
}

VRecoil = -20
HRecoil = -12
VMoved = 0
HMoved = 0
HeightLimit = 5
Height = 0
SwayLimit = 6
Sway = 0
Recover = False
Left = False
Swayed = False
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pag.position()[0], pag.position()[1], 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pag.position()[0], pag.position()[1], 0, 0)
try:
    RNG = True if input("Turn of spread? (y/n)") == "y" else False
    while 1:
        if is_pressed('Ctrl'):
            click()
            if Height < HeightLimit:
                # Vertical Recoil
                s = Spread[randint(0, 2)] if RNG else 0
                pag.move(s, VRecoil)
                HMoved += s
                VMoved -= VRecoil
                Height += 1
            else:
                if not Swayed:
                    if Sway < (SwayLimit // 2):
                        s = Spread[randint(0, 2)] if RNG else 0
                        pag.move(HRecoil, s)
                        VMoved -= s
                        HMoved += HRecoil
                        Sway += 1
                    else:
                        Sway = 0
                        HRecoil *= -1
                        Swayed = True
                else:
                    if Sway < SwayLimit:
                        s = Spread[randint(0, 2)] if RNG else 0
                        pag.move(HRecoil, s)
                        VMoved -= s
                        HMoved += HRecoil
                        Sway += 1
                    else:
                        Sway = 0
                        HRecoil *= -1
            Recover = True
            sleep(0.01)
        elif Recover:
            ToMoveVertical = int(VMoved / 5)
            ToMoveHorizontal = int(-HMoved / 5)
            for i in range(5):
                pag.move(ToMoveHorizontal, ToMoveVertical)
                sleep(0.01)
            VMoved = 0
            HMoved = 0
            Height = 0
            Sway = 0
            Recover = False
            Swayed = False

except KeyboardInterrupt:
    print(f"Terminated!")