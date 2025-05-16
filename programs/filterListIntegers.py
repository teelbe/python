def filter_list(lst):
    # use a list comprehension to filter out integers
    return [ x for x in lst if isinstance(x, int)]

print(filter_list([1, 2, 3, "a", "b", 4]))
print("-------------------")
print(filter_list(["A", 0, "Edabit", 1729, "Python", 1729]))
print("-------------------")
print(filter_list(["Nothing", "here"]))
