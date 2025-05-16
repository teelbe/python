# Input two digits: X, Y
X, Y = map(int, input("Enter tw digits (X, Y):").split(','))

# initialize a 2D array filled with zeros
array = [[0 for j in range(Y)] for i in range(X)]

# fill the array with values i*j
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j

# print 2D array
for row in array:
    print(row)
