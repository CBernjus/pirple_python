# Project # 2 - Hangman

# Credit: words_alpha.txt from https://github.com/dwyl/english-words
# Credit: ascii art from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

import hangman_ascii

import os
from random import randint


max_errors = len(hangman_ascii.HANGMANPICS) - 1


def clearScreen():
    os.system('clear')


def printTitle():
    print(hangman_ascii.TITLE, end="\n")


def printOptions():
    print('''
    1 - Player vs. Computer
    2 - Player vs. Player
    ''')


def printWord(word, revealed):
    for i in range(len(word)):
        if revealed[i]:
            print(word[i] + " ", end="")
        else:
            print("_ ", end="")
    print()


def printGallowsAndErrors(wrongChars):
    print(hangman_ascii.HANGMANPICS[len(wrongChars)])
    print("\nErrors:", ", ".join(wrongChars).upper())


def randomWord():
    wordsFile = open("projects/02_hangman/words_alpha.txt")
    words = wordsFile.read().splitlines()
    wordsFile.close()
    return words[randint(0, len(words))]


def chooseWord():
    word = input("\nExecutioner, please type in a word: ")
    return word


def revealChar(word, char, revealed):
    for i in range(len(word)):
        if word[i] == char:
            revealed[i] = True
    return revealed


def playGame(word):
    wrongChars = []
    revealed = [False] * len(word)
    while True:
        clearScreen()
        printWord(word, revealed)
        printGallowsAndErrors(wrongChars)
        if len(wrongChars) >= max_errors:
            return endGame(False, word)
        elif all(r for r in revealed):
            return endGame(True, word)
        char = ""
        while True:
            char = input("\nPick a character: ").upper()
            if len(char) == 1 and char.isalnum() and char not in wrongChars:
                break
        if char in word:
            revealed = revealChar(word, char, revealed)
        else:
            wrongChars.append(char)


def chooseOption():
    option = int(input("Choose an option: "))
    if option == 1:
        # Player vs Computer
        word = randomWord().upper()
        playGame(word)
    elif option == 2:
        # Player vs Player
        word = chooseWord().upper()
        playGame(word)
    else:
        return chooseOption()


def startGame():
    clearScreen()
    printTitle()
    printOptions()
    chooseOption()


def endGame(won, word):
    print()
    if won:
        print("You saved the victim! \\(^^)/")
        print("New game (Y/N)?")
    else:
        print("You were too slow! T.T")
        print("The word was: " + word)
        print("Wanna try again (Y/N)?")
    if input().upper() == "Y":
        clearScreen()
        startGame()


startGame()
