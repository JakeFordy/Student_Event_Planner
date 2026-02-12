def read_from_file(filename: str):
    activities = []
    total_time = 0
    total_cost = 0

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


def print_solution(algorithm: str, enjoyment: int, solution: dict, time_budget: int, exec_time):
    print('\n--- ', algorithm, ' ---')
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
