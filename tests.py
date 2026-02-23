"""
This is a file to combine all tests.
"""

import time 
from tests.known_tests import assertion_test
from tests.benchmark_case_creator import generate_random_input_series
from tests.benchmark_test import benchmark_algorithms
from tests.benchmark_graph import create_graphs

if __name__ == "__main__":
    print("\n------- Assertion tests -------")
    print("\nThe following tests test the algorithms against input files with known desired outputs.")
    print("")
    time.sleep(1) # .sleep() to allow time to read information on screen 
    assertion_test()
    time.sleep(3) # .sleep() to allow time to read information on screen 
    print("\n------- Benchmark tests -------")
    print("\nThe following tests the algorithms against input files of size n, where n is the number")
    print("of activities in the input file, to measure estimated the execution time of the algorithms.")
    print("Please note, the bruteforce algorithm would be expected to pass 10 mins at n = 30. ")
    b = int(input("\nWhat value of n would you like to test Bruteforce to? "))
    a = int(input("\nWhat value of n would you like to test Dynamic programming to? "))
    time.sleep(1) # .sleep() to allow time to read information on screen 
    generate_random_input_series(a)
    benchmark_algorithms(a, b)
    create_graphs()