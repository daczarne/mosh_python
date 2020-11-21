#### LESSON 07 - CLASSES ####

### Classes ###

# A Class is a blueprint for creating new objects
# An Object is an instance of a class

# For example:
#   Class: Human
#   Objects: John, Mary, Jack

### Creating classes ###

# Creating with a point class, with Pascal naming convention

"""
class Point:
    # define the methods for objects of class point
    def draw(self):
        print("draw")
"""

# to create a point object we call the class like we'd do a function
# point also inherited other methods
point = Point()
point.draw()

# check if an object is an instance of a given class
print(isinstance(point, Point))

### Constructors ###

# initial values for x and y coords are supplied by a constructor
# a class or an object bundles data and functions related to that into one unit

# Example:
#   Class: Human
#   Object: John
#   Attributes: hair color, eye color, height, weight, etc
#   Methods: walk, run, talk, eat, etc

"""
class Point:
    # self is a reference to the current point object
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # define the methods for objects of class point

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
"""

### Class attributes Vs Instance attributes ###

# objects are dynamic so additional attributes can be defined as needed
# those are called instance attributes, they belong to a spcific instance of an object
# classes can also have class attributes and every instance of that class with share it

# Example
#   Class: Human
#   Object (instance of the class): John
#   Class Attributes: two legs, two arms, liver, heart, etc
#   Instance attributes: eye color, height, weight, etc
#   Methods: walt, talk, eat, etc

"""
class Point:
    # class level attribute
    default_color = "red"

    # self is a reference to the current point object
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # define the methods for objects of class point

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
"""

# define an instance of class Point
point = Point(1, 2)
# Access default color attribute
point.default_color
# Access to the attribute
Point.default_color

# Can redefine default
Point.default_color = "yellow"

### Class methods Vs Instance methods ###

# Methods can also be defined for either instance or class
# methods that creat new instances are called "factory methods"
point = Point(0, 0)

"""
class Point:
    # class level attribute
    default_color = "red"

    # define a class method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # self is a reference to the current point object
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # define the methods for objects of class point

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
"""

### Magic Methods ###

# magic methods start and end with __
# they are called automaticly when creat a new instance of that class

"""
class Point:
    # class level attribute
    default_color = "red"

    # define a class method
    @classmethod
    def zero(cls):
        return cls(0, 0)

    # self is a reference to the current point object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define the methods for objects of class point

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
"""

### Comparing objects ###


"""
class Point:
    # self is a reference to the current point object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define the methods for objects of class point

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y
"""

### Performing arithmetic operations ###


class Point:
    # self is a reference to the current point object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # define the methods for objects of class point
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


### Making custom containers ###

# data structures = container types
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


### Private members ###

# don't have private memebers in python
# use __memeber to use it

### Properties ###

# A property is an object that sits in front of an attribute and allows us to get or set the value of that attribute
# A property has two methods called getter and setter
# can use a decorator to make properties
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

    #price = property(get_price, set_price)


### Inheritance ###


### The object class ###


### Method overriging ###


### Multi-level inheritance ###


### Multiple inheritance ###


### A good example of inheritance ###


### Abstract base classes ###


### Polymorphism ###


### Duck typing ###


### Extending built-in types ###


### Data classes ###
