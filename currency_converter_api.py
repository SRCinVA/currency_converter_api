from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "89fa56e292ed77a89e10"

# need to send some query parameters if we want to get some specific data
    # a.) get a list of currencies

printer = PrettyPrinter()  # remember that PrettyPrinter is a formating tool for JSON.

def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}" # remember that '?' starts the query parameter.
    url = BASE_URL + endpoint
    data = get(url).json()['results'] # 'results' will be a dictionary ...

    data = list(data.items()) # ... then we cast it as a list.
    data.sort() # defaults to alphabetical order

    return data

def print_currencies(currencies):
    for name, currency in currencies: # we have to give two items because it's a list of tuples
        name = currency["currencyName"]
        _id = currency["id"]
        symbol = currency.get("currencySymbol", " ") # get() will give you the value or the default (an empty string)s
        print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"  # he doesn't explain the reasoning behind this.
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print("Invalid currencies")
        return
    
    rate = list(data.values())[0] # this is to grab the pair; the 0th item should be the exchange rate.
    print(f"{currency1} -> {currency2} = {rate}")

    return rate

    # printer.pprint(data)

# data = get_currencies()
# print_currencies(data)

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:  # ... which would mean that we got an invalid currency
        return

    try:
        amount = float(amount) # try to convert the amount into a float.
    except:
        print("Invalid amount") # if you got a string or other issue.
        return

    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

def main():
    currencies = get_currencies()
    print("Welcome to the currency converter.")
    print("List - lists the different currencies.")
    print("Convert - convert from one currency to another.")
    print("Rate - get the exchange rate of two currencies")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies(currencies)
        elif command == "convert":
            currency1 = input("Enter a base currency id: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency id to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == "rate":
            currency1 = input("Enter a base currency id: ").upper()
            currency2 = input("Enter a currency id to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command!")

main()

# rate = exchange_rate("USD", "CAD")
# print(rate)
# convert("USD","CAD",2)
