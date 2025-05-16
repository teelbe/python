import re


def check_special_char(in_str):
    # define a regular expression pattern to match special characters
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'

    # use re.search to find a match in the input string
    if re.search(pattern, in_str):
        return True
    else:
        return False


# input a string
input_string = str(input("Enter a string: "))

# check if the string contains any special characters
contains_string = check_special_char(input_string)

# print result
if contains_string:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")
