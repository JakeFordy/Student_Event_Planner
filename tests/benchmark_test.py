'''
This file is to implement the testing of the bruteforce and dynamic programming algorithms
Test the small imput size for both algorithms
Compare the output to a known (computed by hand) algorithm
This verifies that the algorithm 'work' 

Mention possibility of edge-cases 
i.e. test for file not found, isuse converting to int

Measure time complexity of algorithms
O notation and time measurements for different cases
Test this for small, medium, large

Also, test this for n = 10, 15, 20, 25, 30, ...
Print statement, and export to csv file 

Stress testing, use high number of itterations of random ints

Both run as perform_algorithms()
Or individually run as bruteforce_costonly(activity_num, cost_left, current_selection, activities)
Or dynamic_costonly(total_budget, activities)
'''

from time import perf_counter
import statistics
import csv
import glob
import os

import sys
from pathlib import Path

from algorithms.components import read_from_file
from algorithms.bruteforce import bruteforce_costonly
from algorithms.dynamic import dynamic_costonly

INPUT_DIRECTORY = "tests/benchmark_inputs/"

def time_for_bruteforce(filepath: str ) -> float:
    activities, time_budget, cost_budget = read_from_file(filepath)

    start = perf_counter()
    bruteforce_costonly(0, cost_budget, [], activities)
    return perf_counter() - start

def time_for_dynamic(filepath: str ) -> float:
    activities, time_budget, cost_budget = read_from_file(filepath)

    start = perf_counter()
    dynamic_costonly(cost_budget, activities)
    return perf_counter() - start

def step_for_n(n):
    if n <= 98:
        return 2
    elif n <= 290:
        return 10
    else:
        return 50

def cases_for_dynamic(n: int) -> int:
    if n <= 100:
        return 30
    elif n <= 500:
        return 10
    else:
        return 3

def cases_for_bruteforce(n: int) -> int:
    return 3

def benchmark_algorithms(output_file = "tests/benchmark_results/benchmark_result.csv"):

    n_max = 1000
    bf_max_n = 26

    results = []

    print("\nBenchmarking Brute Force and Dynamic Programming")
    print("n\tBF_min\tBF_med\tBF_max\tDP_min\tDP_med\tDP_max\tSpeedup")

    n = 2
    while n<= n_max:

        dynamic_cases = cases_for_dynamic(n)
        bruteforce_cases = cases_for_bruteforce(n) if n <= bf_max_n else 0

        brute_times = []
        dynamic_times = []

        for case_index in range(dynamic_cases):
            filepath = f"{INPUT_DIRECTORY}input_{n}_{case_index}.txt"
            if not os.path.exists(filepath):
                continue

            # Dynamic programming always runs
            dynamic_times.append(time_for_dynamic(filepath))

            if bruteforce_cases and case_index < bruteforce_cases:
                brute_times.append(time_for_bruteforce(filepath))
        
        if not dynamic_times:
            n += step_for_n(n)
            continue

        # Dynamic stats
        dp_min = min(dynamic_times)
        dp_max = max(dynamic_times)
        dp_med = statistics.median(dynamic_times)

        if brute_times:
            bf_min = min(brute_times)
            bf_max = max(brute_times)
            bf_med = statistics.median(brute_times)
            speedup = bf_med / dp_med if dp_med > 0 else float("inf")

            print(f"{n}\t{bf_min:.4f}\t{bf_med:.4f}\t{bf_max:.4f}\t"
                  f"{dp_min:.4f}\t{dp_med:.4f}\t{dp_max:.4f}\t{speedup:.2f}x")

            results.append([
                n, 
                bf_min, bf_med, bf_max,
                dp_min, dp_med, dp_max,
                speedup
            ])
        else:
            print(f"{n}\t-\t-\t-\t{dp_min:.4f}\t{dp_med:.4f}\t{dp_max:.4f}\t-")

            results.append([
                n,
                None, None, None,
                dp_min, dp_med, dp_max,
                None
            ])

        n += step_for_n(n)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
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
