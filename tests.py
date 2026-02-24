"""
This is a file to combine all tests.
"""

import time 
from tests.known_tests import assertion_test_all, assertion_test_cost_only
from tests.known_tests import assertion_test_both_constraints, assertion_test_greedy
from tests.benchmark_case_creator import generate_random_input_series
from tests.benchmark_test import benchmark_algorithms
from tests.benchmark_graph import create_graphs

if __name__ == "__main__":
    
    print("\n------- Assertion tests -------")
    print("\nThe following tests test the algorithms against input files with known desired outputs.")
    print("")
    
    time.sleep(1)
    assertion_test_all()
    assertion_test_cost_only()
    assertion_test_both_constraints()
    assertion_test_greedy()
    
    time.sleep(1)
    print("\n------- Benchmark Tests -------")
    print("\nThe following tests evaluate the algorithms using input files of size n, where n")
    print("represents the number of activities in the input file.")
    print("The average execution time of the algorithms will be measured for each n across multiple input")
    print("files of the same size, providing a minimum, median and maximum execution time value.")
    print("n will step in contextually suitable steps until the provided maximum is reached")

    time.sleep(1)
    print("\nPlease note:")
    print("1. The brute force algorithm is expected to exceed 10 minutes at approximately n = 30.")
    print("2. Due to the reduced time complexity of the Dynamic Programming algorithm,")
    print("   the value of n for Dynamic Programming must be greater than or equal to")
    print("   the value chosen for the Bruteforce algorithm.")
    
    while True:
        try:
            b_input = input("\nMaximum input size of Bruteforce benchmark test (default 20): ")
            a_input = input("Maximum input size of Dynamic Programming benchmark test (default 1000): ")

            a = int(a_input) if a_input else 1000
            b = int(b_input) if b_input else 20

            if a < b:
                print("The input size (n) of the Dynamic Programming must be greater than or")
                print("equal to that of brute force, please try again.")
                continue

            break 
        except ValueError:
            print("Please enter the values as integers.")

    generate_random_input_series(a)
    benchmark_algorithms(a, b)
    create_graphs()