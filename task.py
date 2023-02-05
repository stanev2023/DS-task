from polygonscan import PolygonScan
import pandas as pd
import requests
import json

# Select a random address with more than a few transactions. example: (0x5118639e30f555cC30A266971C08b83EF2eD66A3)
x = requests.get('https://api.polygonscan.com/api?module=account&action=balance&address=0x5118639e30f555cC30A266971C08b83EF2eD66A3&apikey=AI3BS8YDCEJZIGHN24HSFI9IT1373GQKNC%27')

#Get all asset balances available to the owner of this address
word = requests.get('https://api.polygonscan.com/api?module=token&action=tokeninfo&contractaddress=0x5118639e30f555cC30A266971C08b83EF2eD66A3&apikey=AI3BS8YDCEJZIGHN24HSFI9IT1373GQKNC%27')
print(word.text)

# Get all transactions of address
x2 = requests.get('https://api.polygonscan.com/api?module=account&action=txlist&address=0x5118639e30f555cC30A266971C08b83EF2eD66A3&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=AI3BS8YDCEJZIGHN24HSFI9IT1373GQKNC%27')

x3 = x2.json().get('result');
array = json.dumps(x3)
df = pd.read_json(array)
df.to_csv('sample.csv')
print(df)
