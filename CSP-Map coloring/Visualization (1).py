#!/usr/bin/env python
# coding: utf-8

# In[9]:


#installation commands for visualization
# for pip
# pip install cufflinks
# pip install plotly

# or pip install cufflinks plotly

# for conda-
# conda install plotly
# conda install -c conda-forge cufflinks-py
import time
import random
import csv
import plotly.graph_objects as go
import pandas as pd

#Australia Map    
aus_state_mapping={0:'Western Australia',1:'Northern Territory',2:'South Australia',3:'Queensland',4:'New South Wales',
               5:'Victoria',6:'Tasmania'}

aus_edges={
    0:[1,2],
    1:[0,2,3],
    2:[0,1,3,4,5],
    3:[1,2,4],
    4:[2,3,5],
    5:[2,4],
    6:[]
}
#USA Map
us_state_mapping={0:'Washington',1:'Oregon',2:'California',3:'Idaho',4:'Nevada',5:'Arizona',6:'Utah',7:'Montana',
              8:'Wyoming',9:'Colorado',10:'New Mexico',11:'North Dakota',12:'South Dakota',13:'Nebraska',14:'Kansas',
              15:'Oklahoma',16:'Texas',17:'Minessota',18:'Iowa',19:'Missouri',20:'Arkansas',21:'Lousiana',22:'Wisconsin',
              23:'Illinois',24:'Mississippi',25:'Michigan',26:'Indiana',27:'Kentucky',28:'Tennessee',29:'Alabama',30:'Ohio',
              31:'West Virginia',32:'Virgnia',33:'North Carolina',34:'South Carolina',35:'Georgia',36:'Florida',
              37:'Pennsylvania',38:'Maryland',39:'Delaware',40:'New Jersey',41:'New York',42:'Connecticut',43:'Hawaii',44:'Massachusetts',
              45:'Rhode Island',46:'Vermont',47:'New Hamsphire',48:'Maine',49:'Alaska'}

us_edges ={
    0:[3,1],
    1:[0,3,4,2],
    2:[1,4,5],
    3:[0,1,4,6,8,7],
    4:[1,2,5,6,3],
    5:[2,4,6,9,10],
    6:[3,4,5,10,9,8],
    7:[3,8,12,11],
    8:[7,3,6,9,13,12],
    9:[8,6,5,10,15,14,13],
    10:[5,6,9,15,16],
    11:[7,12,17],
    12:[11,7,8,13,18,17],
    13:[18,12,8,9,14,19],
    14:[13,9,15,19],
    15:[16,20,19,14,9,10],
    16:[10,15,20,21],
    17:[11,12,18,22],
    18:[17,12,13,19,23,22],
    19:[18,13,14,15,20,27,28,23],
    20:[19,15,16,21,24,28],
    21:[16,20,24],
    22:[17,18,23,25],
    23:[22,18,19,27,26],
    24:[29,21,28,20],
    25:[22,26,30],
    26:[25,23,27,30],
    27:[26,23,19,28,32,31,30],
    28:[27,19,20,24,29,35,33,32],
    29:[28,24,36,35],
    30:[25,26,27,31,37],
    31:[30,27,32,37,38],
    32:[38,31,27,28,33],
    33:[32,28,35,34],
    34:[33,35],
    35:[29,28,33,34,36],
    36:[29,35],
    37:[30,31,41,40,38,39],
    38:[31,32,39,37],
    39:[40,38,37],
    40:[39,37,41],
    41:[37,40,42,44,45,46],
    42:[40,41,44,45],
    43:[],
    44:[42,47,41,45,46],
    45:[44,42],
    46:[41,44,47],
    47:[46,44,48],
    48:[47],
    49:[]   
}

color_list = {1:'Red',2:'Blue',3:'Green',4:'Yellow',5:'Cyan',6:'Magenta',6:'Black',7:'White'}

class Map:
    def __init__(self, tot_states,state_neighbors):
        self.tot_states = tot_states
        self.state_neighbors = state_neighbors
        self.chromatic_num = 0
        self.color = [0] * self.tot_states #1 color for each state
        self.backtrack_count = 0
        
    def assignDomain(self,num):
        domain_dict = {}
        for i in range(self.tot_states):
            domain_dict[i]={}
            for n in range(1,num+1):                
                domain_dict[i][n] = 2
        return domain_dict

    def assignTrack(self,num):
        track = {}
        for i in range(self.tot_states):
            track[i]={}
            for n in range(1,num+1):                
                track[i][n] = -1                  
        return track
   
    def assignColor(self,num,domain_dict):
        visited = []
        backtracks = 0
        for state in self.state_neighbors:
            if state not in visited:
                for color in domain_dict[state]:
                    if self.checkConstraint(state, color) == False:
                        self.color[state] = color
                        visited.append(state)
                        break                  
                for neighbor in self.state_neighbors[state]:
                    if neighbor not in visited:
                        for color in domain_dict[neighbor]:
                            if self.checkConstraint(neighbor, color) == False: 
                                self.color[neighbor] = color
                                visited.append(neighbor)
                                break
                            else:
                                backtracks+=1
        return  max(self.color)        

    def checkConstraint(self, state, color): 
        for j in self.state_neighbors[state]:
            if self.color[j] == color: 
                return True
        return False      

    def colorMap(self, max_num): 
        domain_dict = self.assignDomain(max_num)
        min_chrom = self.assignColor(max_num,domain_dict)
        return min_chrom
    
    def DFS_backtrack(self,chrom_num,random_list):
        domain_dict = self.assignDomain(chrom_num)
        global status 
        global parent
        status={}
        parent={}
        self.backtrack_count=0
        for state in self.state_neighbors:
            status[state] = 10
            parent[state] = -1

        for rnd in random_list:
            state = rnd
            if status[state] == 10:
                bTrack = self.DFSvisit_backtrack(state,domain_dict)
                if bTrack == -1:
                    break
        return bTrack      
                
    def DFSvisit_backtrack(self,state,domain_dict):
        global status
        global parent
        assigned = 0
        status[state] = 20
        for c in domain_dict[state]:
            if self.checkConstraint(state, c) == False:
                if assigned == 0:
                    self.color[state] = c
                    domain_dict[state][c] = 1
                    assigned = 1
            else:
                if assigned == 0:
                    self.backtrack_count+=1
                domain_dict[state][c] = 0
        if assigned == 0:
            return -1
                
        for neighbor in self.state_neighbors[state]:
            if status[neighbor] == 10:
                parent[neighbor] = state
                bTrack = self.DFSvisit_backtrack(neighbor,domain_dict)
                if bTrack == -1:
                    return bTrack
        status[state] = 30
        return self.backtrack_count
                          
    def DFS_forwardCheck(self,chrom_num,random_list):
        global status 
        global parent
        domain_dict = self.assignDomain(chrom_num)
        track = self.assignTrack(chrom_num)
        status={}
        parent={}
        self.backtrack_count=0
        for state in self.state_neighbors:
            status[state] = 10
            parent[state] = -1

        for rnd in random_list:
            state = rnd
            if status[state] == 10:
                bTrack = self.DFSvisit_forward(state,domain_dict,track)
        return bTrack   
    
    def DFSvisit_forward(self,state,domain_dict,track):
        global status
        global parent
        assigned = 0
        prev_c = -1
        color={}
        status[state] = 20
        for c in domain_dict[state]:
            if domain_dict[state][c] == 2:
                if assigned == 0:
                    self.color[state] = c
                    domain_dict[state][c] = 1
                    assigned = 1 
                    self.reduceDomain(state,c,domain_dict,track)
                    
            elif domain_dict[state][c] == 1:
                prev_c = c
                    
        if assigned == 1 and prev_c != -1:
            self.undo(state,prev_c,domain_dict,track)
            color[prev_c] = 2 

        if assigned == 0:
            self.backtrack_count+=1
            if parent[state] != -1:
                self.DFSvisit_forward(parent[state],domain_dict,track)
                            
        for neighbor in self.state_neighbors[state]:
            if status[neighbor] == 10:
                parent[neighbor] = state
                self.DFSvisit_forward(neighbor,domain_dict,track)
        status[state] = 30
        return self.backtrack_count
    
    def reduceDomain(self,state,c,domain_dict,track):
        for neighbor in self.state_neighbors[state]:
            domain_dict[neighbor][c] = 0
            if track[neighbor][c] == -1:
                track[neighbor][c] = state
    
    def undo(self,state,c,domain_dict,track):
        for neighbor in self.state_neighbors[state]:
            if track[neighbor][c] == state and domain_dict[neighbor][c] == 0:
                domain_dict[neighbor][c] = 2

    def DFS_forwardSingleton(self,chrom_num,random_list): 
        global status 
        global parent
        domain_dict = self.assignDomain(chrom_num)
        track = self.assignTrack(chrom_num)
        status={}
        parent={}
        self.backtrack_count=0
        for state in self.state_neighbors:
            status[state] = 10
            parent[state] = -1
            
        for rnd in random_list:
            state = rnd
            if status[state] == 10:
                bTrack = self.DFSvisit_Singleton(state,domain_dict,track)
        return bTrack 
    
    def DFSvisit_Singleton(self,state,domain_dict,track):
        global status
        global parent
        assigned = 0
        prev_c = -1
        color={}
        status[state] = 20
        for c in domain_dict[state]:
            if domain_dict[state][c] == 2:
                if assigned == 0:
                    self.color[state] = c
                    domain_dict[state][c] = 1
                    assigned = 1 
                    self.reduceDomainSingleton(state,c,domain_dict,track)
            elif domain_dict[state][c] == 1:
                prev_c = c
                    
        if assigned == 1 and prev_c != -1:
            self.undoSingleton(state,prev_c,domain_dict,track)
            color[prev_c] = 2 

        if assigned == 0:
            self.backtrack_count+=1
            if parent[state] != -1:
                self.DFSvisit_Singleton(parent[state],domain_dict,track)
                            
        for neighbor in self.state_neighbors[state]:
            if status[neighbor] == 10:
                parent[neighbor] = state
                self.DFSvisit_Singleton(neighbor,domain_dict,track)
        status[state] = 30
        return self.backtrack_count
    
    def reduceDomainSingleton(self,state,c,domain_dict,track):
        for neighbor in self.state_neighbors[state]:
            check = domain_dict[neighbor][c] 
            domain_dict[neighbor][c] = 0
            if check == 2:
                colorS=self.checkSingleton(neighbor, domain_dict)
                if colorS>0:
                    self.reduceDomainSingleton(neighbor,colorS,domain_dict,track)
            if track[neighbor][c] == -1:
                track[neighbor][c] = state
                
    def checkSingleton(self,neighbor, domain_dict):
        color_dict = domain_dict[neighbor]
        count=0
        temp_c = 0
        for key in color_dict:
            if color_dict[key]==2:
                count+=1
                temp_c = key         
        if count != 1:  
            temp_c=0
            
        return temp_c
        
    def undoSingleton(self,state,c,domain_dict,track):
        for neighbor in self.state_neighbors[state]:
            if track[neighbor][c] == state and domain_dict[neighbor][c] == 0:
                domain_dict[neighbor][c] = 2                

#MAIN
def main():
    map_choice=input('Select map to be colored : \n1.Australia\n2.US\n')
    print()
    if map_choice == '1':
        state_mapping=aus_state_mapping
        edges = aus_edges
        m = Map(len(edges),edges)
        min_possible=m.colorMap(5) 
        m.chromatic_num=min_possible
        print("Minimum chromatic number possible for Australia map = ", m.chromatic_num)
        print()
        
    elif map_choice == '2':
        state_mapping=us_state_mapping
        edges = us_edges
        m = Map(len(edges),edges)
        min_possible=m.colorMap(5) 
        m.chromatic_num=min_possible
        print("Minimum chromatic number possible for US map = ", m.chromatic_num)
        print()

#Generate a random list of states
    random_list=[]
    states=[]
    states_colored = []
    for i in range(m.tot_states):
        random_list.append(i)
    random.shuffle(random_list)
    for s in random_list:
        states.append(state_mapping[s])
    print("Search starts from state: ",states[0])
    print()
    
#Print the Results
    print("1.DFS Only:")
    print()
    start = time.process_time()
    m.backtracks=0
    m.backtracks = m.DFS_backtrack(m.chromatic_num,random_list)
    end = time.process_time()
    assigned = []
    print("Number of backtracks = ", m.backtracks)
    for colors in m.color:
        assigned.append(color_list[colors])
    print("Colors assigned for states in original order = ", assigned)
    print("Time taken", (end-start), 's')
    print()
    map_color=m.color

    print("2.DFS with Forward Check:")
    print()
    start = time.process_time()
    m.backtracks=0
    m.backtracks = m.DFS_forwardCheck(m.chromatic_num,random_list)
    end = time.process_time()
    assigned = []
    print("Number of backtracks = ", m.backtracks)
    for colors in m.color:
        assigned.append(color_list[colors])
    print("Colors assigned for states in original order = ", assigned)
    print("Time taken", (end-start), 's')
    print()
        
    print("3.DFS with Forward Check and propagation through Singleton domains:")
    print()
    start = time.process_time()
    m.backtracks=0
    m.backtracks = m.DFS_forwardSingleton(m.chromatic_num,random_list)
    end = time.process_time()
    assigned = []
    print("Number of backtracks = ", m.backtracks)
    for colors in m.color:
        assigned.append(color_list[colors])
    print("Colors assigned for states in original order = ", assigned)
    print("Time taken", (end-start), 's')
    print()
        #VISUALIZATION FOR USA MAP
    states=["WA","OR","CA","ID","NV","AZ","UT","MT","WY","CO","NM","ND","SD","NE","KS","OK","TX","MN","IA","MO","AR",
       "LA","WI","IL","MS","MI","IN","KY","TN","AL","OH","WV","VA","NC","SC","GA","FL","PA","MD","DE","NJ","NY","CT",
       "HI","MA","RI","VT","NH","ME","AK"]
    if map_choice=='2':
        row_list=[]
        row_list.append(["code", "color"])
        for x,y in zip(states,map_color):
            row_list.append([x,y])
        with open('map_color.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(row_list)

        df = pd.read_csv('map_color.csv')
        fig = go.Figure(data=go.Choropleth(
            locations=df['code'], # Spatial coordinates
            z = df['color'], # Data to be color-coded
            locationmode = 'USA-states', # set of locations match entries in `locations`
            colorscale = ['Red','Blue','Green','Yellow']
        #     colorbar_title = "Millions USD",
        ))

        fig.update_layout(
            title_text = 'Coloured Map',
            geo_scope='usa', # limite map scope to USA
        )
        fig.show()


    
            
main()


# In[ ]:




