# sample list of numbers
numbers = [30, 10, 120, 5, 90]

# sort the list in descending order
numbers.sort(reverse=True)

# check if there are at least two element in the list
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number")
