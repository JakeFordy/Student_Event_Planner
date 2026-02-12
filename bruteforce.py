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


def bruteforce_costonly(i, cost_left, current_selection, activities):
    #base - no more activities
    if i == len(activities):
        return 0, current_selection

    #2 routes: either skip this activity or take it
    #A: skip
    skip_enjoyment, skip_selection = bruteforce(i+1, cost_left, current_selection, activities)

    #B: Take (only if possible tho)
    if cost_left >= activities[i]["cost"]:
        take_enjoyment, take_selection = bruteforce(i+1, cost_left - activities[i]["cost"], current_selection + [activities[i]], activities)
        take_enjoyment += activities[i]["enjoyment"]

        #if better selection when taking this activity
        if take_enjoyment > skip_enjoyment:
            return take_enjoyment, take_selection

    #else if better selection when skipping this activity
    return skip_enjoyment, skip_selection

def bruteforce(i, time_left, cost_left, current_selection, activities):
    #base - no more activities
    if i == len(activities):
        return 0, current_selection

    #2 routes: either skip this activity or take it
    #A: skip
    skip_enjoyment, skip_selection = bruteforce(i+1, time_left, cost_left, current_selection, activities)

    #B: Take (only if possible tho)
    if time_left >= activities[i]["time"] and cost_left >= activities[i]["cost"]:
        take_enjoyment, take_selection = bruteforce(i+1, time_left - activities[i]["time"], cost_left - activities[i]["cost"], current_selection + [activities[i]], activities)
        take_enjoyment += activities[i]["enjoyment"]

        #if better selection when taking this activity
        if take_enjoyment > skip_enjoyment:
            return take_enjoyment, take_selection

    #else if better selection when skipping this activity
    return skip_enjoyment, skip_selection