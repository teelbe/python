def is_disarium(number):
    # convert number to a string to iterate over its digits
    num_str = str(number)
    # calculate sum of digits
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    # check if sum is equal to the original number
    return digit_sum == number


# input number from user
try:
    num = int(input("Enter a number: "))
    # check if it's disarium number
    if is_disarium(num):
        print(f"{num} is a Disarium number")
    else:
        print(f"{num} is not a disarium number")
except ValueError:
    print("Invalid input. Please enter a valid number")
