def main():
    name = input("What's your name?: ")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")

    with open("names.txt", "r") as file:
        for line in file:
            print("hello,", line, end='')


if __name__ == "__main__":
    main()
