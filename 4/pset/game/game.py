import sys
import random as rand


def main():
    level = get_input("Level: ")
    number = rand.randint(1, level)
    while True:
        guess = get_input("Guess: ")
        if guess > number:
            print("Too large!")
            pass
        elif guess < number:
            print("Too small!")
            pass
        else:
            print("Just right!")
            sys.exit(0)


def get_input(text):
    while True:
        try:
            x = int(input(text))
            if x > 1:
                return x
        except (ValueError, IndexError):
            pass


if __name__ == "__main__":
    main()
