def find_largest_element(arr):
    if not arr:
        return "Array is empty"

    # Initialize the first element as the largest
    largest_element = arr[0]

    # iterate through the array to find the largest element
    for element in arr:
        if element > largest_element:
            largest_element = element
    return largest_element


# example usage:
my_array = [10, 20, 40, 99]
result = find_largest_element(my_array)
print(f"The largest element in the array is: {result}")
