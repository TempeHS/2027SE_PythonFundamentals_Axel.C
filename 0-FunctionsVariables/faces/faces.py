def convert(userStr):
    return userStr.replace(":)", "🙂").replace(":(", "🙁")


def main():
    userInput = input("Enter text for emoji conversion: ")
    # this is passing userInput as userStr in the convert function
    print(convert(userInput))


main()
# just a note: a def function can be ordered in any way, because python reads the def statement as define on first cycle of code, defining it so order doesnt matter
