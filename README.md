# bitkub
my functions in bitkub.com

## get last price
bitkub.getprice('symbol')


## get my open orders
### Get list all open orders of the given symbol.
bitkub.my_open_orders('symbol')

## import bitkub
### 
bitkub.my_open_orders('symbol')

from bitkub import bitkub
import schedule


# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = 'EDIT'
API_SECRET = b'EDIT' #b = byte Array
bitkub = bitkub(API_HOST=API_HOST,
                API_KEY=API_KEY,
                API_SECRET=API_SECRET)


product = 'THB_XRP'
price = bitkub.getprice(name=product)
print(price)
