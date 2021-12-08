import os
import requests
import datetime
import time
from datetime import date, timedelta

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'da62bf9d-971f-4a45-abd1-d6c558606b01',
}

response = requests.get(url, params = parameters, headers = headers)
data = response.json()['data']
today = date.today()
yesterday = str(today - timedelta(days=1))
yesterday_datetime = datetime.datetime.strptime(yesterday, '%d-%m-%Y')

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def newCoins():
    
    try:

        for i in range(0,len(data), 1):
            
            name = data[i]['name']
            symbol = data[i]['symbol']
            price = data[i]['quote']['USD']['price']
            date_added_str = data[i]['date_added'][:10]
            date_added = datetime.datetime.strptime(date_added_str, '%d-%m-%Y')

            if yesterday_datetime < date_added:
                #print(data)
                print("Name:",name," | Symbol:",symbol," | Price USD:",price," | Date added:",date_added_str)

               
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        
        
while True:
    
    newCoins()
    time.sleep(3)
    clearConsole()