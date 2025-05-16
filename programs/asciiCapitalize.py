def ascii_capitalize(input_str):
    result = ""

    for char in input_str:
        if ord(char) % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result

print(ascii_capitalize("To be or not to be"))
print("----    ----    ----    ----")
print(ascii_capitalize("THE LITTLE MERMIAD"))
print("----    ----    ----    ----")
print(ascii_capitalize("Oh what a beautiful morning."))