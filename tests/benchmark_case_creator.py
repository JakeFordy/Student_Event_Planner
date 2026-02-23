'''
Benchmark Input File Generator

This script generates structured input files for benchmark testing.

The generated files:
- Follow a consistent input file structure.
- Contain randomly generated activities.
- Use approximately 50% of the total available time and cost as constraints
  to avoid creating trivial problem instances.

Generation rules:
- 30 files per n from 2 to 100 (step size = 2)
- 10 files per n from 110 to 300 (step size = 10)
- 3 files per n from 350 to 1000 (step size = 50)

Output directory:
    tests/benchmark_inputs/
'''

import random
from pathlib import Path

OUTPUT_DIRECTORY = "tests/benchmark_inputs/"

def step_for_n(n):
    """
    This determines the step between values of n based upon n
    """
    if n <= 98:
        return 2
    elif n <= 290:
        return 10
    else:
        return 50

def cases_for_n(n):
    """
    This determines the number of cases created based upon n
    """
    if n <= 100:
        return 30
    elif n <= 500:
        return 10
    else:
        return 3

def generate_random_input(n, seed = 0, case_index = 0):
    """
    Generate a single random input file of size n
    """
    
    # Create a deterministic random generator to allow reproducible results
    rng = random.Random(seed)

    activities = [] 

    # Generate random activities
    for i in range(n):
        name = f"Act-{i}"
        time = rng.randint(1, 10)
        cost = rng.randint(1, 20)
        enjoyment = rng.randint(1, 100)
        activities.append((name, time, cost, enjoyment))

    # Compute total time and cost across all activites
    total_cost = sum(a[2] for a in activities)
    total_time = sum(a[1] for a in activities)

    # Set budget constrains to ~50% of total
    # This prevents a trivial full selection case
    Cost_budget = total_cost // 2
    Time_allocation = total_time // 2

    # Prepare file contents
    lines = []
    lines.append(str(n))
    lines.append(f"{Time_allocation} {Cost_budget}")

    # Append activity data
    for name_append, time_append, cost_append, enjoyment_append in activities:
        lines.append(f"{name_append} {time_append} {cost_append} {enjoyment_append}")
    
    # Create filepath
    filepath = f"{OUTPUT_DIRECTORY}input_{n}_{case_index}.txt" 

    # Write file to disk    
    Path(filepath).write_text("\n".join(lines) + "\n", encoding = "utf-8")

def generate_random_input_series(a :int):
    """
    Generate a full benchmark dataset according to predefined rules
    """
    n = int(2)
    total_files = 0

    while n <= a:
        cases_per_n = cases_for_n(n)
        for case_index in range(cases_per_n):
            
            # Unique deterministic seed to allow reproducible files
            seed = (n * 1000) + case_index

            generate_random_input(n, seed=seed, case_index=case_index)
            total_files += 1
        
        # Increase n using the dynamic step size
        n += step_for_n(n)

    print(f"\n{total_files} input files have been created for benchmark tests.")