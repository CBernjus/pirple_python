def drawField(field):
    for row in range(5):
        if(row % 2 == 0):
            for col in range(5):
                if(col % 2 == 0):
                    print(field[int(row / 2)][int(col / 2)],
                          end="\n" if col == 4 else "")
                else:
                    print("|", end="")
        else:
            print("-----")


def checkWinner(field):
    for i in range(3):
        if(field[i][0] == field[i][1] == field[i][2] and field[i][0] != " "):
            return field[i][0]
        if(field[0][i] == field[1][i] == field[2][i] and field[0][i] != " "):
            return field[0][i]
        if(field[1][1] != " " and (field[0][0] == field[1][1] == field[2][2] or field[0][2] == field[1][1] == field[2][0])):
            return field[1][1]
    return None


xIsNext = True
field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

while(True):
    print("It's " + ("X" if xIsNext else "O") + "'s Turn.")
    row = int(input("Row: "))
    col = int(input("Col: "))
    if(row < 0 or row > 2 or col < 0 or col > 2 or field[row][col] != " "):
        print("Please Choose an other field")
        continue

    field[row][col] = "X" if xIsNext else "O"
    xIsNext = not xIsNext
    drawField(field)
    winner = checkWinner(field)
    if(winner != None):
        print(winner, "has won.")
        break
    print("")
