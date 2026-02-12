from time import perf_counter

from components import read_from_file, print_solution
from bruteforce import bruteforce
from config import INPUT_DIRECTORY, INPUT_FILE


def perform_algorithms():
    activities, time_budget, cost_budget = read_from_file(f'{INPUT_DIRECTORY}{INPUT_FILE}')

    bruteforce_start_time = perf_counter()
    bruteforce_enjoyment, bruteforce_solution = bruteforce(0, time_budget, cost_budget, [], activities)
    bruteforce_end_time = perf_counter()

    print('========================================')
    print('EVENT PLANNER - RESULTS')
    print('========================================\n')
    print('Input file:', INPUT_FILE)
    print('Available Time:', time_budget, 'hours')
    print(f'Available Budget: £{cost_budget}')

    print_solution('BRUTE FORCE ALGORITHM', bruteforce_enjoyment, bruteforce_solution, bruteforce_end_time - bruteforce_start_time)


if __name__ == '__main__':
    perform_algorithms()


