# accept input from the user
sentence = input("Enter a sentence: ")

# initialize counters for letters and digits
letter_count = 0
digit_count = 0

# iterate through each character in the sentence
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

# print result
print("LETTERS", letter_count)
print("DIGITS", digit_count)
