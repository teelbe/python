import math

# fixed value
C = 50
H = 30


# Function to calculate Q
def calculate_Q(D):
    return int(math.sqrt((2 * C * D) / H))


# Input comma-separated sequence of D value
input_sequence = input("Enter comma-separated value of D: ")
D_value = input_sequence.split(',')

# calculate and print Q of each D value
result = [calculate_Q(int(D)) for D in D_value]
print(','.join(map(str, result)))
