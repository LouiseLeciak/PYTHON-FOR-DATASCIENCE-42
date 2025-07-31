import sys

if (len(sys.argv) != 2):
    print("AssertionError: more than one argument is provided")
    exit(1)

arg = sys.argv[1]

if arg.startswith("-"): #checking the negatives numbers
    is_int = arg[1:].isdigit() # if it's neg we pass the -
else:
    is_int = arg.isdigit()

if not is_int: # if isdigit says there is no digit
    print("AssertionError: argument is not an integer")
    exit(1)

value = int(arg)

if (value % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
exit(1)