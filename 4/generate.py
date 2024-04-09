from random import choice, randint, shuffle
import statistics

coin = choice(["heads", "tails"])
print(coin)
print("---")

num = randint(1, 10)
print(num)
print("---")

cards = ["jack", "queen", "king"]
shuffle(cards)
for card in cards:
    print(card)
print("---")

print(statistics.mean([100, 90]))
print("---")
