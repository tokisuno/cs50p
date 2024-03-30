def main():
    user_input = input("Input: ")
    remove_vowels(user_input)


def remove_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in string:
        if char.lower() not in vowels:
            result.append(char)
    result = "".join(result)
    print(result)


if __name__ == "__main__":
    main()
