
import random
from methods import solveNQueens
from NQueensCSP import NQueensCSP

c = NQueensCSP(1000)
solved = solveNQueens(c, 100) 
solved.printBoard()



