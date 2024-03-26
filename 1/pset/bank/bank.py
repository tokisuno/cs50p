import string


def main():
    ans = input("Greeting: ").lower().strip()
    print(f"${is_greeting(remove_punct(ans))}")
    

def is_greeting(g):
    if g.partition(' ')[0] == "hello,":
        return 0
    elif g.partition(' ')[0] == "hello":
        return 0
    elif g.startswith("h"):
        return 20
    else:
        return 100

def remove_punct(s):
    t = str.maketrans('', '', string.punctuation)
    return s.translate(t)

if __name__ == "__main__":
    main()
