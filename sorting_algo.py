
def sequential_sort_one_pass(input_array):
    """
    One pass only. completion of sorting is done by the main while loop at len(input_array)-1 times
    :param input_array:
    :return:
    """
    if len(input_array)==1:
        return input_array
    else:
        if input_array[0]>input_array[1]:
            temp = input_array[1]
            input_array[1]=input_array[0]
            input_array[0]=temp

            return input_array[:1]+sequential_sort_one_pass(input_array[1:])

        else:
            return input_array[:1] + sequential_sort_one_pass(input_array[1:])

def selection_sort_one_pass(input_array):
    current_largest = 0
    index_of_current_largest = 0
    def index_largest(input_array, current_largest, index_of_current_largest):
        if input_array[0]>current_largest:
            current_largest = input_array[0]
            index_of_current_largest = 0

        if len(input_array)==1:  # reached the end of array during comparison
            return current_largest, index_of_current_largest
        else:
            return index_largest(input_array[1:], current_largest, index_of_current_largest)

    current_largest, index_of_current_largest = index_largest(input_array, current_largest, index_of_current_largest)

    if index_of_current_largest==len(input_array)-1:
        pass
    else:
        temp = input_array[-1]
        input_array[-1] = current_largest
        input_array[index_of_current_largest] = temp

    if len(input_array)==1:
        return input_array
    else:
        selection_sort_one_pass(input_array[:len(input_array)]) + input_array[len(input_array):]






