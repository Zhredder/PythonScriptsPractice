import requests

#! This file fetches cryptocurrency price data from an API #!

def get_crypto_data():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data

