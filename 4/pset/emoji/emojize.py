from emoji.core import emojize


def main():
    try:
        resp = emojize(input("Input: "), language="alias")
        print(resp)
        print(f"Output: {resp}")
    except (TypeError, IndexError):
        pass


if __name__ == "__main__":
    main()
