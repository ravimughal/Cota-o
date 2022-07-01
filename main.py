## Cotação - Ravi Mughal
from time import sleep
import requests

req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL").json()

usd = req["USDBRL"]["bid"]
eur = req["EURBRL"]["bid"]
btc = req["BTCBRL"]["bid"]

while True:
    print("-" * 30)
    print("Bitcoin:", btc)
    print("Euro:", eur)
    print("Dólar:", usd)
    print("-" * 30)
    sleep(30)