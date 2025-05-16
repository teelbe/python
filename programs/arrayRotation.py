def rotate_array(arr, d):
    n = len(arr)

    # check if 'd' is valid
    if d < 0 or d >= n:
        return "Invalid rotation value"
    # create new array
    rotated_arr = [0] * n
    # perform rotation
    for i in range(n):
        rotated_arr[i] = arr[(i + d) % n]
    return rotated_arr


# input array
arr = [1, 2, 3, 4, 5]
# number of position to rotate
d = 2
# call rotate function
result = rotate_array(arr, d)
# print array and rotated array
print("Original array: ", arr)
print("Rotated array: ", result)
