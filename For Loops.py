for variable in range(10):
    print("Hello World")

for iterator in range(1500):
    print("Computer Science")

for i in range(2, 5):
    print("How many times will this print?")

for i in range(4, 10):
    print("Magic")

for i in range(8):
    print(200)

for i in range(5):
    print(i)

for i in range(12):
    print(i)

for i in range(10000):
    print(i)

for i in range(5, 10):
    print(i)

for i in range(5, 10):
    print(i + 4)

for i in range(10, 20):
    print("The number 'i' was:")
    print(i)
    print("Now it is:")
    print(i + 5)
    print()

for i in range(0, 16, 2):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(1, 8, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

# -----------
# Day 2
# -----------
print()
print("This is day 2 work")
print()

# Adding the numbers 1-100
total = 0
for i in range(1, 101):
    total += i
    print("The total so far is", total)
print(total)

# Factorial
print()
total = 1
for i in range(1, 101):
    total *= i
    print("The total so far is", total)
print(total)

# Checking divisibility
# This will print the numbers 1-1000
# That are divisible by 2
print()
print()
for i in range(1, 1001):
    if i % 2 == 0:
        print(i)
print()
print()
print()
for i in range(1, 1001):
    if i % 3 == 0:
        print(i)
print()

for i in range(1, 201):
    if i % 6 == 0 and i % 4 == 0:
        print("{} is divisible by 6 and 4".format(i))
    elif i % 6 == 0:
        print("{} is divisible by 6".format(i))
    elif i % 4 == 0:
        print("{} is divisible by 4".format(i))