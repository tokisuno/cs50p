def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) == 4 | len(s) == 6:
        length = len(s)
    else:
        length = len(s) - 1

    if len(s) < 4:
        return False
    if len(s) > 6:
        return False

    if s[0].isalpha() & s[1].isalpha():
        if s[length//2-1].isalpha():
            if any(map(str.isdigit, s)):
                numbers = []
                half = s[length//2:]

                for num in half:
                    if num.isnumeric():
                        numbers.append(num)

                if numbers[0] == "0":
                    return False
                elif s[-1].isnumeric():
                    return True
                else:
                    return False
            else:
                return True
    else:
        return False


if __name__ == "__main__":
    main()
