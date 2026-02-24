'''
Benchmark Test

This script measures the execution times of the algorithms for an input size n.

Test rules:
- Brute force is always run on 3 different files of input size n.
- Dynamic programming is run on a dynamic number of different input files based on the value of n.
- The test outputs a minimum, median, and maximum value for execution time for each algorithm along
  with the associated speedup value.

Output directory:
    tests/benchmark_results/
'''

from time import perf_counter
import statistics
import csv
import os

from algorithms.components import read_from_file
from algorithms.bruteforce import bruteforce_costonly
from algorithms.dynamic import dynamic_costonly

INPUT_DIRECTORY = "tests/benchmark_inputs/"

def time_for_bruteforce(filepath: str) -> float:
    """
    Measures the execution time of the bruteforce algorithm for a given file 
    """
    activities, time_budget, cost_budget = read_from_file(filepath)

    start = perf_counter()
    bruteforce_costonly(activities, cost_budget)
    return perf_counter() - start

def time_for_dynamic(filepath: str) -> float:
    """
    Measures the execution time of the dynamic programming algorithm for a given file
    """
    activities, time_budget, cost_budget = read_from_file(filepath)

    start = perf_counter()
    dynamic_costonly(activities, cost_budget)
    return perf_counter() - start

def step_for_n(n):
    """
    This determines the step in n for each range of values 
    """
    if n <= 98:
        return 2
    elif n <= 290:
        return 10
    else:
        return 50

def cases_for_dynamic(n: int) -> int:
    """
    This determines the number of test iterations per n for 
    the dynamic programming algorithm
    """
    if n <= 100:
        return 30
    elif n <= 500:
        return 10
    else:
        return 3

def cases_for_bruteforce(n: int) -> int:
    """
    Iterations per n is always 3 for bruteforce due to time 
    complexity related to the algorithm
    """
    return 3

def benchmark_algorithms(a: int, b: int, output_file = "tests/benchmark_results/benchmark_result.csv"):
    """
    Carries out the benchmark tests under the given constraints

    Prints the results to the command line, and also exports a 
    csv file containing all of the results to tests/benchmark_results
    """

    results = []

    print("\nBenchmarking Brute Force and Dynamic Programming")
    print("n\tBF_min\tBF_med\tBF_max\tDP_min\tDP_med\tDP_max\tSpeedup")

    # Initial value of n
    n = int(2)

    # Steps until n = a
    while n <= a:
        
        # Determine number of cases for each algorithm
        dynamic_cases = cases_for_dynamic(n)
        bruteforce_cases = cases_for_bruteforce(n) if n <= b else 0

        brute_times = []
        dynamic_times = []

        # Run benchmarks for avilable test cases
        for case_index in range(dynamic_cases):
            filepath = f"{INPUT_DIRECTORY}input_{n}_{case_index}.txt"
            
            # Skip if the file does not exist
            if not os.path.exists(filepath):
                continue

            # Dynamic programming always runs
            dynamic_times.append(time_for_dynamic(filepath))

            # Only run bruteforce for small n
            if bruteforce_cases and case_index < bruteforce_cases:
                brute_times.append(time_for_bruteforce(filepath))
        
        # If no test cases were found, step to next n
        if not dynamic_times:
            n += step_for_n(n)
            continue

        # Compute dynamic programming stats
        dp_min = min(dynamic_times)
        dp_max = max(dynamic_times)
        dp_med = statistics.median(dynamic_times)

        if brute_times:
            # Compute bruteforce stats
            bf_min = min(brute_times)
            bf_max = max(brute_times)
            bf_med = statistics.median(brute_times)

            # Compute speedup ratio
            speedup = bf_med / dp_med if dp_med > 0 else float("inf")

            print(f"{n}\t{bf_min:.4f}\t{bf_med:.4f}\t{bf_max:.4f}\t"
                  f"{dp_min:.4f}\t{dp_med:.4f}\t{dp_max:.4f}\t{speedup:.2f}x")

            # Added to results array to be written to CSV
            results.append([
                n, 
                bf_min, bf_med, bf_max,
                dp_min, dp_med, dp_max,
                speedup
            ])
        else:
            # brute_times does not exist for this n
            # So bruteforce is skipped for large n
            print(f"{n}\t-\t-\t-\t{dp_min:.4f}\t{dp_med:.4f}\t{dp_max:.4f}\t-")

            # Added to results array to be written to CSV
            results.append([
                n,
                None, None, None,
                dp_min, dp_med, dp_max,
                None
            ])

        # Step in n is decided based on the value of n
        n += step_for_n(n)

    # Write results to CSV file
    with open(output_file, "w", newline = "") as f:
        writer = csv.writer(f)
        writer.writerow([
        "n", 
       "bf_min", "bf_med", "bf_max",
        "dp_min", "dp_med", "dp_max",
        "speedup"
       ])
        writer.writerows(results)
    
    print(f"\nResults exported to {output_file}")
