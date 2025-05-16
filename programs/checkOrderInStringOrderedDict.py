from collections import OrderedDict


def check_order(string, reference):
    # create OrderedDicts for both string
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)

    # check if the OrderedDict for the string matches the OrderedDict in reference
    return string_dict == reference_dict


# input string
input_string = "hello world"
reference_string = "hi world"

# check if order of characters in input_string matches reference_string
if check_order(input_string, reference_string):
    print("The order of characters in the input string matches the reference string")
else:
    print("The order of characters in the input string does not matches the reference string")
