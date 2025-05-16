def multiply_nums(nums_str):
    # split the input string by comma and space, then convert to integer
    nums = [int(num) for num in nums_str.split(", ")]

    # initialize the result with 1
    result = 1

    # multiply all the numbers together
    for num in nums:
        result *= num

    return result


print(multiply_nums("2, 3"))
print("----    ----    ----    ----")
print(multiply_nums("1, 2, 3, 4"))
print("----    ----    ----    ----")
print(multiply_nums("54, 75, 243, 0"))
print("----    ----    ----    ----")
print(multiply_nums("20, -3"))
