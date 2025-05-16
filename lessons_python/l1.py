import sys

# printig text
print("Hello World!")
print('Hi, Python!')
# printing system information
print(sys.version)  # version control
print(sys.winver)  # only for Windows, version number of the Python DLL
print(sys.gettrace)  # get the global debug tracung function
print(sys.argv)  # keeps the parameters used while running the program we wrote the list

help(sys)
