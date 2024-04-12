import random

# 10 levels
# 3 tries per equation
# returns score/10
# randomly generates 10 math problems formatted as (x + y =)
# each integer is positive
# only addition


def main():
    level = get_level()
    questions = 1
    correct = 0
    while questions <= 10:
        guesses = 0
        i1 = generate_integer(level)
        i2 = generate_integer(level)
        answer = eval(f"{i1} + {i2}")
        while True:
            if guesses == 3:
                print(f"{i1} + {i2} =", eval(f"{i1} + {i2}"))
                break

            x = int(input(f"{i1} + {i2} = "))

            if x != answer:
                print("EEE")
                guesses += 1
            elif x == answer:
                correct += 1
                break

        questions += 1
    print(f"Score: {correct}")


def get_level():
    while True:
        try:
            x = int(input("Level: ").strip())
            if x > 0 and x <= 3:
                return x
            else:
                raise ValueError
        except ValueError:
            pass


def generate_integer(level):
    while True:
        try:
            match level:
                case 1:
                    return random.randint(0, 9)
                case 2:
                    return random.randint(10, 99)
                case 3:
                    return random.randint(100, 999)
                case _:
                    raise ValueError
        except ValueError:
            break


if __name__ == "__main__":
    main()
