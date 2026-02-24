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

# Dictionary of the input files paired with the expected enjoyment values for cost only algorithms
EXPECTED_ALL = {
    "test_exact_fit.txt": 55,
    "test_unbounded_bug.txt": 10,
    "test_tie.txt": 20,
    "test_none_feasible.txt": 0,
}

# Dictionary of the input files paired with the expected enjoyment values for cost only algorithms
EXPECTED_COST_ONLY = {
    "test_tradeoff.txt": 110,
    "test_both_binding.txt": 55,
}

# Dictionary of the input files paired with the expected enjoyment values for both constraint algorithms
EXPECTED_BOTH_CONSTRAINTS = {
    "test_both_considered.txt": 95,
}

# Dictionary of the input files paired with the expected enjoyment values for the greedy algorithms
EXPECTED_GREEDY = {
    "test_local_optimal.txt": 45,
}

def solve_bruteforce_costonly(filepath: str) -> int:
    """
    Returns optimal values from bruteforce cost only algorithm
    """
    activities, _, cost_budget = read_from_file(filepath)
    return bruteforce_costonly(activities, cost_budget)

def solve_dynamic_costonly(filepath: str) -> int:
    """
    Returns optimal values from dynamic programming cost only algorithm
    """
    activities, _, cost_budget = read_from_file(filepath)
    return dynamic_costonly(activities, cost_budget)

def solve_bruteforce_bothconstraints(filepath: str) -> int:
    """
    Returns optimal values from bruteforce both constraints algorithm
    """
    activities, time_budget, cost_budget = read_from_file(filepath)
    return bruteforce_bothconstraints(activities, time_budget, cost_budget)

def solve_dynamic_bothconstraints(filepath: str) -> int:
    """
    Returns optimal values from dynamic programming both constraints algorithm
    """
    activities, time_budget, cost_budget = read_from_file(filepath)
    return dynamic_bothconstraints(activities, time_budget, cost_budget)

def solve_greedy_costonly(filepath: str) -> int:
    """
    Returns optimal values from greedy cost only algorithm
    """
    activities, _, cost_budget = read_from_file(filepath)
    return greedy_costonly(activities, cost_budget)

def solve_greedy_bothconstraints(filepath: str) -> int:
    """
    Returns optimal values from greedy both constraints algorithm
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

    Compares the enjoyment values output from the algorithms with the known answers, 
    and prints a summary of PASSed and FAILed tests.

    This includes the tests for ALL algorithms, which tests for the logic within 
    the algorithm implementation. 
    """

    print("\n----- Tests for ALL algorithms -----")
    print("The following tests test for the key logic within the algorithms.")

    # Loops through all file names in EXPECTED_ALL dictionary        
    for test_file_name, expected in EXPECTED_ALL.items():
        
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        # Default value, as no tests have failed
        all_passed = True

        # Dictionary for algorithm name to output enjoyment value
        results = {
        "Bruteforce (cost only)": best_value(solve_bruteforce_costonly(path)),
        "Dynamic (cost only)": best_value(solve_dynamic_costonly(path)),
        "Bruteforce (both constraints)": best_value(solve_bruteforce_bothconstraints(path)),
        "Dynamic (both constraints)": best_value(solve_dynamic_bothconstraints(path)),
        "Greedy (cost only)": best_value(solve_greedy_costonly(path)),
        "Greedy (both constraints)": best_value(solve_greedy_bothconstraints(path)),
        }

        print("")

        # Loop to perform assertion for result vs expected value 
        for algorithm, result in results.items():
            try:
                assert result == expected, f"expected {expected}, got {result}"
                # If test passes print:
                print(f"PASS {algorithm} on {test_file_name}: enjoyment = {expected}")
            except AssertionError as e: # Exception to catch assertion error is the test fails
                # Changes all_passed to false so test summary is altered
                all_passed = False
                # If test fails print:
                print(f"FAIL {algorithm} on {test_file_name}: {e}")
        
        if all_passed:
            # If all tests pass, all_passed remains True, so prints:
            print(f"-----PASS for all algorithms on {test_file_name}: enjoyment = {expected}-----")
        else:
            # If ANY tests fail, all_passed changes to False, so prints:
            print(f"-----Some tests FAILED on {test_file_name} (expected enjoyment = {expected})-----")

    time.sleep(1)

def assertion_test_cost_only():
    """
    Implementation of the assertion tests

    Compares the enjoyment values output from the algorithms with the known answers, 
    and prints a summary of PASSed and FAILed tests.

    This includes the tests for COST ONLY algorithms, which tests to ensure that the
    cost only rules have been adhered to. 
    """

    print("\n----- Tests for COST ONLY algorithms -----")
    print("The following tests test for adherence to the cost budget.")

    # Loops through all file names in EXPECTED_ALL dictionary
    for test_file_name, expected in EXPECTED_COST_ONLY.items():
        
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        # Default value, as no tests have failed
        all_passed = True

        # Dictionary for algorithm name to output enjoyment value
        results = {
        "Bruteforce (cost only)": best_value(solve_bruteforce_costonly(path)),
        "Dynamic (cost only)": best_value(solve_dynamic_costonly(path)),
        }

        print("")

        # Loop to perform assertion for result vs expected value 
        for algorithm, result in results.items():
            try:
                assert result == expected, f"expected {expected}, got {result}"
                # If test passes print:
                print(f"PASS {algorithm} on {test_file_name}: enjoyment = {expected}")
            except AssertionError as e: # Exception to catch assertion error is the test fails
                # Changes all_passed to false so test summary is altered
                all_passed = False
                # If test fails print:
                print(f"FAIL {algorithm} on {test_file_name}: {e}")
        
        if all_passed:
            # If all tests pass, all_passed remains True, so prints:
            print(f"-----PASS for all algorithms on {test_file_name}: enjoyment = {expected}-----")
        else:
            # If ANY tests fail, all_passed changes to False, so prints:
            print(f"-----Some tests FAILED on {test_file_name} (expected enjoyment = {expected})-----")

    time.sleep(1)

def assertion_test_both_constraints():
    """
    Implementation of the assertion tests

    Compares the enjoyment values output from the algorithms with the known answers, 
    and prints a summary of PASSed and FAILed tests.

    This includes the tests for BOTH CONSTRAINTS algorithms, which tests to ensure that both the
    cost and time rules have been adhered to. 
    """

    print("\n----- Tests for BOTH CONSTRAINTS algorithms -----")
    print("The following tests test for adherence to both the cost budget and the time budget.")

    # Loops through all file names in EXPECTED_ALL dictionary
    for test_file_name, expected in EXPECTED_BOTH_CONSTRAINTS.items():
        
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        # Default value, as no tests have failed
        all_passed = True

        # Dictionary for algorithm name to output enjoyment value
        results = {
        "Bruteforce (both constraints)": best_value(solve_bruteforce_bothconstraints(path)),
        "Dynamic (both constraints)": best_value(solve_dynamic_bothconstraints(path)),
        }

        print("")

        # Loop to perform assertion for result vs expected value 
        for algorithm, result in results.items():
            try:
                assert result == expected, f"expected {expected}, got {result}"
                # If test passes print:
                print(f"PASS {algorithm} on {test_file_name}: enjoyment = {expected}")
            except AssertionError as e: # Exception to catch assertion error is the test fails
                # Changes all_passed to false so test summary is altered
                all_passed = False
                # If test fails print:
                print(f"FAIL {algorithm} on {test_file_name}: {e}")
        
        if all_passed:
            # If all tests pass, all_passed remains True, so prints:
            print(f"-----PASS for all algorithms on {test_file_name}: enjoyment = {expected}-----")
        else:
            # If ANY tests fail, all_passed changes to False, so prints:
            print(f"-----Some tests FAILED on {test_file_name} (expected enjoyment = {expected})-----")

    time.sleep(2)

def assertion_test_greedy():
    """
    Implementation of the assertion tests

    Compares the enjoyment values output from the algorithms with the known answers, 
    and prints a summary of PASSed and FAILed tests.

    This includes the tests for GREEDY algorithms, that the logic for the greedy heurisitc
    algorithm has been followed. 

    Please note, this tests for an expected solution based on the algorithm taking the local
    optima rather than the global optimal solution.
    """

    print("\n----- Tests for GREEDY algorithms -----")
    print("The following tests test for adherence to the greedy heuristic logic.")

    # Loops through all file names in EXPECTED_ALL dictionary 
    for test_file_name, expected in EXPECTED_GREEDY.items():
        
        path = os.path.join(KNOWN_INPUT_DIRECTORY, test_file_name)

        # Default value, as no tests have failed
        all_passed = True

        # Dictionary for algorithm name to output enjoyment value
        results = {
        "Greedy (cost only)": best_value(solve_greedy_costonly(path)),
        "Greedy (both constraints)": best_value(solve_greedy_bothconstraints(path)),
        }

        print("")

        # Loop to perform assertion for result vs expected value 
        for algorithm, result in results.items():
            try:
                assert result == expected, f"expected {expected}, got {result}"
                # If test passes print:
                print(f"PASS {algorithm} on {test_file_name}: enjoyment = {expected}")
            except AssertionError as e: # Exception to catch assertion error is the test fails
                # Changes all_passed to false so test summary is altered
                all_passed = False
                # If test fails print:
                print(f"FAIL {algorithm} on {test_file_name}: {e}")
        
        if all_passed:
            # If all tests pass, all_passed remains True, so prints:
            print(f"-----PASS for all algorithms on {test_file_name}: enjoyment = {expected}-----")
        else:
            # If ANY tests fail, all_passed changes to False, so prints:
            print(f"-----Some tests FAILED on {test_file_name} (expected enjoyment = {expected})-----")

        time.sleep(2)