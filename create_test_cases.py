import random
from pathlib import Path

INPUT_DIRECTORY = "inputs/"

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

def generate_random_input_series(k=10):
    n_values = range(3, 36, 3)  # 5,10,15,...50

    for n in n_values:
        print(f"\nGenerating {k} cases for n={n}")
        
        for case_index in range(k):
            seed = (n * 1000) + case_index
            generate_random_input(n, seed=seed, case_index=case_index)

generate_random_input_series(k = 10)