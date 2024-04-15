def main():
    with open("students.csv") as file:
        for line in file:
            # If you know your csv will be a list with 2 values:
            #   You can create 2 vars which automaticall assign to each value
            name, house = line.rstrip().split(",")
            print(f"{name} is in {house}")
            # 0 is the key
            # 1 is the value
            # print(f"{row[0]} is in {row[1]}")


if __name__ == "__main__":
    main()
