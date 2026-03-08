import random

while True:
    level = input("Enter a level: ")
    try:
        if int(level) > 0:
            break
    except ValueError:
        pass

answer = random.randint(1, int(level))

while True:
    user_guess = int(input("Guess the number! "))
    if user_guess > 0:
        if user_guess > answer:
            print("Too large!")
        elif user_guess < answer:
            print("Too small!")
        else:
            print("Just right!")
            break
