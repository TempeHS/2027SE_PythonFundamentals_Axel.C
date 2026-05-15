def main():
    user_tweet = input("Please input a variable name: ")
    print(shorten(user_tweet))


def shorten(word):
    vowels = ["a", "i", "e", "o", "u"]
    shortened_tweet = ""
    for character in word:
        if character.lower() not in vowels:
            shortened_tweet += character
    return str(shortened_tweet)


if __name__ == "__main__":
    main()
