import requests
import sys


if len(sys.argv) != 2:
    sys.exit("Incorrect arguments.")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Http error. Try again.")

o = response.json()

final_bitcoin = o["bpi"]["USD"]["rate_float"]

try:
    print(f"${(final_bitcoin * float(sys.argv[1])):,.4f}")
except ValueError:
    sys.exit("Argument is not an integer")
