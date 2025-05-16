# factorial of a number using recursion

def recur_factiorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factiorial(n - 1)


num = int(input("Enter the number: "))

# check if the number is negative
if num < 0:
    print("Sorry, factorial doesn't exist for negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of: ", num, "is", recur_factiorial((num)))
