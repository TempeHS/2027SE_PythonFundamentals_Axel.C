import sys
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Incorrect number of command line arguments")

if sys.argv[1].endswith(".csv"):
    pass
else:
    sys.exit("Incorrect file type given.")

processed_file = []

try:
    with open(sys.argv[1]) as file:
        for line in file:
            processed_file.append(line.split(","))
except FileNotFoundError:
    sys.exit("File given does not exist")

print(tabulate(processed_file, headers="firstrow", tablefmt="grid"))
