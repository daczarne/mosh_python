# while: input is not "quit", keep asking for commands
command = ""

while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
