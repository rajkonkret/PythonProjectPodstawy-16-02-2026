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

print(response.text)  # json czyli tekst

data = response.json()
print(data)
print(type(data))
# {"categories":[],"created_at":"2020-01-05 13:42:28.420821",
# "icon_url":"https://api.chucknorris.io/img/avatar/chuck-norris.png",
# "id":"qP7S71sER2iFdk8OzsISug","updated_at":"2020-01-05 13:42:28.420821",
# "url":"https://api.chucknorris.io/jokes/qP7S71sER2iFdk8OzsISug",
# "value":"Chuck Norris spent a day digging a canal in the United States. We know that project as the Mississippi River."}

for i in data:
    print(i)
# categories
# created_at
# icon_url
# id
# updated_at
# url
# value

print(f"Kawał na dzisiaj: {data['value']}")
# Kawał na dzisiaj: Elizabeth Taylor's last words were - "I only ever loved Chuck Norris".

icon_url = data.get("icon_url")
print(icon_url)

response_img = requests.get(icon_url)

with open('icon.png', "wb") as f:
    f.write(response_img.content)

print("Zdjęcie zostało zapisane")
