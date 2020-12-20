### Handling different exceptions ###

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("Not a valid age")
else:
    print("No exceptions where thrown")
