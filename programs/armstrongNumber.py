number = int(input("Enter a number: "))
# calculate the number of digits in number
num_str = str(number)
num_digits = len(num_str)
# initialize variables
sum_of_power = 0
temp_num = number
# calculate the sum of digits raised to the power of num_digits
while temp_num > 0:
    digit = temp_num % 10
    sum_of_power += digit ** num_digits
    temp_num //= 10
# check if it's an Armstrong number
if sum_of_power == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
