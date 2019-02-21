import sys
from math import trunc
from graphSearch import *
from fifteenProblem import *


def main():
    input = sys.argv[1].replace('start=','').replace('.','0')

    grid = [[input[trunc(y * 4) + x] for x in range(4)] for y in range(4)]

    for i in range(4):
        for j in range(4):
            if (grid[i][j] == 'A'):
                grid[i][j] = 10
            elif (grid[i][j] == 'B'):
                grid[i][j] = 11
            elif (grid[i][j] == 'C'):
                grid[i][j] = 12
            elif (grid[i][j] == 'D'):
                grid[i][j] = 13
            elif (grid[i][j] == 'E'):
                grid[i][j] = 14
            elif (grid[i][j] == 'F'):
                grid[i][j] = 15
            else:
                grid[i][j] = int(grid[i][j])

    print(grid)
    fifteen_problem = FifteenProblem(grid)
    # print(fifteen_problem.goal_test([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]))
    print(graph_search(fifteen_problem))

if (__name__ == "__main__"):
    main()
