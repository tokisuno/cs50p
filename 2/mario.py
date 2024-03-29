def main():
    print_column(3)
    print()
    print_row(4)
    print()
    print_square(3)


def print_row(width):
    print("?" * width, end="")


def print_column(height):
    for _ in range(height):
        print("#")


def print_square(size):
    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")
        print()


if __name__ == "__main__":
    main()
