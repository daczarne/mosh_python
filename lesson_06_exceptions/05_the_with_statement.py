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
    age = int(input("Age: "))
    xfactor = age / 10
except (ValueError, ZeroDivisionError):
    print("Not a valid age")
else:
    print("No exceptions where thrown")
