import string


def main():
    ans = input("Greeting: ")
    print(f"${value(ans)}")


def value(greeting):
    for punctuation in string.punctuation:
        greeting = greeting.replace(punctuation, '').lower().strip()

    if greeting.partition(' ')[0] == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
