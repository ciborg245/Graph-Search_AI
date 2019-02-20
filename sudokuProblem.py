from math import sqrt, trunc, log, exp, e, ceil

def is_move_possible(state, i, j, a, entries, grids = None):
    if a in state[i]:
        return False
    if a in [state[x][j] for x in range(entries)]:
        return False
    r = sqrt(entries)
    if not grids:
        if a in [state[x][y] for x in range(entries) for y in range(entries) if trunc(y / r) == trunc(j / r) and trunc(x / r) == trunc(i / r)]:
            return False
    else:
        if a in grids[3*trunc(i/3)+trunc(j/3)]:
            return False
    return True

class SudokuProblem(object):

    def __init__(self, initial, n = 4):
        self.initial = initial
        self.n = n
        self.total = n**n

    def actions(self, state):
        res = []

        grids = []
        r = trunc(sqrt(self.n))
        for i in range(0, self.n, r):
            for j in range(0, self.n, r):
                grids.append([state[x][y] for x in range(self.n) for y in range(self.n) if trunc(y / r) == trunc(j / r) and trunc(x / r) == trunc(i / r)])

        for i in range(self.n):
            for j in range(self.n):
                if (state[i][j] == 0):
                    for a in range(1, self.n + 1):
                        if is_move_possible(state, i, j, a, self.n, grids):
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

        moves = 0
        if len(states) > 1:
            second_to_last_state = states[-2]
            # grids = []

            # r = trunc(sqrt(self.n))
            # for i in range(0, self.n, r):
            #     for j in range(0, self.n, r):
            #         grids.append([second_to_last_state[x][y] for x in range(self.n) for y in range(self.n) if trunc(y / r) == trunc(j / r) and trunc(x / r) == trunc(i / r)])

            for i in range(self.n):
                for j in range(self.n):
                    if (second_to_last_state[i][j] != last_state[i][j]):
                        moves = 1
                        for a in range(1, self.n + 1):
                            if last_state[i][j] != a:
                                if is_move_possible(second_to_last_state, i, j, a, self.n):
                                    moves += 1

        # print(states)
        # score = 140 - trunc(e*len(states)) + 5**moves
        score = self.n + trunc(exp(moves)) - ceil(log(len(states), 2))
        # print(score)
        return score
