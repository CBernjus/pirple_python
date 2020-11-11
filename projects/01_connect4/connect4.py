# Project # 1 - Connect 4

import os
from termcolor import colored, cprint

Height = 6
Width = 7
Colors = {
    " ": "white",
    "X": "red",
    "O": "blue"
}
WinningCoins = []


def checkCol(field, colIndex):
    if colIndex < 0 or colIndex >= Width:
        return False
    col = field[colIndex]
    return col["fill"] < Height


def placeCoin(field, colIndex, player):
    col = field[colIndex]
    col["fields"][col["fill"]] = player
    col["fill"] += 1
    return field


def drawField(field):
    os.system('clear')
    for row in range(Height * 2 + 1):
        if(row % 2 == 1):
            for col in range(Width * 2 + 1):
                if(col % 2 == 1):
                    colIndex = int(col / 2)
                    rowIndex = Height - int(row / 2) - 1
                    value = field[colIndex]["fields"][rowIndex]
                    if (colIndex, rowIndex) in WinningCoins:
                        cprint(f" {value} ", Colors[value], attrs=["reverse",
                                                                   "bold"], end="")
                    else:
                        cprint(f" {value} ", Colors[value], end="")
                else:
                    print("|", end="\n" if col == 14 else "")
        else:
            print("-" * (Width * 4 + 1))


def initField():
    field = []
    for _ in range(Width):
        col = []
        for _ in range(Height):
            col.append(" ")
        field.append({
            "fields": col,
            "fill": 0
        })
    return field


def checkWinner(field):
    board = []
    for col in field:
        board.append(col["fields"])

    for col in range(Width):
        for row in range(Height):
            player = board[col][row]
            if player == " ":
                continue

            if (col + 3 < Width and
                player == board[col + 1][row] and
                player == board[col + 2][row] and
                    player == board[col + 3][row]):
                setWinningCoins(col, row, 1, 0)
                return player

            if row + 3 < Height:
                if (player == board[col][row+1] and
                    player == board[col][row+2] and
                        player == board[col][row+3]):
                    setWinningCoins(col, row, 0, 1)
                    return player
                if (col + 3 < Width and
                    player == board[col+1][row+1] and
                    player == board[col+2][row+2] and
                        player == board[col+3][row+3]):
                    setWinningCoins(col, row, 1, 1)
                    return player
                if (col - 3 >= 0 and
                    player == board[col-1][row+1] and
                    player == board[col-2][row+2] and
                        player == board[col-3][row+3]):
                    setWinningCoins(col, row, -1, 1)
                    return player

    return None


def setWinningCoins(col, row, colDelta, rowDelta):
    for _ in range(4):
        WinningCoins.append((col, row))
        col += colDelta
        row += rowDelta


def nextTurn(field, player):
    print(player, "'s turn")
    colIndex = 0
    while True:
        colIndex = input("Choose Column: ")
        if colIndex.isnumeric() and checkCol(field, int(colIndex)):
            break
    field = placeCoin(field, int(colIndex), player)


xIsNext = True
field = initField()
while True:
    drawField(field)
    nextTurn(field, "X" if xIsNext else "O")
    winner = checkWinner(field)
    if winner != None:
        drawField(field)
        print("X" if xIsNext else "O", "has won.")
        break
    xIsNext = not xIsNext
input()
