"""
Contains all miscellaneous helper functions for reading files and printing formatted outputs.
- read_from_file()
- print_solution()
- print_header()

Also contains constants for the string values, to avoid any possible typos in accessing dicts
"""
# CONSTANTS
NAME = "name"
TIME = "time"
COST = "cost"
ENJOYMENT = "enjoyment"

def read_from_file(filename: str):
    """
    Given a filename, reads through each line and interprets values.
    - Ignores the first line
    - Splits the 2nd line in half (time is 1st number, cost is 2nd)
    - For every other line (activity), it splits them into name, time, cost, enjoyment
    Contains error/exception handling with appropriate error messages.
    Returns the read activities list, total time and total cost
    """
    activities = []
    total_time = 0
    total_cost = 0

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            f.readline() # ignore first line (title)
            (total_time, total_cost) = f.readline().split(' ')
            for line in f:
                name, time, cost, enjoyment = line.strip().split()

                activities.append({
                    NAME: name,
                    TIME: int(time),
                    COST: int(cost),
                    ENJOYMENT: int(enjoyment)                
                    })
        return activities, int(total_time), int(total_cost)

    except FileNotFoundError:
        print("Error: could not find file.")
        return [], -1, -1
    except (TypeError, ValueError):
        print("Error: values in file are invalid types/format.")
        return [], -1, -1
    except Exception:
        print("Error: problem occurred reading file.")
        return [], -1, -1


def print_solution(algo_name: str, enjoyment: int, solution: dict, time_budget: int, exec_time):
    """
    Prints the given algorithm name along with a formatted list of its selected activities.
    Calculates the total time and cost used, displaying them accordingly.
    Also displays the total running time.
    """
    print('\n--- ', algo_name, ' ---')

    # custom message if no solution found
    if len(solution) == 0:
        print("No solutions found within constraint(s).")
        print('\nExecution Time:', exec_time, 'seconds')
        return

    print('Selected Activities:')

    total_time = 0
    total_cost = 0

    # print each activity, and calculate total time and cost
    for activity in solution:
        print(f'\t - {activity[NAME]} ({activity[TIME]} hours, £{activity[COST]}, enjoyment {activity[ENJOYMENT]})')
        total_time += int(activity[TIME])
        total_cost += int(activity[COST])

    print('\nTotal Enjoyment:', enjoyment)
    print(f'Total Cost: £{total_cost}')

    # if only considering cost constraint, then also display how far over time it took
    if total_time > time_budget:
        print(f'Total Time Used: {total_time} hours ({round(total_time-time_budget)} hours over)')
    else:
        print(f'Total Time Used: {total_time} hours')

    print('\nExecution Time:', exec_time, 'seconds')


def print_header(input_file: str, time_budget: int, cost_budget: int):
    """
    Prints the starting header for the following outputs,
    including title, input file used, and constraints.
    """
    print('========================================')
    print('EVENT PLANNER - RESULTS')
    print('========================================\n')
    print('Input file:', input_file)
    print('Available Time:', time_budget, 'hours')
    print(f'Available Budget: £{cost_budget}')
