# ZeroDivisionError
# Must only handle ints
# No floats
# Top can't be bigger than bottom

import re


def main():
    user_input = fuel()
    if user_input <= 1:
        print("E")
    elif user_input >= 98:
        print("F")
    else:
        print(str(user_input) + "%")


def fuel():
    while True:
        try:
            x = input("Fraction: ")
            expr = re.findall(r'[0-9\.]+|[^0-9\.]+', x)
            if expr[0] == "0":
                return 0/int(expr[2])
            if int(expr[0]):
                if int(expr[2]):
                    if expr[1] == "/":
                        if int(expr[0]) <= int(expr[2]):
                            return round(int(expr[0]) / int(expr[2]) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


# 1. Get user input
# 2. Make user input into list
# 3. Make sure all types match up
# 4. Make sure middle list item is always /

if __name__ == "__main__":
    main()
