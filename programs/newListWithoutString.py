def filter_list(lst):
    # initialize an empty list to store non-string elements
    result = []

    # iterate through the elements in the input list
    for element in lst:
        # check if the element is a non-negative integer (not a string)
        if isinstance(element, int) and element >= 0:
            result.append(element)

    return result


print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))
