# REST API
# json, xml
# GET, POST, PUT/PATCH, DELETE, HEAD

# klient http
import requests

# pip install requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)
# <Response [200]>
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP
# 200 ok
# 3xx - warningi, przekierowania
# 4xx - 404 - brak strony, 400 Bad Request - błedne dane
# 5xx - błedy po stronie serwera 500 Internal Server Error

print(response.text) # json czyli tekst

data = response.json()
print(data)
print(type(data))