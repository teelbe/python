print("Wstan z lozka")
print("umyj zeby")
print("podsmaz mieso")
print("podsmaz bulke")
print("dodaj pomidora")
print("zjedz burgera")
print("pracuj")
print("podsmaz mieso")
print("podsmaz bulke")
print("dodaj pomidora")
print("zjedz burgera")
print("pracuj")
print("podsmaz mieso")
print("podsmaz bulke")
print("dodaj pomidora")
print("zjedz burgera")
print("graj w gry")
print("idz spac")

def make_and_eat_burger():
    print("podsmaz mieso")
    print("podsmaz bulke")
    print("dodaj pomidora")
    print("zjedz burgera")

print("Wstan z lozka")
print("umyj zeby")
make_and_eat_burger()
print("pracuj")
make_and_eat_burger()
print("pracuj")
make_and_eat_burger()
print("graj w gry")
print("idz spac")

def print_a():
    print("a")
def print_a_and_b():
    print_a()
    print("b")

print_a()
print_a_and_b()
print_a()

def first_function():
    print("3")
    print("4")
def second_function():
    print("6")
    print("7")
print("1")
print("2")
first_function()
print("5")
second_function()
print("8")

def cheer(who_to_cheer):
    print(f"Siema {who_to_cheer}!")

cheer("Czytelniku")
cheer("Wszystkim")
cheer(42)

def sum(a, b):
    print(a + b)
sum(1,2)

def numbers(a, b):
    while a < b:
        print(a)
        a += 1
numbers(2,7)
def print_numbers(a, b):
    for i in range (a, b +1):
        print(i)
print_numbers(2,7)

def print_stars(num):
    stars = ""
    for i in range(num):
        stars +="*"
    print(stars)

print_stars(3)
print_stars(4)
print_stars(5)

def print_square(size):
    for i in range(size):
        print_stars(size)
print_square(2)
print_square(4)

def print_triangle(size):
   for i in range(size):
       print_stars(i + 1)
print_triangle(3)
print_triangle(4)
print_triangle(5)

def return_number():
    return 42
result = return_number()
print(result)
def return_num(num):
    return num
res = return_num(10)
print(res)
def double(num):
    return num * 2
print(double(13))
def square(x):
    return x * x
print(square(2))
print(square(4))
print(square(10))

def absolute(x):
    if x >= 0:
        return x
    return -x
print(absolute(0))
print(absolute(-2))
print(absolute(5))
print(absolute(-90))
print(absolute(100))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return(result)

def factor(num):
    if num <=1:
        return 1
    return num * factor(num -1)
print(factorial(0))
print(factor(0))
print(factorial(1))
print(factor(1))
print(factorial(2))
print(factor(2))
print(factorial(3))
print(factor(3))
print(factorial(4))
print(factor(4))
print(factorial(5))
print(factor(5))

def days_to_millis(days):
    if days <= 0:
        return("bad format")
    return days * 24 * 60 * 60 * 1000
print(days_to_millis(1))
print(days_to_millis(3))
print(days_to_millis(0))

def triangle_area(a, b):
    if a ==0:
        return("change size")
    elif b == 0:
        return ("change size")
    return ((a * b) /2)
print(triangle_area(0,1))
print(triangle_area(2,0))
print(triangle_area(1,1))
print(triangle_area(10,20))

def biggest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c
print(biggest(2, 3, 1))
print(biggest(2, 3, 5))
print(biggest(3, 3, 1))
def sum_range(a, b):
    if b<=a:
        return 0
    return sum_range(a+1, b)+a

print(sum_range(1,4))
print(sum_range(2,5))
print(sum_range(10,12))



