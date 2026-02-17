from time import perf_counter

from components import read_from_file, print_solution
from bruteforce import bruteforce_bothconstraints, bruteforce_costonly
from dynamic import dynamic_costonly
from config import INPUT_DIRECTORY, INPUT_FILE


def perform_algorithms():
    activities, time_budget, cost_budget = read_from_file(f'{INPUT_DIRECTORY}{INPUT_FILE}')

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
    print('Input file:', INPUT_FILE)
    print('Available Time:', time_budget, 'hours')
    print(f'Available Budget: £{cost_budget}')

    print_solution('BRUTE FORCE ALGORITHM (cost only)', bruteforce_enjoyment, bruteforce_solution, time_budget,
                   bruteforce_running_time)
    print_solution('DYNAMIC ALGORITHM (cost only)', dynamic_enjoyment, dynamic_solution, time_budget,
                   dynamic_running_time)
    print_solution('BRUTE FORCE ALGORITHM (cost+time)', bruteforce_bothconstraints_enjoyment, bruteforce_bothconstraints_solution, time_budget,
                   bruteforce_bothconstraints_running_time)


if __name__ == '__main__':
    perform_algorithms()
