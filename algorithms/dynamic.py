"""
Docstring for dynamic

note for future reference:
backtracking algo is different in 2d than in 1d.

this is because
...

also reminder for presentation: that sometimes bruteforce/dynamic might get diff cost/time but same enj
this is cuz we not optimising for MINIMAL cost/time, just MAX enj
we could add this tho by:

...


"""

def dynamic_costonly(total_budget, activities):
    """
    docstring
    """
    total_activities = len(activities)

    enjoyment_table = []

    #create enjoyment table (n+1)x(cost_budget+1) size full of 0s
    for _ in range(total_activities+1):
        row = []
        for _ in range(total_budget+1):
            row.append(0)
        enjoyment_table.append(row)

    #go through all options and fill table:
    for i in range(1, total_activities+1):
        activity_cost = activities[i-1]["cost"]
        activity_enjoyment = activities[i-1]["enjoyment"]

        for budget_left in range(total_budget+1):

            #either skip activity:
            skip_value = enjoyment_table[i-1][budget_left]  #assume best value is if we skip
            take_value = 0

            #or take activity (if can afford)
            if activity_cost <= budget_left:
                take_value = enjoyment_table[i-1][budget_left - activity_cost] + activity_enjoyment

            if skip_value > take_value:
                enjoyment_table[i][budget_left] = skip_value
            else:
                enjoyment_table[i][budget_left] = take_value
                

    max_enjoyment = enjoyment_table[total_activities][total_budget]

    #backtrack to return selected activities
    selected_activities = []
    remaining_budget = total_budget

    for i in range(total_activities, 0, -1):
        if enjoyment_table[i][remaining_budget] != enjoyment_table[i-1][remaining_budget]:
            activity = activities[i-1]
            selected_activities.append(activity)
            remaining_budget -= activity["cost"]

    return max_enjoyment, selected_activities

def dynamic_bothconstraints(total_time, total_budget, activities):
    """
    docstring
    """
    total_activities = len(activities)

    enjoyment_table = []

    #create 3d enjoyment table (n+1)x(budget+1)x(time+1) size full of 0s
    for _ in range(total_activities+1):
        row = []
        for _ in range(total_time+1):
            column = []
            for _ in range(total_budget+1):
                column.append(0)
            row.append(column)
        enjoyment_table.append(row)

    #go through all options and fill table:
    for i in range(1, total_activities+1):
        activity_time = activities[i-1]["time"]
        activity_cost = activities[i-1]["cost"]
        activity_enjoyment = activities[i-1]["enjoyment"]

        for time_left in range(total_time+1):
            for budget_left in range(total_budget+1):

                #either skip activity:
                skip_value = enjoyment_table[i-1][time_left][budget_left]
                take_value = 0

                #or take activity (if can afford)
                if activity_time <= time_left and activity_cost <= budget_left:
                    take_value = enjoyment_table[i-1][time_left - activity_time][budget_left - activity_cost] + activity_enjoyment

                if skip_value > take_value:
                    enjoyment_table[i][time_left][budget_left] = skip_value
                else:
                    enjoyment_table[i][time_left][budget_left] = take_value


    max_enjoyment = enjoyment_table[total_activities][total_time][total_budget]

    #backtrack to return selected activities
    selected_activities = []
    remaining_time = total_time
    remaining_budget = total_budget

    for i in range(total_activities, 0, -1):
        activity = activities[i-1]
        activity_time = activity["time"]
        activity_cost = activity["cost"]
        activity_enjoyment = activity["enjoyment"]

        #skip if cost and time are not within boundary (to prevent negative indexing in next lines)
        if remaining_time < activity_time or remaining_budget < activity_cost:
            continue

        #if value is same as cell where it wouldve been stored if taken, then the activity was taken (so add it to list)
        if enjoyment_table[i][remaining_time][remaining_budget] == (enjoyment_table[i-1][remaining_time - activity_time][remaining_budget - activity_cost] + activity_enjoyment):
            selected_activities.append(activity)
            remaining_time -= activity["time"]
            remaining_budget -= activity["cost"]

    return max_enjoyment, selected_activities

