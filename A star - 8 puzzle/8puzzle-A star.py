class state:
    #intializes data to each state, cost(g), and initial value to f for each state
    def __init__(self,data, g, f, h, p_key):
        self.data = data
        self.g = g
        self.f = f
        self.h = h
        #key of parent node to trace back the solution path
        self.p_key = p_key
        #key of the current node
        self.s_key = key
        
    #function to calculate heuristic based on the input from the user
    def heuristic(self, inp, initial, goal):
        #for calculating misplaced tiles
        if inp == '1':
            h = 0
            for i in range(len(self.data)):
                for j in range(len(self.data)):
                    #check if position of a value(not space) in initial state and goal state is different and increment h
                    if self.data[i][j] != goal[i][j] and self.data[i][j] != '0':
                        h+=1
            return h
        #for calculating Manhattan distance
        elif inp == '2':
            h=0
            for i in range(len(self.data)):
                for j in range(len(self.data)):
                    if self.data[i][j] != '0':
                        x,y = self.find(goal,self.data[i][j])
                        #to find how many blocks away is the position of a value in initial state from the position in goal state
                        if i == x and j!=y:
                            h += abs(y-j)
                        if i!=x and j == y:
                            h += abs(x-i)
                        if i!=x and j!=y:
                            h += abs(x-i) + abs(y-j)

            return h
        
    #helper function to find the indices of a number in goal state
    def find(self,goal,num):
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if goal[i][j] == num:
                    return i,j

        
class grid:
    #intializes size, a list for storing generated states, and a list for storing expanded states
    def __init__(self,size):
        self.size = size
        self.gen = []
        self.exp = []
        
    #function to take input and goal states from a user 
    def get(self,n):
        grid = []
        for i in range(n):
            row = input().split(" ")
            grid.append(row)
        return grid
    
    #helper function to copy the parent state and form a successor state
    def copy(self, parent):
        copy_node = []
        for i in parent.data:
            elem = []
            for j in i:
                elem.append(j)
            copy_node.append(elem)
        return copy_node
    
    #function to swap positions of the space('0') and the adjacent number 
    def swap_pos(self,parent,sp_x,sp_y,val_x,val_y):
        p_copy = self.copy(parent)
        temp = p_copy[sp_x][sp_y]
        p_copy[sp_x][sp_y] = p_copy[val_x][val_y]
        p_copy[val_x][val_y] = temp
        return p_copy

    #function to calculate f
    def f(self,h, node):
          return (h + node.g)
    
    #function to generate successor states
    def generate_child(self,node):
        global key
        for i in range(len(node.data)):
            for j in range(len(node.data)):
                if node.data[i][j] == '0':
                    x=i
                    y=j
                    break
        
        adj_pos = [[x-1, y], [x+1,y], [x,y-1], [x,y+1]]
        
        children = []
        for i in adj_pos:
            #check if adjacent position is a valid position
            if i[0]>=0 and i[0]<len(node.data) and i[1]>=0 and i[1]<len(node.data):
                child = self.swap_pos(node,x,y,i[0],i[1])
                
                #increment key before assigning a new state as value in the dictionary
                key = key + 1
                child_state = state(child, node.g+1,0,0,node.s_key)
                child_state.h = child_state.heuristic(inp,self,goal)
                child_state.f = self.f(child_state.h, child_state)
                #list of successor states from 
                children.append(child_state)
                
                #add the new child state to dictionary with a unique key
                track[key]=child_state
                
        return children 
         
       
    #Asks the user for intial state, goal state, the choice of heuristic, and generates successive states
    def main(self):
        global inp
        global goal
        #unique value as key for a dictionary
        global key
        #a dictionary to store a unique key for each state
        global track
        key = 0
        track={}        
        
        print("Which heuristic?")
        print("1. Misplaced Tiles")
        print("2. Manhattan Distance")
        inp = input()
        if inp!='1' and inp!='2':
            print("Invalid choice")
            return
        
        print("Enter numbers from 1-8 for the initial state in 3x3 format(3 values in a row; 0 for blank)")
        initial = self.get(p.size)
        print("Enter numbers from 1-8 for the goal state in 3x3 format(3 values in a row; 0 for blank)")
        goal = self.get(p.size)
        
        #increment key before assigning a new state as value in the dictionary
        key = key + 1
        initial_state = state(initial,0,0,0,0)
        initial_state.h = initial_state.heuristic(inp,initial,goal)
        initial_state.f = self.f(initial_state.h, initial_state)
        
        #add initial state to dictionary
        track[key] = initial_state
        
        count_gen = 1
        self.gen.append(initial_state)
        print()

 
        while True:
            #sort the list that has the generated states in ascending order of 'f' value 
            self.gen.sort(key = lambda x:x.f, reverse=False)
            
            #get the first state(with least f value)
            first = self.gen[0]
        
            if first.h == 0:
                val = first.s_key
                break
                
            successors = self.generate_child(first)
            count_gen += len(successors)
            self.exp.append(first)
            del self.gen[0]
            for child in successors:
                self.gen.append(child)
                
        #trace back from goal state to initial state using key of the parent state
        pr = []
        key = val
        while key!= 0:
            cur_node = track[key]
            pr.append(cur_node)
            key = cur_node.p_key
        
        #sort the list in ascending order of the key
        pr.sort(key = lambda x:x.s_key, reverse=False)
           
        for k in pr:
            if k.s_key!=1:
                print("   |   ")
                print("   V   ")
            
            for i in k.data:
                print("|", end='')
                for j in i:
                    print(j, end='|')
                print()
            print("---------------------")
            print("h =", k.h, end=', ')
            print("g =", k.g, end=', ')
            print("f =", k.f)
            print("---------------------")  
            
        print("Number of nodes generated: ", end='')
        print(count_gen)
        print("Number of nodes expanded: ", end='')
        print((len(self.exp)+1))
            
p = grid(3)
p.main()