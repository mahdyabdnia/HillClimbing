from random import *
from math import *


class SearchAgent(object):
    pass


class Queens:
    def __init__(self):
        self.board=[0]*8
        for i in range(8):
            self.board[i]=i
        """for i in range(8):
            newcol = randint(0, 7)

            temp = self.board[i]
            self.board[i] = self.board[newcol]
        self.board[newcol] = temp"""


    def __createRandomBoard__(self):
        for i in range(8):
            newcol = randint(0, 7)

            temp = self.board[i]
            self.board[i] = self.board[newcol]
        self.board[newcol] = temp


    def __getstate__(self):
        self.__createRandomBoard__()
        return self.board

    def __isSolve__(self):
        if self.__herustic__()==0:
            return True

    def __getGaurd__(self,qu1pos1,qu2pos2):
        [r1,c1]=qu1pos1
        [r2,c2]=qu2pos2

        if r1==r2 or c1==c2 or fabs(r1-r2)==fabs(c1-c2):
            return True

    def __herustic__(self):
        gaurd_number=0

        for x in range(8):
            for y in range(8):
                if x !=y:
                    if self.__getGaurd__([x,self.board[x]],[y,self.board[y]]):
                        gaurd_number+=1
        return gaurd_number

    def setQueen(self, queen_number, new_row_number):
        if self.board[queen_number] == new_row_number:
            return 1
        other_queen_number = -1;
        for i in range(8):  # find the other queen number
            if (self.board[i] == new_row_number):
                 other_queen_number = i;
        if other_queen_number == -1:
            return 0
        self.board[other_queen_number] = self.board[queen_number]
        self.board[queen_number] = new_row_number

        return 1


    def __showBoard__(self):

        for i in range(8):
            s = "";
            spaces = ["[ ]", "{ }"]  # stands for black & white tiles
            for j in range(self.board[i]):
                s = s + spaces[(j + i) % 2]
            if ((self.board[i] + i) % 2):
                s = s + "{#}"
            else:
                s = s + "[#]"
            for j in range(8 - self.board[i] - 1):
                s = s + spaces[(self.board[i] - 1 + j + i) % 2]
        print s













class SearchAgent:
    def __init__(self,problem):
        self.problem=problem
        self.end=False

    def searchHillClimb(self):

        nextQueen=-1;nextPlace=-1;initiaHerustic=8;

        while not self.end:

            if initiaHerustic > self.problem.__herustic__():

                self.problem.setQueen(nextQueen,nextPlace);



            for i in range(8):
                for j in range(8):
                    prvr=self.problem.board[i]
                    self.problem.setQueen(i,j)
                    if initiaHerustic < self.problem.__herustic__():
                        temp=self.problem.__herustic__()







class Solve:
    def __init__(self,solverCounter):
        self.solverCounter=solverCounter;
        self.solver=[0]*solverCounter;
        self.end=True


        for i in range(solverCounter):
            board=Queens()
            #board=board.__createRandomBoard__();
            se=SearchAgent(board)
            self.solver[i]=se

    def __allSolverDuty__(self):
        gameTheEnd=0
        if  self.end:
            return 0

        for s in self.solver:
            gameTheEnd+=(s.searchHillClimb==0)
        print "Solver ",gameTheEnd,"finish his game"

        if gameTheEnd==self.solverCounter:

            return 0

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







a=Solve(1000)
a.__showSolution__()