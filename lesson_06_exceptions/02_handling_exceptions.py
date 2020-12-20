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
