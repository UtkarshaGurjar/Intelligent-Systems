import random
import math

class state:
#   global variable to store the h value of each board state.
    global h_dash 
    
#   constructor of class state that initializes size, data, and h field of the board.
    def __init__(self, size, data=None):
        self.size = size
        self.data = data
        self.h = -1                                                 #initializing with a non-positive number
    
#   function that generates the initial configuration of the board.
    def generate_initial(self):
        board_s=[]
        for i in range(int(self.size)):
            col=[None]*int(self.size)
            rand = random.randint(0,int(self.size)-1)
            for j in range(int(self.size)):
                if j == rand:
                    col[j]='Q'
                else:
                    col[j]='_'
            board_s.append(col)
        self.data = board_s
        
        return self.data
    
#   function to generate a successor board by moving the queen from its current location(old_pos) to a 
#   specified location(new_pos) on the board.
    def generate_successor(self, old_pos, new_pos):
        x = new_pos[0]
        y = new_pos[1]
        
        old_x = old_pos[0]
        old_y = old_pos[1]
        
        nxt = self.copy(self.data)
        
        for i in range(0, len(nxt)):
            for j in range(0, len(nxt)):
                if i==x and j==y:
                    nxt[i][j]='Q'

                if i==old_x and j==old_y:
                    nxt[i][j]='_'
        return nxt
    
#   helper function to copy the data of the board of which a successor needs to be generated, 
#   onto a new board.
    def copy(self,prev):
        copy_board=[]
        
        for i in prev:
            squares=[]
            for j in i:
                squares.append(j)
            copy_board.append(squares)
        return copy_board
        
#   function to calculate the h value of a board.    
    def calc_h(self):
        count=0
                    
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if self.data[i][j]=='Q':
                    pos = [None]*2
                    pos[0]=i
                    pos[1]=j
                    v,d = self.findAttckPos(pos)

                    for k in range(len(self.data)):
                        for l in range(len(self.data)):
                                if self.data[k][l]=='Q':
                                    for e in v:
                                        if e[0] == k and e[1] == l:
                                            count+=1
                                    for e in d:
                                        if e[0] == k and e[1] == l:
                                            count+=1
        return math.ceil(count/2)
        
#   helper function to calculate the attack positions(vertical and diagonal) from a
#   particular position(x,y) on the board.     
    def findAttckPos(self,pos): 
        ver = []                          #an empty list to store the vertical sttack positions    
        x=pos[0]
        y=pos[1]
        
        if x==0:
            while(x < len(self.data)-1):
                attck_v=[None]*2
                x+=1

                attck_v[0]=x
                attck_v[1]=y
                ver.append(attck_v)
        
        elif x==len(self.data):
            while(x>=0):
                attck_v=[None]*2
                x-=1

                attck_v[0]=x
                attck_v[1]=y
                ver.append(attck_v)
        
        else:
            while(x < len(self.data)-1):
                attck_v=[None]*2
                x+=1

                attck_v[0]=x
                attck_v[1]=y
                ver.append(attck_v)
                
            x=pos[0]
            y=pos[1]
                
            while(x>=0):
                attck_v=[None]*2
                x-=1

                attck_v[0]=x
                attck_v[1]=y
                ver.append(attck_v)
                
        diag = []                         #an empty list to store the diagonal attack positions
        x=pos[0]
        y=pos[1]  
        #1. Checking upper left squares
        while x>0 and x<len(self.data) and y>0 and y<len(self.data):
            attck_d=[None]*2
            x-=1
            y-=1

            attck_d[0]=x
            attck_d[1]=y
            diag.append(attck_d)
            
        x=pos[0]
        y=pos[1]    
        #2. Checking lower left squares
        while x>=0 and x<len(self.data)-1 and y>0 and y<len(self.data):
            attck_d=[None]*2
            x+=1
            y-=1

            attck_d[0]=x
            attck_d[1]=y
            diag.append(attck_d)
            
        x=pos[0]
        y=pos[1]
        #3. Checking upper right squares
        while x>0 and x<len(self.data) and y>=0 and y<len(self.data)-1:
            attck_d=[None]*2
            x-=1
            y+=1

            attck_d[0]=x
            attck_d[1]=y
            diag.append(attck_d)
        
        x=pos[0]
        y=pos[1]
        #4. Checking lower right squares
        while x>=0 and x<len(self.data)-1 and y>=0 and y<len(self.data)-1:
            attck_d=[None]*2
            x+=1
            y+=1

            attck_d[0]=x
            attck_d[1]=y
            diag.append(attck_d) 
        
        return ver, diag
    
class board:
#   global variable that stores the input of number of queens to be placed on the board from a user.
    global n
    
    def __init__(self):
        self.successes = 0
        self.failures = 0
        self.steps = 0
        self.tot_sSteps = 0
        self.tot_fSteps = 0
        self.count_init = 0

#   function to find the position of the queen on a particular row on the initial board.
    def find_rowPos(self,data,row_num):    
        for j in range(len(data)):
            if data[row_num][j] == 'Q':
                pos = [None]*2
                pos[0]= row_num
                pos[1]= j     
                break
        return pos
    
#   main function
    def main(self):
        global n
        
        print("How many Queens do you want to place on the board?")
        n = input()
        
        print("How many runs?")
        r = input()
        
        print()

#       Call for Hill-Climbing search.
        print("Hill-Climbing search:")
        for x in range(int(r)):
            self.steps = 0
            self.calc_board(x)
        print()
        print("....")
        print("....")
        print("....")
        print("....")
        print("....")
        print()
        print("Hill-Climbing search stats for " + str(n) + "-Queens problem for " + str(r) + " runs:")
        print("Success Rate: ", 100*self.successes/int(r),"%")
        print("Failure Rate: ", 100*self.failures/int(r), "%")
        print("Average number of steps for successes: ", self.tot_sSteps/self.successes)
        print("Average number of steps for failures: ", self.tot_fSteps/self.failures)
        print()

#       call for Hill-climbing search with sideways move. 
        print("Hill-Climbing search with sideways move:")
        self.successes = 0
        self.failures = 0
        self.steps = 0
        self.tot_sSteps = 0
        self.tot_fSteps = 0
 
        for x in range(int(r)):
            self.steps = 0        
            self.calc_board_wSideway(x)
        print()
        print("....")
        print("....")
        print("....")
        print("....")
        print("....")
        print()
        print("Hill-Climbing search with sideways move stats for " + str(n) + "-Queens problem for " + str(r) + " runs:")
        print("Success Rate: ", 100*self.successes/int(r),"%")
        print("Failure Rate: ", 100*self.failures/int(r), "%")
        print("Average number of steps for successes: ", self.tot_sSteps/self.successes)
        print("Average number of steps for failures: ", self.tot_fSteps/self.failures)
        print()
        
#       call for random-restart without sideways move.
        print("Random-Restart Hill-Climbing search:")
        self.steps = 0
        self.count_init = 0
        for x in range(int(r)):
            y=self.steps
            self.calc_RandomRestart(0)
        print()
        print("Random-Restart Hill-Climbing search without sideways move stats for " + str(n) + "-Queens problem for " + str(r) + " runs:")
        print("Average number of random-restarts without sideways move: ", self.count_init/int(r))
        print("Average number of steps required without sideways move: ", self.steps/int(r))
        print()

#       call for random-restart with sideways move.
        self.steps = 0
        self.count_init = 0
        for x in range(int(r)):
            self.calc_RandomRestart(1)
        print()
        print("Random-Restart Hill-Climbing search with sideways move stats for " + str(n) + "-Queens problem for " + str(r) + " runs:")
        print("Average number of random-restarts with sideways move: ", self.count_init/int(r))
        print("Average number of steps required with sideways move: ", self.steps/int(r))
        print()

#   Hill-Climbing search.     
    def calc_board(self, call):
        h_dash=-1
        
        initial_board = state(n)
        initial_board.data = initial_board.generate_initial()
        initial_board.h = initial_board.calc_h()
        if call < 4:
            print("Search Sequence " + str(call+1) + ":")
            print("Initial state:")
            for x in initial_board.data:
                for y in x:
                    print(y, end=" ")
                print()
            print("h value:", initial_board.h)
            print()

        min_board = initial_board.data
        while h_dash !=0:
            store_min_hPos = []
            previous_board = state(n, min_board)
            previous_board.h = previous_board.calc_h()
            h_dash = previous_board.h
            for i in range(int(n)):
                pos = self.find_rowPos(previous_board.data,i)
                for j in range(int(n)):
                    new_pos = [None]*2
                    new_pos[0]=i
                    new_pos[1]=j
                    if new_pos == pos:
                        continue    

                    successor_board = state(n)
                    successor_board.data = previous_board.generate_successor(pos, new_pos)
                    successor_board.h = successor_board.calc_h()

                    if successor_board.h <= h_dash:
                        h_dash = successor_board.h
                        store_pos =new_pos
                        store_pos.append(successor_board.h)
                        store_min_hPos.append(store_pos)
                        
            if store_min_hPos:            
                l = len(store_min_hPos)-1
                while l>=0:
                    y = store_min_hPos[l]
                    if y[2] != h_dash:
                        del store_min_hPos[l]
                    l-=1

                rand = random.randint(0,len(store_min_hPos)-1)
                pos_dash = store_min_hPos[rand]
                del pos_dash[2]
                pos_parent = self.find_rowPos(previous_board.data,pos_dash[0])
                min_board = previous_board.generate_successor(pos_parent, pos_dash)

            if h_dash == previous_board.h:
                if h_dash == 0:
                    if call < 4:
                        print("Solution found.")
                    self.successes +=1
                else:
                    self.tot_fSteps +=self.steps
                    if call < 4:
                        for x in min_board:
                            for y in x:
                                print(y, end=" ")

                            print()
                        print("h value: " + str(h_dash))
                        print()
                        print("Solution not found.")
                        print()
                    self.failures +=1
                break

            else:
                self.steps +=1
                if call < 4:
                    print("Next state:")
                    for x in min_board:
                        for y in x:
                            print(y, end=" ")

                        print()
                    print("h value:", h_dash)
                    print()

                if h_dash==0:
                    self.tot_sSteps += self.steps
                    if call < 4:
                        print("Solution found.")
                        print()
                    self.successes += 1

#   Hill-climbing search with sieways move.
    def calc_board_wSideway(self, call):
        try_ = 0
        h_dash=-1
        
        initial_board = state(n)
        initial_board.data = initial_board.generate_initial()
        initial_board.h = initial_board.calc_h()
        if call < 4:
            print("Search Sequence " + str(call+1) + ":")
            print("Initial state:")
            for x in initial_board.data:
                for y in x:
                    print(y, end=" ")
                print()
            print("h value:", initial_board.h)
            print()

        min_board = initial_board.data
        while h_dash !=0:
            store_min_hPos = []
            self.steps +=1
            check_hHigh = 0 
            previous_board = state(n, min_board)
            previous_board.h = previous_board.calc_h()
            h_dash = previous_board.h
            for i in range(int(n)):
                pos = self.find_rowPos(previous_board.data,i)
                for j in range(int(n)):
                    new_pos = [None]*2
                    new_pos[0]=i
                    new_pos[1]=j
                    if new_pos == pos:
                        continue    

                    successor_board = state(n)
                    successor_board.data = previous_board.generate_successor(pos, new_pos)
                    successor_board.h = successor_board.calc_h()

                    if successor_board.h <= h_dash:
                        h_dash = successor_board.h
                        store_pos =new_pos
                        check_hHigh = 1
                        if successor_board.h < h_dash:
                            try_ = 0
                        store_pos.append(successor_board.h)
                        store_min_hPos.append(store_pos)
                        
            if store_min_hPos:            
                l = len(store_min_hPos)-1
                while l>=0:
                    y = store_min_hPos[l]
                    if y[2] != h_dash:
                        del store_min_hPos[l]
                    l-=1

                rand = random.randint(0,len(store_min_hPos)-1)
                pos_dash = store_min_hPos[rand]
                del pos_dash[2]
                pos_parent = self.find_rowPos(previous_board.data,pos_dash[0])
                min_board = previous_board.generate_successor(pos_parent, pos_dash)
            
            if h_dash == previous_board.h:                
                if h_dash == 0:
                    if call < 4:
                        print("Solution found.")
                        print()
                    self.tot_sSteps += self.steps
                    self.successes +=1                
                else:
                    if check_hHigh != 0:
                        try_ +=1
                        if call < 4:
                            print("Next state:")
                            for x in min_board:
                                for y in x:
                                    print(y, end=" ")

                                print()
                            print("h value:", h_dash)
                            print()                        
                    else:
                        self.tot_fSteps +=self.steps
                        self.failures +=1
                        if call < 4:
                            print("Solution not found.")
                            print()
                        break
                    if try_ >=100:
                        self.tot_fSteps +=self.steps
                        self.failures +=1
                
                        if call < 4:
                            for x in min_board:
                                for y in x:
                                    print(y, end=" ")
                                print()
                            print("h value:", h_dash)
                            print()
                            
                            print("Solution not found after 100 sideways move.")
                            print()
                        break
            else:
                if call < 4:
                    print("Next state:")
                    for x in min_board:
                        for y in x:
                            print(y, end=" ")

                        print()
                    print("h value:", h_dash)
                    print()

                if h_dash==0:
                    self.tot_sSteps += self.steps
                    if call < 4:
                        print("Solution found.")
                        print()
                    self.successes += 1

#   Random-restart.
    def calc_RandomRestart(self, sideway):
        try_=0
        h_dash=-1
        
        while h_dash != 0:
            self.count_init +=1
            initial_board = state(n)
            initial_board.data = initial_board.generate_initial()
            initial_board.h = initial_board.calc_h()
            
            if initial_board.h == 0:
                self.successes +=1
                break

            min_board = initial_board.data
            while h_dash !=0:
                store_min_hPos = []
                check_hHigh = 0
                previous_board = state(n, min_board)
                previous_board.h = previous_board.calc_h()
                h_dash = previous_board.h
                for i in range(int(n)):
                    pos = self.find_rowPos(previous_board.data,i)
                    for j in range(int(n)):
                        new_pos = [None]*2
                        new_pos[0]=i
                        new_pos[1]=j
                        if new_pos == pos:
                            continue    

                        successor_board = state(n)
                        successor_board.data = previous_board.generate_successor(pos, new_pos)
                        successor_board.h = successor_board.calc_h()

                        if successor_board.h <= h_dash:
                            if successor_board.h < h_dash:
                                try_ = 0
                            h_dash = successor_board.h
                            store_pos =new_pos                            
                            store_pos.append(successor_board.h)
                            store_min_hPos.append(store_pos)
                            check_hHigh = 1     
                
                if h_dash == 0 or check_hHigh == 0: 
                    if h_dash == 0:
                        self.steps+=1
                        self.tot_sSteps += self.steps
                        self.successes +=1

                    if check_hHigh == 0:
                        self.tot_fSteps +=self.steps
                        self.failures +=1
                    break

                if store_min_hPos:            
                    l = len(store_min_hPos)-1
                    while l>=0:
                        y = store_min_hPos[l]
                        if y[2] != h_dash:
                            del store_min_hPos[l]
                        l-=1
                    rand = random.randint(0,len(store_min_hPos)-1)
                    pos_dash = store_min_hPos[rand]
                    del pos_dash[2]
                    pos_parent = self.find_rowPos(previous_board.data,pos_dash[0])
                    min_board = previous_board.generate_successor(pos_parent, pos_dash)

                if h_dash == previous_board.h:
                    if sideway == 0:
                        break

                    if sideway == 1:
                        self.steps+=1
                        if check_hHigh != 0:
                            try_ +=1
                        if try_ >=100:
                            break
                else:
                    self.steps+=1                        


start = board()
start.main()