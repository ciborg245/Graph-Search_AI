import sys
from math import trunc
from graphSearch import *
from sixteenProblem import *


def main():
    input = sys.argv[1].replace('start=','').replace('.','0')

    grid = [[input[trunc(y * 4) + x] for x in range(4)] for y in range(4)]

    for i in grid:
        for j in i:
            if (j == 'A'):
                j = 10
            elif (j == 'B'):
                j = 11
            elif (j == 'C'):
                j = 12
            elif (j == 'D'):
                j = 13
            elif (j == 'E'):
                j = 14
            elif (j == 'F'):
                j = 15

    print(grid)
    # sixteen_problem = SixteenProblem(grid)
    # print(graph_search(sixteen_problem))

if (__name__ == "__main__"):
    main()
