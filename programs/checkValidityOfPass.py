import re


# function to check if a password is valid
def is_valid_password(password):
    # check the length of the password
    if 6 <= len(password) <= 12:
        # check if the password matches alle the criteria using
        if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
    return False


# accept input from the user as comma-separated passwords:
passwords = input("Enter passwords separated by commas: ").split(',')

# initialize a list to store valid passwords
valid_password = []

# iterate through the passwords and check their validity
for psw in passwords:
    if is_valid_password(psw):
        valid_password.append(psw)

# print the valid passwords separated by commas
print(','.join(valid_password))
