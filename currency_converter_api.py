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

data = get_currencies()
print_currencies(data)