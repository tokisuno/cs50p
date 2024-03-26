x = int(input("What's x?: "))
y = int(input("What's y?: "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else: 
    print("x is equal to y")

# Instead of 
#   if x > y or x < y:
if x != y:
    print("x and y are not equal")
else:
    print("x is equal to y")

# Or
if x == y:
    print("x is equal to y")
else:
    print("x and y are not equal")


