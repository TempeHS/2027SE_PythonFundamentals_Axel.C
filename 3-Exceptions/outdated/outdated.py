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

while True:
    user_date = input("Please enter a date: ").replace(",", "").replace("/", " ")
    try:
        user_date = user_date.replace(
            user_date.split(" ")[0], str(months.index(user_date.split(" ")[0]) + 1)
        )
    except IndexError:
        pass
