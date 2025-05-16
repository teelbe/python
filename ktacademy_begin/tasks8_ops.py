print(1)
print("AAA")
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"User(name = {self.name})"
user = User("Alojzy")
print(user)
print("User: "+ user.__str__())
print("User: " + str(user))
print(f"User: {user}")

l = [1, "A", True]
print(l)
print(repr("A"))
print(str("A"))
print("A".__repr__())
print("A".__str__())

class FullName:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return(f"{self.name} {self.surname}")
    def __repr__(self):
        return "FullName ("+\
            f"name={repr(self.name)}, "+\
            f"surname={repr(self.surname)})"
player = FullName("Alojzy", "Moskała")
print(player)
print(str(player))
print(repr(player))

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

    __repr__ = __str__
    #lub
    #def __repr__(self):
    #   return self.__str__()
position = Position(10, 20)
print(position)
print(repr(position))

class User:
    def __init__(self, name):
        self.name = name
user1 = User("Alek")
user2 = User("Alek")
user3 = User("Bolek")
print(user1 == user1)
print(user1 == user2)
print(user1 == user3)
print(user1 is user1)
print(user1 is user2)
print(user1 is user3)
print(user1 != user1)
print(user1 != user2)
print(user1 != user3)

class A:
    pass
class B:
    pass
a = A()
b = B()
print(isinstance(a, A))
print(isinstance(a, B))
print(isinstance(b, A))
print(isinstance(b, B))
print("NEXT")
class Users:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return (
                isinstance(other, Users)
                and other.name == self.name
        )
user1 = Users("Alek")
user2 = Users("Alek")
user3 = Users("Bolek")
print(user1 == user1)
print(user1 == user2)
print(user1 == user3)
print(user1 != user1)
print(user1 != user2)
print(user1 != user3)
print(user1 is user1)
print(user1 is user2)
print(user1 is user3)
print("NEXT")
class Positions:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (
                isinstance(other, Positions) and
                self.x == other.x and
                self.y == other.y
        )
    def __str__(self):
        return f"(({self.x}, {self.y})"
    __repr__ = __str__
position1 = Positions(10, 20)
position2 = Positions(10, 20)
position3 = Positions(1, 2)
print(position1 == position2)
print(position1 == position3)
print("NEXT NEXT NEXT")
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def __eq__(self, other):
        return(
            isinstance(other, Money) and
            self.amount == other.amount and
            self.currency == other.currency
        )
    def __str__(self):
        return f"{self.amount} {self.currency}"
    def __repr__(self):
        return "Money("+f"amount={repr(self.amount)}, "+f"currnecy={repr(self.currency)})"
money1 = Money(10.0, "PLN")
money2 = Money(10.0, "PLN")
money3 = Money(20.0, "PLN")
money4 = Money(10.0, "EUR")

print(money1 == money1)
print(money1 == money2)
print(money1 == money3)
print(money1 == money4)
print(money1)
print(money2)
print(money3)
print(money4)
print(repr(money1))
print(repr(money3))
print(repr(money4))

class FakeMoney:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

money = Money(10, "PLN")
fakeMoney = FakeMoney(10, "PLN")
print(money == fakeMoney)

class Position1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        return Position1(self.x + other.y, self.y + other.y)
    def __sub__(self, other):
        return Position1(self.x - other.y, self.y - other.y)
    def __mul__(self, other):
        return Position1(self.x * other, self.y * other)
p1 = Position1(1.0, 2.0)
p2 = Position1(3.0, 4.0)
p3 = p1 + p2
p4 = p1 * 3
print("NEXT NEXT NEXT")
print(p3)
print(p4)

class Position2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag
    def __le__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag <= other_mag
p3 = Position2(1.0, 2.0)
p4 = Position2(3.0, 4.0)
print("NEXT NEXT NEXT")
print( p3 > p4)
print( p3 < p4)
print( p3 < p3)
print( p3 >= p4)
print( p3 <= p4)
print( p3 <= p3)

class Echo:
    def __getattr__(self, item):
        return f"Echo: {item}"
echo = Echo()
print("NEXT NEXT NEXT")
print(echo.Aaa)
print(echo.Ooo)
print(echo.Hejaa)
