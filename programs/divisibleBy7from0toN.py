class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_divisible_by_seven(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num


n = int(input("Enter Your desire range: "))

divisible_by_seven_generator = DivisibleBySeven(n).generate_divisible_by_seven()

for num in divisible_by_seven_generator:
    print(num)
