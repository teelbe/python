import salaries
for person in salaries.workers:
    print(person)
print(salaries.Person("Ala Mała", 5678.00))

def brutto_to_netto(brutto):
    return brutto * 0.75
if __name__ == '__main__':
    for worker in salaries.workers:
        salary_netto = brutto_to_netto(worker.salary)
        print(f"{salary_netto} for {worker.full_name}")
print("NEXT NEXT NEXT")
print("NEXT NEXT NEXT")
print("NEXT NEXT NEXT")
import salaries as hr
for person in hr.workers:
    print(person)
print(hr.Person("Ala Mała", 5678.00))

def brutto_to_netto(brutto):
    return brutto * 0.75
if __name__ == '__main__':
    for worker in hr.workers:
        salary_netto = brutto_to_netto(worker.salary)
        print(f"{salary_netto} for {worker.full_name}")

print("NEXT NEXT NEXT")
print("NEXT NEXT NEXT")
print("NEXT NEXT NEXT")

from salaries import Person
print(Person("Ala Mała", 5678.00))

from salaries import workers
for person in workers:
    print(person)
def calculate_salary(brutto):
    return brutto * 0.75
if __name__ == '__main__':
    for worker in hr.workers:
        salary_netto = calculate_salary(worker.salary)
        print(f"{salary_netto} for {worker.full_name}")