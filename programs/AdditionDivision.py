# Addition
number1 = float(input("Enter the first number for addition: "))
number2 = float(input("Enter the second number for addition: "))
number3 = float(input("Enter the third number for addition: "))
summary_result = number1 + number2 + number3
print(f"summary: {number1} + {number2} + {number3} = {summary_result}")
# Division
number4 = float(input("Enter the dividend for division: "))
number5 = float(input("Enter the divisor for division: "))
if number5 == 0:
    print("Error: Division by zero is not allowed")
else:
    div_result = number4 / number5
    print(f"Division: {number4} / {number5} ={div_result}")
