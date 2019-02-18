from sudokuProblem import *

def a_star(frontier, problem):
    shortest = None
    for path in frontier:
        if not shortest or problem.path_cost(shortest) + problem.h(shortest) > problem.path_cost(path) + problem.h(path):
            shortest = path
    return shortest

def graph_search(problem):
    frontier = [[problem.initial]]
    explored = []

    # while True:
    for n in range(2):
        if len(frontier):
            path = a_star(frontier, problem)
            # print("frontier:", frontier)
            print("path: ", path)


            s = path[-1]
            explored.append(s)

            if problem.goal_test(s):
                print("solved")
                return path

            for a in problem.actions(s):
                result = problem.result(s, a)
                # print("result: ", result)

                if result not in explored:
                    new_path = []
                    new_path = path[:]
                    new_path.append(result)

                    frontier.append(new_path)

        else:
            return False
