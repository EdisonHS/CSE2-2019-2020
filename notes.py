print("Hello World!")

print(True)
print(15)
# print(TRUE) This doesn't work

print(9001)  # This is an Integer
print(True)  # This is a boolean
print(9.81)  # This is a float
print("Hello")  # This is a string

print(5.5)
print("This is a thing")
print(False)
print("Seven")
print("15")

print("This is a string")
print("Hello)")

# ----------
# Math
# ----------
print()  # This prints out a blank line
print()
print(3 + 5)
print(5 - 2)
print(5 * 2)
print(50 / 5)
'''
This is a multi-line comment.

I can type whatever I want here
and it does not run
'''

"""
This is also a multi-line comment
"""
print()  # This prints out a blank line
print()

# Exponents (Powers)
print(3 ** 2)  # The answer is 9
print(6 ** 2)  # The answer is 36
print(2 ** 3)  # The answer is 8
print(2 ** 4)  # The answer is 16

# To do a square root: do a power of 1/2
print(36 ** (1/2))

print()
print()
# This is floor division (It rounds down)
print(16 // 4)  # The answer is 4
print(15 // 4)  # The answer is 3
print(13 // 4)  # The answer is 3
print(12 // 4)  # The answer is 3
print(7 // 3)  # The answer is 2
print(-8 // 3)  # The answer is -3

print()
print()
# Figure this out (Modulus)
print(13 % 12)  # The answer is 1
print(14 % 12)  # The answer is 2
print(25 % 12)  # The answer is 1
print(7 % 4)  # The answer is 3
print(155 % 50)  # The answer is 5

# Mixed Review (Do not run this part)
print(3 ** 3)  # The answer is 27
print(18 // 5)  # The answer is 3
print(13 % 4)  # The answer is 1
print(21 // 5)  # The answer is 4

# ---------
# Variables
# ---------

print()
print()
the_number = 3
# the "=" is the assignment operator
print(the_number)

print()
print()
the_number = the_number + 5
print(the_number)
# This adds 100 to the variable and assigns it
the_number += 100
print(the_number)
the_number -= 8
the_number /= 100
the_number *= 50
print(the_number)  # It is 50
the_number %= 10  # This is 0 (The remainder is 0)

drinks = 5
drinks + 3  # This does not modify drinks
print(drinks)

print(drinks == 3)  # Is drinks equal to 3?
print(drinks == 5)  # This is True
print(drinks > 3)
print(drinks <= 10)
print(drinks != 10)  # Not equal to

the_string = "hello"
second_string = "world"
print(the_string, second_string)
print("The first word is " + the_string)

the_word = "basketball"
the_other_word = "London"
the_last_word = "food"

# The word of the day:
# Concatenation - putting multiple strings together
print("The words are: " + the_word + ", " +
      the_other_word + ", and " + the_last_word)

print("The first words are:", the_word, the_other_word)

# This is the print you will be using most often
print("The three words are {}, {}, and {}".format(the_other_word, the_word, the_last_word))

# ----
# Inputs - This is the ONLY way to interact
# ----

name = input("What is your name? ")
print("Hello {}".format(name))

age = input("How old are you? ")
print("{}?!?!?! You belong in a museum!".format(age))

# INPUTS ARE ALWAYS OF TYPE STRING!!!!!!
# Recasting
age = int(age)  # This turns age into a number
print("Next year, you will be {}".format(age + 1))

# Funny things in python
number = str(5)  # This is "5"
print(str(5) + str(8))
