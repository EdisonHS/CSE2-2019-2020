"""
What you think will be on the final:
Identifying Data types*
Math functions
variables
integers
rounding
concatenation (adding strings together)
print statements
finding errors (error analysis)
exponents
floor division (//)
Modulus (%)
Booleans (<, >, !=, ==, etc.)
prints with variables (.format,  ","  , "+")
inputs
recasting (  "int()"   )
keywords (print, input, etc.)
escape characters***
"""

# Basic Print
print("Hello world")

# Math Functions
print(3 + 5)
print(5 * 5)
print(5 / 3)

# Exponents
print(5 ** 2)  # this is 5 to the 2nd power
print(3 ** 4)
print(2 ** 101)

# Escape Characters ***
# THIS IS NEW!!!!

print("The fox says \"Ring-dingeringeding!\"")
print("This is on one line. \nThis is on a second line")
print("\tThis is a tab")
print('This is Mr. Wiebe\'s trick')

print("\tThis is indented. \nThis is on a new line.")
print("AM\\PM")  # This prints "AM\PM"

# Rounding
number = 3.652415655676
print("The number rounded to 2 decimals: {:.2f}".format(number))
print("The number rounded to 7 decimals: {:.7f}".format(number))

# Floor Division
print(14 // 5)  # 2
print(17 // 2)   # 8

# Modulus
print(5 % 2)  # 1
print(199 % 100)  # 99

# variables
number = 500
number += 100
print(number)  # 600

first_num = 15  # This gets overridden
second_num = 4
third_num = 12
first_num = third_num - second_num  # First num is 8
first_num += 2
third_num -= 7
second_num /= 2
print(first_num)  # 10
print(second_num)  # 2
print(third_num)  # 5


num1 = 13
num2 = 16
num3 = 10
num2 = num1 - num3  # num2 = 3
num2 -= 2  # num2 = 1
num1 += 5  # num1 = 18
num3 %= 2  # num3 = 0
print(num1)  # 18
print(num2)  # 1
print(num3)  # 0


# Printing With Variables
num4 = "18"
print("Num1 is", num1)  # Commas put in spaces
print("Num4 is" + num4)  # Just combines - no extra chars
print("num3 is {}".format(num3))

# Booleans
print(5 > 3)  # True (note the capital T)
print(5 == 5)  # 5 is equal to 5
print(5 != 6)  # 5 is NOT equal to 6
print(5 <= 10)  # 5 is less than or equal to 10

# Printing with variables
str1 = "10"
print(str1)  # Prints just 10
print("Num1 is", num1)  # Num1 is 18
print("Str1 is" + str1)  # Str1 is10
print("Num3 is {}".format(num3))  # Num3 is 0

# Inputs
on_task = input("Are we on task?")  # This should be a question
print(on_task)

# Recasting
age = input("How old are you?")
age = int(age)
print("Next year, you will be {} years old"
      .format(age + 1))

cost = input("How much does it cost?")
cost = float(cost)
tax = 1.0795  # Taxes in Fresno are 7.95%
print("The item costs ${}".format(cost * tax))

# Keywords
'''
These are special keywords:
(You cannot name a variable these)
print
input
int
str
float
'''
# Concatenation
thing1 = "a"
thing2 = "b"
print(thing1 + thing2)  # ab

thing3 = "6"
thing4 = "12"
print(thing3 + thing4)  # 612

print(int("5") + int("15") + 5)  # 25
