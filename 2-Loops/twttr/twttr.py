user_tweet = input("Please input a variable name: ")
vowels = ["a", "i", "e", "o", "u"]

shortened_tweet = ""


for character in user_tweet:
    if character.lower() not in vowels:
        shortened_tweet += character


print(shortened_tweet)
