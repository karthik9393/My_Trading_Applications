import requests

# Replace 'api_key' with actual TradeStation API key
api_key = 'api_key'
url = 'https://api.tradestation.com/v2/marketdata/quotes'

headers = {
    'Authorization': f'Bearer {api_key}'
}


params = {
    'symbol': 'AAPL'
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print(data)
