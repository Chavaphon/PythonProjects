import pyautogui as pag
from time import sleep
from random import randint
keylist = {
    1 : "a",
    2 : "d",
}
warning = 0
timeAFKed = 0
warningLimit = 50
AFKing = False

def move():
    x = keylist[randint(1, 2)]
    pag.keyDown(x)
    sleep(0.2)
    pag.keyUp(x)

lastPosition = pag.position()
sleep(1)
try:
    while 1:
        currentPosition = pag.position()
        if currentPosition == lastPosition:
            warning += 1
            print(f"Warning! {warning}/{warningLimit}")
        else:
            warning = 0
            print(f"Warning resets")
            AFKing = False

        if warning >= warningLimit:
            move()
            print(f"AFKing")
            AFKing = True
            while AFKing == True:
                lastPosition = pag.position()
                sleep(0.2)
                currentPosition = pag.position()
                timeAFKed += 0.4
                if currentPosition != lastPosition:
                    AFKing = False
                    print(f"Back online!\n")
                    print(f"You have been AFKing for {timeAFKed} second(s)")
                    timeAFKed = 0
                else:
                    move()
                    print(f"moved!")


        lastPosition = pag.position()
        sleep(1)
except KeyboardInterrupt:
    print(f"Terminated")
