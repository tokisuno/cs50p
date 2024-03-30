def main():
    name = input("camelCase: ")
    snake_case(name)


def snake_case(name):
    for char in name:
        if char.isupper():
            print("_" + char.lower(), end="")
            char.replace(char, "")
        else:
            print(char, end="")


if __name__ == "__main__":
    main()
