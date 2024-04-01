def main():
    fruits = [
              {"apple": 130},
              {"avocado": 50},
              {"banana": 110},
              {"cantaloupe": 50},
              {"grapefruit": 60},
              {"grapes": 90},
              {"honeydew melon": 50},
              {"kiwifruit": 90},
              {"lemon": 15},
              {"lime": 90},
              {"nectarine": 15},
              {"orange": 20},
              {"peach": 60},
              {"pear": 100},
              {"pineapple": 50},
              {"plums": 70},
              {"strawberries": 50},
              {"sweet cherries": 100},
              {"tangerine": 50},
              {"watermelon": 80},
             ]
    user_input = str(input("Item: ")).lower()
    get_cals(user_input, fruits)


def get_cals(input, fruits):
    calories = 0
    for i in fruits:
        for j in i.keys():
            if input == j:
                calories = list(i.values())
                calories = str(calories)[1:-1]
                print("Calories:", calories)
            else:
                break



if __name__ == "__main__":
    main()
