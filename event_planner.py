"""
add docstrings

add flags for choosing which algos, and whether both/1 constraint
eg -gbd1 or -bd2 or -bd or ... for default

-h or -help or help for instruction info


also reorganise to do loops for each algo, instead of bunchhh of reused code
maybe have a class which has
enjoyment, solution attributes
and a time getter/starter method
"""

from time import time
from os import getcwd
from argparse import ArgumentParser

from algorithms.components import read_from_file, print_solution, print_header

from algorithms.bruteforce import bruteforce_bothconstraints, bruteforce_costonly
from algorithms.dynamic import dynamic_costonly, dynamic_bothconstraints
from algorithms.greedy import greedy_costonly, greedy_bothconstraints

INPUT_DIRECTORY = getcwd() + '/inputs/'
ALGORITHMS = {
    "bruteforce": {
        1: bruteforce_costonly,
        2: bruteforce_bothconstraints,
        "name": "BRUTE FORCE ALGORITHM"
    },
    "dynamic": {
        1: dynamic_costonly,
        2: dynamic_bothconstraints,
        "name": "DYNAMIC ALGORITHM"
    },
    "greedy": {
        1: greedy_costonly,
        2: greedy_bothconstraints,
        "name": "GREEDY HEURISTIC ALGORITHM"
    }
}

def timed_func_run(func, *args):
    """
    """
    start_time = time()
    enjoyment, solution = func(*args)
    running_time = time() - start_time

    return enjoyment, solution, running_time

def parse_args():
    parser = ArgumentParser(description="""Data Structures & Algorithms group coursework for ECM1414
    Contains an Event Planner system that calculates and displays the most optimal selection of possible activities, 
    within a given budget (and additionally timeframe) that produces the maximum enjoyment.
    By default runs all 3 algorithms and both 1 constraint (cost) and 2 constraints (cost&time)""")

    #mandatory string arg
    parser.add_argument("input_file")

    #optional algorithm mode flags
    parser.add_argument("-b", action="store_true", help="Run bruteforce algorithm")
    parser.add_argument("-d", action="store_true", help="Run dynamic algorithm")
    parser.add_argument("-g", action="store_true", help="Run greedy heuristic algorithm")

    #optional algorithm constraint number (1/2 = cost/cost+time) flags
    parser.add_argument("-1", dest="v1", action="store_true", help="Use just cost constraint")   #arg name cant be integer, so store as v1/v2 (for 1 and 2)
    parser.add_argument("-2", dest="v2", action="store_true", help="Use time and cost constraints")

    args = parser.parse_args()

    selected_algos = []
    if args.b:
        selected_algos.append("bruteforce")
    if args.d:
        selected_algos.append("dynamic")
    if args.g:
        selected_algos.append("greedy")

    #if no algorithms specified, run all
    if len(selected_algos) == 0:
        selected_algos = ["bruteforce", "dynamic", "greedy"]

    selected_constraint_num = []
    if args.v1:
        selected_constraint_num.append(1)
    if args.v2:
        selected_constraint_num.append(2)

    #if no constriant num specified, run both
    if len(selected_constraint_num) == 0:
        selected_constraint_num = [1,2]

    return args.input_file, selected_algos, selected_constraint_num


def perform_algorithms(activities, time_budget, cost_budget, selected_algos, selected_constraint_nums):
    """
    add docstring
    """

    for algorithm in selected_algos:
        for constraint_num in selected_constraint_nums:
            func = ALGORITHMS[algorithm][constraint_num]
            algo_title = ALGORITHMS[algorithm]["name"]
            try:
                if constraint_num == 1:
                    enjoyment, solution, running_time = timed_func_run(func, activities, cost_budget)
                    algo_title += "(cost only)"
                    print_solution(algo_title, enjoyment, solution, time_budget, running_time)
                else:
                    enjoyment, solution, running_time = timed_func_run(func, activities, time_budget, cost_budget)
                    algo_title += "(cost & time)"
                    print_solution(algo_title, enjoyment, solution, time_budget, running_time)
            except Exception as e:
                print('\n--- ', algo_title, ' ---')
                print("Error ocurred while running algorithm")
                print(e)
                print("\nExecution Time:', exec_time, 'seconds")


def main():
    """
    """
    input_file, selected_algos, selected_constraint_nums = parse_args()

    activities, time_budget, cost_budget = read_from_file(f'{INPUT_DIRECTORY}{input_file}')

    if len(activities) == 0 or time_budget < 0 or cost_budget < 0:
        print("Ending program... please check the file you input and try again")
        return
    
    print_header(input_file, time_budget, cost_budget)
    
    perform_algorithms(activities, time_budget, cost_budget, selected_algos, selected_constraint_nums)


if __name__ == '__main__':
    main()
