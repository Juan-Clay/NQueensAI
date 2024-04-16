

class NQueensCSP:
    def __init__(self, N) -> None:
        self.n = N

        

        #Will be a list where each value is a tuple of a position on the chess board
        self.variables = self.getVariables(N)

        self.queenCoords = []

        #The domain will be a dict where the key will be a tuple with the coords and the value will be either 1 or 0, 1 being the presence of a queen 
        #Queens will begin all on the top row
        self.domains = self.getStartingDomains(self.variables)

        

        #Will be a dictionary where they key will be the a tuple of a position on a chess board, and the value will be a list of all the positions that coord cannot be equal to
        self.constraints = self.getConstraints(self.variables, N)


        self.solution = None



    #SETUP FUNCTIONS !!!DO NOT CALL!!!=======================================================================



    #sets up the variables
    def getVariables(self, N):
        res = []
        for y in range(0, N):
            for x in range(0, N):
                res.append((x, y))
        return res
    

    #Sets up the starting domains
    def getStartingDomains(self, vars):
        doms = {}

        for x in vars:
            doms[x] = 0
            if x[1] < 1:
                doms[x] = 1
                self.queenCoords.append(x)
        return doms
    

    #returns a list of all the spots that cannot be equal to 1 while the given is equal to 1, just returns a list of all the spots it has to check 
    def getSpaceConstraints(self, coord, N):
        res = []

        #================================================================
        #Get vertical spaces
        for y in range(0, N):
            if y != coord[1]:
                res.append((coord[0], y))
        #================================================================

        #================================================================
        #Get horizontal spaces
        for x in range(0, N):
            if x != coord[0]:
                res.append((x, coord[1]))
        #================================================================

        #================================================================
        #Get diagonal spaces
        check = False
        for d in range(1, N + 1):
            check = False
            
            # -, -
            if (coord[0] - d) >= 0 and (coord[1] - d) >= 0:
                check = True
                res.append((coord[0] - d, coord[1] - d))

            # +, -
            if (coord[0] + d) < N and (coord[1] - d) >= 0:
                check = True
                res.append((coord[0] + d, coord[1] - d))

            # -, +
            if (coord[0] - d) >= 0 and (coord[1] + d) < N:
                check = True
                res.append((coord[0] - d, coord[1] + d))

            # +, +
            if (coord[0] + d) < N and (coord[1] + d) < N:
                check = True
                res.append((coord[0] + d, coord[1] + d))


            if check == False:
                break
        return res
        #================================================================



    def getConstraints(self, vars, N):
        cons = {}

        for v in vars:
            cons[v] = self.getSpaceConstraints(v, N)

        return cons
    


    #SETUP FUNCTIONS !!!DO NOT CALL!!!=======================================================================



    #SOLVING FUNCTIONS=======================================================================================

    #checks if a given coord is valid, True if valid, False if not valid
    def checkCoordinate(self, coord):

        #If the var has a zero, not worth to check if there are ones on the lines
        if self.domains[coord] == 0:
            return True
        
        #Checks if the queen has any other queens it can attack
        for c in self.constraints[coord]:
            if self.domains[c] == 1:
                return False
            
        return True

        



    #Checks if the current domains do not disagree with any constrains
    def checkForSolution(self):

        #Loop that checks all variables
        for v in self.variables:
            if self.checkCoordinate(v):
                continue
            else:
                return False
        return True
    


    #Checks how many queens the given coordinate is in conflict with
    def checkQueenConflict(self, coord, givenQueen):
        sum = 0
        for q in self.queenCoords:
            if q == givenQueen:
                continue
            for c in self.constraints[q]:
                #c is the current square that the queen is attacking
                if c == coord:
                    sum += 1
                    break
        return sum


    #Returns a coordinate on the board with the least amount of conflicts compared to the other queens
    def conflicts(self, coord):
        
        conflictCount = 0
        minConflicts = self.n
        minConflictsCoord = coord

        #loop goes through the queens column in order to find the square with minimum conflicts
        for y in range(0, self.n):
            if y == coord[1]:
                continue
            conflictCount = self.checkQueenConflict((coord[0], y), coord)

            if conflictCount < minConflicts:
                minConflictsCoord = (coord[0], y)
                minConflicts = conflictCount
        return minConflictsCoord


        

      


    #takes a coordinate of presumably a queen and moves it to the given coord, along with updating anything needing updating
    def moveQueen(self, coord, target):
        if self.domains[coord] == 0:
            print("This is not a queen")
            return 
        
        self.queenCoords[self.queenCoords.index(coord)] = target
        self.domains[coord] = 0
        self.domains[target] = 1

    #called in the minConflict function, will update the whole CSP and return nothing
    def update(self, coord):
        self.moveQueen(coord, self.conflicts(coord))



    #SOLVING FUNCTIONS=======================================================================================


    def printBoard(self):
        for y in range(0, self.n):
            for x in range(0, self.n):
                print(self.domains[(x,y)], end = ' ')
            print("")






