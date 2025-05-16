number = int(input("Enter a number: "))
# define flag variable
flag = False
if number == 1:
    print(f"{number}, is not a prime number")
elif number > 1:
    # check for factor
    for i in range(2, number):
        if (number % i) == 0:
            flag = True  # if factor iis found, set flag to true
            # break the loop
            break
    # check if flag is true
if flag:
    print(f"{number}, is not a prime number")
else:
    print(f"{number}, is a prime number")
