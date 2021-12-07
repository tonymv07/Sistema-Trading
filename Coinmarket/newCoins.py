import os
import requests
import datetime
import sched
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
yesterday = str(today - timedelta(days=2))
yesterday_datetime = datetime.datetime.strptime(yesterday, '%Y-%m-%d')
clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

list_old = []
list_new = []
 
def new_coins(cont,vali):
    
    try:
        
        list_new.clear()
        
        for i in range(0,len(data), 1):
            name = data[i]['slug']
            date_added_str = data[i]['date_added'][:10]
            date_added = datetime.datetime.strptime(date_added_str, '%Y-%m-%d')
            
            
            if cont == 0:

                if yesterday_datetime < date_added:
                    #list_new.append(name)
                    list_old.append(name)

                    #print(name," : ",date_added_str)
                    
            else:
                
                if yesterday_datetime < date_added:
                    list_new.append(name)
                    
                
                
        if cont != 0:
            
            #print("List Old")
            #print(list_old)
            check_lists(list_new)
            
            
        else:
            print("List Old")
            print(list_old)
            #for i in list_old:
                #print(i)
        
        #print(list_old)       
          
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        
        
def check_lists(list_n):
    new = []
    vali = False


    for i in list_n:
        if i not in list_old:
            new.append(i)
            vali = True

    if vali == True:
        print("Hay monedas nuevas:\n")
        for i in new:
            print(i)
            
        

    else:
        print("No hay monedas nuevas")
        
    list_old = list_n

def delay(period,message):
    how_often =  sched.scheduler(time.time,time.sleep)
    how_often.enterabs(period,1,print,argument=(message,))
    print("Se mostrará un mensaje cada: 10 segundos ")
    how_often.run()
    



cont = 0
vali = True

list_new2 = ['btc']

while True:
    
    new_coins(cont,vali)
    time.sleep(5)
    clear_console()
    cont = cont + 1
    
#while True:
    
    #delay(time.time()+10,"ejecutando una función")
    