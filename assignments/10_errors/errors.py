# Homework Assignment # 11 - Errors

# Slimmed Down And Simplified Version Of The Second Project

from random import randint

options = ["r", "a", "o", "w", "l"]


# Dummy implementations of needed functions

def randomWord():
    return ["Hello", "World", "Bye", "Thanks", "Welcome"][randint(0, 5)]


def chooseWord():
    return input("Choose a word: ")


def playGame(word):
    print("Start Playing")
    print(word)


# Modified function

def chooseOption():
    word = ""
    try:
        option = int(input("Choose an option: "))
        if option == 1:
            # Player vs Computer
            word = randomWord().upper()
        elif option == 2:
            # Player vs Player
            word = chooseWord().upper()
    except ValueError as e:
        print(str(e))
        return chooseOption()
    finally:
        playGame(word)
