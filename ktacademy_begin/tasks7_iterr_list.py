names = ["Ala", "Basia", "Celina"]
for name in names:
    print(name)
numbers = [x + 1 for x in range(5)]
print(numbers)
numbers2 = [x * 10 for x in range(5)]
print(numbers2)
names_upper = [name.upper() for name in names]
"""new_list = [transformation(x) for x in old_list]
new_list2 = []
for x in old_list:
    new_list.append(transformation(x))"""

#lista składa z warunkiem
names2 = ["Jola", "Marcin", "Kamil", "Maja", "Stefan"]
m_names = [name for name in names2 if name[0] == "M"]
print(m_names)
m_names2 = [name.upper() for name in names2
            if name[0] == "M"]
print(m_names2)
names3 = tuple(name for name in names2 if name[0] == "M")
print(names3)
print(type(names))
print(type(names3))

names4 = [ "michał", "nela", "ola", "przemek"]
m_names3 = [name.capitalize() for name in names4]
print(m_names3)
names5 = tuple(name.capitalize() for name in names4
            if name[-1] == "a")
print(names5)
countNames = len(names4)
print(countNames)
countLetters = 0
for name in names4:
    countLetters += len(name)
print(countLetters)

