from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://freecurrcov.com/"
API_KEY = "89fa56e292ed77a89e10"

# need to send some query parameters if we want to get some specific data
    # a.) get a list of currencies

printer = PrettyPrinter()  # remember that PrettyPrinter is a formating tool for JSON.

endpoint = f"api/v7/currencies?apiKey={API_KEY}" # remember that '?' starts the query parameter.
