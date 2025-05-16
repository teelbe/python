def missing_num(lst):
    total_sum = sum(range(1,11)) # sum of numbers from 1 to 10
    given_sum = sum(lst) # sum of the given list od numbers
    missing = total_sum - given_sum
    return missing

print(missing_num([1,2,3,4,6,7,8,9,10]))
print("-------------------")
print(missing_num([7,2,3,6,5,9,1,4,8]))
print("-------------------")
print(missing_num([10,5,1,2,4,6,8,3,9]))
