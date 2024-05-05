100#JUAN LAYRISSE U43230984
from methods import minConflicts
from NQueensCSP_2 import NQueensCSP
import time


 

print("\n\n\n")
nSelect = int(input("Please input any natural number N (Excluding 2 and 3): "))

while nSelect == 2 or nSelect == 3 or nSelect <= 0:
    nSelect = int(input("Please input any natural number N (Excluding 2 and 3): "))

start = time.time()
c = NQueensCSP(nSelect)
solved = minConflicts(c, 1000) 
end = time.time()
solved.printBoard()

result = solved.variables

if solved.checkForSolution():
    print("VALID")
else:
    print("--------------------------------------------------------F   A   I   L--------------------------------------------------------")
print("Queens: ", nSelect)
ti = end - start
print("Allotted time in seconds: ", ti)