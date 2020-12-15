### Infinite Loops ###

# a loop that runs for ever
# use break to exit

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
