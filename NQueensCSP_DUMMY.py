#JUAN LAYRISSE U43230984

from NQueensCSP_2 import NQueensCSP



class NQueensCSP_DUMMY(NQueensCSP):

    def __init__(self, N, vars, rq, cq) -> None:

        self.n = N

        
        #Dict that tracks the {QueenNum:CurrentRow}
        self.variables = vars


        #The domain will be a list of all possible positions for all queens (rows)
        self.domains = list(range(0,N,1))


        #Returns a dict where {Row:list of queens on that row}
        self.rowQueens = rq


        #Will be a dictionary where {QueenNumber:List of queens attacking it}
        self.conflictQueens = cq
