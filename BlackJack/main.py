import random as rng
AI = 0
you = 0
stop = False
cardList = [10, 10, 10, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2,
            10, 10, 10, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2,
            10, 10, 10, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2,
            10, 10, 10, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2]

def addCards(player):
    cardsAmount = len(cloneCardList)
    cardsPositon = rng.randint(1, cardsAmount - 1)
    amount = cloneCardList[cardsPositon]
    cloneCardList.pop(cardsPositon)

    return player + amount
try:
    while stop == False:

        cloneCardList = cardList
        AI = 0
        you = 0
        start = input("Welcome to BlackJack. ""ENTER"" to start!")
        if start == "":
            stop = False
        else:
            stop = True
            print("Bruh, why did you play then...")


        AI = addCards(AI)
        you = addCards(you)
        print(f"AI = {AI}\n")
        print(f"You = {you}\n")

        ask = (input("Hit(""enter"") or Stand(0)"))
        while ask != "0":
            if ask != "0":
                you = addCards(you)
                print(f"You = {you}\n")
            ask = (input("Hit(""enter"") or Stand(0)"))
        while AI < 16:
            AI = addCards(AI)

        print(f"AI = {AI}\n")
        print(f"You = {you}\n")

        if you == 21:
            if AI == 21:
                print("Tie!!!")
                continue
            else:
                print("YOU WON!!!")
                continue
        elif AI == 21 and you != 21:
            print("You lost...")
            continue

        if you > AI:
            if you < 21:
                print("YOU WON!!!")
                continue
            else:
                print("You lost...")
                continue
        elif AI > you:
            if AI < 21:
                print("You lost...")
                continue
            else:
                print("YOU WON!!!")
                continue

        again = input("GG. Wanna play again?(""ENTER"" to play again)")
        if again == "":
            stop = False
        else:
            stop = True

except KeyboardInterrupt:
    print("Terminated")
