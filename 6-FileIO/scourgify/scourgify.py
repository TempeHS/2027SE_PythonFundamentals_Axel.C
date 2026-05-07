import sys
import csv

if len(sys.argv) != 3:
    sys.exit("Incorrect number of command line arguments")

if sys.argv[1].endswith(".csv"):
    pass
else:
    sys.exit("Incorrect file type given.")
