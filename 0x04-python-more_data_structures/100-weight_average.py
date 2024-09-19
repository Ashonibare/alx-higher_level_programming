def weight_average(my_list=[]):
    if not my_list:  # Return 0 if the list is empty
        return 0
    # To accumulate the sum of score * weight
    total_weighted_sum = 0
    total_weight = 0  # To accumulate the sum of weights

    for score, weight in my_list:
        # Multiply score by its weight
        total_weighted_sum += score * weight
        total_weight += weight  # Accumulate the total weight
    # Return the weighted average
    return total_weighted_sum / total_weight
