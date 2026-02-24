"""
Dynamic algorithms work by splitting the problem into subproblems and then adding the 
solutions of the subproblems together to solve the overall problem.

Our dynamic algorithm takes a bottom-up approach that solves all related sub-problems 
first and branches upwards. It creates an enjoyment table with all the possible activities 
listed and goes through the table for each activity, adding them up one-by-one depending on 
if there is still enough budget to cover the cost of the activity. It then calculates the enjoyment 
level by adding together the enjoyment values of all the items that are within budget. The algorithm 
backtracks to create the list of the best combination of activities to get the most enjoyment for 
the given budget and also avoids repeating activities which are not allowed in the problem brief. 
The activity is only added if it creates a higher enjoyment level than without adding it. The end 
combination of activities may not use all of the available budget but should never go over budget.
"""

from algorithms.components import TIME, COST, ENJOYMENT


def dynamic_costonly(activities: list, total_budget: int):
    """
    Creates an empty 2D enjoyment table, then iterates through all activities, filling the table
    by either taking or skipping the activity. Afterwards, it backtracks through the table and
    figures out the selected activities using the max enjoyment.
    Takes into account just cost (not time).
    Returns max enjoyment and selected activities
    """
    total_activities = len(activities)

    enjoyment_table = []

    # create enjoyment table (n+1)x(cost_budget+1) size full of 0s
    for _ in range(total_activities+1):
        row = []
        for _ in range(total_budget+1):
            row.append(0)
        enjoyment_table.append(row)

    # go through all options and fill table:
    for i in range(1, total_activities+1):
        activity_cost = activities[i-1][COST]
        activity_enjoyment = activities[i-1][ENJOYMENT]

        for budget_left in range(total_budget+1):

            # either skip activity:
            skip_value = enjoyment_table[i-1][budget_left]  #assume best value is if we skip
            take_value = 0

            # or take activity (if can afford)
            if activity_cost <= budget_left:
                take_value = enjoyment_table[i-1][budget_left - activity_cost] + activity_enjoyment

            if skip_value > take_value:
                enjoyment_table[i][budget_left] = skip_value
            else:
                enjoyment_table[i][budget_left] = take_value
                

    max_enjoyment = enjoyment_table[total_activities][total_budget]

    # backtrack to return selected activities
    selected_activities = []
    remaining_budget = total_budget

    for i in range(total_activities, 0, -1):
        if enjoyment_table[i][remaining_budget] != enjoyment_table[i-1][remaining_budget]:
            activity = activities[i-1]
            selected_activities.append(activity)
            remaining_budget -= activity[COST]

    return max_enjoyment, selected_activities

def dynamic_bothconstraints(activities: list, total_time: int, total_budget: int):
    """
    Creates an empty 2D enjoyment table, then iterates through all activities, filling the table
    by either taking or skipping the activity. Afterwards, it backtracks through the table and
    figures out the selected activities using the max enjoyment.
    Takes into account time and cost.
    Returns max enjoyment and selected activities
    """
    total_activities = len(activities)
    
    enjoyment_table = []

    # create 3d enjoyment table (n+1)x(budget+1)x(time+1) size full of 0s
    for _ in range(total_activities+1):
        row = []
        for _ in range(total_time+1):
            column = []
            for _ in range(total_budget+1):
                column.append(0)
            row.append(column)
        enjoyment_table.append(row)

    # go through all options and fill table:
    for i in range(1, total_activities+1):
        activity_time = activities[i-1][TIME]
        activity_cost = activities[i-1][COST]
        activity_enjoyment = activities[i-1][ENJOYMENT]

        for time_left in range(total_time+1):
            for budget_left in range(total_budget+1):

                # either skip activity:
                skip_value = enjoyment_table[i-1][time_left][budget_left]
                take_value = 0

                # or take activity (if can afford)
                if activity_time <= time_left and activity_cost <= budget_left:
                    take_value = enjoyment_table[i-1][time_left - activity_time][budget_left - activity_cost] + activity_enjoyment

                if skip_value > take_value:
                    enjoyment_table[i][time_left][budget_left] = skip_value
                else:
                    enjoyment_table[i][time_left][budget_left] = take_value

    max_enjoyment = enjoyment_table[total_activities][total_time][total_budget]

    # backtrack to return selected activities
    selected_activities = []
    remaining_time = total_time
    remaining_budget = total_budget

    for i in range(total_activities, 0, -1):
        activity = activities[i-1]
        activity_time = activity[TIME]
        activity_cost = activity[COST]
        activity_enjoyment = activity[ENJOYMENT]

        # skip if cost and time are not within boundary (to prevent negative indexing in next lines)
        if remaining_time < activity_time or remaining_budget < activity_cost:
            continue

        # if value is same as cell where it wouldve been stored if taken, then the activity was taken (so add it to list)
        if enjoyment_table[i][remaining_time][remaining_budget] == (enjoyment_table[i-1][remaining_time - activity_time][remaining_budget - activity_cost] + activity_enjoyment):
            selected_activities.append(activity)
            remaining_time -= activity[TIME]
            remaining_budget -= activity[COST]

    return max_enjoyment, selected_activities
