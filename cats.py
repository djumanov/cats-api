import requests
from pprint import pprint

URL = 'https://api.thecatapi.com/v1/images/search'

r = requests.get(url=URL, params={"limit": 5})
pprint(r.json())