import string


def main():
    ans = input("Greeting: ").lower().strip()
    print(f"${value(ans)}")


def value(greeting):
    greeting = str.maketrans('', '', string.punctuation)

    if greeting.partition(' ')[0] == "hello,":
        return 0
    elif greeting.partition(' ')[0] == "hello":
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


def remove_punct(s):
    return s.translate(t)


if __name__ == "__main__":
    main()
