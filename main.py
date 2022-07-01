## Cotação - Ravi Mughal
from time import sleep
import requests

DOL = "https://economia.awesomeapi.com.br/last/USD-BRL"
EUR = "https://economia.awesomeapi.com.br/last/EUR-BRL"
BTC = "https://economia.awesomeapi.com.br/last/BTC-BRL"

dam = requests.get(DOL).json()
dam_USD = dam["USDBRL"]

eam = requests.get(EUR).json()
eam_EUR = eam["EURBRL"]

bam = requests.get(BTC).json()
bam_BTC = bam["BTCBRL"]

while True:
    print("-" * 30)
    print("Bitcoin:",bam_BTC["bid"])
    print("Euro:",eam_EUR["bid"])
    print("Dólar:",dam_USD["bid"])
    print("-" * 30)
    sleep(30)