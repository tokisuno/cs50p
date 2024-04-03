import math

def main():
    x = fuel()

    x *= 100
    # print(x)
    while True:
        if x > 100 or x < 0:
            try:
                x = fuel()
            except ValueError:
                pass
            except ZeroDivisionError:
                pass
        break


    if x == (2/3) * 100:
        x = math.ceil(x)
        print(str(int(x)) + "%")
    elif x <= 1:
        print("E")
    elif x >= 99:
        print("F")
    else:
        print(str(int(x)) + "%")

def fuel():
    while True:
        try:
            x = eval(input("Fraction: "))
            return x
        except NameError:
            pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass



if __name__ == "__main__":
    main()
