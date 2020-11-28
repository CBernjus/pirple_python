# Homework Assignment  # 6 - Advanced Loops

import os

terminalSize = os.get_terminal_size()


def drawBoard(rows, columns):
    # invalid input
    if ((rows * 2 - 1) > terminalSize.lines) | ((columns * 2 - 1) > terminalSize.columns):
        return False

    for i in range(rows):
        # draw vertical lines
        for j in range(columns):
            if j != (columns - 1):
                print(" |", end='')
        # line break
        print()

        # draw horizontal lines
        if i != (rows - 1):
            print("-" * (columns * 2 - 1))
    return True
