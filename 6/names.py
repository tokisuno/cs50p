def main():
    names = []

    for _ in range(3):
        names.append(input("What's your name?: "))

    for name in sorted(names):
        print(f"hello, {name}")


if __name__ == "__main__":
    main()
