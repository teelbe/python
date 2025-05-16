# sample list of numbers
numbers = [30, 10, 20, 55, -75, 120]

# initialize a variable to store the minimum value
maximum = numbers[0]
# iterate through the list and update a max value
for i in numbers:
    if i > maximum:
        maximum = i

# print result
print("The largest number in the list is:", maximum)
