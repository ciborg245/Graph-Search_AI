from math import trunc

class FifteenProblem(object):
    def __init__(self, initial):
        self.initial = initial

    def actions(self, state):
        res = []
        pos_i = None
        pos_j = None

        for i in range(4):
            for j in range(4):
                if state[i][j] == 0:

                    if i - 1 >= 0:
                        temp = []
                        for k in state:
                            temp.append(k[:])

                        temp[i][j], temp[i-1][j] = temp[i-1][j], temp[i][j]
                        res.append(temp)
                    if i + 1 <= 3:
                        temp = []
                        for k in state:
                            temp.append(k[:])

                        temp[i][j], temp[i+1][j] = temp[i+1][j], temp[i][j]
                        res.append(temp)
                    if j - 1 >= 0:
                        temp = []
                        for k in state:
                            temp.append(k[:])

                        temp[i][j], temp[i][j-1] = temp[i][j-1], temp[i][j]
                        res.append(temp)
                    if j + 1 <= 3:
                        temp = []
                        for k in state:
                            temp.append(k[:])

                        temp[i][j], temp[i][j+1] = temp[i][j+1], temp[i][j]
                        res.append(temp)

        # print(res)
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
                    if (state[i][j] != i*4 + j + 1):
                        return False

        return True

    def step_cost(self, s, a, s_prime):
        return 1

    def path_cost(self, ss):
        # return len(ss)
        return 1

    def h(self, states):
        score = 0
        last_state = states[-1]
        # h1 = 0
        # h1 = sum([1 for x in range(4) for y in range(4) if last_state[x][y] != x*4 + y + 1 and last_state[x][y] != 0])
        # print(last_state)
        # print(h1)
        line = [last_state[x][y] for x in range(4) for y in range(4)]

        # print(last_state)
        # print(line)
        # pos_x = None
        # pox_y = None
        # for x in range(4):
        #     for y in range(4):
        #         if last_state[x][y] == 0:
        #             pos_x = x
        #             pos_y = y

        # mod_zero = pos_x % 4
        # div_zero = trunc(pos_y / 4)


        # h2 = sum([\
        #     (abs((line[x]-1) % 4 - x % 4) + abs(trunc((line[x]-1) / 4) - trunc(x / 4)))\
        #     # (abs((line[x]-1) % 4 - mod_zero) + abs(trunc((line[x]-1) / 4) - div_zero))*(line[x])\
        #     for x in range(16)\
        #     if line[x] != 0])
        # print(h2)

        h2 = 0
        for x in range(16):
            if line[x] != 0:
                h2 += abs((line[x]-1) % 4 - x % 4) + abs(trunc((line[x]-1) / 4) - trunc(x / 4))

                if (x % 4) < 3:
                    temp = []
                    for k in last_state:
                        temp.append(k[:])
                    temp[trunc(x / 4)][x % 4], temp[trunc(x / 4)][x % 4 + 1] = temp[trunc(x / 4)][x % 4 + 1], temp[trunc(x / 4)][x % 4]
                    if (temp[trunc(x / 4)][x % 4] - 1 == x) and (temp[trunc(x / 4)][x % 4 + 1] - 1 == x + 1):
                        # print(last_state)
                        # print(temp)
                        h2 += 2

                if trunc(x / 4) < 3:
                    temp = []
                    for k in last_state:
                        temp.append(k[:])
                    temp[trunc(x / 4)][x % 4], temp[trunc(x / 4) + 1][x % 4] = temp[trunc(x / 4) + 1][x % 4], temp[trunc(x / 4)][x % 4]
                    if (temp[trunc(x / 4)][x % 4] - 1 == x) and (temp[trunc(x / 4) + 1][x % 4] - 1 == x + 4):
                        # print(last_state)
                        # print(temp)
                        h2 += 2

        # score = max(h1, h2)
        # score = h1 + h2
        # print(last_state)
        # print(h2)
        score = h2

        return score
