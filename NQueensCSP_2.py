#JUAN LAYRISSE U43230984

class NQueensCSP:

    def __init__(self, N) -> None:
        self.n = N

        
        #Dict that tracks the {QueenNum:CurrentRow}
        self.variables = self.getStartingVariables(N)


        #The domain will be a list of all possible positions for all queens (rows)
        self.domains = list(range(0,N,1))


        #Returns a dict where {Row:list of queens on that row}
        self.rowQueens = self.setDomains()


        #Will be a dictionary where {QueenNumber:List of queens attacking it}
        self.conflictQueens = self.setStartingViolationsQueens()

        



    #CONSTRAINT FUNCTIONS =======================================================================================================
    #False: Attacking each other
    #True: Not attacking: no constraints were violated
    def constraintsCheck(self, q1, q2):
        if self.variables[q1] == self.variables[q2]:
            return False
        if abs(self.variables[q1] - self.variables[q2]) == abs(q1 - q2):
            return False
        return True

    #Checks constraints but through x and y coords
    def constraintsCheck_XY(self, xy1:tuple, xy2:tuple):
        if xy1[1] == xy2[1]:
            return False
        if abs(xy1[1] - xy2[1]) == abs(xy1[0] - xy2[0]):
            return False
        return True

    #Checks constraints between a queen and an xy coord
    def constraintsCheck_Q_XY(self, xy1:tuple, q2):
        if xy1[1] == self.variables[q2]:
            return False
        if abs(xy1[1] - self.variables[q2]) == abs(xy1[0] - q2):
            return False
        return True

    #given an x and y, will check if there are any queens in the horizontal and diagonal
    def constraintCheckSpace(self, x, y):
        if len(self.rowQueens[y]) != 0:
            return False
        
        
        mul = 1
        while True:
            it = 0


            if self.variables.get(x - mul, -1) != -1:
                if self.variables[x - mul] == (y - mul):
                    return False
            else:
                it += 1


            if self.variables.get(x - mul, -1) != -1:
                if self.variables[x - mul] == (y + mul):
                    return False
            else:
                it += 1


            
            if self.variables.get(x + mul, -1) != -1:
                if self.variables[x + mul] == (y - mul):
                    return False
            else:
                it += 1



            if self.variables.get(x + mul, -1) != -1:
                if self.variables[x + mul] == (y + mul):
                    return False
            else:
                it += 1

            if it >= 3:
                break
            mul += 1
        return True

    #Returns a list of all the queens the coordinate is attacking 
    def constraintCheckGetQueens(self, x, y):
        res = []
        
        #add horizontal queens within LOS

        #Position  of the queen on the list 
        self.rowQueens[y] = sorted(self.rowQueens[y])
        pos = self.rowQueens[y].index(x)

        if len(self.rowQueens[y]) > 1:
            if pos != 0:
                res.append(self.rowQueens[y][pos - 1])
            if pos != len(self.rowQueens[y]) - 1:
                res.append(self.rowQueens[y][pos + 1])
        



        #Up left check
        mul = 1
        while x - mul > -1 and y - mul > -1:
            if self.variables.get(x - mul, -1) != -1:
                if self.variables[x - mul] == (y - mul):
                    res.append(x - mul)
                    break
            mul += 1
        

        #Down left check
        mul = 1
        while x - mul > -1 and y + mul < self.n:
            if self.variables.get(x - mul, -1) != -1:
                if self.variables[x - mul] == (y + mul):
                    res.append(x - mul)
                    break
            mul += 1

        
        #Up right check
        mul = 1
        while x + mul < self.n and y - mul > -1:
            if self.variables.get(x + mul, -1) != -1:
                if self.variables[x + mul] == (y - mul):
                    res.append(x + mul)
                    break
            mul += 1

        #Down right check 
        mul = 1
        while x + mul < self.n and y + mul < self.n:
            if self.variables.get(x + mul, -1) != -1:
                if self.variables[x + mul] == (y + mul):
                    res.append(x + mul)
                    break
            mul += 1
            
        
        return res


    #Takes a current state and checks how many total conflict there are.
    #Requires an updated conflict queens dict for that specific state
    #cq is dict {queen#: list of queens attacking it}
    def checkConflictsCurrentState(self):
        total = 0
        #runs through every queen 
        for q in range(0, self.n):
            for c in self.conflictQueens[q]:
                if c > q:
                    total += 1
        return total 




    #UNUSED============================================
    #Given a queen and row it could move to, check how many conflicts there are in that row 
    def checkConflictsWithRows(self, q, r):
        #Number of conflicts per row on current column 
        res = {}
        




    #SETUP FUNCTIONS ===============================================================================================================

    #Sets queens all along the top of the board to begin
    def getStartingVariables(self, N):
        vars = {}
        for x in range(0, N):
            vars[x] = 0
        return vars
    
    #Takes the current list of variables and returns a dict where {Row:list of queens on row}
    def setDomains(self):
        res = {}
        #Run through every queen
        for q in self.domains:
            val = self.variables[q]
            if res.get(val, -1) == -1:
                res[val] = [q]
            else:
                res[val].append(q)
        return res

    #Returns starting violations dict, where {Queen#:list of queens attacking it}
    def setStartingViolationsQueens(self):
        res = {}

        for queen in range(0, self.n):
            if queen == 0:
                res[queen] = [1]
            elif queen == self.n - 1:
                res[queen] = [self.n - 2]
            else:
                res[queen] = [queen - 1, queen + 1]
        return res





    #SELECTING VARIABLE FUNCTION ==================================================================================================
    
    #Will return the number of the queen with the most amount of conflicts
    #pq is the previously moved queen 
    #MOST CONSTRAINING VARIABLE
    #Chose variable that has most constraints on it 
    def chooseMaxConflictedVar(self, pq):
        maxCons = 0
        maxConsQueen = 0

        for q in range(0, self.n):
            if q == pq:
                continue
            if len(self.conflictQueens[q]) > maxCons:
                maxCons = len(self.conflictQueens[q])
                maxConsQueen = q
        
        
        
        return maxConsQueen
    

        
    #MISCELLANEOUS FUNCTIONS =======================================================================================================
    

    #Checks if the current state is a valid solution 
    def checkForSolution(self):
        for q in range(0, self.n):
            for qc in range(q + 1, self.n):
                if not self.constraintsCheck(q, qc):
                    return False
        return True

    #Should also change the conflicts dict, takes in the queen and where it will be moving 
    def update(self, row, queen):
        oldRow = self.variables[queen]

        self.rowQueens[oldRow].remove(queen)


        #Updating the Row Queens
        if self.rowQueens.get(row, -1) == -1:
                self.rowQueens[row] = [queen]
        else:
            self.rowQueens[row].append(queen)
            self.rowQueens[row] = sorted(self.rowQueens[row])






        #Updating the conflictQueens

        #list of queens whos lists also need to be edited
        queensList = self.conflictQueens[queen]
        #print(queensList)
        #print("-------------------------------")

        #Update queens where it moved away from 
        for qe in queensList:
            self.conflictQueens[qe].remove(queen)


        #Updating variables 
        self.variables[queen] = row

        #ADDED THIS SECTION
        for qe in queensList:
            self.conflictQueens[qe] = self.constraintCheckGetQueens(qe, self.variables[qe])
            self.conflictQueens[qe] = list(dict.fromkeys(self.conflictQueens[qe]))


        #Sets new list for queen for new position 
        self.conflictQueens[queen] = self.constraintCheckGetQueens(queen, row)
        self.conflictQueens[queen] = list(dict.fromkeys(self.conflictQueens[queen]))
        

        #Update queens that are now in line of sight
        for qi in self.conflictQueens[queen]:
            self.conflictQueens[qi].append(queen)
            self.conflictQueens[qi] = list(dict.fromkeys(self.conflictQueens[qi]))

    #Print the current state of the board
    def printBoard(self):
        for y in range(0, self.n):
            for x in range(0, self.n):
                if self.variables[x] == y:
                    print("1", end = ' ')
                else:
                    print("0", end = " ")
            print("")



