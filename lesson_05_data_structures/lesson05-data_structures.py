#### DATA STRUCTURES ####

# this will be used throughout the lesson
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque

### Lists ###
# Define a list with []
letters = ["a", "b", "c"]
numbers = [1, 2, 3]
booleans = [True, True, False]

# Define list of lists
# A matrix is a two dimensional list
matrix = [[0, 1], [2, 3]]

# Use * to repeat item in list
# List of 5 zeros
zeros = [0] * 5

# Use + to contactenate lists
combined = zeros + letters

# Every object in a list can be of a different type
print(combined)

# Use list() to create lists using a iterable
numbers = list(range(20))  # List from 0 too 19
characters = list("Hello World")  # List of letters in Hello World

# Number of items in list
print(len(characters))

### Accessing items ###
letters = ["a", "b", "c", "d"]
print(letters[0])  # Prints the first item in letters: "a"
print(letters[-1])  # Last item of the list

# Modify list
letters[0] = "A"

# Can use two indecies to slice a list
print(letters[0:3])

# If first index is not specified, 0 is assumed
print(letters[:3])

# If second index is not specified, last index is assumed
print(letters[1:])

# Omitting both ideces will copy the list
print(letters[:])

# Use step argument to skip
numbers = list(range(20))
print(numbers[::2])

# Return all items in reverse order
print(numbers[::-1])

### List unpacking ###
numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

# Unpack list into multiple variables (numberr of variables needs to be equal to list length)
first, second, third = numbers

# Can unpack multiple elements in one residual list called using *
numbers = [1, 2, 3, 4, 4, 4, 4, 4]
first, second, *other = numbers

# Unpacking first and last
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, *other, last = numbers

### Looping over lists ###
letters = ["a", "b", "c"]

# The following code generates a tupple where the first element is the position and the second item is the letter
for letter in enumerate(letters):
    print(letter)

# They can be accessed using [] function
for letter in enumerate(letters):
    print(letter[0], letter[1])

# Or we can use unpacking
for index, letter in enumerate(letters):
    print(index, letter)

### Adding or removing items ###
letters = ["a", "b", "c"]

# Adding elemnts to the end with append method
letters.append("d")
print(letters)

# Adding at a spcific possition with insert method
letters.insert(0, "-")

# Removing at the end with pop method
letters.pop()

# Removing at specific positions with pop method and an index
letters.pop(0)

# Removing without knowing the index (first occurrance)
letters.remove("b")

# delete statement for removing ranges of items
del letters[0]
del letters[0:3]

# Removing every element in a list
letters.clear()

### Finding items ###
letters = ["a", "b", "c"]

# Find the index of a given element (element must be in the list or we'll get an error)
print(letters.index("a"))

# Can check if an element exists in the list with the in operator
if "d" in letters:
    print(letters.index("d"))

# Number of occurances of an element (will return 0 if element not in list)
letters.count("d")

### Sorting lists ###
numbers = [3, 51, 2, 8, 6]
print(numbers)

# Sort a list with the sort method (ascending order)
numbers.sort()
print(numbers)

# Sort a list with the sort method (decending order)
numbers.sort(reverse=True)
print(numbers)

# Bulit in function sorted() - Original list is not modified
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# Sorting a list of tupples
items = [
    # Product name + items
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

# sort method will fail since Python doesn't know which index to sort over
print(items.sort())

# First we define a functions that, for every tupple, returns the sortting index


def sort_item(item):
    return item[1]


# Now we use that function's name (not calling) as the key argument in sort
items.sort(key=sort_item)
print(items)

### Lambda functions ###
items = [
    # Product name + items
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

# We can make the key argument in the sort method prettier
# We can use lambda expressions: lambda parameters:exprerssion
items.sort(key=lambda item: item[1])
print(items)

### Map function ###
items = [
    # Product name + items
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

# Want to transform the list of tupples in a list of numbers
prices = []
for item in items:
    prices.append(item[1])

# Use the map function and assign it to a list
# map takes a lambda function and applies it to every item of an iterable
prices = list(map(lambda item: item[1], items))
print(prices)

### Filter function ###
items = [
    # Product name + items
    ("Product 1", 10),
    ("Product 2", 9),
    ("Product 3", 12)
]

# Filtering items to get items with price equal or greatter than 10
# filter will return a filter object that needs to be coerced into a list
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

### List comprehensions ###

# Use a comprehension expression: [expression for item in items]
prices = [item[1] for item in items]
print(prices)

filtered = [item for item in items if item[1] >= 10]
print(filtered)

### Zip functions ###
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Combine lists into a list of tupples
list(zip(list1, list2))
list(zip("abc", list1, list2))

### Stacks ###

# Stacks work with LIFO (Last in - First out)
# A list can be used as a stack
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)

last = browsing_session.pop()
print(last)
print(browsing_session)
print("Redirect", browsing_session[-1])

# Check if stack is empty
if not browsing_session:
    print("disable")

### Queues ###

# FIFO (First in - First out)
# Can use a list to implement a list in Python

# Create a queue
queue = deque([])

# Append items to the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Remove from the beggining
queue.popleft()

# Check if queue is empty
if not queue:
    print("empty")

### Tuples ###
# Tuples are read-only lists

# Can be defined with () or without. If it's length one, then add trailing comma
point = (1, 2)
point = 1, 2
point = 1,
point = ()

# Concatenate
point = (1, 2) + (3, 4)

# Repear
point = (1, 2) * 3

# Convert list into tuple
point = tuple([1, 2])
point = tuple("Hello World!")

# Indexing
point = (1, 2, 3)
print(point[0])  # first item
print(point[0:2])  # first three

# Unpacking
x, y, z = point

# in operator to check existance of item
if 10 in point:
    print("exists")

### Swapping variables ###
x = 10
y = 11

# right hand-side is a tupple and can not be modified
# it then unpacks it
x, y = y, x

### Arrays ###

# Arrays are more efficient for large lists of numbers
# typecode: one character string that determines type of object in the list
numbers = array("i", [1, 2, 3])

# Add elements to the end of the list wth append method
numbers.append(4)

# Add elements at specific index with insert method
numbers.insert(4, 0)

# Remove last item with pop method
numbers.pop()

# Remove
numbers.remove(3)

# Access items with index
numbers[0]

# Must respect type of object: numbers[0] = 1.0 will produce an error since 1.0 is a float
numbers[0] = 1

### Sets ###

# Collection with no duplicates
numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print(uniques)

# Create a set with {}
second = {1, 4}

# methods
second.add(5)
second.remove(5)

# Set length
len(second)

# Mathematical operations
first = set(numbers)
second = {1, 5}

print(first | second)  # union
print(first & second)  # intersection
print(first - second)  # difference
print(first ^ second)  # symetric difference

# sets are unordered so can not access them with index

# check existance
if 1 in first:
    print("yes")

### Dictionaries ###

# collections of key-value pairs
# use them to map keys and values

# keys and only be inmutable types
# values have no such limitations
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)

# can get the value associated with a key using indexing
point["x"]

# updateing value
point["x"] = 10

# add new key
point["z"] = 20
print(point)

# check existance of key
if "a" in point:
    print(point["a"])

# returns None if item key doesn't exist
print(point.get("a"))

# returns 0 if item key doesn't exist
print(point.get("a", 0))

# delete items
del point["x"]
print(point)

# looping over dictionaries
for x in point:
    print(x)

# in each iteration loop variable will hold the key of an item

# rename x to key
for key in point:
    print(key, point[key])

# outputting tuples
for x in point.items():
    print(x)

# unpack them with
for key, value in point.items():
    print(key, value)

### Dictionaries comprehensions ###
values = []  # empty list
for x in range(5):
    values.append(x * 2)

# list comprehension
values = [x * 2 for x in range(5)]

# sets and dictionaries also support comprehension
values = {x * 2 for x in range(5)}  # set
values = {x: x * 2 for x in range(5)}  # dictionary

### Generator expressions ###

# generator objects are iterable
# they generate a new value in each iteration
values = (x * 2 for x in range(5))
for x in values:
    print(x)

# size of generator objects
values = (x * 2 for x in range(1000))
print("generator:", getsizeof(value))

values = (x * 2 for x in range(1000000))
print("generator:", getsizeof(value))

values = [x * 2 for x in range(1000000)]
print("list:", getsizeof(value))

### Unpacking operator ###

numbers = [1, 2, 3]
print(numbers)
print(1, 2, 3)

# unpacking operator
print(*numbers)
print(1, 2, 3)

# unpacking operator can unpack any iterable
values = [*range(5), *"Hello World!"]
print(values)

# to unpack dictionaries we need **
# if multiple values have the same key, the last value will be used
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}


#### Exercise ####
# Find the most common character in a text
sentence = "This is a common interview question"

# generate a dictionary where each letter is a key and it's value is it's frequency
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency, width=1)

# sort the dictionary
char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True
)

print(char_frequency_sorted[0])
