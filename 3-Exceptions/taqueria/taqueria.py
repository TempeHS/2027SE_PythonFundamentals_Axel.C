menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
user_total = float(0)
while True:
    try:
        user_input = input("Add an item for purchase: ")
    except EOFError:
        
    for item in menu:
        if user_input == item:
            user_total += round(menu[item], 2)
