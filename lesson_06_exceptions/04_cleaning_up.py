### Cleaning up ###

# Need to close open connections once we are done with them
# We can use the finally clause for that since it will always be run

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
