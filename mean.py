# return mean of all digits
def mean(n):
    # convert the number to a string to interante through its digits
    n_str = str(n)

    # calculate the sum of digits
    digit_sum = sum(int(digit) for digit in n_str)

    # calculate the mean by dividing the sum by the number of digits
    digit_count = len(n_str)
    digit_mean = digit_sum / digit_count

    return int(digit_mean)


print(mean(42))
print("----    ----    ----    ----")
print(mean(12345))
print("----    ----    ----    ----")
print(mean(666))
