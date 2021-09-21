import random
import copy

def Queens():
    board = [["q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q","q"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"],
         ["w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w","w"]]

    completedRows = []
    conflicts = 25
    currentColumn = 1
    # initial 25 columns from left to right
    for i in range(1, 25):
        tempBoard = copy.deepcopy(BestNeighbor(board, 0, i))
        if (tempBoard != [[]]):
            conflicts = GetConflicts(tempBoard)
            print("Step " + str(currentColumn) + " (" + str(conflicts) + "):\n" + "\n".join(' '.join(str(x) for x in row) for row in tempBoard))#str(tempBoard))
            board = copy.deepcopy(tempBoard)         
        else:
            print("Step " + str(currentColumn) + ": Failed")
        currentColumn = currentColumn + 1
    
    
    while (conflicts != 0):
            for i in range(25):
                for j in range(25):
                    if board[j][i] == "q":
                        tempBoard = copy.deepcopy(BestNeighbor(board, j, i))
                        if (tempBoard != [[]]):
                            conflicts = GetConflicts(tempBoard)
                            print("Step " + str(currentColumn) + " (" + str(conflicts) + "):\n" + "\n".join(' '.join(str(x) for x in row) for row in tempBoard))#str(tempBoard))
                            board = copy.deepcopy(tempBoard)                                   
                        else:
                            print("Step " + str(currentColumn) + ": Failed")
         
                currentColumn = currentColumn + 1   
#
def Check(newBoard, newCol, newRow):    
    # check sideways
    for i in range(25):
        if (i != newCol and newBoard[newRow][i] == "q"):
            return False
    # top left diagonal
    for i, j in zip(range(newRow, -1, -1), range(newCol, -1, -1)):
        if i != newRow and j != newCol and newBoard[i][j] == "q":
            return False
    # bottom left diagonal
    for i, j in zip(range(newRow, 25, 1), range(newCol, -1, -1)):
        if i != newRow and j != newCol and newBoard[i][j] == "q":
            return False
    # top right diagonal
    for i, j in zip(range(newRow, -1, -1), range(newCol, 25, 1)):
        if i != newRow and j != newCol and newBoard[i][j] == "q":
            return False
    # bottom right diagonal
    for i, j in zip(range(newRow, 25, 1), range(newCol, 25, 1)):
        if i != newRow and j != newCol and newBoard[i][j] == "q":
            return False 
         
    return True

def GetConflicts(newBoard):
    confs = 0
    for i in range(25):
        for j in range(25):
            if (newBoard[i][j] == "q"):
                if (Check(newBoard, j, i) is False):
                    confs = confs + 1
                    
    return confs

def BestNeighbor(board, row, column):
    newBoard = [[]]
    randomNeighbor = [column]
    for i in range(5):
        randomNeighbor.append(random.randint(0, 24))
    bestNeighbor = 500
    colQueenRow = []
    betterFound = False
    temp = copy.deepcopy(board)
    for j in randomNeighbor:  
        for i in range(25):
            if temp[i][j] == "q":
                colQueenRow.append(i)                                
     
    for j in range(5):
        temp = copy.deepcopy(board)        
        for k in range(25):
            temp[colQueenRow[j]][randomNeighbor[j]] = "w" 
            if (k != colQueenRow):
                temp[k][j] = "q"
                newConfs = GetConflicts(temp)
                oldConfs = GetConflicts(board)
                if  newConfs < oldConfs and newConfs < bestNeighbor:
                    newBoard = copy.deepcopy(temp)
                    betterFound = True
                    bestNeighbor = newConfs
                elif newConfs == oldConfs or newConfs < bestNeighbor:
                    if (betterFound is False):
                        newBoard = copy.deepcopy(temp)
                temp[k][j] = "w"
                             
            temp[colQueenRow[j]][randomNeighbor[j]] = "q" 
            
    if (betterFound):
        return newBoard
    else:
        beepboop = random.randint(0,1)
        # 50% pick random
        if (beepboop == 0):
            boopbeep = random.randint(0, 24)
            newCol = random.randint(0, 5)       
            temp[boopbeep][newCol] = "q"
            return copy.deepcopy(temp)
        # 50% pick least bad 
        else:
            return newBoard
    
Queens();