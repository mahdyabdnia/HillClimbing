from random import *
from math import *




class Queens:
    def __init__(self):
        self.board=[0]*8
        for i in range(8):
            self.board[i]=i
        for i in range(8):
            newcol = randint(0, 7)

            temp = self.board[i]
            self.board[i] = self.board[newcol]
        self.board[newcol] = temp

    def __getstate__(self):
        return self.board

    def __isSolve__(self):
        if self.__herustic__()==0:
            return 1

    def __getGaurd__(self,qu1pos1,qu2pos2):
        [r1,c1]=qu1pos1
        [r2,c2]=qu2pos2

        if r1==r2 or c1==c2 or fabs(r1-r2)==fabs(c1-c2):
            return 1

    def __herustic__(self):
        gaurd_number=0

        for x in range(8):
            for y in range(8):
                if x !=y:
                    if self.__getGaurd__([x,self.board[x]],[y,self.board[y]]):
                        gaurd_number+=1
        return gaurd_number

    def put(self, q_n, n_r_n):
        if self.board[q_n] == n_r_n:
            return 1
        other_queen_number = -1;
        for i in range(8):
            if (self.board[i] == n_r_n):
                 other_queen_number = i;
        if other_queen_number == -1:
            return 0
        self.board[other_queen_number] = self.board[q_n]
        self.board[q_n] = n_r_n

        return 1


    def __showBoard__(self):

        for i in range(8):
            b = "";
            spaces = ["[ ]", "{ }"]
            for j in range(self.board[i]):
                b += spaces[(j + i) % 2]
            if ((self.board[i] + i) % 2):
                b += "{#}"
            else:
                b += "[#]"
            for j in range(8 - self.board[i] - 1):
                b+= spaces[(self.board[i] - 1 + j + i) % 2]
        print b













class SearchAgent:
    def __init__(self,problem):
        self.problem=problem
        self.end=0



    def searchHillClimb(self):
        if self.end:
            return 0
        nextQueen=-1;nextPlace=-1;initiaHerustic=8;
        for i in range(8):
            for j in range(8):
                prev = self.problem.board[i]
                self.problem.put(i, j)
                te=self.problem.__herustic__()
                if initiaHerustic > self.problem.__herustic__():
                    nextQueen=i;nextPlace=j;initiaHerustic=te;
                self.problem.put(i,prev)
        if nextQueen==-1:
            self.end=1
            return 0
        if initiaHerustic < self.problem.__herustic__():
            self.problem.put(nextQueen,nextPlace);










class Solve:
    def __init__(self,solverCounter):
        self.solverCounter=solverCounter;
        self.solver=[0]*solverCounter;
        self.end=0


        for i in range(solverCounter):
            board=Queens()

            se=SearchAgent(board)
            self.solver[i]=se

    def __allSolverDuty__(self):
        gameTheEnd=0
        if  self.end:
            return 0

        for s in self.solver:
            if s.searchHillClimb()==0:
                gameTheEnd+=1
        print "Solver ",gameTheEnd,"finish his game"

        self.end=(gameTheEnd==self.solverCounter)
        if self.end:
            return 0
        return 1;



    def __showSolution__(self):
        answer=0;
        sol=-1;
        while not self.end:
            self.__allSolverDuty__()

        for s in self.solver:
            sol+=1
            if s.problem.__isSolve__():
                answer+=1
                print "Answer ",answer,"from solver ",sol
                s.problem.__showBoard__()
                print'\n'


        print "total Solver :",self.solverCounter,'\n'
        print "succesfull Solver",answer,'\n'
        print "sucess Rate:",((answer+0.0)/self.solverCounter)







