def main():
    print(f"{dots(input())}")


def dots(x):
    return x.strip().replace(" ", "...")


main()
