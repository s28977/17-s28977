# Task 1: List Comprehensions
# Write a Python program that generates a list of squares of numbers from 1 to 10 using list
# comprehensions

squares = [x ** 2 for x in range(1, 10)]
print(squares)


# Task 2: Functions
# Expand the previous program by defining a function that takes a range of numbers as input
# and returns a list of squares for that range.e_squares(start, end))

def squares(start, end):
    return [x ** 2 for x in range(start, end)]


print(squares(2, 8))

