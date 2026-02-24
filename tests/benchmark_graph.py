"""
Benchmark Test Graph Creator

This program creates two graphs using the output file from the 
benchmark test file.

Graph 1 (Execution Time vs n (Logarithmic Scale)):
- The graph plots the number of activities in the input of the algorithms the median execution time.
- It uses a logarithmic scale due to the 'explosion' in the Brute Force execution time. 
- It includes 2^n and n^2 scaled to the final values of the Brute Force and Dynamic Programming respectively. 

Graph 2 (Speedup Factor (Brute Force / Dynamic Programming)(Logarithmic Scale)):
- The graph plots the number of activities in the input file to the speedup factor from 
  Brute Force to Dynamic Programming.
- The graph uses a logarithmic scale as the speedup factor for smaller values 
  of n could be considered insubstantial compared to the speedup factor at larger values of n.  
"""

import csv
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

CSV_PATH = Path("tests/benchmark_results/benchmark_result.csv")

def csv_cleaning(value: str):
    """
    Standardises any null values to None
    """
    if value is None:
        return None

    value = value.strip()
    if value == "": 
        return None
    
    return float(value)

def read_results(csv_path: Path):
    """
    Reads the results from the CSV and stores them in arrays
    """

    n_values = []

    bf_min = []
    bf_med = []
    bf_max = []

    dp_min = []
    dp_med = []
    dp_max = []

    speedup = []

    # Opens the CSV file
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # Loops through all lines (rows) in the CSV file
        for row in reader:
            n_values.append(int(row["n"]))

            bf_min.append(csv_cleaning(row.get("bf_min")))
            bf_med.append(csv_cleaning(row.get("bf_med")))
            bf_max.append(csv_cleaning(row.get("bf_max")))

            dp_min.append(csv_cleaning(row.get("dp_min")))
            dp_med.append(csv_cleaning(row.get("dp_med")))
            dp_max.append(csv_cleaning(row.get("dp_max")))

            speedup.append(csv_cleaning(row.get("speedup")))

        # Returns the arrays with values with the read values
        return n_values, bf_min, bf_med, bf_max, dp_min, dp_med, dp_max, speedup

def filter_valid(x_values, y_values):
    """
    Filters out any null values
    """
    xs, ys = [], []
    for x, y in zip(x_values, y_values):
        if y is not None:
            xs.append(x)
            ys.append(y)
    return xs, ys

def log_time_vs_n(n_values, bf_med, dp_med):
    """
    Creates the graph of time vs n with logarithmic scaling.

    Lines for the theoretical time complexity have been scaled and included for context.
    """

    brute_x, brute_y = filter_valid(n_values, bf_med)
    dynamic_x, dynamic_y = filter_valid(n_values, dp_med)

    # Constants for colours within plots
    BRUTE_COLOUR = "#d62728"     
    DYNAMIC_COLOUR = "#1f77b4"        
    BRUTE_THEORY = "#fb6a4a"   
    DYNAMIC_THEORY = "#6baed6"

    # Convert to numpy arrays
    # 'algorithm'_x is the n values input into them
    brute_x = np.array(brute_x)
    dynamic_x = np.array(dynamic_x)

    # Theoretical curves
    theory_exp = 2 ** brute_x # 2 ^ n
    theory_poly = dynamic_x ** 2 # n ^ 2

    # Scale exponential to match the final brute force value
    scale_exp = brute_y[-1] / theory_exp[-1]
    theory_exp_scaled = theory_exp * scale_exp

    # Scale polynomial to match the final DP value
    scale_poly = dynamic_y[-1] / theory_poly[-1]
    theory_poly_scaled = theory_poly * scale_poly

    plt.style.use("default")
    plt.figure(figsize=(9,6), facecolor="white")

    # Plotting of Bruteforce and Dynamic programming 
    plt.plot(brute_x, brute_y, marker = "o", markersize = 7,
             linewidth = 3, color = BRUTE_COLOUR,
             label = "Brute Force (median)")
    plt.plot(dynamic_x, dynamic_y, marker = "o", markersize = 7, 
             linewidth = 3, color = DYNAMIC_COLOUR,
             label = "Dynamic Programming (median)")
    
    # Plotting of the scaled theoretical time complexity
    plt.plot(brute_x, theory_exp_scaled, 
         linewidth=1.5, color = BRUTE_THEORY,
         label = r"Theoretical $2^n$ (scaled)")
    plt.plot(dynamic_x, theory_poly_scaled, 
         linewidth=1.5, color = DYNAMIC_THEORY,
         label = r"Theoretical $n^2$ (scaled)")
    
    plt.xlim(left=0)
    plt.title("Execution Time vs n (Logarithmic Scale)")
    plt.xlabel("n (number of activities)")
    plt.yscale("log")
    plt.ylabel("Exection time (seconds, logarithimic scale)")
    plt.legend(frameon = False)
    plt.grid(True, which = "both", alpha = 0.25)
    plt.tight_layout()
    plt.show()
    
def speedup_chart_logarithmic(n_values, speedup):
    """
    Creates the graph of n vs speedup with logarithmic scaling.
    """

    x_vals = []
    y_vals = []

    # Adds any non null values to the x and y arrays
    for n, s in zip(n_values, speedup):
        if s is not None:
            x_vals.append(str(n))
            y_vals.append(s)

    plt.style.use("default")
    plt.figure(figsize=(9,6), facecolor="white")

    # Plot values of x and y
    plt.bar(x_vals, y_vals)
     
    plt.title("Speedup Factor (Brute Force / Dynamic Programming)(logarithimic scale)")
    plt.xlabel("n (number of activities)")
    plt.yscale("log")
    plt.ylabel("Speedup Factor (times, logarithmic scale)")
    plt.grid(True, axis="y", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()

    
def create_graphs():
    """
    Function to consolidate graph creation functions
    """
    n_values, bf_min, bf_med, bf_max, dp_min, dp_med, dp_max, speedup = read_results(CSV_PATH)

    log_time_vs_n(n_values, bf_med, dp_med)
    speedup_chart_logarithmic(n_values, speedup)
