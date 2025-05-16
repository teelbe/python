def is_binary_str(input_str):
    # iterate through each character in the input string
    for i in input_str:
        # check if the i is not '0' or '1'
        if i not in '01':
            return False  # if any character is not '0' or '1'
    return True  # if all characters are '0' or '1'


# input string
input_str = "1001110"

# check if the input string is a binary string
if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string")
else:
    print(f"'{input_str}' is not a binary string")
