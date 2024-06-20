import json
from urllib.request import urlopen

# Fetching JSON data from the URL
url = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json"
with urlopen(url) as response:
    source = response.read()

data = json.loads(source)

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

if 'USD/INR' in usd_rates:
    usd_inr_rate = float(usd_rates['USD/INR'])
    print(f"50 USD is equal to {50 * usd_inr_rate} INR")
else:
    print("USD/INR rate not found in the data.")
