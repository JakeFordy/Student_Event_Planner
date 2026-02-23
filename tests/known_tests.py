"""
This is a module to implement assertion tests.

The input files were created manually with known values to test 
cases that would cause issues in an incorrecly implemented algorithm.

The readme file contains further information on what each test is testing for, 
why the issue is being tested, and the usage issues if the tests do not pass.
"""

import os
from algorithms.components import read_from_file
from algorithms.bruteforce import bruteforce_costonly
from algorithms.dynamic import dynamic_costonly
from algorithms.bruteforce import bruteforce_bothconstraints
from algorithms.dynamic import dynamic_bothconstraints

KNOWN_INPUT_DIRECTORY = "tests/known_inputs"

# Dictionary of the input files paired with the expected enjoyment values
EXPECTED = {
    "test_exact_fit.txt": 55,
    "test_tradeoff.txt": 110,
    "test_both_binding.txt": 55,
    "test_unbounded_bug.txt": 10,
    "test_tie.txt": 20,
    "test_none_feasible.txt": 0,
}

def solve_bruteforce_costonly(filepath: str) -> int:
    """
    Returns optimal values from bruteforce algorithm
    """
    activities, _, cost_budget = read_from_file(filepath)
    return bruteforce_costonly(0, cost_budget, 0, [], activities)

def solve_dynamic_costonly(filepath: str) -> int:
    """
    Returns optimal values from dynamic programming algorithm
    """
    activities, _, cost_budget = read_from_file(filepath)
    return dynamic_costonly(cost_budget, activities)

def solve_bruteforce_bothconstrains(filepath: str) -> int:
    """
    Returns optimal values from bruteforce algorithm
    """
    activities, time_budget, cost_budget = read_from_file(filepath)
    return bruteforce_bothconstraints(0, time_budget, cost_budget, 0, [], activities)

def solve_dynamic_bothconstrains(filepath: str) -> int:
    """
    Returns optimal values from dynamic programming algorithm
    """
    activities, time_budget, cost_budget = read_from_file(filepath)
    return dynamic_bothconstraints(time_budget, cost_budget, activities)

def best_value(result):
    """
    Returns only the enjoyment value from the algorithm output
    """
    if isinstance(result, tuple):
        return result[0] 
    return result

def assertion_test():
    """
    Implementation of the assertion tests

    Compares the enjoyment values output from the algorithms with the known answers

    If each test is passed, Pass 'test_file_name' : enjoyment = 'expected'"
    """
    for test_file_name, expected in EXPECTED.items():
        # Fetches the input file using tests/known_inputs/filename
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        # Computes the solutions for each algorithm
        brute = best_value(solve_bruteforce_costonly(path))
        dynamic = best_value(solve_dynamic_costonly(path))
        brute_both = best_value(solve_bruteforce_bothconstrains(path))
        dynamic_both = best_value(solve_dynamic_bothconstrains(path))

        # Checks that the computed solution matches the optimal solution
        assert brute == expected, f"{test_file_name}: brute force got {brute}, expected {expected}"
        assert dynamic == expected, f"{test_file_name}: dynamic got {dynamic}, expected {expected}"
        assert brute_both == expected, f"{test_file_name}: brute force got {brute}, expected {expected}"
        assert dynamic_both == expected, f"{test_file_name}: dynamic got {dynamic}, expected {expected}"

        # Prints the following statement only if both assertions passed
        print(f"PASS {test_file_name}: enjoyment = {expected}")
