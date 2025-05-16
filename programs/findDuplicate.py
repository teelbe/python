def find_duplicates(input_str):
    # create an empty dictionary to store character counts
    char_count = {}

    # initialize a list to store duplicate characters
    duplicates = []

    # iterate through each character in the input string
    for i in input_str:
        # if the character is already in the dictionary, increment its
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    # iterate through the dictionary and add characters with count > 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates


# input string
input_string = "piyush sharma"

# find duplicate characters in the string
duplicate_chars = find_duplicates(input_string)

# print the list of duplicate characters
print("Duplicate characters:", duplicate_chars)
