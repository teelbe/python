def hamming_distance(str1, str2):
    # check if the strings have the same length
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    # initialize a counter to keep track of differences
    distance = 0

    # iterate through the characters of both strings
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1  # increment the counter for differences

    return distance


# print result
print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
