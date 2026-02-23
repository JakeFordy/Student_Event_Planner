"""
docstring

pass in ratio consts as args and through terminal (tho have default vals)


diffferent ratios:

- normalised_ratio = enjoyment / (cost/maxcost)

- weighted_ratio = enjoyment / (cost*weight)    or enjoyment / (cost*weight0 + time*weight1)

- combined_ratio = (enjoyment / cost) + (enjoyment / time)
"""

#sorts by ratio (custom function) descending
def merge_sort_activities(activities, get_ratio):
    if len(activities) <= 1:
        return activities
    
    mid = len(activities) // 2
    left = merge_sort_activities(activities[:mid], get_ratio)
    right = merge_sort_activities(activities[mid:], get_ratio)

    return merge(left, right, get_ratio)


def merge(left, right, get_ratio):
    merged_arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_ratio = get_ratio(left[i])
        right_ratio = get_ratio(right[j])

        #descending order
        if left_ratio > right_ratio:
            merged_arr.append(left[i])
            i+= 1
        else:
            merged_arr.append(right[j])
            j+= 1

    #add remaining items
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])

    return merged_arr


def greedy_costonly(total_budget, activities):
    """
    placeholder function
    """
    def get_ratio(activity):
        return activity["enjoyment"] / activity["cost"]
    
    #sort activities by ratio descending
    sorted_activities = merge_sort_activities(activities, get_ratio)

    selected_activities = []
    remaining_budget = total_budget
    total_enjoyment = 0

    #add all top activities that can afford
    for activity in sorted_activities:
        if activity["cost"] <= remaining_budget:
            selected_activities.append(activity)
            remaining_budget -= activity["cost"]
            total_enjoyment += activity["enjoyment"]

    return total_enjoyment, selected_activities

def greedy_bothconstraints(total_time, total_budget, activities, ratio_weighting=[50,1]):
    """
    placeholder function
    """

    def get_ratio(activity):
        return activity["enjoyment"] / (ratio_weighting[0]*activity["time"] + ratio_weighting[1]*activity["cost"])
    
    #sort activities by ratio descending
    sorted_activities = merge_sort_activities(activities, get_ratio)

    selected_activities = []
    remaining_budget = total_budget
    remaining_time = total_time
    total_enjoyment = 0

    #add all top activities that can afford
    for activity in sorted_activities:
        if activity["time"] <= remaining_time and activity["cost"] <= remaining_budget:
            selected_activities.append(activity)

            remaining_time -= activity["time"]
            remaining_budget -= activity["cost"]
            total_enjoyment += activity["enjoyment"]

    return total_enjoyment, selected_activities
