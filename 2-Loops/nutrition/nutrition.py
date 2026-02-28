fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "honeydew melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80",
}

user_input = input("Please enter a fruit: ")
you_fucked_up = False
fruit_exists = False

for fruit in fruits:
    if fruit == user_input.lower():
        fruit_exists = True
        print(fruits[fruit] + " calories.")
    else:
        you_fucked_up = True

while you_fucked_up == True and fruit_exists == False:
    print("That is a forbidden fruit. The call of sin has found you.")
