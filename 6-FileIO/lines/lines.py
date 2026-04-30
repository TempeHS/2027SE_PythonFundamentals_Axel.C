import sys

file_length = 0

# checks length and stuff

if len(sys.argv) != 2:
    sys.exit("Incorrect number of command line arguments.")

# idk these comments are here as a test

if sys.argv[1].endswith(".py"):
    pass
else:
    sys.exit("Incorrect file type given.")


try:
    with open(sys.argv[1], "r") as user_given_file:
        for line in user_given_file:
            line = line.lstrip()
            if line.isprintable() or line.startswith("#") or line.startswith(" "):
                pass
            else:
                file_length += 1
                print(line.lstrip(), end=" ")  # this is here fpr debugging
                print("ENDLINE")
except FileNotFoundError:
    sys.exit("File given does not exist.")


print(f"The chosen file has {file_length} lines.")
