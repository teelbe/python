from pprint import pprint

# creating a list
nlis = ['python', 25, 2022]
print(nlis)
print('Positive and negative indexing of the first element: \n-Positive index: ', nlis[0], '\n-Negative index: ',
      nlis[-3])
print('========')
print('Positive and negative indexing of the second element: \n-Positive index: ', nlis[1], '\n-Negative index: ',
      nlis[-2])
print('========')
print('Positive and negative indexing of the third element: \n-Positive index: ', nlis[2], '\n-Negative index: ',
      nlis[-1])
print('========')
print('========')
nlis2 = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3, 14, 2022)]
pprint(nlis2)
print('========')
print(len(nlis))
print(len(nlis2))
print('========')
# slicing
print(nlis2[0:2])
print(nlis2[2:4])
print(nlis2[4:6])
print('========')
# extend
nlis2.extend(['hello world!', 1.168])
pprint(nlis2)
print('========')
# append
nlis2.append(['hi people', 2.729])
pprint(nlis2)
print('========')
# lists operations
lis = [1, 2, 3, 4, 5, 6, 7]
print(len(lis))
lis.append(4)
print(lis)
print(lis.count(4))
print(lis.index(2))
lis.insert(8, 9)
pprint(lis)
print(max(lis))
print(min(lis))
print(sum(lis))
print('========')
# change element in the list
print('Before changing: ', nlis2)
nlis2[0] = 'hello python'
print('After changing: ', nlis2)
nlis2[1] = 1.168
print('After changing: ', nlis2)
nlis2[2] = [3.14, 2022]
print('After changing: ', nlis2)
print('========')
# deleting element
print('Before changing: ', nlis2)
del (nlis2[0])
print('After changing: ', nlis2)
del (nlis2[-1])
print('After changing: ', nlis2)
print('========')
print('Before deleting: ', nlis)
# del nlis
print('After deleting: ', nlis)
# conversion of a string
message = 'Python is a programming language'
print(message.split())
text = 'p,y,t,h,o,n'
print(text.split(','))
print('========')
print('========')
# basic operations
nlis_1 = ['a', 'b', 'hello', 'python']
nlis_2 = [1, 2, 3, 4, 5, 6]
print(len(nlis_1))
print(len(nlis_2))
print(nlis_1 + nlis_2)
print(nlis_1 * 3)
print(nlis_2 * 3)
for i in nlis_1:
    print(i)
for i in nlis_2:
    print(i)
print(4 in nlis_1)
print(4 in nlis_2)
print('========')
# copy the list
copy_list = nlis2
print('nlis2: ', nlis2)
print('copy_list: ', copy_list)
print('========')
print('copy_list[0]: ', copy_list[0])
nlis2[0] = 'hello python!'
print('copy_list[0]: ', copy_list[0])
print('========')
# clone the list
clone_lis = nlis2[:]
pprint(clone_lis)
print('========')
print(nlis2)
print(clone_lis)
print('clone_lis[0]: ', clone_lis[0])
nlis2[0] = 'hi python'
print('nlis2[0]: ', nlis2[0])
print('========')
# concatenate the list
a_list = ['a', 'b', ['c', 'd'], 'e']
b_list = [1, 2, 3, 4, 5, (6, 7), True, False]
new_list = a_list + b_list
print(new_list)
print('========')
# input
text = input('Enter a string:')
print('The text is ', text)
print(type(text))
print('========')
number = input('Enter an integer:')
print('The number is: ', number)
print(type(number))
print('========')
number2 = int(input('Enter an integer:'))
print('The number is:', number2)
print(type(number2))
print('========')
number3 = float(input('Enter an integer:'))
print('The number is: ', number3)
print(type(number3))
print('========')
# eval() functions
expression = '8+7'
total = eval(expression)
print('Sum of the expresion is: ', total)
print(type(expression))
print(type(total))
print('========')
a = float(input('Enter the pi number:'))
b = float(input('Enter the golden ratio:'))
total2 = a + b
print('Sum of {} and {} is {}.'.format(a, b, total2))
print('========')
c = input('Enter your favorite fruit:')
d = input('Ente your favorite food:')
print('I like {} nad {}'.format(c, d))
print('I like {0} and {1}'.format(c, d))
print('I like {1} and {0}'.format(c, d))
print('========')
# comparision operotors
e = 3.14
f = 1.168
print('e>f is:', e > f)
print('e<f is:', e < f)
print('e<=f is:', e <= f)
print('e>=f is:', e >= f)
print('e==f is:', e == f)
print('e!=f is:', e != f)
print('========')
# logical operators
m = 3.14
n = 1.169
o = 12
p = 3.14
print(m > n and o > m)
print(n > o and p > m)
print(n < o or p > m)
print(not m == n)
print(not m == p)
print('========')
# assignment operators
x = 3.14
x += 5
print(x)
print('========')
xx = 3.14
xx -= 5
print(xx)
print('========')
y = 3.14
y *= 5
print(y)
print('========')
yy = 3.14
yy /= 5
print(yy)
print('========')
z = 3.14
z %= 5
print(z)
print('========')
zz = 3.14
zz //= 5
print(zz)
print('========')
ac = 3.14
ac **= 5
print(ac)
print('========')
# identity operators
aa = 3.14
bb = 1.168
print(aa is bb)
print(aa is not b)
msg1 = "Hello, Python!"
msg2 = 'Hello, World!'
print(msg1 is msg2)
print(msg1 is not msg2)
lis1 = [3.14, 1.168]
lis2 = [3.14, 1.168]
print(lis1 is lis2)
print(lis1 is not lis2)
print('========')
# membership operators
nlist = [4, 6.7, 8, 'hello', (4, 5), {'name': 'Python'}, {1, 2, 3}, [1, 2, 3]]
print(5 in nlist)
print(4 not in nlist)
print((4, 5) in nlist)
print(9 not in nlist)
print('========')
