import sys


def main():
    name_list = list()
    while True:
        try:
            x = input("Name: ").strip().capitalize()
            name_list.append(x)
        except EOFError:
            if len(name_list) == 1:
                print("\nAdieu, adieu, to " + str(name_list[0]))
                sys.exit(0)
            elif len(name_list) == 2:
                print("\nAdieu, adieu, to " + str(name_list[0] + " and " + str(name_list[1])))
                sys.exit(0)
            elif len(name_list) >= 3:
                listed = ', '.join(name_list[:-1])
                print("\nAdieu, adieu, to " + listed + ", and " + name_list[-1])
                sys.exit(0)


if __name__ == "__main__":
    main()
