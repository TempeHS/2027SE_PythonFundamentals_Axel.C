import inflect

names = []

p = inflect.engine()
while True:
    try:
        names.append(input("Please enter a name: "))
    except EOFError:
        print("\n")
        break

print("Adieu, adieu, to " + p.join(names))
