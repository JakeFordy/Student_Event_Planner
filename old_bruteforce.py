"""
Brute force algorithm

must generate all possible subsets and keep track of best solution (highest enjoyment)

returns in format:

========================================
EVENT PLANNER - RESULTS
========================================

Input File: input_small.txt
Available Time: 10 hours
Available Budget: £200

--- BRUTE FORCE ALGORITHM ---
Selected Activities:
- Game-Night (3 hours, £80, enjoyment 120)
- Pizza-Workshop (2 hours, £60, enjoyment 100)
- Hiking (5 hours, £30, enjoyment 140)

Total Enjoyment: 360
Total Time Used: 10 hours
Total Cost: £170

Execution Time: 0.002 seconds
"""


from copy import deepcopy
from time import perf_counter


NAME = 0
TIME = 1
COST = 2
ENJOYMENT = 3

INPUT_DIRECTORY = './inputs/'
INPUT_FILE = 'input_large.txt'


def read_from_file(filename: str):
    activities = []
    total_time = 0
    total_cost = 0

    with open(filename, 'r', encoding='utf-8') as f:
        f.readline()
        (total_time, total_cost) = f.readline().split(' ')
        for line in f:
            data = line.strip().split(' ')
            activities += [data]
            
    #print(activities)
    return activities, int(total_time), int(total_cost)

def bruteforce_best_solution(cost_budget, time_budget, remaining_options):
    start_time = perf_counter()
    best_solution = recursive_options([], remaining_options, cost_budget, time_budget, 0, 0)
    end_time = perf_counter()
    best_solution['exec_time'] = end_time - start_time
    return best_solution

def recursive_options(current_selection: list, remaining_options: list, budget_left: int, time_left: int, current_enjoyment: int, depth: int):
    best_solution = {
        'options': current_selection,
        'enjoyment': current_enjoyment
    }
    print('depth: ', depth)
    print(time_left, budget_left, current_enjoyment)
    
    for option in remaining_options:
        if (time_left - int(option[TIME])) < 0:
            continue
        if (budget_left - int(option[COST])) < 0:
            continue

        other_options = deepcopy(remaining_options)
        other_options.remove(option)
        calculated_solution = recursive_options(current_selection + [option], other_options, budget_left - int(option[COST]), time_left - int(option[TIME]), current_enjoyment + int(option[ENJOYMENT]), depth +1)

        if calculated_solution['enjoyment'] > best_solution['enjoyment']:
            best_solution = calculated_solution

    return best_solution


def print_solution(algorithm: str, solution: dict):
    print('\n--- ', algorithm, ' ---')
    print('Selected Activities:')
    total_enjoyment = solution['enjoyment']
    activities = solution['options']
    exec_time = solution['exec_time']

    total_time = 0
    total_cost = 0

    for activity in activities:
        print(f'\t - {activity[NAME]} ({activity[TIME]} hours, £{activity[COST]}, enjoyment {activity[ENJOYMENT]})')
        total_time += int(activity[TIME])
        total_cost += int(activity[COST])
    
    print('\nTotal Enjoyment:', total_enjoyment)
    print('Total Time Used:', total_time, 'hours')
    print(f'Total Cost: £{total_cost}')

    print('\nExecution Time:', exec_time, 'seconds')
    #get execution time for algos

def perform_algorithms():
    remaining_options, time_budget, cost_budget = read_from_file(f'{INPUT_DIRECTORY}{INPUT_FILE}')
    #print(remaining_options, time_budget, cost_budget)

    bruteforce_solution = bruteforce_best_solution(cost_budget, time_budget, remaining_options)

    print('========================================')
    print('EVENT PLANNER - RESULTS')
    print('========================================\n')
    print('Input file:', INPUT_FILE)
    print('Available Time:', time_budget, 'hours')
    print(f'Available Budget: £{cost_budget}')

    print_solution('BRUTE FORCE ALGORITHM', bruteforce_solution)





if __name__ == '__main__':
    perform_algorithms()




#TODO:
#ORGANISE BRUTEFORCE FUNCTION HIERARCHY
#--------- INPUT FROM TXT FILE
#DYNAMIC ALGO
#G-------------- ET EXECUTION TIMES
#MAYBE RESTRUCTURE BRUTEFORCE METHOD?? like return budget used etc so no need to recalculate
#and maybe call print from inside the bruteforce function to reduce redundancy in going through all algo solution loop at end again