x, y = map(int, input("Please enter a fraction: ").split("/"))
fuel_level = 0
try:
    fuel_level = (x / y) * 100
except ValueError:
    print("Values given were not integers.")
except ZeroDivisionError:
    print("Fuel level given is impossible.")


if fuel_level <= 1:
    print("E")
elif fuel_level >= 99:
    print("F")
else:
    print(str(round(fuel_level)) + "%" + " fuel remaining.")
