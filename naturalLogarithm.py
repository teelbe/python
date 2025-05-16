import math

number = float(input("Enter a number: "))
if number <= 0:
    print("Please enter a positive number")
else:
    # calculate the natural logarithm ( base e) of the number
    result = math.log(number)
    print(f"Natural logarithm of {number} is: {result}")
