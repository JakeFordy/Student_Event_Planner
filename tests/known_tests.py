import os
from algorithms.components import read_from_file
from algorithms.bruteforce import bruteforce_costonly
from algorithms.dynamic import dynamic_costonly

KNOWN_DIRECTORY = "tests/known_inputs"

EXPECTED = {
    "test_exact_fit.txt": 55,
    "test_tradeoff.txt": 110,
    "test_both_binding.txt": 55,
    "test_unbounded_bug.txt": 10,
    "test_tie.txt": 20,
    "test_none_feasible.txt": 0,
}

def solve_bruteforce_costonly(filepath: str) -> int:
    activities, _, cost_budget = read_from_file(filepath)
    return bruteforce_costonly(0, cost_budget, [], activities)

def solve_dynamic_costonly(filepath: str) -> int:
    activities, _, cost_budget = read_from_file(filepath)
    return dynamic_costonly(cost_budget, activities)

def best_value(result):
    if isinstance(result, tuple):
        return result[0] 
    return result

def assertion_test():
    for fname, expected in EXPECTED.items():
        path = os.path.join(KNOWN_DIRECTORY, fname)

        bf = best_value(solve_bruteforce_costonly(path))
        dp = best_value(solve_dynamic_costonly(path))

        assert bf == expected, f"{fname}: brute force got {bf}, expected {expected}"
        assert dp == expected, f"{fname}: dynamic got {dp}, expected {expected}"

        print(f"PASS {fname}: enjoyment={expected}")

