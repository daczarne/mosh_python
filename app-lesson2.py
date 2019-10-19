#### Lesson 2 - Primitive Types ####
import math

### Primitive types in Python: numbers, booleans and strings ###
students_count = 1000  # an integer
rating = 4.99  # a float
is_published = False  # Boolean
course_name = "Python programming"  # string

### Variable names ###

## Principles ##
# variable names need to be descriptive
# lower case letters to name variables
# underscore to separate words
# pep8: space around equal signs

### Strings ###

# strings need to be surrounded with quotes
# use triple quotes for long messages

course = "Python Programming"
# lenght of a string
print(len(course))
# access first character
print(course[0])
# access last character (first from the end)
print(course[-1])
# new string with the first three characters (end index not included)
print(course[0:3])
# same string (starts from index 0 and goes all the way to the end)
print(course[0:])
# string with first three letters
print(course[:3])
# copy of the original string
print(course[:])

### Escape sequences ###

# use single quotes
course = 'Python "Programming'

# use escape character \
# escape squence \"
course = "Python \"Programming"
print(course)
# escape squence \'

course = "Python \'Programming"
print(course)

# escape squence \\
course = "Python \\Programming"
print(course)

# escape squence \n
course = "Python \nProgramming"
print(course)

### Formatted Strings ###

## Concatenation ##
first = "Daniel"
last = "Czarnievicz"
full = first + " " + last
print(full)

## Formatted strings ##
first = "Daniel"
last = "Czarnievicz"
full = f"{first} {last}"
print(full)

# Can be used while calling functions too
full = f"{len(first)} {2 + 2}"
print(full)

### String Methods ###
course = " Python programming  "
print(course)
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.lstrip())
print(course.rstrip())
print(course.find("pro"))
print(course.find("Pro"))
print(course.replace("p", "j"))
print("pro" in course)
print("swift" not in course)

### Numbers ###
# Three types of numbers: integers, floats, complex numbers
x = 1  # integers
x = 1.1  # float
x = 1 + 2j  # complex

# two diferent types of division
print(10 / 3)  # will give us a float
print(10 // 3)  # will five us an integer

# modulus
print(10 % 3)

# exponent: left to the power of right
print(10 ** 3)

# Auggmented assignment operator
x = 10
print(x)
x = x + 3
print(x)
x += 3
print(x)

### Working with numbers ###
print(round(2.9))
print(abs(-2.9))

## importing math modulus for more complex operations ##
# autopep places the call on the top of the program upon saving
# use .to access methods (complete list can be found in Google)
print(math.ceil(2.2))

### Type conversion ###
# to get input from the user
x = input("x: ")
y = float(x) + 1
print(f"x: {x}, y: {y}")

## use the folowing functions to convert ##
# int() for integers
# float() for floats
# bool() for booleans
# str() for strings

## Trufy and Falsy ##
# Falsy: "", 0, None
# Trufy: everything else
