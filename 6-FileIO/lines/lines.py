import sys

file_length = 0

# checks length and stuff

if len(sys.argv) != 2:
    sys.exit()

# idk these comments are here as a test

if sys.argv[1].endswith(".py"):
    pass
else:
    sys.exit()


try:
    with open(sys.argv[1], "r") as user_given_file:
        for line in user_given_file:
            line = line.lstrip()
            if line.isprintable() or line.startswith("#"):
                pass
            else:
                file_length += 1
                print(line.lstrip())
                print("ENDLINE")
except FileNotFoundError:
    sys.exit()


print(f"The chosen file has {file_length} lines.")
