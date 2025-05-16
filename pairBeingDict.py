def mapping(letters):
    result = {}
    for letter in letters:
        result[letter] = letter.upper()
    return result


print(mapping(["p", "s"]))
print("----    ----    ----    ----")
print(mapping(["a", "b", "c"]))
print("----    ----    ----    ----")
print(mapping(["a", "v", "y", "z"]))
print("----    ----    ----    ----")
print(mapping(["l", "u", "k", "a", "s", "z"]))
