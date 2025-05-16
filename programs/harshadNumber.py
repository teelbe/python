def is_harshad_number(num):
    # calculate the sun of the digits if the number
    digit_sum = sum(int(i) for i in str(num))

    # check if the number is divisible by the sum of the digits
    return num % digit_sum == 0


# input number
num = int(input("Enter a number: "))

# check if it is a Harshad Number
if is_harshad_number(num):
    print(f"{num} is a Harshad NUmber")
else:
    print(f"{num} is not a Harshad Number")
