from pprint import pprint

# take  a tuple
tuple_1 = ('hello', 'python', 3.14, 1.168, True, False, 32, [1, 2, 3], {1, 2, 3}, {'A': 3, 'B': 8}, (0, 1))
pprint(tuple_1)
print('========')
print(type(tuple_1))
print(len(tuple_1))
print('========')
# indexing
print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[2])
print(tuple_1[-1])
print(tuple_1[-2])
print(tuple_1[-3])
print('========')
# type of each value
print(type(tuple_1[0]))
print(type(tuple_1[2]))
print(type(tuple_1[4]))
print(type(tuple_1[6]))
print(type(tuple_1[7]))
print(type(tuple_1[8]))
print(type(tuple_1[9]))
print(type(tuple_1[10]))
print('========')
# concatenation of tuples
tuple_2 = tuple_1 + ('Hello World', 2022)
pprint(tuple_2)
print('========')
# repetition of a tuple
rep_tup = (1, 2, 3, 4)
print(rep_tup * 2)
print('========')
# membership
print(2 in rep_tup)
print(2 not in rep_tup)
print(5 in rep_tup)
print(5 not in rep_tup)
print('========')
# iteration
for i in rep_tup:
    print(i)
print('========')


# cmp() function
def cmp(t1, t2):
    return bool(t1 > t2) - bool(t1 < t2)


def cmp(t3, t4):
    return bool(t3 > t4) - bool(t3 - t4)


def cmp(t5, t6):
    return bool(t5 > t6) - bool(t5 < t6)


t1 = (1, 2, 3)
t2 = (2, 4, 6)
t3 = (5,)
t4 = (4,)
t5 = (3.14,)
t6 = (3.14,)
print(cmp(t1, t2))
print(cmp(t3, t4))
print(cmp(t5, t6))
print('========')
# min() function
print(min(rep_tup))
print('========')
# max() function
print(max(rep_tup))
print('========')
# tup(seq) function
seq = 'ATGCGTATTGCCAT'
print(tuple(seq))
print('========')
# slicing
print(tuple_1[2:7])
print('========')
print(tuple_1[-4:-1])
print('========')
# len() function
print(len(tuple_1))
print('========')
# sorting tuple
tuple_3 = (0, 9, 7, 4, 6, 2, 9, 8, 3, 1)
sorted_tuple_3 = sorted(tuple_3)
print(sorted_tuple_3)
print('========')
# nested tuple
nested_tuple = ('biotechnology', (0, 5), ('fermentation', 'ethanol'), (3.14, 'pi', (1.168, 'golden ratio')))
pprint(nested_tuple)
print('========')
print('Item 0 of nested tuple is: ', nested_tuple[0])
print('Item 1 of nested tuple is: ', nested_tuple[1])
print('Item 2 of nested tuple is: ', nested_tuple[2])
print('Item 3 of nested tuple is: ', nested_tuple[3])
print('========')
#using second index
print('Item 1, 0 of the nested tuple is: ', nested_tuple[1][0])
print('Item 1, 1 of the nested tuple is: ', nested_tuple[1][1])
print('Item 2, 0 of the nested tuple is: ',nested_tuple[2][0])
print('Item 2, 1 of the nested tuple is: ',nested_tuple[2][1])
print('Item 3, 0 of the nested tuple is: ', nested_tuple[3][0])
print('Item 3, 1 of the nested tuple is: ', nested_tuple[3][1])
print('Item 3, 2 of the nested tuple is: ',nested_tuple[3][2])
print('========')
#using third index
print('Item 3, 2, 0 of the nested tuple is: ', nested_tuple[3][2][0])
print('Item 3, 2, 1 of the nested tuple is: ', nested_tuple[3][2][1])
print('========')
#tuples are immutable
tuple_4=(1,3,5,7,8)
#tuple_4[0]=9
print(tuple_4)
print('========')
#delete a tuple
# element can not be deleted, only whole tuple
print('Before deleting: ',tuple_4)
del tuple_4
#print('After deleting: ',tuple_4)
print('========')
#count() method
tuple_5=(1,1,3,3,5,5,5,5,6,6,7,8,9)
print(tuple_5.count(5))
print('========')
#index method
print(tuple_5.index(5))
print(tuple_5.index(1))
print(tuple_5.index(9))
print('========')
#one element tuple
tuple_6=(0)
print(tuple_6)
print(type(tuple_6))
print('========')
tuple_7=(0,)
print(tuple_7)
print(type(tuple_7))
print('========')
