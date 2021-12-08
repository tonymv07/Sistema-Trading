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



clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
list_old = []

 
def new_coins(cont):
    
    response = requests.get(url, params = parameters, headers = headers)
    data = response.json()['data']
    today = date.today()
    yesterday = str(today - timedelta(days=1))
    yesterday_datetime = datetime.datetime.strptime(yesterday, '%Y-%m-%d')
    

    global list_old
    
    try:
        
        list_new = []
        
        for i in range(0,len(data), 1):
            name = data[i]['slug']
            date_add = data[i]['date_added']
            #json['name'] = data[i]['name']
            #json['date_added'] = data[i]['date_added']
            date_added_str = data[i]['date_added'][:10]
            date_added = datetime.datetime.strptime(date_added_str, '%Y-%m-%d')
            date_dt = datetime.datetime.strptime(date_add, '%Y-%m-%dT%H:%M:%S'+'.000Z')
        
            if yesterday_datetime < date_added:
                #print(date_dt)
                json = {}
                json['name'] = data[i]['name']
                json['date_added'] = data[i]['date_added']
                json['price'] = data[i]['quote']['USD']['price']
                json['id'] = data[i]['id']
                list_new.append(json)
                
                       
        order_list(list_new)
                  
        if cont != 0:
            
            check_lists(list_new)
            list_old = list(list_new)
            
            
        else:
            
            print("List New:\n")
            for i in list_new:
                print(i)
            print(len(list_new))
            list_old = list(list_new)
                   
          
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        
        
def check_lists(list_n):
    
    global list_old
    
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
    


def delay(period):
    
    print("\n\nSe mostrará un mensaje cada: 30 minutos ")
    time.sleep(period)
    

def order_list(list_n):
    
    for i in range(0,len(list_n),1):
        for j in range(0,len(list_n)-1,1):
            if list_n[j]['date_added'] < list_n[j+1]['date_added']:
                aux = list_n[j]
                list_n[j] = list_n[j+1]
                list_n[j+1] = aux     
    
    

    
    
    
cont = 0                                      
                                        
while True:
    
    new_coins(cont)
    delay(1800)
    clear_console()
    cont = cont + 1
    

    