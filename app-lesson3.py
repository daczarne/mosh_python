#### Lesson 3 - Control flow ####

### Comparison operators ###
# Use comparison operators to compare values
10 > 3
10 >= 3
10 < 20
10 <= 20
10 == 10
10 == "10"
10 != "10"

# can also use them with strings
"bag" > "apple"
"bag" == "BAG"
print(ord("b"))  # ord() returns the Unicod code point
print(ord("B"))

### Conditional Statements ###
temperature = 25
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

### Ternary Operator ###
age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# A cleaner way to write this
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

# A cleaner way to write this (using a ternary operator)
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

### Logical Operators ###
# Three logical operator: and, or, not

# and evals to True if both statements are true
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# or evals to True if at least one statement is true
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

# not negates values
high_income = False
good_credit = True
student = True

if not student:
    print("Eligible")
else:
    print("Not eligible")

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

### Short-circuiting ###
# and: Python interpreter will stop as soon as it finds the first False statement
# or: Python interpreter will stop as soon as it finds the first True statement
high_income = False
good_credit = True
student = True

if (high_income and good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

### Chaining ###
# rule: age should be between 18 and 65
age = 22

if age >= 18 and age > 65:
    print("Eligible")
else:
    print("Not eligible")

# chaining comparison operators
if 18 <= age < 65:
    print("Eligible")
else:
    print("Not eligible")

### For loops ###
print("Sending a message")

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):
    print("Attempt", number + 1, (number + 1) * ".")

### For..Else ###
# Exiting a loop when message is successfully sent
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

# what if after 3 attempts we are not successful?
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

### Nested Loops ###
# putting one loop inside another loop

for x in range(5):  # outer loop
    for y in range(3):  # inner loop (child of the previous for statement)
        print(f"({x}, {y})")

### Iterables ###
print(type(range(5)))  # object of type "range"

# range objects are iterable
for x in range(5):
    print(type(x))

# strings are also iterable
for x in "Python":
    print(x)

# So are lists
for x in [1, 2, 3, 4]:
    print(x)

# other custom objects can be created so that they are iterable

### While ###

# repeat as long as a condition is true
number = 100
while number > 0:
    print(number)
    number //= 2  # divided by half with aggmented operator

# while input is not "quit" keep asking for commands
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

### Infinite Loops ###
# a loop that runs for ever
# use break to exit
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

### Exercise ###
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
