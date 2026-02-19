'''
This file is to implement the testing of the bruteforce and dynamic programming algorithms
'''

# Test the small imput size for both algorithms
# Compare the output to a known (computed by hand) algorithm
# This verifies that the algorithm 'work' 

# Mention possibility of edge-cases 
# i.e. test for file not found, isuse converting to int

# Measure time complexity of algorithms
# O notation and time measurements for different cases
# Test this for small, medium, large

# Also, test this for n = 10, 15, 20, 25, 30, ...
# Print statement, and export to csv file 

# Stress testing, use high number of itterations of random ints

# Both run as perform_algorithms()
# Or individually run as bruteforce_costonly(activity_num, cost_left, current_selection, activities)
# Or dynamic_costonly(total_budget, activities)

from time import perf_counter
from sys import argv
from os import getcwd

from components import read_from_file
from bruteforce import bruteforce_bothconstraints, bruteforce_costonly
from dynamic import dynamic_costonly

INPUT_DIRECTORY = getcwd() + '/inputs/'

def perform_tests():
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

if __name__ == '__main__':
    perform_tests()

# Creates files for each value of n, 3 random for each. 
# Runs each file and creates an average run time for the algorithm. 