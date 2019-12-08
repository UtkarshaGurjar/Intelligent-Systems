read me file

Program Description :

The program demonstrates the use of hill climbing algorithm to solve an n queens problem. N queens problem is described as a way to place n queens on a n*n board such that no two queens are in attacking position with one another(no 2 queens should be in same row or column or diagonal).The algorithm strives to find the solution by choosing the best successor value as the next state. The evaluation of a successor state is done by using a heuristic which is calculated by total number of threats in the current board. While proceeding with finding the solution to the problem, the algorithm can get stuck when the successors have same h value and the algorithm cannot proceed to find a lower h value state. In such situation, random restart can be used where a new board configuration is generated and the program proceeds from there. Sideways move is another approach to solve the program of local maxima, a limit on number of sideway moves is set.The algorithm randomly chooses one of the successor with the same h value as its current value and proceeds to find a solution.

Input:
The program takes 2 inputs : number of queens and number of runs. 
Output: 
For the given number of runs, four random search sequences are displayed along with the statistics for the given number of runs. The statistics includes the success percentage, failure percentage, average number of steps taken in case of success and failure. 
The output is generated for cases where the solution is found using basic hill climbing search, hill climbing search with sideway moves, Random-Restart Hill-Climbing search without sideways move, Random-Restart Hill-Climbing search with sideways move.

Initial Board :

The initial board for the program implemented is generated such that there is one queen placed per row.

Instructions to run the program : 

The algorithm is implemented using python programming language.
File name : IS_proj2.py
1.The program can be opened in Jupiter notebook or IDE like PyCharm or using command prompt.In cmd, navigate to the folder where the code is saved.
   Use 'python IS_proj2.py' to run the code
2. When prompted, enter the number of queens, n to be placed on an n*n board and enter the number of runs for generating statistics.

- An '_' represents an empty position in the n*n board. 'Q' represents the positions of queen in each row.
- Four random sequence of steps out of n runs are displayed. Each state of the board is followed by its h value. When the value of h is equal to zero, goal is reached and 'Solution found' is displayed. If the program cannot find a better solution and gets stuck at local maxima then 'Solution not found' is displayed.