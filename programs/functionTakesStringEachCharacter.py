# double char

def double_char(input_str):
    doubled_str = ""

    for char in input_str:
        doubled_str += char * 2

    return doubled_str

print(double_char("String"))
print("-------------------")
print(double_char("Hello World"))
print("-------------------")
print(double_char("1234!_"))