import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Incorrect number of command line arguments")

if sys.argv[1].endswith(".csv"):
    pass
else:
    sys.exit("Incorrect file type given.")


try:
    with open(sys.argv[2], "a") as file_write:
        writer = csv.DictWriter(file_write, fieldnames=["first", "last", "house"])
        writer.writeheader()
        with open(sys.argv[1]) as file_read:
            reader = csv.DictReader(file_read)
            for row in reader:
                lastN, firstN = row["name"].split(",")
                writer.writerow(
                    {"first": firstN.lstrip(), "last": lastN, "house": row["house"]}
                )
except FileNotFoundError:
    sys.exit("One or more files provided do not exist.")
