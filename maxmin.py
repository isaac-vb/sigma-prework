def find_min_max(array):
    min_value = max_value = array[0]
    for num in array:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    return min_value, max_value

test_array = [2, 4, 1, 0, 2, -1]
minimum, maximum = find_min_max(test_array)
print("Minimum value: ", minimum)
print("Maximum value: ", maximum)
