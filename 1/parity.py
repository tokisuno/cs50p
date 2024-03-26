def main():
    x = int(input("What's x?: "))
    if is_even(x) == True:
        print("True")
    else:
        print("False")


def is_even(n):
    # Returns True or False based on the condition
    #   being met by the comparative ==
    return n % 2 == 0


if __name__ == "__main__":
    main()
