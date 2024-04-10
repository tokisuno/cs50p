def main():
    user_input = names()
    if len(user_input) <= 2:
        print("Adieu, adieu, to " + str(user_input[0] + "and " + str(user_input[1])))
    elif len(user_input) >= 3:
        print(user_input)
        listed = ', '.join(user_input[:-1])
        print("Adieu, adieu, to " + listed + ", and " + user_input[-1])
    else:
        return 

def names():
    name_list = list()
    while True:
        try:
            x = input("Name: ").strip().capitalize()
            name_list.append(x)
        except ValueError:
            pass
        except KeyError:
            pass
        except EOFError:
            print("")
            break
    return name_list
if __name__ == "__main__":
    main()
