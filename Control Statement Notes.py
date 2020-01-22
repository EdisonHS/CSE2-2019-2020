score = 130
if score > 100:
    print("HIGHSCORE!")

number = 3
if number > 10:
    print("You win!")

grade = 80
if grade >= 60:
    print("You passed the test!")
if grade == 0:
    print("You got a zero")

print("Grade 2:")
grade2 = 55
if grade2 > 60:
    print("You passed!")
    print("You got a {}".format(grade2))
else:
    print("You didn't pass.")

if True:
    print("Does this print?")
    print("Will this work?")

cost = int(input("How much does it cost?"))
if cost < 5:
    print("Pay with a few dollar bills")
elif cost < 20:
    print("Pay with a $20 bill")
else:
    print("You can't afford it")

your_grade = int(input("Enter your percentage"))
if your_grade >= 90:
    print("You got an A")
elif your_grade >= 80:
    print("You got a B")
elif your_grade >= 70:
    print("You got a C")
elif your_grade >= 60:
    print("You got a D")
else:
    print("You got an F.")

num = int(input("Enter a number"))
if num < 0:
    print("Invalid Number")
if num > 10:
    print("Output 1")
elif num > 4 and num < 8:
    print("Output 2")
else:
    print("Output 3")

x = int(input("Enter a number"))
if x < 5:
    print("Output 1")
elif x > 10:
    print("Output 2")
if x == 3:
    print("Output 3")
elif x > 12:
    print("Output 4")