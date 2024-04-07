menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    user_input = menu_item()
    print(user_input)


def menu_item():
    total = 0
    m = dict_tolower(menu)
    while True:
        try:
            x = input("Item:").lower()
            if x in m.keys():
                total += m[x]
                print(f"${total:.2f}")
        except ValueError:
            pass
        except KeyError:
            pass
        except EOFError:
            break


def dict_tolower(i):
    better = dict()
    for k in i.keys():
        if type(i[k]) is dict:
            better[k.lower()] = dict_tolower(i[k])
        else:
            better[k.lower()] = i[k]
    return better


# User inputs item
# Program in loop returns total of the items added together
# Program remembers the added amount
# Case insensitive
# Runs until the user hits ends program


if __name__ == "__main__":
    main()
