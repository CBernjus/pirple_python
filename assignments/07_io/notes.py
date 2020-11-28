# Homework Assignment # 8 - I/O

import os

options = ["r", "a", "o", "w", "l"]


def printLines(lines):
    print()
    for i in range(len(lines)):
        print(i, lines[i], end="\n")
    print()


def takeNote():
    print("Please enter a filename: ")
    filename = input()
    option = "w"
    if os.path.isfile(filename):
        printHelp()

        chosenOption = input("Choose: ").lower()
        if chosenOption in options:
            option = chosenOption

        if option == "o" or option == "d":
            os.remove(filename)
            if option == "d":
                return
            option = "w"

        if option == "r" or option == "l":
            lines = open(filename, "r").read().splitlines()
            printLines(lines)

            if option == "l":
                linenumber = int(
                    input("Please select line number (first is 0): "))
                lines[linenumber] = getInputString()
                open(filename, "w").write("\n".join(lines))
            return

    noteFile = open(filename, option)
    print("A new note was created.\n")

    noteFile.write(getInputString() + "\n")
    noteFile.close()


def getInputString():
    print("What do you want to remember?")
    return input()


def printHelp():
    print("- Available Options -")
    print(" R : Read file")
    print(" A : Append to file")
    print(" L : Replace line")
    print(" O : Overwrite file")
    print(" D : Delete file")
    print("-------------------")


takeNote()
