# https://github.com/public-apis/public-apis - różne api
import requests

# url = "https://api.nbp.pl/api/exchangerates/rates/A/usd/"
url = "https://api.nbp.pl/api/exchangerates/rates/A/eur/"

# nazwa waluty, kurs
response = requests.get(url)
print(response.text)
# {
#   "table": "A",
#   "currency": "dolar amerykański",
#   "code": "USD",
#   "rates": [
#     {
#       "no": "034/A/NBP/2026",
#       "effectiveDate": "2026-02-19",
#       "mid": 3.5780
#     }
#   ]
# }

data = response.json()
print(data)

print("Waluta:", data['currency'])  # Waluta: dolar amerykański

print(data['rates'])
# [{'no': '034/A/NBP/2026', 'effectiveDate': '2026-02-19', 'mid': 3.578}]
print(data['rates'][0])
# {'no': '034/A/NBP/2026', 'effectiveDate': '2026-02-19', 'mid': 3.578}
print(f"Kurs dnia: {data['rates'][0]['mid']} pln")  # Kurs dnia: 3.578 pln

# Waluta: euro
# [{'no': '034/A/NBP/2026', 'effectiveDate': '2026-02-19', 'mid': 4.222}]
# {'no': '034/A/NBP/2026', 'effectiveDate': '2026-02-19', 'mid': 4.222}
# Kurs dnia: 4.222 pln