number = int(input("Enter a number: "))
factorial = 1
if number < 0:
    print("Factorial does not exist for negative numbers")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print(f"The factorial of {number} is {factorial}")
