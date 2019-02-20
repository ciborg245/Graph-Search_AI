class SixteenProblem(object):
    def __init__(self, initial):
        self.initial = initial

    def actions(self, state):
        res = []
        pos_i = None
        pos_j = None

        for i in range(4):
            for j in range(4):
                if state[i][j] == '0':

                    if i - 1 >= 0:
                        state[i][j], state[i-1][j] = state[i-1][j], state[i][j]
                        temp = []
                        for k in state:
                            temp.append(k[:])

                        res.append(temp)
                    if i + 1 <= 3:
                        state[i][j], state[i+1][j] = state[i+1][j], state[i][j]
                        temp = []
                        for k in state:
                            temp.append(k[:])

                        res.append(temp)
                    if j - 1 >= 0:
                        state[i][j], state[i][j-1] = state[i][j-1], state[i][j]
                        temp = []
                        for k in state:
                            temp.append(k[:])

                        res.append(temp)
                    if j + 1 <= 3:
                        state[i][j], state[i][j+1] = state[i][j+1], state[i][j]
                        temp = []
                        for k in state:
                            temp.append(k[:])

                        res.append(temp)

        print(res)
        return res

    def result(self, s, a):
        return a

    def goal_test(self, state):
        for i in range(4):
            for j in range(4):
                if (i == 3 and j == 3):
                    if state[i][j] != 0:
                        return False
                else:
                    if not (state[i][j] != i*4 + j + 1):
                        return False

        return True

    def step_cost(self, s, a, s_prime):
        return 1

    def path_cost(self, ss):
        return 1

    def h(self, states):
        score = 0
        last_state = states[-1]
        print(last_state)
        h1 = sum([1 for x in range(4) for y in range(4) if last_state[x][y] != x*4 + y + 1])

        score = h1

        return h1
