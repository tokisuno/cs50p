import sys
from pyfiglet import Figlet
import random as rand

def main():
    if len(sys.argv) == 1:
        print(rand.randint(1, 2))

    for arg in sys.argv[1:]:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            try:
                res = input("Input: ")
                fig = Figlet(font=sys.argv[2])
                print(fig.renderText(res))
            except TypeError:
                return
            else:
                return
        else:
            try:
                res = input("Input: ")
                fig = Figlet()
                print(fig.renderText(res))
            except TypeError:
                return
            else:
                return

    return


if __name__ == "__main__":
    main()
