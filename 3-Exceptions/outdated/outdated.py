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
    if user_date.split(" ")[0] in months:
        