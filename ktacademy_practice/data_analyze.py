import csv

file = open("titanic.csv")
data=[row for row in csv.reader(file)]
file.close()
header = data[0]
data = data[1:]

rows_num = len(data)
print(rows_num)

print(header)
print(data[0])
print(data[1])
print(data[2])

class_1 = [row for row in data if row[1] == '1st']
class_2 = [row for row in data if row[1] == '2nd']
class_3 = [row for row in data if row[1] == '3rd']
print(class_1)
print(class_2)
print(class_3)
print(len(class_1))
print(len(class_2))
print(len(class_3))

class_1_survived = [row for row in class_1 if row[4] == '1']
print(len(class_1_survived) / len(class_1))

def print_survival_rate(data):
    count = 0
    survived = 0
    for row in data:
        count += 1
        if row[4] == '1':
            survived += 1
    print(float(survived / count))

print_survival_rate(class_1)
print_survival_rate(class_2)
print_survival_rate(class_3)

males = [row for row in data if row[3] == 'male']
print(len(males))
print_survival_rate(males)

females = [row for row in data if row[3] == 'female']
print(len(females))
print_survival_rate(females)

kids = [row for row in data if row[2] != '' and float(row[2]) <= 15]
print(len(kids))
print_survival_rate(kids)
adults = [row for row in data if row[2] != '' and float(row[2]) > 15]
print(len(adults))
print_survival_rate(adults)
