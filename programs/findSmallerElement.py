# sample list of numbers
numbers = [30, 10, -45, 5, 20]

# initialize a variable to store the minimum value, initially set
minimum = numbers[0]

# iterate through the list and update the minimum value
for i in numbers:
    if i < minimum:
        minimum = i
# print result
print("Smaller of element in the list is:", minimum)
