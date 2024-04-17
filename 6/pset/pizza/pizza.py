import csv
import os
import sys
from tabulate import tabulate


def main():
    menu = []

    split_file = os.path.splitext(sys.argv[1])
    ext = split_file[1]
    if ext != ".csv":
        print("Not a CSV file")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file, fieldnames=["pizza", "small", "large"])
            for row in reader:
                menu.append({"Penis": row["pizza"],
                             "Small": row["small"],
                             "Large": row["large"]}
                            )
            print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)


if __name__ == "__main__":
    main()
