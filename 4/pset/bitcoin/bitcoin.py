import requests
import sys


def main():

    try:
        requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        print("oops")
        return

    req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

    try:
        if not float(sys.argv[1]):
            raise ValueError
        elif not sys.argv[1]:
            raise IndexError
    except IndexError:
        print("Missing argument")
        sys.exit(1)
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    data = req["bpi"]["USD"]["rate_float"]
    value = float(data) * float(sys.argv[1])
    print(f"${value:,.4f}")

    return


if __name__ == "__main__":
    main()
