#Play Connect

global ThisPlayer
global GameFinished

Board = []

for i in range(8):
    Board.append([])
for i in range(8):
    for j in range(9):
        Board[i].append([])

#print (Board)

def InitialiseBoard(Board):
    for i in range(1,7):
        for j in range(1,8):
            Board[i][j] = "_"
    return

def SetUpGame():

    global ThisPlayer
    global GameFinished
    ThisPlayer = "O"
    GameFinished = False
    return 

def OutputBoard(Board):
    print()

    print("   ",1," ",2," ",3," ",4," ",5," ",6," ",7)
    print()
    for i in range(6,0,-1):
        print (i, end=" ")
        for j in range(1,8):
            print(" ", Board[i][j],end=" ")
        print (" ", i)
        print ()
    print("   ",1," ",2," ",3," ",4," ",5," ",6," ",7)
    print()
    return

def ThisPlayerMakesMove(Board):
    ValidColumn = ThisPlayerChoosesColumn(Board)
    ValidRow = FindNextFreePositionInColumn(Board,ValidColumn)
    Board[ValidRow][ValidColumn] = ThisPlayer
    

    return ValidRow, ValidColumn

def ThisPlayerChoosesColumn(Board):
    print ("Player", ThisPlayer, "'s turn.")
    ColumnNumber = int(input ("Enter a valid column number:"))
    while not ColumnNumberValid(Board, ColumnNumber):
        ColumnNumber = int(input ("Enter a valid column number:"))

    return ColumnNumber

def ColumnNumberValid(Board, ColumnNumber):
    Valid = False
    if ColumnNumber >= 1 and ColumnNumber <= 7:
        if Board[6][ColumnNumber] == "_":
            Valid = True
    

    return Valid


def FindNextFreePositionInColumn(Board,ValidColumn):
    ThisRow = 1
    while Board[ThisRow][ValidColumn] != "_":
        ThisRow+=1
    

    return ThisRow

def CheckIfThisPlayerHasWon(Board, ValidRow, ValidColumn):
    global ThisPlayer
    global GameFinished
    WinnerFound = False
    WinnerFound = CheckHorizontalLineInValidRow(ValidRow)
    if WinnerFound == False:
        WinnerFound = CheckverticalLineInValidColumn(ValidRow, ValidColumn)
    if WinnerFound == True:
        GameFinished = True
        print(ThisPlayer, "is the winner")
    else:
        CheckForFullBoard(Board)
        
    return 

def CheckHorizontalLineInValidRow(ValidRow):
    for i in range(1,5):
        if (Board[ValidRow][i] == ThisPlayer and
            Board[ValidRow][i+1] == ThisPlayer and
            Board[ValidRow][i+2] == ThisPlayer and
            Board[ValidRow][i+3] == ThisPlayer):
            return True

    return False

def CheckverticalLineInValidColumn(ValidRow, ValidColumn):
    if (ValidRow == 4 or ValidRow ==5 or ValidRow == 6):
        if (Board[ValidRow][ValidColumn] == ThisPlayer and
            Board[ValidRow - 1][ValidColumn] == ThisPlayer and
            Board[ValidRow - 2][ValidColumn] == ThisPlayer and
            Board[ValidRow - 3][ValidColumn] == ThisPlayer):
            return True
    
    return False

def CheckForFullBoard(Board):
    global GameFinished
    for i in range(6,0,-1):
        for j in range(1,8):
            if Board[i][j] == "_":
                return

    print("It is a draw")
    GameFinished = True
    

    return

def SwapThisPlayer():
    global ThisPlayer
    if ThisPlayer == "O":
        ThisPlayer = "X"
    else:
        ThisPlayer = "O"

    return



#Start Game

InitialiseBoard(Board)
#print (Board)

SetUpGame()
#print (ThisPlayer, GameFinished)

OutputBoard(Board)

while GameFinished == False:
    ValidRow, ValidColumn = ThisPlayerMakesMove(Board)
    OutputBoard(Board)
    CheckIfThisPlayerHasWon(Board, ValidRow, ValidColumn)
    if GameFinished == False:
        SwapThisPlayer()


