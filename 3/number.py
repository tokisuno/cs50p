def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def main():
    x = get_int("What's x?: ") 
    print(f"x is {x}")


if __name__ == "__main__":
    main()
