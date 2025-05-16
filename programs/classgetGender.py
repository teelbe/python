class Person:
    def getGender(self):
        return "Unknown"


class Male:
    def getGender(self):
        return "Male"


class Female:
    def getGender(self):
        return "Female"


person = Person()
male = Male()
female = Female()

print(person.getGender())
print(male.getGender())
print(female.getGender())
