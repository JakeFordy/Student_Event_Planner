"""
Recursively iterates through each activity and branches between “taking” and “skipping” 
the activity. Thus, creates every single possible subset of selected activities (2^n total subsets)

It keeps recursively calling/iterating until reaches last activity, and returns enjoyment 
(so long as within cost constraint). It gathers the best possible enjoyment subset and returns up 
through the recursive call stack, comparing whether taking or skipping the activity led to the 
better subset. Overall returns the total enjoyment and activity selection

"""

from algorithms.components import TIME, COST, ENJOYMENT

def bruteforce_costonly(activities: list, budget_left: int, current_enjoyment: int=0, current_selection: list=None, activity_num: int=0):
    """
    Recursively iterate through every possible combination of activities (given within time 
    constraint) by branching between either taking or not taking the current activity.
    Base condition is when it reaches the final activity in the list. It will then return 
    up the current selection that provided the maximum enjoyment through the call stack.

    Default base values for current_enjoyment, current_selection and activity_num so that the 
    algorithm can be first called and started with only necessary args (activities, budget_left, 
    current_enjoyment), similar to other algorithms.
    """
    # (avoid python early-bound default param), set default param of current_selection to empty list
    if current_selection is None:
        current_selection = []

    # base case - no more activities, evaluate current subset
    if activity_num == len(activities):

        # if within budget, return subset enjoyment, selection
        if budget_left >= 0:
            return current_enjoyment, current_selection

        # if not within budget, return empty enjoyment, selection
        return 0, current_selection


    # 2 routes: either skip this activity or take it
    # A: Skip (increment activity, but keep values same)
    skip_enjoyment, skip_selection = bruteforce_costonly(activities, budget_left,
                                                         current_enjoyment,
                                                         current_selection, activity_num+1)

    # B: Take (increment activity, and calculate new vals)
    activity = activities[activity_num]
    take_enjoyment, take_selection = bruteforce_costonly(activities, budget_left - activity[COST],
                                                        current_enjoyment + activity[ENJOYMENT],
                                                        current_selection + [activity],
                                                        activity_num+1)

    # if better selection when taking this activity
    if take_enjoyment > skip_enjoyment:
        return take_enjoyment, take_selection

    # else if better selection when skipping this activity
    return skip_enjoyment, skip_selection

def bruteforce_bothconstraints(activities: list, time_left: int, budget_left: int, current_enjoyment: int=0, current_selection: list=None, activity_num: int=0):
    """
    Recursively iterates through every possible combination of activities (given within both time 
    & cost constraints) by branching between either taking or not taking the current activity.
    Base condition is when it reaches the final activity in the list. It will then return 
    up the current selection that provided the maximum enjoyment through the call stack.

    Default base values for current_enjoyment, current_selection and activity_num so that the 
    algorithm can be first called and started with only necessary args (activities, budget_left, 
    current_enjoyment), similar to other algorithms.
    """
    # (avoid python early-bound default param), set default param of current_selection to empty list
    if current_selection is None:
        current_selection = []


    # base case - no more activities, evaluate current subset
    if activity_num == len(activities):

        # if within budget and time limit, return subset enjoyment, selection
        if time_left >= 0 and budget_left >= 0:
            return current_enjoyment, current_selection

        # if not within budget and time limit, return empty enjoyment, selection
        return 0, current_selection


    #2 routes: either skip this activity or take it
    # A: Skip (increment activity, but keep values same)
    skip_enjoyment, skip_selection = bruteforce_bothconstraints(activities, time_left,
                                                         budget_left, current_enjoyment,
                                                         current_selection, activity_num+1)

    # B: Take (increment activity, and calculate new vals)
    activity = activities[activity_num]
    take_enjoyment, take_selection = bruteforce_bothconstraints(activities,
                                                        time_left - activity[TIME],
                                                        budget_left - activity[COST],
                                                        current_enjoyment + activity[ENJOYMENT],
                                                        current_selection + [activity],
                                                        activity_num+1)

    # if better selection when taking this activity, return 'take subset'
    if take_enjoyment > skip_enjoyment:
        return take_enjoyment, take_selection

    # else if better selection when skipping this activity, return 'skip subset'
    return skip_enjoyment, skip_selection
