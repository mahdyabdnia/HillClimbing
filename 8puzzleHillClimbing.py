from random import random
import math



class Search:
     problem=EightPuzzle();
    def __hillClimbing__(self,problem):
       current=problem.getStartState();

        while not current.__isSolved__():
           current_value= current.__mantahan__();
           for s in current.__nextStep__():
               s_value=s.__mantahan__()

               if s_value < current_value:
                   current=s






































class EightPuzzle:

    def __init__(self):
        self.goal=[[0,0,0],[0,0,0],[0,0,0]]
        i=0
        while i<9:
            self.goal[i/3][i%3]=i+1
            i+=1
        self.empty=2,2





    def __genreate__(self):
        a=[[[1,2,3],[4,6,5],[0,8,7]],[[2,3,1],[4,6,5],[8,7,0]],[[1,2,4],[3,5,8],[0,6,7]]]
        self.board=[[0,0,0],[0,0,0],[0,0,0]]
        self.board=a[math.floor(random()*3)]
        x=0;y=0;
        for i in range(0,2):
            for j in range(0,2):
                if self.board[i][j]==0:
                    x=i;y=j;
        self.curt=x,y


    def __getStartState__(self):
        return self.board

    def __isSolved__(self):
        for i in range(0,8):
            if self.board[i/3][i%3]==self.goal[i/3][i/3]:
                return 1
            else :
                return 0


    def __goUp__(self):
        i,j=self.empty;
        if j==0:
            return False
        else:
            self.board{i}[j]=self.board[i][j-1];
            self.board[i][j-1]=0
            self.empty=i,j-1;

    def __goDown__(self):
        i,j=self.empty;
        if j==2:
            return False;
        else:
            self.board[i][j]=self.board[i][j+1];
            self.board[i][j+1]=0
            self.empty=i,j+1


    def __goLeft__(self):
        i,j=self.empty;
        if i==0:
            return False;
        else:
            self.board[i][j]=self.board[i-1][j];
            self.board[i-1][j]=0;
            self.empty=i-1,j;


    def __goRight__(self):
        i,j=self.empty
        if i==2:
            return False
        else:
            self.board[i][j]=self.board[i+1][j]
            self.board[i+1][j]=0
            self.empty=i+1,j

    def __nextStep__(self):
        self.nextMove=[];



        self.nextMove=[self.__goUp__(),self.__goDown__(),self.__goRight__(),self.__goLeft__()]


    def __mantahan__(self):
        distance=0
        x=0;y=0
        for i in range(0,8):
            for j in range(0,2):
                for h in range(0,2):
                    if(self.board[j][h]==i+1):
                        x=j;
                        y=h;
             distance+=math.abs(self.board[x][y])+math.abs(self.goal[i/3][i%3])
        distance=(int)math.sqrt(distance)
        return distance;

    def __show__(self):
        print self.board[0]
        print self.board[1]
        print self.board[2]






























