original_list = [1, 2, 3, 4, 5]
# 1. using the slice operator
cloned_1 = original_list[:]
# 2. using the list() constructor
cloned_2 = list(original_list)
# 3. using list comprehension
cloned_3 = [item for item in original_list]
print("Original list:           ", original_list)
print("Cloned by slice:         ", cloned_1)
print("Cloned by constructor:   ", cloned_2)
print("Cloned by comprehension: ", cloned_3)
