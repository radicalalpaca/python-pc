"""
Simple algorithmic trading bot using the Alpaca API.
"""

import alpaca_trade_api as tradeapi
import time
import requests

API_KEY = "PK6P10GRV2NU7ZJWF4V6"
SECRET_KEY = "66Y2X9fT6W1r6kN0xf5FA4z280ooC8SxrdLcoH8H"

#Alpaca API endpoint URL
endpoint_url = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, SECRET_KEY, endpoint_url, api_version='v2')

account = api.get_account()

print(account)