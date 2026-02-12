"""
Docstring for dynamic
"""

def dynamic_costonly(cost_budget, activities):
    n = len(activities)

    enjoyment_table = []

    #create enjoyment table (n+1)x(cost_budget+1) size full of 0s
    for i in range(n+1):
        row = []
        for j in range(cost_budget+1):
            row.append(0)
        enjoyment_table.append(row)

    #go through all options and fill table:
    for i in range(1, n+1):
        activity_cost = activities[i-1]["cost"]
        activity_enjoyment = activities[i-1]["enjoyment"]

        for current_budget in range(cost_budget+1):

            #either skip activity:
            enjoyment_table[i][current_budget] = enjoyment_table[i-1][current_budget]

            #or take activity (if can afford)
            if activity_cost <= current_budget:
                take_value = enjoyment_table[i-1][current_budget - activity_cost] + activity_enjoyment

                #if greater enjoyment than current selection for budget, then add:
                if take_value > enjoyment_table[i][current_budget]:
                    enjoyment_table[i][current_budget] = take_value

    max_enjoyment = enjoyment_table[n][cost_budget]

    #backtrack to return selected activities
    selected_activities = []
    remaining_budget = cost_budget
    
    for i in range(n, 0, -1):
        if enjoyment_table[i][remaining_budget] != enjoyment_table[i-1][remaining_budget]:
            activity = activities[i-1]
            selected_activities.append(activity)
            remaining_budget -= activity["cost"]

    return max_enjoyment, selected_activities