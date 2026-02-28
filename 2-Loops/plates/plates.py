def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() == False or len(s) < 2 or len(s) > 6:
        return False
    if s.isalnum() == False:
        return False

    numbers_check = False

    for character in s:
        if character == " ":
            return False
        if character.isnumeric():
            if character == "0" and numbers_check == False:
                return False
            numbers_check = True
        elif numbers_check == True:
            return False

    return True


main()
