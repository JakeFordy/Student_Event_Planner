def read_from_file(filename: str):
    activities = []
    total_time = 0
    total_cost = 0

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            f.readline()
            (total_time, total_cost) = f.readline().split(' ')
            for line in f:
                name, time, cost, enjoyment = line.strip().split()
                
                activities.append({
                    "name": name,
                    "time": int(time),
                    "cost": int(cost),
                    "enjoyment": int(enjoyment)                
                    })
        return activities, int(total_time), int(total_cost)
    
    except FileNotFoundError:
        print("Error: could not find file.")
        return [], -1, -1 #IM NOT SURE IF THIS IS THE BEST WAY TO DO IT???
    except TypeError:
        print("Error: values in file are invalid types/format.")
        return [], -1, -1
    except Exception:
        print("Error: problem occurred reading file.")
        return [], -1, -1


def print_solution(algorithm_name: str, enjoyment: int, solution: dict, time_budget: int, exec_time):
    print('\n--- ', algorithm_name, ' ---')

    if len(solution) == 0:
        print("No solutions found within constraint(s).")
        print('\nExecution Time:', exec_time, 'seconds')
        return
    
    print('Selected Activities:')

    total_time = 0
    total_cost = 0

    for activity in solution:
        print(f'\t - {activity["name"]} ({activity["time"]} hours, £{activity["cost"]}, enjoyment {activity["enjoyment"]})')
        total_time += int(activity["time"])
        total_cost += int(activity["cost"])

    print('\nTotal Enjoyment:', enjoyment)
    print(f'Total Cost: £{total_cost}')
    #if only considering cost constraint, then also display how far over time it took
    if (total_time > time_budget):
        print(f'Total Time Used: {total_time} hours ({total_time-time_budget} hours over)')
    else:
        print(f'Total Time Used: {total_time} hours')

    print('\nExecution Time:', exec_time, 'seconds')
