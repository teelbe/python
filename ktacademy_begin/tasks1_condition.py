if True:
    print("To się wypisze")
if False:
    print("A to już nie")
tweet_type = "promotional"
tweet_owner = "marcinmoskala"
your_key = "lukasztulibacki"

if tweet_type == "promotional":
    print("Promowany")

if tweet_owner == your_key:
    print("Your tweet")
else:
    print("wrong tweet owner")
weekday = "Saturday"
if weekday == 'friday':
    print("party time")
else:
    print("lazy day")
is_logged = True
is_admin = False

if is_logged:
    print("User logged")
    if is_admin:
        print("Admin welcome")
is_important = True
if is_important:
    print("Szanowanie")
if True:
    print("Welcome")
gender = "male"
if gender == 'male':
    print("Pani")
else:
    print("Pana")

if tweet_type == "promotional":
    print("Promowany")
elif tweet_type == "followed":
    print("zwykły")
elif tweet_type == "own":
        print("własny")
else:
    print("inny")

coffee_finished = True
days_until_deadline = 4

if not coffee_finished:
    print("drink coffee")
elif days_until_deadline < 2:
    print("Working")
else:
    print("is learning programming")

user_name = "Michal"
user_age = 31
user_name = "Prezes Marek"
user_age = 61
user_name = "Paweł"
user_age = 10
user_name = ""
user_age = 14

if user_name == "Prezes Marek":
    print("Witamy Pana Prezesa")
if user_name != "":
    print("Cześć " + user_name)
if user_age < 18:
    print("Mozesz czekolade")
if user_age >= 18:
    print("Moze coś do picia?")


if user_name == "Prezes Marek":
    print("Witamy Pana Prezesa")
else:
    print("Cześć " + user_name)
if user_age <18:
    print("Mozesz czekolade")
else:
    print("Moze coś do picia?")


if user_name == "Prezes Marek":
    print("Witamy Pana Prezesa")
elif user_name != "":
    print("Cześć " + user_name)

if user_age <= 10:
    print("kategoria: dzieci")
elif user_age <= 20:
    print("kategoria: młodzież")
elif user_age <= 60:
    print("kategoria: dorośli")
else:
    print("kategoria: starsi")

has_computer = True
passed_test = False
is_grounded = False

print(has_computer and passed_test)
print(passed_test or is_grounded)
print(has_computer and not passed_test)

can_play_games = has_computer and not is_grounded
print(can_play_games)
play_games = has_computer and can_play_games
if not passed_test:
    is_grounded = True

print(play_games)
print(passed_test or not is_grounded)
print(not(not has_computer or not passed_test))