import os
import sys


def main():
    split_file = os.path.splitext(sys.argv[1])
    ext = split_file[1]
    if ext != ".csv":
        print("Not a CSV file")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    try:
        with open(sys.argv[1]) as file:
            with open(sys.argv[2], "w") as new_file:
                new_file.write("first,last,house\n")
                next(file)
                for line in file:
                    first, last, house = line.split(",")
                    new_line = f'{last.lstrip().rstrip(chr(34))},{first.lstrip(chr(34))},{house}'
                    line = line.replace(line, new_line)
                    new_file.write(line)

    except FileNotFoundError:
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)


if __name__ == "__main__":
    main()
