import constant as const


def main():
    speed_of_light(input("Input mass (in kg): "))


def speed_of_light(i):
    print(int(i) * const.SOL ** 2)


if __name__ == "__main__":
    main()
