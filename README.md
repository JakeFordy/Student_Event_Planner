# Student Event Planner

A Python-based event planning tool built for the ECM1414 Data Structures & Algorithms module. Given a list of possible activities, a budget, and an optional time constraint, it finds the optimal selection of activities to maximise enjoyment.

## Getting Started

### Running the Planner

No dependencies required. Run the main script from the root directory:

```
python event_planner.py <input_file>
```

Replace `<input_file>` with one of the provided input files from the `/inputs` folder:

```
input_small.txt
input_medium.txt
input_large.txt
```

You can also pass optional flags to control which algorithm runs (see [Flags](#flags)).

### Running the Tests

The test script requires two additional dependencies:

```
pip install numpy matplotlib
```

Then run from the root directory:

```
python tests.py
```

Further prompts will appear in the terminal during runtime.

## Algorithms

Six algorithm variants are included, covering two constraint modes (cost only, or cost + time):

- Brute Force (cost only)
- Brute Force (cost & time)
- Dynamic Programming (cost only)
- Dynamic Programming (cost & time)
- Greedy Heuristic (cost only)
- Greedy Heuristic (cost & time)

## Project Structure

```
./ECM1414_Event_Planner
├── algorithms/
│   ├── bruteforce.py
│   ├── components.py
│   ├── dynamic.py
│   ├── greedy.py
│   └── __init__.py
├── inputs/
│   ├── input_large.txt
│   ├── input_medium.txt
│   └── input_small.txt
├── tests/
│   ├── benchmark_case_creator.py
│   ├── benchmark_graph.py
│   ├── benchmark_inputs/
│   ├── benchmark_test.py
│   ├── known_inputs/
│   │   ├── test_both_binding.txt
│   │   ├── test_exact_fit.txt
│   │   ├── test_none_feasible.txt
│   │   ├── test_tie.txt
│   │   ├── test_tradeoff.txt
│   │   └── test_unbounded_bug.txt
│   ├── known_tests.py
│   └── __init__.py
├── event_planner.py
├── tests.py
└── README.md
```

## Flags

Optional flags can be passed to select specific algorithms and constraint modes:

| Flag | Description |
|------|-------------|
| `-h`, `--help` | Show help and flag descriptions |
| `-b` | Run brute force algorithm |
| `-d` | Run dynamic programming algorithm |
| `-g` | Run greedy heuristic algorithm |
| `-1` | Use cost constraint only |
| `-2` | Use both cost and time constraints |

Example - show help:
```
python event_planner.py <input_file> -h
```
