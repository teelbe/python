class Cookie:
    pass
cookie1 = Cookie()
cookie2 = Cookie()
cookie1.type = "Dog"
cookie1.breed = "Boxer"
cookie2.type = "Food"
cookie2.breed = "Pasta"
print(cookie1.type)
print(cookie1.breed)
print(cookie2.type)
print(cookie2.breed)
class Player:
    pass
player = Player()

player.points = 0
print(player.points)
player.points = 1
print(player.points)

class User():
    def cheer(self):
        print(f"Cześć, jestem {self.name}")
    def say_hello(self, other):
        print(f"Czesc {other}, jestem {self.name}")

user = User()
user.name = "Maciek"
user.cheer()
user.say_hello("Marta")

class Position:
    def step_right(self):
        self.x +=1.0
    def move_up(self, value):
        self.y += value

pos = Position()
pos.x = 0.0
pos.y = 0.0
pos.step_right()
print(pos.x)
pos.move_up(6.0)
print(pos.y)
pos.move_up(3.0)
print(pos.y)

class Game:
    def __init__(self):
        print("Starting...")
        self.started = True
game = Game()
print(game.started)

class Users:
    def __init__(self, name):
        self.name = name
user1 = Users("Maciek")
user2 = Users("Marta")
print(user1.name)
print(user2.name)

class Players:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"
        self.points = 0
player1 = Players("Michał", "Mazur")
print(player1.name)
print(player1.surname)
print(player1.full_name)
print(player1.points)

class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance
    def deposite(self, amount):
        self.balance += amount
    def with_draw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

account1 = BankAccount()
account2 = BankAccount()
account1.deposite(1000)
print(account1.balance)
print(account2.balance)
account1.deposite(1000)
print(account1.balance)
account1.deposite(2000)
print(account1.balance)
res = account1.with_draw(1500)
print(res)
print(account1.balance)
res = account1.with_draw(2000)
print(res)
print(account1.balance)