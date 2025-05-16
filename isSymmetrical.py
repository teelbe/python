def is_symetrical(num):
    # convert the number to a string
    num_str = str(num)

    # check if the string is equal to its reverse
    return num_str == num_str[::-1]


print(is_symetrical(7227))
print("----    ----    ----    ----")
print(is_symetrical(12567))
print("----    ----    ----    ----")
print(is_symetrical(44444444))
print("----    ----    ----    ----")
print(is_symetrical(4444444))
print("----    ----    ----    ----")
print(is_symetrical(1112111))
