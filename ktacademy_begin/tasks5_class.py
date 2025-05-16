class User:
    def __init__(self, name):
        self.name = name
user1 = User("Rafał")
user2 = User("Rafał")
print(user1.name)
print(user2.name)
user1.name = "Bartek"
print(user1.name)
print(user2.name)

user3 = User("Piotr")
user4 = user3
print(user3.name)
print(user4.name)
user3.name = "Karol"
print(user3.name)
print(user4.name)

user5 = User("Nikodem")
user6 = user5
print(user5.name)
print(user6.name)
user5 = User("Tomek")
print(user5.name)
print(user6.name)

class Score:
    points = 0
print(Score.points)
Score.points = 1
print(Score.points)

score1 = Score()
print(score1.points)
score1.points = 10
print(score1.points)
score2 = Score()
score3 = Score()
print(score1.points)
print(score2.points)
print(score3.points)
Score.points = 2
print(score1.points)
print(score2.points)
print(score3.points)

class Direction:
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

direction = Direction.UP
if direction == Direction.UP:
    direction = Direction.DOWN

class Counter:
    num = 0

    def __init__(self):
        print("Create")
        Counter.num +=1
    @staticmethod
    def print_counter():
        print(f"Created {Counter.num}")
c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.print_counter()

class Cookie:
    pass
c = Cookie()
print(type(c))
print(type(c) is Cookie)
print(type(c) is not Cookie)
print(type(c) is int)
print(type(c).__name__)

str1 = "AAA"
print(type(str1))
i = 10
print(type(i))
str2 = str(i)
print(type(str2))
b = True
print(type(b))
str3 = str(b)
print(type(str3))

name = "dOmInIkA sito"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
text = "Hi {name}, I'm wtiring to you"
print(text)
new_text = text.replace("{name}", "Michał")
print(new_text)
new_text = new_text.replace("you", "You")
print(new_text)