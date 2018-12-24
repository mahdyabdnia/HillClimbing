from random import *
from math import *

class Queens:
    def __init__(self):
        self.board=[0]*8
        for i in range(8):
            self.board[i]=i


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

        if r1==r2 | c1==c2 | fabs(r1-r2)==fabs(c1-c2):
            return True

    def __herustic__(self):
        gaurd_number=0

        for x in range(8):
            for y in range(8):
                if x !=y:
                    if self.__getGaurd__([x,self.board[x]],[y,self.board[y]]):
                        gaurd_number+=1
        return gaurd_number




