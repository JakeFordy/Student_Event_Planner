"""
Quick, but non-optimal greedy heuristic algorithm

Uses a normalised ratio of enjoyment to cost and time, and uses that value
to sort each activity descending. It then goes through and continuously selects
activities from the top of the sorted list if it can afford it (cost/time constraints).

As it chooses the locally-optimal choice, it often does not return the solution with the 
highest enjoyment, but it gets quite close in an extremely quick time.
"""

from algorithms.components import TIME, COST, ENJOYMENT


# sorts by ratio (custom function) descending
# divide and conquer merge sort
def merge_sort_activities(activities: list, get_ratio: callable):
    """
    Merge sort that recursively splits the list into two halves until
    all elements in single item lists (base case). Call and return the
    sorted list from merge()
    """
    # base case (when split into single activities)
    if len(activities) <= 1:
        return activities

    # recursively split list into two halves
    mid = len(activities) // 2
    left = merge_sort_activities(activities[:mid], get_ratio)
    right = merge_sort_activities(activities[mid:], get_ratio)

    return merge(left, right, get_ratio)


def merge(left: list, right: list, get_ratio: callable):
    """
    Once all activities broken down into single item lists, 
    remerge all lists repeatedly, according to which activity 
    has the higher ratio (calculated using the callable argument)
    Return sorted list
    """
    merged_arr = []
    i = 0
    j = 0

    # iteratively move left and right pointers inwards
    while i < len(left) and j < len(right):
        left_ratio = get_ratio(left[i])
        right_ratio = get_ratio(right[j])

        # sort by ratio in descending order
        if left_ratio > right_ratio:
            merged_arr.append(left[i])
            i+= 1
        else:
            merged_arr.append(right[j])
            j+= 1

    # add remaining items
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def greedy_costonly(activities: list, total_budget: int):
    """
    Using the merge sort function, sorts all activities into a
    new list by ratio value descending (essentially most valuable activities).
    Iteratively go through and continuously select activities from the top of 
    the sorted list if it can afford it (cost/time constraints).
    """
    # custom cost ratio callable function (to sort activities)
    def get_ratio(activity):
        return activity[ENJOYMENT] / (activity[COST]/total_budget)
    
    # sort activities by ratio descending
    sorted_activities = merge_sort_activities(activities, get_ratio)

    selected_activities = []
    remaining_budget = total_budget
    total_enjoyment = 0

    # add all top activities that can afford within cost budget
    for activity in sorted_activities:
        if activity[COST] <= remaining_budget:
            selected_activities.append(activity)
            remaining_budget -= activity[COST]
            total_enjoyment += activity[ENJOYMENT]

    return total_enjoyment, selected_activities

def greedy_bothconstraints(activities: list, total_time: int, total_budget: int):
    """
    Using the merge sort function, sorts all activities into a
    new list by ratio value descending (essentially most valuable activities).
    Iteratively go through and continuously select activities from the top of 
    the sorted list if it can afford it (cost/time constraints).
    """

    # custom cost&time ratio callable function (to sort activities)
    def get_ratio(activity):
        return activity[ENJOYMENT] / (activity[TIME]/total_time) + activity[ENJOYMENT] / (activity[COST]/total_budget)

    # sort activities by ratio descending
    sorted_activities = merge_sort_activities(activities, get_ratio)

    selected_activities = []
    remaining_budget = total_budget
    remaining_time = total_time
    total_enjoyment = 0

    # add all top activities that can afford within time&cost constraints
    for activity in sorted_activities:
        if activity[TIME] <= remaining_time and activity[COST] <= remaining_budget:
            selected_activities.append(activity)

            remaining_time -= activity[TIME]
            remaining_budget -= activity[COST]
            total_enjoyment += activity[ENJOYMENT]

    return total_enjoyment, selected_activities
