input_sentence = input("Enter a sentence: ")

# split the sentence into words
words = input_sentence.split()

# create a dictionary to store word frequency
word_freq = {}

# count word frequencies
for word in words:
    # remove punctuation (.,?) from the word
    word = word.strip('.,?')
    # convert the word to Lowercase to ensue case-insensitive counting
    word = word.lower()
    # update the world frequency in the dictionary
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# sort the words alphanumerically
sorted_words = sorted(word_freq.items())

# print the world frequencies
for word, frequency in sorted_words:
    print(f"{word}: {frequency}")
