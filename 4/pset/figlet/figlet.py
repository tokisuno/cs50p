
import sys
import random as rand
import pyfiglet
from pyfiglet import Figlet

fonts = pyfiglet.FigletFont.getFonts()

def main():
    for arg in sys.argv:
        if len(sys.argv) - 1 == 2:
            if sys.argv[2] in fonts:
                if sys.argv[1] == "-f" or sys.argv[1] == "--font":
                    try:
                        res = input("Input: ")
                        fig = Figlet(font=sys.argv[2])
                        print(sys.argv[2])
                        print(fig.renderText(res))
                    except (TypeError, IndexError):
                        sys.exit(0)
                    else:
                        sys.exit(0)
                else:
                    sys.exit(1)
            else:
                sys.exit(1)
        elif len(sys.argv) - 1 == 1:
            sys.exit(1)
        else:
            try:
                res = input("Input: ")
                fig = Figlet(font=fonts[rand.randint(0, len(fonts))-1])
                print(fig.renderText(res))
            except TypeError:
                sys.exit(0)
            else:
                sys.exit(1)
    return

if __name__ == "__main__":
    main()
