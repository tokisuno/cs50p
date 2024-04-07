# Get user input and add each item.upper() into an array
# on EOFError count each item in the array,
# and then print them in alphabetical order
from collections import Counter


def main():
    shop = list()
    while True:
        try:
            items = input("")
            shop.append(items.upper())
            shop.sort()
        except EOFError:
            s = Counter(shop)
            for k, v in s.items():
                print(v, k)
            break


if __name__ == "__main__":
    main()
