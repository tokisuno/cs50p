def main():
    user_input = int(input("Insert Coin: "))
    amount_due(user_input)


def amount_due(paid):
    coke = 50
    q = 25
    d = 10
    n = 5
    while True:
        if paid == q or paid == d or paid == n:
            coke -= paid
        else:
            print(f"Amount Due: {coke}")

        if coke > 0:
            print(f"Amount Due: {coke}")
        elif coke < 0:
            print(f"Change Owed: {coke * -1}")
            break
        else:
            print(f"Change Owed: {coke * -1}")
            break

        paid = int(input("Insert Coin: "))


if __name__ == "__main__":
    main()
