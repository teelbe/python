def index_of_caps(word):
    # use list comprehension to find indices of capital letters
    return [i for i, char in enumerate(word) if char.isupper()]
print(index_of_caps("eDaBiT"))
print("-------------------")
print(index_of_caps("eQuINoX"))
print("-------------------")
print(index_of_caps("determine"))
print("-------------------")
print(index_of_caps("STRIKE"))
print("-------------------")
print(index_of_caps("sUp"))