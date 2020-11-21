#### FUNCTIONS ####

### Defining functions ###
# def defines a functions
# functions take two line breaks in Python


def greet_1():
    print("Hi there")
    print("Welcome aboard")


greet_1()

### Arguments ###
# parameter: input defined for a function
# argument: value given for a parameter


def greet_2(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet_2("Daniel", "Czarnievicz")
greet_2("John", "Smith")

### Types of functions ###


def greet_3(name):
    print(f"Hi {name}")

# Two types of functions:
#   1 - Functions that perform a task, for example: print()
#   2 - Functions that calculate and return a value, for example round()

# By default all functions return the None value (object that represents the absence
# of a value)


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Daniel")
print(message)
file = open("content.txt", "w")
file.write(message)

### Keyword arguments ###


def increment(number, by):
    return number + by


result = increment(2, 1)
print(result)

# we can simplfy the code by passing increment() to print()
print(increment(2, 1))

# keyword arguments (i.e. naming arguments in function calls)
print(increment(2, by=1))

### Default arguments ###
# optional parameters always come after the required parameters


def increment_by(number, by=1):
    return number + by


print(increment_by(2))
print(increment_by(2, 5))

### xargs ###
# Functions that take a variable number of arguments

# Product of two numbers


def multiply_2(x, y):
    return x * y


multiply_2(2, 3)

# Product of n numbers


def multiply_n(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply_n(2, 3, 4, 5))

### xxargs ###
# user object is a dictionary
# ** allows function parameters to take multiple arguments and Python will pack them in
# a dictonary (the one with {})
# We can then access the values using the bracket notation


def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)

### Scope ###
# Scope: region of the code where a variable is defined

# Functions have local variables
# After function call is evaluated, Python will garbage collect them

# Variables outside a function, are global variables
# Global = any point in the file

# Not recomended, but global variables can be modified inside a function
message = "a"


def greet_4(name):
    global message
    message = "b"


print(message)

### Debugging ###

# Add break point by moving cursor to line and pressing F9
# Remove break point by pressing F9 again (while in the line)
# Press F5 to run application upto the break point
# Execute one statement at a time press F10
# To access user defined functions press F11
# To exit user defined functions press Shift + F11
# To stop the debugger and fix a problem press Shift + F5

### Exercise ###


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
