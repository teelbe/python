# find HCF of two numberw
# define function
def compute_hcf(x, y):
    # choose smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

number1 = int(input("Enter the number: "))
number2 = int(input("Enter the number: "))
print("HCF is: ", compute_hcf(number1, number2))
