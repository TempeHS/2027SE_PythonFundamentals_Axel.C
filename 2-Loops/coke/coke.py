amount_due = 50


while amount_due > 0:
    cents = int(input("Coke is $0.50 cents. Please enter coin: "))
    if cents == 25 or cents == 10 or cents == 5:
        amount_due -= cents
    else:
        print("Invalid coin. Accepts 25c, 10c, 5c.")
    print("Amount due: " + str(amount_due))
