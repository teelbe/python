def add_indexes(lst):
    # use list comprehension to add index to each element
    return [i + val for i, val in enumerate(lst)]

print(add_indexes([0,0,0,0,0]))
print("-------------------")
print(add_indexes([1,2,3,4,5]))
print("-------------------")
print(add_indexes([5,4,3,2,1]))
