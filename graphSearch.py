from sudokuProblem import *

def a_star(frontier, problem):
    shortest = None
    shortest_score = None

    # for path in frontier:
    #     if not shortest or problem.path_cost(shortest) + problem.h(shortest) > problem.path_cost(path) + problem.h(path):
            # shortest = path
    for path in frontier:
        path_score = problem.path_cost(path) + problem.h(path)
        if not shortest or shortest_score > path_score:
            shortest = path
            shortest_score = path_score

    print(shortest_score)
    return shortest

def graph_search(problem):
    frontier = [[problem.initial]]
    explored = []

    # while True:
    for n in range(1000):
        if len(frontier):
            path = a_star(frontier, problem)
            # print("frontier:", frontier)
            print(n)
            print("path: ", path)
            print("len: ", len(path))
            # print(n)

            s = path[-1]
            frontier.remove(path)
            explored.append(s)

            if problem.goal_test(s):
                print(n)
                print("Solution: ", s)
                print("Solved.")
                return path

            for a in problem.actions(s):
                result = problem.result(s, a)

                if result not in explored:
                    new_path = path[:]
                    new_path.append(result)

                    frontier.append(new_path)

        else:
            print("No solution.")
            return False
