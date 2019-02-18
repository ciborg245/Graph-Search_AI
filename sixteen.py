import sys
# from math import trunc, sqrt
from graphSearch import *
from sudokuProblem import *

def main():
    input = sys.argv[1].replace('start=','').replace('.','0')

    input = create_grid(input, 9)

    # asdf = [1, 2, 0, 4]
    #
    # cont = sum(1 for x in range(4) if asdf[x] != 0)
    #
    # print(cont)

    # sudoku_problem = SudokuProblem(input, 9)
    # print(graph_search(sudoku_problem))


    # print([input[x][y] for x in range(4) for y in range(4) if trunc(y / 2) == trunc(3 / 2) and trunc(x / 2) == trunc(0 / 2)])

    # input = [[2,4,3,1],[3,1,4,2],[1,3,2,4],[4,2,1,3]]
    # print(goal_test(input))
    # r = 2
    # for i in range(0, 4, r):
    #     for j in range(0, 4, r):
    #         grid = [input[x][y] for x in range(4) for y in range(4) if trunc(y / r) == trunc(j / r) and trunc(x / r) == trunc(i / r)]
            # grid.sort()

            # print(grid)/

def create_grid(input, n=4):
    return [[int(input[x+y*n]) for x in range(n)] for y in range(n)]

if (__name__ == "__main__"):
    main()
