import requests

url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

response = requests.get(url)
json_data = response.json()
usd_rate = float(json_data[0]['sale'])
uah_rate = float(json_data[0]['buy'])
print(json_data[0])


