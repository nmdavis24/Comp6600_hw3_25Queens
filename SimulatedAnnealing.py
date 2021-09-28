import random
import copy
import math

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
    currentStep = 1
    # initial 25 columns from left to right
    for i in range(1, 25):
        tempBoard = copy.deepcopy(RandomNeighbor(board, currentStep))
        if (tempBoard != [[]]):
            conflicts = GetConflicts(tempBoard)
            print("Step " + str(currentStep) + " (" + str(conflicts) + "):\n" + "\n".join(' '.join(str(x) for x in row) for row in tempBoard))#str(tempBoard))
            board = copy.deepcopy(tempBoard)
            currentStep = currentStep + 1       
        else:
            print("Step " + str(currentStep) + ": Failed")
        
    
    
    while (conflicts != 0):
            for i in range(25):
                for j in range(25):
                    if board[j][i] == "q":
                        tempBoard = copy.deepcopy(RandomNeighbor(board, currentStep))
                        if (tempBoard != [[]]): 
                            conflicts = GetConflicts(tempBoard)                            
                            print("Step " + str(currentStep) + " (" + str(conflicts) + "):\n" + "\n".join(' '.join(str(x) for x in row) for row in tempBoard))#str(tempBoard))
                            board = copy.deepcopy(tempBoard)
                            currentStep = currentStep + 1
                            if (conflicts == 0):
                                print("Nice!")
                                return
                        else:
                            print("Step " + str(currentStep) + ": Failed")   
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

def RandomNeighbor(board, epoch):
    temperature = 10
    newBoard = [[]]
    randomNeighbor = []
    while len(randomNeighbor) < 6:
        num = random.randint(0, 24)
        if num not in randomNeighbor:
            randomNeighbor.append(num)
    bestNeighbor = 500
    colQueenRow = []
    
    betterFound = False
    temp = copy.deepcopy(board)
    for j in randomNeighbor:  
        for i in range(25):
            if temp[i][j] == "q":
                colQueenRow.append(i)                                
    randRow = random.randint(0,24)
    for j in range(5):
            for h in range(25):
                temp[h][randomNeighbor[j]] = "w"
            #temp[colQueenRow[j]][randomNeighbor[j]] = "w" 
            if (randRow != colQueenRow[j]):
                temp[randRow][randomNeighbor[j]] = "q"
                newConfs = GetConflicts(temp)
                oldConfs = GetConflicts(board)
                diff = newConfs - oldConfs
                t = temperature / float(epoch)
                metro = math.exp(-diff/t)
                if  diff < 0 or random.random() < metro:
                    newBoard = copy.deepcopy(temp)
                    return newBoard
                    # betterFound = True
                    # bestNeighbor = newConfs
                # elif newConfs == oldConfs or newConfs < bestNeighbor:
                #     if (betterFound is False):
                #         newBoard = copy.deepcopy(temp)
            temp = copy.deepcopy(board)
           
    return [[]] 
    # if (betterFound):
    #     return newBoard
    # else:
    #     beepboop = random.randint(0,1)
    #     # 50% pick random
    #     if (beepboop == 0):
    #         boopbeep = random.randint(0, 24)
    #         newCol = random.randint(0, 5)
    #         for h in range(25):
    #             temp[h][randomNeighbor[newCol]] = "w"      
    #         temp[boopbeep][randomNeighbor[newCol]] = "q"
    #         return copy.deepcopy(temp)
    #     # 50% pick least bad 
    #     else:
    #         return newBoard
    
Queens();