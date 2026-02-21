import csv
from pathlib import Path
import matplotlib.pyplot as plt

CSV_PATH = Path("tests/benchmark_results/benchmark_result.csv")

def csv_cleaning(value: str):
    if value is None:
        return None

    value = value.strip()
    if value == "": 
        return None
    
    return float(value)

def read_results(csv_path: Path):
    n_values = []

    bf_min = []
    bf_med = []
    bf_max = []

    dp_min = []
    dp_med = []
    dp_max = []

    speedup = []

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            n_values.append(int(row["n"]))

            bf_min.append(csv_cleaning(row.get("bf_min")))
            bf_med.append(csv_cleaning(row.get("bf_med")))
            bf_max.append(csv_cleaning(row.get("bf_max")))

            dp_min.append(csv_cleaning(row.get("dp_min")))
            dp_med.append(csv_cleaning(row.get("dp_med")))
            dp_max.append(csv_cleaning(row.get("dp_max")))

            speedup.append(csv_cleaning(row.get("speedup")))

        return n_values, bf_min, bf_med, bf_max, dp_min, dp_med, dp_max, speedup

def filter_valid(x_values, y_values):
    xs, ys = [], []
    for x, y in zip(x_values, y_values):
        if y is not None:
            xs.append(x)
            ys.append(y)
    return xs, ys

def linear_time_vs_n(n_values, bf_med, dp_med):
    brute_x, brute_y = filter_valid(n_values, bf_med)
    dynamic_x, dynamic_y = filter_valid(n_values, dp_med)

    plt.figure()
    plt.plot(brute_x, brute_y, marker = "o", markersize = 4, linewidth = 2, label = "Brute Force (median)")
    plt.plot(dynamic_x, dynamic_y, marker = "o", markersize = 4, linewidth = 2, label = "Dynamic Programming (median)")

    plt.title("Execution Time vs n (Linear Scale)")
    plt.xlabel("n (number of activities)")
    plt.ylabel("Exection time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def log_time_vs_n(n_values, bf_med, dp_med):
    brute_x, brute_y = filter_valid(n_values, bf_med)
    dynamic_x, dynamic_y = filter_valid(n_values, dp_med)

    plt.figure()
    plt.plot(brute_x, brute_y, marker = "o", markersize = 4, linewidth = 2, label = "Brute Force (median)")
    plt.plot(dynamic_x, dynamic_y, marker = "o", markersize = 4, linewidth = 2, label = "Dynamic Programming (median)")

    plt.title("Execution Time vs n (Linear Scale)")
    plt.xlabel("n (number of activities)")
    plt.yscale("log")
    plt.ylabel("Exection time (seconds, logarithimic scale)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def speedup_chart_linear(n_values, speedup):
    x_vals = []
    y_vals = []

    for n, s in zip(n_values, speedup):
        if s is not None:
            x_vals.append(str(n))
            y_vals.append(s)

    plt.figure()

    plt.bar(x_vals, y_vals)

    plt.title("Speedup Factor in a linear multiplier scale(Brute Force / Dynamic Programming)")
    plt.xlabel("n (number of activities)")
    plt.ylabel("Speedup Factor (times)")
    plt.grid(True, axis="y", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()
    
def speedup_chart_logarithmic(n_values, speedup):
    x_vals = []
    y_vals = []

    for n, s in zip(n_values, speedup):
        if s is not None:
            x_vals.append(str(n))
            y_vals.append(s)

    plt.figure()

    plt.bar(x_vals, y_vals)

    plt.title("Speedup Factor in a logarithmic multiplier scale(Brute Force / Dynamic Programming)")
    plt.xlabel("n (number of activities)")
    plt.yscale("log")
    plt.ylabel("Speedup Factor (times in logarithmic scale)")
    plt.grid(True, axis="y", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.show()

    
def create_graphs():
    n_values, bf_min, bf_med, bf_max, dp_min, dp_med, dp_max, speedup = read_results(CSV_PATH)

    linear_time_vs_n(n_values, bf_med, dp_med)
    log_time_vs_n(n_values, bf_med, dp_med)
    speedup_chart_linear(n_values, speedup)
    speedup_chart_logarithmic(n_values, speedup)
