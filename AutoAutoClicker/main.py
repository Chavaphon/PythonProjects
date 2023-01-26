import pyautogui as pag
from time import sleep

warning = 0
timeAFKed = 0
warningLimit = 50
AFKing = False

def click():
    pag.leftClick()


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
            print(f"AFKing")
            AFKing = True
            while AFKing == True:
                lastPosition = pag.position()
                sleep(5)
                currentPosition = pag.position()
                if currentPosition != lastPosition:
                    AFKing = False
                    print(f"Back online!\n")
                    print(f"You have been AFKing for {timeAFKed} second(s)")
                    timeAFKed = 0
                else:
                    click()
                    print(f"clicked!")
                    timeAFKed += 5

        lastPosition = pag.position()
        sleep(1)
except KeyboardInterrupt:
    print(f"Terminated")