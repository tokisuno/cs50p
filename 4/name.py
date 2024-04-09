import sys

# argv[0] is the program you're running
try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
