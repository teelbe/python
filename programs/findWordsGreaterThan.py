def find_words(words, k):
    # create an empty list to store words greater than k
    result = []

    # iterate through each word in the list
    for i in words:
        # check if the length of the i is greater than k
        if len(i) > k:
            # if yes, append it to the result list
            result.append(i)

    return result


# example list
word_list = ["apple", "banana", "cherry", "data", "date", "elderberry", "dragon fruit"]
k = int(input("Enter a value of letters:"))
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")
