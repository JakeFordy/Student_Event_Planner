import time

def get_data(path):
  activities = []

  with open(path, 'r') as f:
    data = [line.strip() for line in f.readlines()]

    # Get time limit and budget
    time_limit = int(data[1].split(' ')[0])
    budget = int(data[1].split(' ')[1])

    # Get activities data into workable format
    for row in data[2:]:
      row_data = row.split(' ')
      activities.append({
        'name': row_data[0],
        'time': int(row_data[1]),
        'cost': int(row_data[2]),
        'enjoyment': int(row_data[3])
      })

  return time_limit, budget, activities

def fit_time_limit(time_limit, activities):
  dp = [0] * (time_limit + 1)
  selected = [[] for _ in range(time_limit + 1)]

  for activity in activities:
    time_req = activity['time']
    enjoyment = activity['enjoyment']
    name = activity['name']

    for t in range(time_limit, time_req - 1, -1):
      if dp[t - time_req] + enjoyment > dp[t]:
        dp[t] = dp[t - time_req] + enjoyment
        selected[t] = selected[t - time_req] + [name]

  max_enjoyment = max(dp)
  max_index = dp.index(max_enjoyment)
  return max_enjoyment, selected[max_index]


def fit_budget(budget, activities):
  dp = [0] * (budget + 1)
  selected = [[] for _ in range(budget + 1)]

  for activity in activities:
    cost = activity['cost']
    enjoyment = activity['enjoyment']
    name = activity['name']

    for c in range(budget, cost - 1, -1):
      if dp[c - cost] + enjoyment > dp[c]:
        dp[c] = dp[c - cost] + enjoyment
        selected[c] = selected[c - cost] + [name]

  max_enjoyment = max(dp)
  max_index = dp.index(max_enjoyment)
  return max_enjoyment, selected[max_index]

if __name__ == '__main__':  

  # Get data
  path = './inputs/input_100.txt'
  time_limit, budget, activities = get_data(path)

  # Start timer
  start_time = time.time()

  # Find optimal activities
  time_limit__enjoyment, time_limit__plan = fit_time_limit(time_limit, activities)
  budget__enjoyment, budget__plan = fit_budget(budget, activities)

  # End timer
  end_time = time.time()

  # Print results
  print('\n==================================================================')

  print('\nDYNAMIC PROGRAMMING SOLUTION')
  print(f'\nInput file: {path.split("/")[-1]}')
  print(f'Time limit: {time_limit} hours')
  print(f'Budget: £{budget}')
  print(f'\nExecution time: {round((end_time - start_time) * 1000, 1)}ms (1dp)')

  print('\n==================================================================')

  print(f'\nFITTING TO TIME LIMIT:')
  print(f'\nActivities: {', '.join([activity.replace('-', ' ') for activity in budget__plan])}')
  print(f'\nEnjoyment: {time_limit__enjoyment}')
  print(f'Time used: {sum([activity["time"] for activity in activities if activity["name"] in time_limit__plan])} hours')
  print(f'Cost: £{sum([activity["cost"] for activity in activities if activity["name"] in time_limit__plan])}')

  print('\n==================================================================')

  print(f'\nFITTING TO BUDGET:')
  print(f'\nActivities: {', '.join([activity.replace('-', ' ') for activity in budget__plan])}')
  print(f'\nEnjoyment: {budget__enjoyment}')
  print(f'Time used: {sum([activity["time"] for activity in activities if activity["name"] in budget__plan])} hours')
  print(f'Cost: £{sum([activity["cost"] for activity in activities if activity["name"] in budget__plan])}')

  print('\n==================================================================\n')
