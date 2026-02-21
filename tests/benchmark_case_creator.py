'''
This is a script to create input files for benchmark testing.

It creates varied input files, all following the given input file structure.

It sets the cost and time constraints to around 50% of the time or cost budget 
to prevent creating a trivial instance.

I have also set it to create multiple instances for each n, to ensure that the 
testing is more fair.
'''

import random
from pathlib import Path

OUTPUT_DIRECTORY = "tests/benchmark_inputs/"

def generate_random_input(n, seed = 0, case_index = 0):
    
    rng = random.Random(seed)

    activities = [] 
    for i in range(n):
        name = f"Act-{i}"
        time = rng.randint(1, 10)
        cost = rng.randint(1, 20)
        enjoyment = rng.randint(1, 100)
        activities.append((name, time, cost, enjoyment))

    total_cost = sum(a[2] for a in activities)
    total_time = sum(a[1] for a in activities)

    # Set budget constrains to ~50% so doesnt create a trivial instance
    Cost_budget = total_cost // 2
    Time_allocation = total_time // 2

    lines = []
    lines.append(str(n))
    lines.append(f"{Time_allocation} {Cost_budget}")

    for name_append, time_append, cost_append, enjoyment_append in activities:
        lines.append(f"{name_append} {time_append} {cost_append} {enjoyment_append}")
    
    filepath = f"{OUTPUT_DIRECTORY}input_{n}_{case_index}.txt" 
    Path(filepath).parent.mkdir(parents = True, exist_ok = True)
    Path(filepath).write_text("\n".join(lines) + "\n", encoding = "utf-8")

def step_for_n(n):
    if n <= 98:
        return 2
    elif n <= 290:
        return 10
    else:
        return 50

def cases_for_n(n):
    if n <= 100:
        return 30
    elif n <= 500:
        return 10
    else:
        return 3

def generate_random_input_series():
    n = 2
    n_max = 1000
    total_files = 0

    while n <= n_max:
        cases_per_n = cases_for_n(n)
        for case_index in range(cases_per_n):
            seed = (n * 1000) + case_index
            generate_random_input(n, seed=seed, case_index=case_index)
            total_files += 1
        n += step_for_n(n)

    print(f"\n{total_files} input files have been created for benchmark tests.")