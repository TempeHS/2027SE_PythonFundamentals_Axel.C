from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) > 1 and len(sys.argv) < 4:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            if sys.argv[2] in figlet.getFonts():
                figlet.setFont(font=sys.argv[2])
            else:
                sys.exit("Incorrect argument.")
        except IndexError:
            sys.exit("Incorrect arguments.")
    elif sys.argv[1] == "0":
        figlet.setFont(font=random.choice(figlet.getFonts()))
    else:
        sys.exit("Incorrect arguments.")
else:
    sys.exit("Incorrect arguments.")

print(figlet.renderText(input("Please enter text to be converted: ")))
