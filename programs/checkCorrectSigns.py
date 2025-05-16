def correct_sings(expression):
    try:
        return eval(expression)
    except:
        return False


# usage:
print(correct_sings("3 < 7 < 11"))
print(correct_sings("13 > 44 > 33 < 1"))
print(correct_sings("1 < 2 < 6 < 9 > 3"))
