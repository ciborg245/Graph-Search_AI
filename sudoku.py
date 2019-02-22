import sys
from math import trunc, sqrt
from graphSearch import *
from sudokuProblem import *

def main():
    input = sys.argv[1].replace('start=','').replace('.','0')

    if (len(input) == 16):
        cont = 0
        for i in range(len(input)):
            if input[i] == '0':
                cont += 1

        if cont > 12:
            print("Unsolvable sudoku.")
        else:
            input = create_grid(input)
            sudoku_problem = SudokuProblem(input)
            print(graph_search(sudoku_problem))

    elif (len(input) == 81):
        cont = 0
        for i in range(len(input)):
            if input[i] == '0':
                cont += 1

        if cont > 64:
            print("Unsolvable sudoku.")
        else:
            input = create_grid(input, 9)

            sudoku_problem = SudokuProblem(input, 9)
            print(graph_search(sudoku_problem))

    else:
        print('Invalid sudoku.')


def create_grid(input, n=4):
    return [[int(input[x+y*n]) for x in range(n)] for y in range(n)]

if (__name__ == "__main__"):
    main()
