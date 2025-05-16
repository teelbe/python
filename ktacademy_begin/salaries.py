class Person:
    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary
    def __str__(self):
        return self.full_name

workers = [
    Person("Aleksander Brown", 3456.78),
    Person("Celona Drozd", 4567.89),
    Person("Jan Janowski", 5678.90),
    Person("Karol Nowicki", 6789.01),
    #...
]