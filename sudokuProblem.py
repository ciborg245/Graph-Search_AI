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
        self.total = n**n

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

        temp = [x for x in range(1, self.n + 1)]
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
        # return len(ss)
        return 1

    def h(self, states):
        last_state = states[-1]
        res = 0
        row_score = 0
        col_score = 0
        grid_score = 0
        # for i in range(self.n):
        #     row_score += sum(1 for x in range(self.n) if last_state[i][x] != 0)
            # col_score += sum(1 for x in range(self.n) if last_state[x][i] != 0)
        #
        r = trunc(sqrt(self.n))
        for i in range(0, self.n, r):
            for j in range(0, self.n, r):
                grid = [last_state[x][y] for x in range(self.n) for y in range(self.n) if trunc(y / r) == trunc(j / r) and trunc(x / r) == trunc(i / r)]
                grid_score += sum(1 for x in range(self.n) if grid[x] != 0)


        # score = trunc(row_score / (self.n-1)) + trunc(col_score / (self.n-1)) + trunc(grid_score / (self.n-1))
        score = (self.n*3 - trunc(row_score / (self.n-1)) - trunc(col_score / (self.n-1)) - trunc(grid_score / (self.n-1)))
        score += (12 - len(states)) if self.n == 4 else (84 - len(states))
        # score += 84 - len(states)

        # print(states)
        # print(score)
        # print(row_score)
        # print(col_score)
        # print(grid_score)
        return score
