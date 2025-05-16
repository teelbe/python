my_list = []
print(my_list)
fruits = ["Apple", "Banana", "Plum"]
print(fruits)
my_list1 = [1, "A", True, [], {}]
print(my_list1)

fruits1 = ["Apple"]
print(fruits1)
fruits1.append("Banana")
print(fruits1)
fruits1.append("Plum")
print(fruits1)
ret = fruits1.pop()
print(fruits1)
print(ret)

values = [True, 42, "AAA"]
print(values.pop())
print(values.pop())
values.append(88)
print(values)

pets= ["dog", "cat"]
pets.pop()
pets.append("pig")
print(pets)
pet = pets.pop()
print(pets)
print(pet)

print(fruits)
print(fruits[1])
print(fruits[0])
print(fruits)
fruit = fruits[2]
print(fruit)

print(fruits[-1])
print(fruits[-2])
fruit2 = fruits[-3]
print(fruit2)

names = ["Ada", "Bartek", "Czarek", "Daria", "Ewa"]
print(names[0])
print(names[3])
print(names[-1])
print(names[-2])
print(names[1])
print(names[-4])

letters = ["A", "B", "C", "D"]
print(letters[1:-1])
print(letters[0:-2])
print(letters[0:-1])

print(letters[2:])
print(letters[1:])
print(letters[:2])
print(letters[:])

print(names[0:2])
print(names[2:4])
print(names[:3])
print(names[3:-1])
print(names[1:])
print(names[1:3])
print(names[-3:])
print(names[1:-2])
print(names[:])

names1 = ["Ada", "Bartek", "Czarek"]
print(names1)
names1[1] = "Marek"
print(names1)
names1[-1] = "Nina"
print(names1)

names2 = ["Ada", "Bartek", "Czarek", "Daria"]
print(names2)
names2[1:3] = ["Ola"]
print(names2)
names2[1:2] = ["Paulina", "Robert"]
print(names2)
names2[2:] = []
print(names2)
names2[:1] = []
print(names2)
names2[:] = []
print(names2)

names3 = ["Ada", "Bartek", "Czarek"]
print(names3)
names3[2] = "Figa"
print(names3)
names3[-2] = "Geralt"
print(names3)
names3[:1] = []
print(names3)
names3[2:] = ["Ewa", "Halina"]
print(names3)
names3[1:2] = ["Iza", "Jan"]
print(names3)
names3[:-1] = ["Kasia"]
print(names3)

empty = []
print(len(empty))
names4 = ["Apple", "Banana"]
print(len(names4))
values2 = [True, "Plum", None, [], 42]
print(len(values2))
print(len(values2[3]))

letters2 = ["A", "B", "C", "D", "E", "F"]
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(len(letters2))
print(letters2[4])
print(len(numbers2))
print(numbers2[3])

sizes = ["M", "L", "XL", "XXL"]
print("L" in sizes)
print("S" in sizes)
print("XXL" in sizes)

numbers3 = [ 3.14, 2.71, 42]
print(1 in numbers3)
print(2.71 in numbers3)
print(45 in numbers3)

letters3 = ["A", "B", "C"]
print("A" in letters3)
print("B" in letters3)
print("C" in letters3)
letters3[1] = "F"
print("F" in letters3)
print("C" in letters3)

list1 = [1, True]
list2 = ["A", []]
list3 = list1 + list2
print(list1)
print(list2)
print(list3)
list1[1] = False
print(list1)
print(list3)

list4 = ["A", "B"]
list4Ref = list4
list4Copy = list4[:]
list4.append("C")
print(list4)
print(list4Ref)
print(list4Copy)

l1 = ["A", "B"]
l2 = ["D", "E"]
letters4 = l1 + l2
l1Copy = l1[:]
print(letters4)
l1.append("C")
print(l1)
print(letters4)
print(l1Copy)

size = ("S", "M", "L", "XL")
print(len(size))
print(size[0])
print(size[1:3])
print("XXL" in size)
print("S" in size)

empty2 = ()
empty3 = tuple()
print(empty2)
print(empty3)

s = ("XXL")
print(type(s))
new_size = ("XXL",)
print(type(new_size))

size = size + new_size
print(size)

values3 = (True, 42, "AAA")
print(values3[1])
print(values3[2])
print(values3[:1])
empty4 = ()
print(len(empty4))
single = ('AAA',)
print(single)
print(type(single))
print(len(single))