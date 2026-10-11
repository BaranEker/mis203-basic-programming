import datetime
import random

messages = [
    "Did you know? A year on Mercury lasts only 88 Earth days.",
    "Did you know? A day on Venus is longer than its year.",
    "Did you know? Neptune takes about 165 Earth years to orbit the Sun.",
    "Did you know? Jupiter's year is about 12 Earth years.",
    "Did you know? A year on Mars lasts about 687 Earth days."]
today = datetime.datetime.now()
while True:
    age = int(input("How old are you (1-120, 0 to exit):"))
    if age == 0:
        print("Goodbye!")
        break
    elif age < 1 or age > 120:
        print("Invalid age! Enter a number between 1 and 120")
        continue
    days = age * 365
    birth_year = today.year - age
    print(f"You were born around {birth_year}")
    print("1 - Mercury")
    print("2 - Venus")
    print("3 - Earth")
    print("4 - Mars")
    print("5 - Jupiter")
    print("6 - Saturn")
    print("7 - Uranus")
    print("8 - Neptune")
    choice = int(input("Choose a planet number: "))
    if choice == 1:
        print(f"Mercury age: {round(days / 88)}")
    elif choice == 2:
        print(f"Venus age: {round(days / 225)}")
    elif choice == 3:
        print(f"Earth age: {round(days / 365)}")
    elif choice == 4:
        print(f"Mars age: {round(days / 687)}")
    elif choice == 5:
        print(f"Jupiter age: {round(days / 4333)}")
    elif choice == 6:
        print(f"Saturn age: {round(days / 10759)}")
    elif choice == 7:
        print(f"Uranus age: {round(days / 30687)}")
    elif choice == 8:
        print(f"Neptune age: {round(days / 60190)}")
    else:
        print("Invalid choice.")
        continue
    print(random.choice(messages))
    print()
