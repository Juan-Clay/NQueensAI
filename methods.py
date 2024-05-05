#JUAN LAYRISSE U43230984

from NQueensCSP_2 import NQueensCSP
from NQueensCSP_DUMMY import NQueensCSP_DUMMY
import random

#new conflicts function, takes the selected current CSP and queen to move and returns state that has lest conflicts
#oR is the queens original row
def conflicts(CSP, q, oR):
        
        #starts as N^2, running min for conflicts of all rows 
        minConflicts = CSP.n * CSP.n
        #keeps track of the current conflicts 
        current = 0

        #for whatever the minimum conlficts is, this will keep track of the rows that have this 
        listOfRows = []

        #Will run through all the queens domain to find what value is the min-Conflict
        for r in CSP.domains:

            #new state to analyze its new conflicts
            copyCSP = NQueensCSP_DUMMY(CSP.n, CSP.variables, CSP.rowQueens, CSP.conflictQueens)
            
            #update state with current row being checked 
            copyCSP.update(r, q)

            #Sets the current equal to the conflicts in the current state
            current = copyCSP.checkConflictsCurrentState()
            
            #compares current state conflicts with the minimum found 
            if current < minConflicts:

                #Creates new min and updates list of rows 
                minConflicts = current
                listOfRows.clear()
                listOfRows.append(r)

            #Checks if the list of rows with this amount of conflicts needs to be updated. 
            if current == minConflicts:
                listOfRows.append(r)
        
        #list of rows will have a list of all rows that have the min amount of conflicts

        #remove the queens origial row if it exists

        
        if len(listOfRows) == 1:
             return listOfRows[0]

        if oR in listOfRows:
             listOfRows.remove(oR)

        #Randomly chooses what value to go with, in short term does not matter since all have same conflict val
        select = random.randint(0, len(listOfRows) - 1)

        return listOfRows[select]




#Solving algo that uses minimum conflicts heuristic
def minConflicts(csp:NQueensCSP, MaxSteps:int):

    current = csp
    prev = -1

    for i in range(0, MaxSteps):
        
       #Check for solution 
        if current.checkForSolution():
            return current
        

        #Gets queen with most amount of conflicts with it 
        queen = current.chooseMaxConflictedVar(prev)

        #sets previous queen 
        prev = queen

        #-1 means no queen is conflicted 
        if queen == -1:
            return current
        
        #Select row where queen will go 
        val = conflicts(current, queen, current.variables[queen])

        #Update the current CSP with the queens new position 
        current.update(val, queen)

    return current


        
