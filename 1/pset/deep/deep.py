def main():
    ans = input("What's the Answer to the Great Question of Life, the Universe, and Everything?: ").lower().strip()
    is42(ans)

def is42(ans):
    match ans:
        case "42" | "forty two" | "forty-two":
            print("Yes")
        case _:
            print("No")

if __name__ == "__main__":
    main()
