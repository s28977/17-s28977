import math
from square_generator import SquareGenerator

# Task 1: List Comprehensions
# Write a Python program that generates a list of squares of numbers from 1 to 10 using list
# comprehensions

squares = [x ** 2 for x in range(1, 11)]
print(squares)


# Task 2: Functions
# Expand the previous program by defining a function that takes a range of numbers as input
# and returns a list of squares for that range.e_squares(start, end))

def squares(start, end):
    return [x ** 2 for x in range(start, end)]


print(squares(2, 8))


# Task 3: Classes
# Create a class called SquareGenerator that has a method to generate squares for a given
# range of numbers.


square_gen = SquareGenerator()
print(square_gen.squares(5, 3))

# Task 4: Libraries
# Utilize the math library to calculate the square root of each number in the generated list from
# the previous task.

square_roots = [math.sqrt(x) for x in square_gen.squares(1, 11)]
print(square_roots)

# Task 5: Exceptions
# Handle the case where the end of the range is less than the start in the SquareGenerator
# class.

print(square_gen.squares(6, 3))

# Task 6: Modules
# Extract the SquareGenerator class into a separate module named square_generator.py.


# Task 7: Packages
# Transform the square_generator module into a package by adding an empty __init__.py file
# and organize it accordingly.
# Task 8: Inheritance
# Create a subclass called CubicGenerator that inherits from the SquareGenerator class.
# Modify the CubicGenerator to generate cubes instead of squares.
# Task 9: Function Overriding
# Override the square generation method in the Cubic Generator class to generate squares
# with a check to see if the start of the range is less than the end, if not return an Exceptions
# Task 10: Abstract Elements
# Convert the SquareGenerator class into an abstract base class (ABC) using the abc module,
# making the generate_squares method abstract. Ensure that the CubicGenerator class
# implements this abstract method.
# Task 11:
# The result of the assignment should be a link to a pull request