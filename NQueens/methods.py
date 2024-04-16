
from NQueensCSP import NQueensCSP
import random


#Solving algo that uses minimum conflicts heuristic
def solveNQueens(csp:NQueensCSP, MaxSteps:int):

   
    current = csp
  

    
    for i in range(0, MaxSteps):
        print(i)
        if current.checkForSolution():
            return current
        
        #Gets random queen coordinate
        var = current.queenCoords[random.randint(0, len(csp.queenCoords) - 1)]
        current.update(var)

        #Moves the queen to the coordinate that has the least conflict between the other queens
    print("--------------------------------------------------------F   A   I   L--------------------------------------------------------")
    return 0


        
