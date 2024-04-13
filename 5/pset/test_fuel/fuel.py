import re


def main():
    user_input = convert(input("Fraction: "))
    if user_input in range(0, 100):
        print(f"{gauge(user_input)}")


def convert(fraction):
    while True:
        try:
            expr = re.findall(r'[0-9\.]+|[^0-9\.]+', fraction)
            if expr[0] == "0":
                return 0/int(expr[2])
            elif expr[2] == "0":
                raise ZeroDivisionError

            if int(expr[0]):
                if int(expr[2]):
                    if expr[1] == "/":
                        if int(expr[0]) <= int(expr[2]):
                            return round(int(expr[0]) / int(expr[2]) * 100)
                        else:
                            raise ValueError
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
