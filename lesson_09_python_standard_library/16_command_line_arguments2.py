import sys

if len(sys.argv) == 1:
    print("USAGE: python lesson_09_python_standard_library/16_command_line_arguments.py <password>")
else:
    password = sys.argv[1]
    print("Password:", password)
