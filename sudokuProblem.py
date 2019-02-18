from math import sqrt, trunc

def is_move_possible(state, i, j, a, entries):
    if a in state[i]:
        return False
    if a in [state[x][j] for x in range(entries)]:
        return False
    r = sqrt(entries)
    if a in [state[x][y] for x in range(entries) for y in range(entries) if trunc(y / r) == trunc(j / r) and trunc(x / r) == trunc(i / r)]:
        return False

    return True

class SudokuProblem(object):

    def __init__(self, initial, n=4):
        self.initial = initial
        self.n = n

    def actions(self, state):
        res = []

        for i in range(self.n):
            for j in range(self.n):
                if (state[i][j] == 0):
                    for a in range(1, self.n + 1):
                        if is_move_possible(state, i, j, a, self.n):
                            temp = []
                            for k in state:
                                temp.append(k[:])
                            temp[i][j] = a
                            res.append(temp)

        # print(res)
        return res

    def result(self, s, a):
        return a

    def goal_test(self, state):
        for i in range(self.n):
            if 0 in state[i]:
                return False

        temp = [x for x in range(1,self.n + 1)]
        for i in range(self.n):

            col = [state[x][i] for x in range(self.n)]
            col.sort()

            if temp != col:
                return False

            rowCopy = state[i][:]
            rowCopy.sort()

            if temp != rowCopy:
                return False

        r = trunc(sqrt(self.n))
        for i in range(0, self.n, r):
            for j in range(0, self.n, r):
                grid = [state[x][y] for x in range(self.n) for y in range(self.n) if trunc(y / r) == trunc(j / r) and trunc(x / r) == trunc(i / r)]
                grid.sort()

                if temp != rowCopy:
                    return False

        return True

    def step_cost(self, s, a, s_prime):
        return 1

    def path_cost(self, ss):
        return len(ss)

    def h(self, state):
        print(states)
        return 0
