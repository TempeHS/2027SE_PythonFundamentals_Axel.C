months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

is_valid = True

while True:
    user_date = input("Please enter a date: ").replace(",", "").replace("/", " ")
    try:
        user_date = user_date.replace(
            user_date.split(" ")[0], str(months.index(user_date.split(" ")[0]) + 1)
        )
    except IndexError:
        pass
    except ValueError:
        pass

    try:
        if (
            1 <= int(user_date.split(" ")[0]) <= 12
            and 1 <= int(user_date.split(" ")[1]) <= 31
        ):
            break
    except ValueError:
        pass
    print("Invalid date.")

user_date = (
    str(f"{int(user_date.split(" ")[2]):04}")
    + "-"
    + str(f"{int(user_date.split(" ")[0]):02}")
    + "-"
    + str(f"{int(user_date.split(" ")[1]):02}")
)

print(user_date)
