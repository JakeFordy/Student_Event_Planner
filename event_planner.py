"""
event_planner.py is the main python file to run the whole program.

When ran in the terminal, it must be followed by the input_file argument. For example:
>> python event_planner.py input_small.txt

There are also optional flags which can be typed to choose which specific algorithms to run and
with how many constraints (time/cost), using the argparse library:
  -h, --help  Brings up a help paragraph and description of tags
  -b          Run bruteforce algorithm
  -d          Run dynamic algorithm
  -g          Run greedy heuristic algorithm
  -1          Use just cost constraint
  -2          Use time and cost constraints

Flags can be combined and rearranged in any order.

If no algorithm flags are entered, by default all 3 will run.
If no constaint number flag is entered, by default algorithms will run on both 1 and 2 constraints.

All algorithm python scripts are imported from separate files, and so are the general components,
such as file reading, formatted printing and constants.
"""

from time import time
from os import getcwd
from argparse import ArgumentParser

from algorithms.components import read_from_file, print_solution, print_header, NAME

from algorithms.bruteforce import bruteforce_bothconstraints, bruteforce_costonly
from algorithms.dynamic import dynamic_costonly, dynamic_bothconstraints
from algorithms.greedy import greedy_costonly, greedy_bothconstraints

# CONSTANTS: 
INPUT_DIRECTORY = getcwd() + '/inputs/'
# dictionary mapping to all the functions for easy access/calling
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

def timed_func_run(func: callable, *args):
    """
    Starts a timer and runs the passed-in callable function, including its arguments.
    It ends the timer as soon as function ends and stores the enjoyment and solution,
    returning the overall enjoyment, solution and running time
    """
    start_time = time()
    enjoyment, solution = func(*args)
    running_time = time() - start_time

    return enjoyment, solution, running_time

def parse_args():
    """
    Defines all the arguments that are passed in when running the python script eg:
    >> python event_planner.py input_small.txt -gfb2
    Looks up which flag corresponds to what algorithm or constraint number.
    Returns the filename, algorithm list, constrain number list
    """

    parser = ArgumentParser(description="""Data Structures & Algorithms group coursework for ECM1414
    Contains an Event Planner system that calculates and displays the most optimal selection of possible activities, 
    within a given budget (and additionally timeframe) that produces the maximum enjoyment.
    By default runs all 3 algorithms and both 1 constraint (cost) and 2 constraints (cost&time)""")

    # mandatory string arg
    parser.add_argument("input_file")

    # optional algorithm mode flags
    parser.add_argument("-b", action="store_true", help="Run bruteforce algorithm")
    parser.add_argument("-d", action="store_true", help="Run dynamic algorithm")
    parser.add_argument("-g", action="store_true", help="Run greedy heuristic algorithm")

    # optional algorithm constraint number (1/2 = cost/cost+time) flags
    # arg name cant be integer, so store as v1/v2 (for 1 and 2)
    parser.add_argument("-1", dest="v1", action="store_true", help="Use just cost constraint")
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
    Runs each algorithm, for each constraint number provided.
    For each run, it gets the enjoyment, solution and running time, and using print_solution(),
    displays it on the screen one-by-one.
    """

    # for each algorithm, for each constrain number, run the algorithm and print results
    for algorithm in selected_algos:
        for constraint_num in selected_constraint_nums:

            func = ALGORITHMS[algorithm][constraint_num]  #callable function
            algo_title = ALGORITHMS[algorithm][NAME]

            try:
                if constraint_num == 1: # run algo with just cost constraint
                    enjoyment, solution, running_time = timed_func_run(func, activities, cost_budget)
                    algo_title += "(cost only)"
                    print_solution(algo_title, enjoyment, solution, time_budget, running_time)

                elif constraint_num == 2: # run algo with cost and time constrains
                    enjoyment, solution, running_time = timed_func_run(func, activities, time_budget, cost_budget)
                    algo_title += "(cost & time)"
                    print_solution(algo_title, enjoyment, solution, time_budget, running_time)

            except Exception as e:
                print('\n--- ', algo_title, ' ---')
                print("Error ocurred while running algorithm")
                print(e)
                print()


def main():
    """
    Main control function that is run at start. Calls other functions to direct flow of program.
    Calls function to: parse arguments, read file, perform the algorithms and print formatted results.
    Displays custom exception/error messages accordingly.
    """
    try:
        input_file, selected_algos, selected_constraint_nums = parse_args()

        activities, time_budget, cost_budget = read_from_file(f'{INPUT_DIRECTORY}{input_file}')

        # if file invalid, don't attempt algorithms
        if len(activities) == 0 or time_budget < 0 or cost_budget < 0:
            print("Ending program... please check the file you input and try again")
            return

        print_header(input_file, time_budget, cost_budget)

        # run all algorithms selected from arguments
        perform_algorithms(activities, time_budget, cost_budget, selected_algos, selected_constraint_nums)
    except KeyboardInterrupt:
        print('\n...\nProgram exited mid-run\n...\n')


if __name__ == '__main__':
    main()
