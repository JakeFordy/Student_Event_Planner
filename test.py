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

from components import read_from_file
from bruteforce import bruteforce_costonly
from dynamic import dynamic_costonly

import random
from pathlib import Path

INPUT_DIRECTORY = "inputs/"

def time_for_bruteforce(filepath):
    activities, time_budget, cost_budget = read_from_file(filepath)

    start = perf_counter()

    bruteforce_costonly(0, cost_budget, [], activities)

    return perf_counter() - start

def time_for_dynamic(filepath):
    activities, time_budget, cost_budget = read_from_file(filepath)

    start = perf_counter()

    dynamic_costonly(cost_budget, activities)

    return perf_counter() - start

def benchmark_algorithms(instances_per_n = 10, output_file = "benchmark_result.csv"):

    results = []

    print("\nBenchmarking Brute Force and Dynamic Programming")
    print("n\tBF_min\tBF_med\tBF_max\tDP_min\tDP_med\tDP_max\tSpeedup")

    for n in range(5, 55, 5):
        brute_times = []
        dynamic_times = []

        for case_index in range(instances_per_n):
            filepath = f"{INPUT_DIRECTORY}input_{n}_{case_index}.txt"

            if not os.path.exists(filepath):
                continue

            brute_times.append(time_for_bruteforce(filepath))
            dynamic_times.append(time_for_dynamic(filepath))
        
        if not brute_times:
            continue

        # Brute stats
        bf_min = min(brute_times)
        bf_max = max(brute_times)
        bf_med = statistics.median(brute_times)

        # Brute stats
        dp_min = min(dynamic_times)
        dp_max = max(dynamic_times)
        dp_med = statistics.median(dynamic_times)

        speedup = bf_med / dp_med if dp_med > 0 else float("inf")

        print(f"{n}\t{bf_min:.4f}\t{bf_med:.4f}\t{bf_max:.4f}\t"
              f"{dp_min:.4f}\t{dp_med:.4f}\t{dp_max:.4f}\t{speedup:.2f}x")

        results.append([
            n, 
            bf_min, bf_med, bf_max,
            dp_min, dp_med, dp_max,
            speedup
        ])

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

if __name__ == "__main__":
    benchmark_algorithms(instances_per_n = 10)