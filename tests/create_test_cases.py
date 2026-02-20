import random
from pathlib import Path

INPUT_DIRECTORY = "tests/test_inputs/"

def cases_for_k(n):
    if n <= 12:
        return 48
    elif n <= 18:
        return 24
    elif n <= 24:
        return 12
    elif n <= 30:
        return 6
    else:
        return 3

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
    
    filepath = f"{INPUT_DIRECTORY}input_{n}_{case_index}.txt" 

    Path(filepath).parent.mkdir(parents = True, exist_ok = True)

    Path(filepath).write_text("\n".join(lines) + "\n", encoding = "utf-8")

    print(f"Created {filepath}")

def generate_random_input_series():
    n_values = range(3, 36, 3)

    for n in n_values:
        k_n = cases_for_k(n)
        print(f"\nGenerating {k_n} cases for n={n}")
        
        for case_index in range(cases_for_k(n)):
            seed = (n * 1000) + case_index
            generate_random_input(n, seed=seed, case_index=case_index)
