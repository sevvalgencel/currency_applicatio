import requests

url = "http://data.fixer.io/api/convert"
key = "kendi_api_keyinizi_yazın"

base = input("Baz alınacak para birimi: ")
currency = input("Çevirelecek para birimi: ")
quantity = float(input("Miktar: "))

payload = {"access_key": key, "from": base, "to": currency, "amount": quantity}
response = requests.get(url, params=payload)
json_data = response.json()

print(float(json_data["rates"][currency]) * quantity)