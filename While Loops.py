number = 0
while number < 10:
    print(number)
    number += 1

number = 0
while number != 17:
    number = int(input("Type the number 17."))
print("You typed 17.")

name = ""
while len(name) < 3:  # You need 3 characters
    name = input("Write your full name: ")
print("Thank you {}".format(name))

# Sport Guessing game
sport = input("Guess my favorite sport: ")
while sport != "basketball":
    if sport == "soccer":
        print("Hint: no feet")
    elif sport == "football":
        print("Think inside")
    else:
        print("Try again")
    sport = input("Guess my favorite sport: ")


import random  # You only to do this once
number = 0
while number != 42:
    number = random.randint(1, 100)
    print("You got the number {}".format(number))
print("You got the number 42!")
