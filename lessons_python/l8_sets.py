from pprint import pprint

x\
    = {}
print(x)
print(type(x))
print('========')
y = set()
print(y)
print(type(y))
print('========')
set1 = {'Hello Python!', 3.14, 1.618, 'Hello World!', 3.14, 1.618, True, False, 2022}
print(set1)
print('========')
# convertingg list to set
nlis = ['Hello Python', 3.14, 1.618, 'Hello World', 3.14, 1.618, True, False, 2022]
set2 = set(nlis)
print(set2)
print('========')
# set operations
set3 = set(['Hello Python', 3.14, 1.618, 'Hello World', 3.14, 1.618, True, False, 2022])
print(set3)
print('========')
# add() function
set3.add('Hi Python')
pprint(set3)
print('========')
# update() function
x_set = {6, 7, 8, 9}
print(x_set)
x_set.update({3, 4, 5})
print(x_set)
print('========')
# remove() function
set3.remove('Hello Python')
print(set3)
print('========')
# discard() function
set3.discard(3.14)
print(set3)
print('========')
print(1.618 in set3)
print('========')
# logic operations in set
set4 = set(['Hello Python', 3.14, 1.618, 'Hello World'])
set5 = set([3.14, 1.618, True, False, 2022])
print(set4, set5)
print('========')
# intersection two sets
intersection = set4 & set5
print(intersection)
print(set4.intersection(set5))
print('========')
# difference function
print(set4.difference(set5))
print(set4 - set5)
print(set5.difference(set4))
print(set5 - set4)
print('========')
# set comparsion
print(set4 > set5)
print(set5 > set4)
print(set4 == set5)
print('========')
