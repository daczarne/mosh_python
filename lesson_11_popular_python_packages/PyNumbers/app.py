import numpy as np

# create numpy arrays with the array method
array = np.array([1, 2, 3])
print(array)
print(type(array))

# We can also create mutidimensional arrays with this method
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)
print(type(array))

# Array objects have an attribute called shape
print(array.shape)
print(type(array.shape))

# Array constructors

# Decimal floating type
array = np.zeros((3, 4))
print("float zeros:", array)

# Integers type
array = np.zeros((3, 4), dtype=int)
print("integer zeros:", array)

array = np.ones((3, 4), dtype=int)
print("integer ones:", array)

array = np.full((3, 4), 5, dtype=int)
print("integer fives:", array)

array = np.random.random((3, 4))
print("random numbers:", array)

# Access first row and first column
print(array[0, 0])

# boolean comparisons
print(array > 0.2)

# boolean indexing
print(array[array > 0.5])

# sum of array items
print(np.sum(array))

# floor of each item
print(np.floor(array))

# ceil of each item
print(np.ceil(array))

#  Arithmatic operations between arrays and numbers
first = np.array([1, 2, 4])
second = np.array([4, 5, 6])
print(first + second)
print(first + 3)
