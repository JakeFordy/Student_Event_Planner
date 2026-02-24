"""
Brute force algorithm

must generate all possible subsets and keep track of best solution (highest enjoyment)

returns in format:

========================================
EVENT PLANNER - RESULTS
========================================

Input File: input_small.txt
Available Time: 10 hours
Available Budget: £200

--- BRUTE FORCE ALGORITHM ---
Selected Activities:
- Game-Night (3 hours, £80, enjoyment 120)
- Pizza-Workshop (2 hours, £60, enjoyment 100)
- Hiking (5 hours, £30, enjoyment 140)

Total Enjoyment: 360
Total Time Used: 10 hours
Total Cost: £170

Execution Time: 0.002 seconds
"""
def bruteforce_costonly(activities, budget_left, current_enjoyment=0, current_selection=None, activity_num=0):
    """
    Goes through every possible combination of activities (given within time constraint) 
    by recursively branching between either taking or not taking the current activity.
    Base condition is when it reaches the final activity in the list. It will then return 
    up the current selection that provided the maximum enjoyment through the call stack.
    """
    #to avoid python early-bound default param, set default param of current_selection to empty list on run
    if current_selection is None:
        current_selection = []

    #base case - no more activities, evaluate current subset
    if activity_num == len(activities):

        #if within budget, return subset enjoyment, selection
        if budget_left >= 0:
            return current_enjoyment, current_selection
        
        #if not within budget, return empty enjoyment, selection
        return 0, current_selection
    

    #2 routes: either skip this activity or take it
    #A: Skip
    skip_enjoyment, skip_selection = bruteforce_costonly(activities, budget_left,
                                                         current_enjoyment,
                                                         current_selection, activity_num+1)

    #B: Take
    activity = activities[activity_num]
    take_enjoyment, take_selection = bruteforce_costonly(activities, budget_left - activity["cost"],
                                                        current_enjoyment + activity["enjoyment"],
                                                        current_selection + [activity],
                                                        activity_num+1)

    #if better selection when taking this activity
    if take_enjoyment > skip_enjoyment:
        return take_enjoyment, take_selection

    #else if better selection when skipping this activity
    return skip_enjoyment, skip_selection

def bruteforce_bothconstraints(activities, time_left, budget_left, current_enjoyment=0, current_selection=None, activity_num=0):
    """
    Goes through every possible combination of activities (given within both time & cost 
    constraints) by recursively branching between either taking or not taking the current activity.
    Base condition is when it reaches the final activity in the list. It will then return 
    up the current selection that provided the maximum enjoyment through the call stack.
    """
    #to avoid python early-bound default param, set default param of current_selection to empty list on run
    if current_selection is None:
        current_selection = []


    #base case - no more activities, evaluate current subset
    if activity_num == len(activities):

        #if within budget and time limit, return subset enjoyment, selection
        if time_left >= 0 and budget_left >= 0:
            return current_enjoyment, current_selection
        
        #if not within budget and time limit, return empty enjoyment, selection
        return 0, current_selection
    

    #2 routes: either skip this activity or take it
    #A: Skip
    skip_enjoyment, skip_selection = bruteforce_bothconstraints(activities, time_left,
                                                         budget_left, current_enjoyment,
                                                         current_selection, activity_num+1)
    #B: Take
    activity = activities[activity_num]
    take_enjoyment, take_selection = bruteforce_bothconstraints(activities, time_left - activity["time"],
                                                                budget_left - activity["cost"],
                                                                current_enjoyment + activity["enjoyment"],
                                                                current_selection + [activity],
                                                                activity_num+1)

    #if better selection when taking this activity, return 'take subset'
    if take_enjoyment > skip_enjoyment:
        return take_enjoyment, take_selection

    #else if better selection when skipping this activity, return 'skip subset'
    return skip_enjoyment, skip_selection
