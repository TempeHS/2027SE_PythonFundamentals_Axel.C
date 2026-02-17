userinput = input("Please enter a math problem: ")
x, y, z = userinput.split(" ")
match y:
    case "+":
        print(round(float(x) + float(z), 1))
    case "-":
        print(round(float(x) - float(z), 1))
    case "*":
        print(round(float(x) * float(z), 1))
    case "/":
        print(round(float(x) / float(z), 1))
