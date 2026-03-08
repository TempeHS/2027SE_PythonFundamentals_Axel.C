import random


def main():
    user_score = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for _ in range(1, 4):
            try:
                if int(input(str(x) + " " + str(y) + " = ")) == (x + y):
                    user_score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            if _ == 3:
                print("Correct answer: " + str(x) + " " + str(y) + " = " + str(x + y))
    print("Correct answers: " + str(user_score) + " / 10")


def get_level():
    while True:
        try:
            user_level = int(input("Level: "))
            if 1 <= user_level <= 3:
                return user_level
        except ValueError:
            pass


def generate_integer(level_input):
    if level_input == 3:
        return random.randint(100, 999)
    elif level_input == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1, 9)


if __name__ == "__main__":
    main()
