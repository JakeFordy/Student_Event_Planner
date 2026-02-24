# ECM1414_Event_Planner
Data Structures & Algorithms group coursework for ECM1414

Contains an Event Planner system that calculates and displays the most optimal selection of possible activities, within a given budget (and additionally timeframe) that produces the maximum enjoyment.

## How to Run and Dependencies:
The main program **event_planner.py** has no prequisites and can simply be ran in the top directory using:

`python event_planner.py input_file.txt`

where input_file.txt should be substituted for an appropriate file that exists within the /inputs folder, such as:
input_small.txt     input_medium.txt       input_large.txt

Optional flag arguments can also be added to run specific algorithms (see *flags*)

However, the testing script **tests.py** requires the following dependencies:
- NumPy
- Matplotlib

These can be installed with pip by running:
`pip install numpy`
`pip install matplotlib`

The tests.py script can then be ran in the top directory using:

`python tests.py`

Further terminal inputs are take in during runtime.

## Algorithms
Algorithms (and constraints considered) included:
- Bruteforce (cost only)  
- Bruteforce (cost & time)  
- Dynamic (cost only)  
- Dynamic (cost & time)  
- Greedy Heuristic (cost)  
- Greedy Heuristic (cost & time)  

## Project Folder:
The project folder is set out as follows:

./ECM1414_Event_Planner  
├── algorithms  
│   ├── bruteforce.py  
│   ├── components.py  
│   ├── dynamic.py  
│   ├── greedy.py  
│   └── __init__.py    
├── event_planner.py  
├── inputs  
│   ├── input_large.txt  
│   ├── input_medium.txt  
│   └── input_small.txt  
├── README.md   
├── tests  
│   ├── benchmark_case_creator.py  
│   ├── benchmark_graph.py  
│   ├── benchmark_inputs  
│   │   ├── ...  
│   │   ├── 'all test input txt files'  
│   │   └──  ...  
│   ├── benchmark_test.py  
│   ├── __init__.py  
│   ├── known_inputs   
│   │   ├── test_both_binding.txt  
│   │   ├── test_exact_fit.txt  
│   │   ├── test_none_feasible.txt  
│   │   ├── test_tie.txt  
│   │   ├── test_tradeoff.txt  
│   │   └── test_unbounded_bug.txt  
│   └── known_tests.py  
└── tests.py  
  
## Flags
There are also optional flags which can be typed to choose which specific algorithms to run and with how many constraints (time/cost), using the argparse library:
  -h, --help  Brings up a help paragraph and description of tags
  -b          Run bruteforce algorithm
  -d          Run dynamic algorithm
  -g          Run greedy heuristic algorithm
  -1          Use just cost constraint
  -2          Use time and cost constraints

  For example, to pull up the help description, in the top directory run:
  `python event_planner.py input_file.txt -h`

  