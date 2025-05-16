# sample doctionary
my_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}

# initialize an empty set to store uniqu values
uni_val = set()

# iterate through the values of the dictionary
for i in my_dict.values():
    # add each values to the set
    uni_val.add(i)

# convert the set of unique values back to a list (if needed)
unique_values_list = list(uni_val)

# print the unique values
print("Unique values in the dictionary:", unique_values_list)
