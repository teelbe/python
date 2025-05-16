from collections import OrderedDict

# create na odreredDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])

# item to instert at the beginning
new_item = ('a', 1)

# create a new orderedDict with the new item as the first element
new_ordered_dict = OrderedDict([new_item])

# merge the new OrderedDict with the oriiginal OrderedDict
new_ordered_dict.update(ordered_dict)

# print the update OrderedDict
print("Updated OrderedDict: ", new_ordered_dict)
