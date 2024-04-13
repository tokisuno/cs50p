def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in word:
        if char.lower() not in vowels:
            result.append(char)
    result = "".join(result)
    return result


if __name__ == "__main__":
    main()
