import sys
from math import trunc, sqrt
from graphSearch import *
from sudokuProblem import *

def main():
    input = sys.argv[1].replace('start=','').replace('.','0')

    input = create_grid(input, 9)

    sudoku_problem = SudokuProblem(input, 9)
    print(graph_search(sudoku_problem))

    
def create_grid(input, n=4):
    return [[int(input[x+y*n]) for x in range(n)] for y in range(n)]

if (__name__ == "__main__"):
    main()
