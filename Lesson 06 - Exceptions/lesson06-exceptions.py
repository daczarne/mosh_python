#### LESSON 6 - EXCEPTIONS ####

from timeit import timeit

### Exceptions ###

# An exception is an error that terminates the excecution of a programm
numbers = [1, 2]
print(numbers[3])

### Handling Exceptions ###

# The else clause will only be executed if there is no exceptions
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("Not a valid age")
    print(ex)
    print(type(ex))
else:
    print("No exceptions where thrown")
print("Execution continues.")

### Handling different exceptions ###
try:
    age = int(input("Age: "))
    xfactor = age / 10
except (ValueError, ZeroDivisionError):
    print("Not a valid age")
else:
    print("No exceptions where thrown")

### Cleaning up ###
# Need to close opened connections once we are done with them
# can use the finally clause for that since it will always be run
try:
    file = open("lesson06-exceptions.py")
    age = int(input("Age: "))
    xfactor = age / 10
except (ValueError, ZeroDivisionError):
    print("Not a valid age")
else:
    print("No exceptions where thrown")
finally:
    file.close()

### The with statement ###

# Another way of closing connections is by using a with statement
# with always closes after using
# with only works with certain kinds of objects: those with __enter__ and __exit__ methods
# methods that start with __ are refered to as "magic methods"
# when an object hace __enter__ and __exit magic methods, we say that it supporrs context management support
# only objects with context management support can use the with statement
try:
    with open("lesson06-exceptions.py") as file:
        print("File opened.")
        file.__ent
    age = int(input("Age: "))
    xfactor = age / 10
except (ValueError, ZeroDivisionError):
    print("Not a valid age")
else:
    print("No exceptions where thrown")

### Raising exceptions ###


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


### Cost of raising exceptions ###
code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

print("first code", timeit(code1, number=10000))

# Not printing message
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print("second code", timeit(code2, number=10000))


# Not printing message
code3 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("third code", timeit(code3, number=10000))
