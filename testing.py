import requests

url = 'https://m.media-amazon.com/images/M/MV5BYWRkZjJiODEtM2IwZi00ZjM1LWEyOTUtOThjMDk3YThjZDUzXkEyXkFqcGdeQXVyMTUzMTg2ODkz._V1_UY209_CR0,0,140,209_AL_.jpg'

response = requests.get(url)

data = response.json()

print(data)