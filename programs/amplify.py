# takes integer and returns a list from 1 to given number
def amplify(num):
    # use a list comprehension to generate the list
    return [n * 10 if n % 4 == 0 else n for n in range(1, num + 1)]


print(amplify(4))
print("----    ----    ----    ----")
print(amplify(3))
print("----    ----    ----    ----")
print(amplify(25))
