# If you are reading this and don't understand the reference, educate yourself

# Ask user for their name
#   * Remove whitespace from str
#   * .strip is a method function
#   * Use title-casing
name = input("What's your name?: ").strip().title()
# first, last = name.split(" ")

print(f"Fuck you, {name}!")

# Using , to separate args automatically adds space before arg being printed
# Using appends to end of string and doesn't add a space beforehand
#   * Concatonation

# print() documentation:
#   print(*objects, sep=' ',  end='\n', file=sys.stdout, flush=False)
