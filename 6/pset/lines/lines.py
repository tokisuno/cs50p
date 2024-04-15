import os
import sys


def main():
    count = 0
    split_file = os.path.splitext(sys.argv[1])
    ext = split_file[1]

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip().startswith("#") or len(line) < 3:
                    pass
                elif line.lstrip() == "":
                    pass
                else:
                    count += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

    if ext != ".py":
        print("Not a Python file")
        sys.exit(1)
    else:
        print(count)


if __name__ == "__main__":
    main()
