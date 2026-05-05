# Student Event Planner

> ECM1414 Data Structures & Algorithms - University Coursework

A Python tool that finds the **optimal selection of activities** within a given budget (and optionally timeframe) to maximise enjoyment - implemented using three distinct algorithm approaches across two constraint modes.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithms-Knapsack-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Algorithms

Six algorithm variants are implemented, split by constraint mode:

| Algorithm | Cost only | Cost + Time |
|---|---|---|
| **Bruteforce** | ✅ | ✅ |
| **Dynamic Programming** | ✅ | ✅ |
| **Greedy Heuristic** | ✅ | ✅ |

The bruteforce approach guarantees an optimal solution but doesn't scale well. Dynamic programming is the efficient exact solution. Greedy is fast but approximate - useful for seeing where heuristics trade accuracy for speed.

---

## Getting Started

### Running the Planner

No dependencies required. Run the main script from the root directory:

```
python event_planner.py <input_file>
```

Replace `<input_file>` with one of the provided input files from the `/inputs` folder:

| File | Size |
|---|---|
| `input_small.txt` | 5-activity dataset |
| `input_medium.txt` | 12-activity dataset |
| `input_large.txt` | 25-activity dataset |

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

---

## Flags

Algorithm and constraint mode can be controlled via flags:

| Flag | Description |
|---|---|
| `-h` / `--help` | Show help and flag descriptions |
| `-b` | Run bruteforce algorithm |
| `-d` | Run dynamic programming algorithm |
| `-g` | Run greedy heuristic algorithm |
| `-1` | Cost constraint only |
| `-2` | Cost + time constraints |

**Example** - run only dynamic with both constraints:
```bash
python event_planner.py input_large.txt -d -2
```

**Example** - run all algorithms on only time constraint:
```bash
python event_planner.py input_large.txt -1
```

**Example** - show help:
```
python event_planner.py -h
```

> Note: Unless specified by flags, the program will run ALL 6 algorithm variants by default

---

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

