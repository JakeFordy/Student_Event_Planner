"""
add docstrings
"""

from time import perf_counter
from sys import argv
from os import getcwd

from components import read_from_file, print_solution
from bruteforce import bruteforce_bothconstraints, bruteforce_costonly
from dynamic import dynamic_costonly

INPUT_DIRECTORY = getcwd() + '/inputs/'

def perform_algorithms(input_file):
    """
    add docstring
    """
    activities, time_budget, cost_budget = read_from_file(f'{INPUT_DIRECTORY}{input_file}')

    if len(activities) == 0 or time_budget < 0 or cost_budget < 0:
        print("Ending program... please check the file you inputted and try again")
        return

    bruteforce_start_time = perf_counter()
    bruteforce_enjoyment, bruteforce_solution = bruteforce_costonly(0, cost_budget, [], activities)
    bruteforce_running_time = perf_counter() - bruteforce_start_time

    dynamic_start_time = perf_counter()
    dynamic_enjoyment, dynamic_solution = dynamic_costonly(cost_budget, activities)
    dynamic_running_time = perf_counter() - dynamic_start_time

    bruteforce_bothconstraints_start_time = perf_counter()
    bruteforce_bothconstraints_enjoyment, bruteforce_bothconstraints_solution = bruteforce_bothconstraints(0, time_budget, cost_budget, [], activities)
    bruteforce_bothconstraints_running_time = perf_counter() - bruteforce_bothconstraints_start_time

    print('========================================')
    print('EVENT PLANNER - RESULTS')
    print('========================================\n')
    print('Input file:', input_file)
    print('Available Time:', time_budget, 'hours')
    print(f'Available Budget: £{cost_budget}')

    print_solution('BRUTE FORCE ALGORITHM (cost only)', bruteforce_enjoyment, bruteforce_solution,
                   time_budget, bruteforce_running_time)
    print_solution('DYNAMIC ALGORITHM (cost only)', dynamic_enjoyment, dynamic_solution,
                   time_budget, dynamic_running_time)
    print_solution('BRUTE FORCE ALGORITHM (cost & time)', bruteforce_bothconstraints_enjoyment,
                   bruteforce_bothconstraints_solution, time_budget,
                   bruteforce_bothconstraints_running_time)


if __name__ == '__main__':
    if len(argv) == 2:
        perform_algorithms(argv[1])
    else:
        print("Please enter the input file you would like to use (max one at a time). For example:")
        print("python event_planner.py input_large.txt")
