def move_to_end(lst, element):
    # initialize a count for the specified element
    count = lst.count(element)

    # remove all accurrences of the element from the list
    lst = [x for x in lst if x != element]

    # Append the element to the end of the list count timse
    lst.extend([element] * count)

    return  lst

print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a"))