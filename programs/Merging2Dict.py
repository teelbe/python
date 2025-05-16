# 1. using the update() method
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)

# the merged dictionary is now in dict 1
print("Merged Dictionary (using update()): ", dict1)

# 2. using dictionary unpacking

dict3 = {'e': 5, 'f': 6}
dict4 = {'g': 7, 'h': 8}

# merge dict4 into dict3 using dictionary unpacking
merged_dict = {**dict3, **dict4}

# the merged dictionary is now in merged_dict
print("Merged Dictionary (using dictionary unpacking): ", merged_dict)
