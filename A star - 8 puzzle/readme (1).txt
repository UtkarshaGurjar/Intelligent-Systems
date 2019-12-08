R E A D M E
-----------

Program Description : 

The program takes an 8 puzzle problem with an initial state and goal state as input along with the choice of heuristic function to solve the problem. It uses A* algorithm to compute and display the path taken from initial state to goal state. Along with the path, the g value( path cost), h value( heuristic value) and f value ( sum of g and h) of every state is displayed. The program also outputs the total number of nodes generated and expanded while solving the problem.


Instructions to run the code : 

The code is written in python. File name : 'is_proj_1.py'

1. In cmd, navigate to the folder where the code exists. Enter below command to run the program:
   python is_proj_1.py

2. Enter heuristic = 1 if you wish to solve the problem using 'misplaced tiles' as heuristic function 
	           = 2 if you wish to solve the problem using 'manhattan distance' as heuristic function.

3. Provide 2 arrays 'initial state' and 'goal state' in the following format:

   - Values are given as rows with each element separated by spaces.
	eg. 1 2 3 (enter)
	    4 5 6 (enter)
	    7 8 0 (enter)
	
   where '0' is used to represent a blank space in which the tile could be moved.

