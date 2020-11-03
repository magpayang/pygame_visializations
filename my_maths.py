
def sum_arrays(input_array):
    sum = 0
    for entry in input_array:
        sum += entry
    return sum

def max_arrays(input_array):
    max = 0
    for entry in input_array:
        if entry > max:
            max = entry
        else:
            pass
    return max