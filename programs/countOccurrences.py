def count_occurrences(l, element):
    count = l.count(element)
    return count


# example usage
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
element_to_count = int(input("Enter element to count:"))

occurrences = count_occurrences(my_list, element_to_count)
if element_to_count in my_list:
    print(f"The element {element_to_count} appears {occurrences} in the list")
else:
    print(f"The element {element_to_count} is not exist in the list")
