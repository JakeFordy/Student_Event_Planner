"""
This is a module to implement assertion tests.

The input files were created manually with known values to test 
cases that would cause issues in an incorrecly implemented algorithm.

The readme file contains further information on what each test is testing for, 
why the issue is being tested, and the usage issues if the tests do not pass.
"""

import os
import time
from algorithms.components import read_from_file
from algorithms.bruteforce import bruteforce_costonly, bruteforce_bothconstraints
from algorithms.dynamic import dynamic_costonly, dynamic_bothconstraints
from algorithms.greedy import greedy_costonly, greedy_bothconstraints

KNOWN_INPUT_DIRECTORY = "tests/known_inputs"

# Dictionary of the input files paired with the expected enjoyment values
EXPECTED_ALL = {
    "test_exact_fit.txt": 55,
    "test_unbounded_bug.txt": 10,
    "test_tie.txt": 20,
    "test_none_feasible.txt": 0,
}

EXPECTED_COST_ONLY = {
    "test_tradeoff.txt": 110,
    "test_both_binding.txt": 55,
}

EXPECTED_BOTH_CONSTRAINTS = {
    "test_non_optimal.txt": 95,
}

EXPECTED_GREEDY = {
    "test_local_optimal.txt": 45,
}

def solve_bruteforce_costonly(filepath: str) -> int:
    """
    Returns optimal values from bruteforce algorithm
    """
    activities, _, cost_budget = read_from_file(filepath)
    return bruteforce_costonly(activities, cost_budget)

def solve_dynamic_costonly(filepath: str) -> int:
    """
    Returns optimal values from dynamic programming algorithm
    """
    activities, _, cost_budget = read_from_file(filepath)
    return dynamic_costonly(activities, cost_budget)

def solve_bruteforce_bothconstraints(filepath: str) -> int:
    """
    Returns optimal values from bruteforce algorithm
    """
    activities, time_budget, cost_budget = read_from_file(filepath)
    return bruteforce_bothconstraints(activities, time_budget, cost_budget)

def solve_dynamic_bothconstraints(filepath: str) -> int:
    """
    Returns optimal values from dynamic programming algorithm
    """
    activities, time_budget, cost_budget = read_from_file(filepath)
    return dynamic_bothconstraints(activities, time_budget, cost_budget)

def solve_greedy_costonly(filepath: str) -> int:
    """
    Returns optimal values from dynamic programming algorithm
    """
    activities, _, cost_budget = read_from_file(filepath)
    return greedy_costonly(activities, cost_budget)

def solve_greedy_bothconstraints(filepath: str) -> int:
    """
    Returns optimal values from dynamic programming algorithm
    """
    activities, time_budget, cost_budget = read_from_file(filepath)
    return greedy_bothconstraints(activities, time_budget, cost_budget)

def best_value(result):
    """
    Returns only the enjoyment value from the algorithm output
    """
    if isinstance(result, tuple):
        return result[0] 
    return result

def assertion_test_all():
    """
    Implementation of the assertion tests

    Compares the enjoyment values output from the algorithms with the known answers

    If each test is passed, Pass 'test_file_name' : enjoyment = 'expected'"
    """

    for test_file_name, expected in EXPECTED_ALL.items():
        
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        all_passed = True

        # Checks that the computed solution matches the optimal solution
        results = {
        "Bruteforce (cost only)": best_value(solve_bruteforce_costonly(path)),
        "Dynamic (cost only)": best_value(solve_dynamic_costonly(path)),
        "Bruteforce (both constraints)": best_value(solve_bruteforce_bothconstraints(path)),
        "Dynamic (both constraints)": best_value(solve_dynamic_bothconstraints(path)),
        "Greedy (cost only)": best_value(solve_greedy_costonly(path)),
        "Greedy (both constraints)": best_value(solve_greedy_bothconstraints(path)),
        }

        print("")

        for algorithm, result in results.items():
            try:
                assert result == expected, f"expected {expected}, got {result}"
                print(f"PASS {algorithm} on {test_file_name}: enjoyment = {expected}")
            except AssertionError as e:
                all_passed = False
                print(f"FAIL {algorithm} on {test_file_name}: {e}")

        if all_passed:
            print(f"-----PASS for all algorithms on {test_file_name}: enjoyment = {expected}-----")
        else:
            print(f"-----Some tests FAILED on {test_file_name} (expected enjoyment = {expected})-----")

        time.sleep(3)

def assertion_test_cost_only():
    """
    Implementation of the assertion tests

    Compares the enjoyment values output from the algorithms with the known answers

    If each test is passed, Pass 'test_file_name' : enjoyment = 'expected'"
    """

    for test_file_name, expected in EXPECTED_COST_ONLY.items():
        
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        all_passed = True

        # Checks that the computed solution matches the optimal solution
        results = {
        "Bruteforce (cost only)": best_value(solve_bruteforce_costonly(path)),
        "Dynamic (cost only)": best_value(solve_dynamic_costonly(path)),
        }

        print("")

        for algorithm, result in results.items():
            try:
                assert result == expected, f"expected {expected}, got {result}"
                print(f"PASS {algorithm} on {test_file_name}: enjoyment = {expected}")
            except AssertionError as e:
                all_passed = False
                print(f"FAIL {algorithm} on {test_file_name}: {e}")

        if all_passed:
            print(f"-----PASS for all algorithms on {test_file_name}: enjoyment = {expected}-----")
        else:
            print(f"-----Some tests FAILED on {test_file_name} (expected enjoyment = {expected})-----")

        time.sleep(3)

def assertion_test_both_constraints():
    """
    Implementation of the assertion tests

    Compares the enjoyment values output from the algorithms with the known answers

    If each test is passed, Pass 'test_file_name' : enjoyment = 'expected'"
    """

    for test_file_name, expected in EXPECTED_BOTH_CONSTRAINTS.items():
        
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        all_passed = True

        # Checks that the computed solution matches the optimal solution
        results = {
        "Bruteforce (both constraints)": best_value(solve_bruteforce_bothconstraints(path)),
        "Dynamic (both constraints)": best_value(solve_dynamic_bothconstraints(path)),
        }

        print("")

        for algorithm, result in results.items():
            try:
                assert result == expected, f"expected {expected}, got {result}"
                print(f"PASS {algorithm} on {test_file_name}: enjoyment = {expected}")
            except AssertionError as e:
                all_passed = False
                print(f"FAIL {algorithm} on {test_file_name}: {e}")

        if all_passed:
            print(f"-----PASS for all algorithms on {test_file_name}: enjoyment = {expected}-----")
        else:
            print(f"-----Some tests FAILED on {test_file_name} (expected enjoyment = {expected})-----")

        time.sleep(3)

def assertion_test_greedy():
    """
    Implementation of the assertion tests

    Compares the enjoyment values output from the algorithms with the known answers

    If each test is passed, Pass 'test_file_name' : enjoyment = 'expected'"
    """

    for test_file_name, expected in EXPECTED_GREEDY.items():
        
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        all_passed = True

        # Checks that the computed solution matches the optimal solution
        results = {
        "Greedy (cost only)": best_value(solve_greedy_costonly(path)),
        "Greedy (both constraints)": best_value(solve_greedy_bothconstraints(path)),
        }

        print("")

        for algorithm, result in results.items():
            try:
                assert result == expected, f"expected {expected}, got {result}"
                print(f"PASS {algorithm} on {test_file_name}: enjoyment = {expected}")
            except AssertionError as e:
                all_passed = False
                print(f"FAIL {algorithm} on {test_file_name}: {e}")

        if all_passed:
            print(f"-----PASS for all algorithms on {test_file_name}: enjoyment = {expected}-----")
        else:
            print(f"-----Some tests FAILED on {test_file_name} (expected enjoyment = {expected})-----")

        time.sleep(3)