import math


# programm 134 not work

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        # calculate and return the area of the circle
        return f"the area of Circle with radius = {self.radius} is {round(math.pi * self.radius ** 2)}"

    def getPerimeter(self):
        # calculate and return the perimeter (circumfefernce) of circiut
        return f"the perimeter of Circle with radius = {self.radius} is {round(2 * math.pi * self.radius)}"


# test case
circy = Circle(11)
print(circy.getArea())
print(circy.getPerimeter())
print("----    ----    ----    ----")
print("    ----    ----    ----    ")
circy2 = Circle(4.44)
print(circy2.getArea())
print(circy2.getPerimeter())
