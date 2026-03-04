grocery_list = {}

while True:
    try:
        user_input = input("Add an item to the shopping list: ")
    except EOFError:
        print("\n")
        break
    else:
        try:
            grocery_list[user_input.upper()] += 1
        except KeyError:
            grocery_list[user_input.upper()] = 1

sorted_grocery_list = dict(sorted(grocery_list.items()))
for item in sorted_grocery_list:
    print(str(sorted_grocery_list[item]) + " " + item)
