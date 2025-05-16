def find_n_largest_element(lst, n):
    # sort the list in descending order
    sorted_list = sorted(lst, reverse=True)

    # get the first N elements
    largest_element = sorted_list[:n]

    return largest_element


# sample list of numbers
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]

# number of largest elements to find
N = int(input("N = "))

# find the N largest elements from the list
result = find_n_largest_element(numbers, N)

# print the N largest elements
print(f"The {N} largest elements in the list are: ", result)
