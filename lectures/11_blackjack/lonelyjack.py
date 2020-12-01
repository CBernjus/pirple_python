from deck import Deck
from player import Player
import os


def clear_screen():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system('clear')


def print_logo():
    print("""  _                     _           _            _    
 | |    ___  _ __   ___| |_   _    | | __ _  ___| | __
 | |   / _ \\| '_ \\ / _ \\ | | | |_  | |/ _` |/ __| |/ /
 | |__| (_) | | | |  __/ | |_| | |_| | (_| | (__|   < 
 |_____\\___/|_| |_|\\___|_|\\__, |\\___/ \\__,_|\\___|_|\\_\\
 ------------------------ |___/ ----------------------
    """)


def drawCards(deck, number):
    return [deck.cards.pop() for _ in range(number)]


def printHouse(house_hand):
    printArr = []
    for card in house_hand:
        printArr.append(str(card))
    printArr[0] = "XX"
    print("House: " + ' '.join(printArr))


printLogo()
cardDeck = Deck()
cardDeck.random()

playerOne = Player(drawCards(cardDeck, 2))
house = Player(drawCards(cardDeck, 2))

print(playerOne)
printHouse(house.hand)
