import time 
from tests.known_tests import assertion_test
from tests.benchmark_case_creator import generate_random_input_series
from tests.benchmark_test import benchmark_algorithms
from tests.benchmark_graph import create_graphs

if __name__ == "__main__":
    print("\n------- Assertion tests -------")
    print("\nThe folowing tests test the algorithms against input files with known desired outputs.")
    print("")
    time.sleep(3)
    assertion_test()
    time.sleep(6)
    print("\n------- Benchmark tests -------")
    print("\nThe following test tests the algorithms against input files of size n, and compares the")
    print("execution time of the algorithms.")
    print("Please note, the bruteforce algorithm is only tested to n = 24 as values above this could")
    print("be considered impractical for compuatation using the bruteforce algorithm.")
    time.sleep(9)
    generate_random_input_series()
    benchmark_algorithms()
    create_graphs()