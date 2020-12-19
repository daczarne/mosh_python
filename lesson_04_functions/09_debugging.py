### Debugging ###

# Add break point by moving cursor to line and pressing F9
# Remove break point by pressing F9 again (while in the line)
# Press F5 to run application upto the break point
# Execute one statement at a time press F10
# To access user defined functions press F11
# To exit user defined functions press Shift + F11
# To stop the debugger and fix a problem press Shift + F5


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
