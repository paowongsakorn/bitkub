# Bitkub
bitkub.com library python


### Get ticker price.
```sh
product = 'THB_XRP'
price = bitkub.getprice(name=product)
print(price)
```

### get my open orders
#### Get list all open orders of the given symbol.
```sh
shbitkub.my_open_orders('symbol')
```

### get order info
#### Get information regarding the specified order.
```sh
order_info = bitkub.orderinfo(name='symbol',orderid=106842,side='sell')
```

### get my balances
#### Get balances info: this includes both available and reserved balances.
```sh
shbitkub.my_open_orders('symbol')
```



### Examples

```sh
from bitkub import bitkub

# API info
'API_HOST = 'https://api.bitkub.com'
API_KEY = 'EDIT'
API_SECRET = b'EDIT' #b = byte Array
bitkub = bitkub(API_HOST=API_HOST,
                API_KEY=API_KEY,
                API_SECRET=API_SECRET)
'

product = 'THB_XRP'
price = bitkub.getprice(name=product)
print(price).


order = bitkub.createsell(name=product,amount=1,rate=10,ordertype='market')
print(order)

```
This will create a sell order.


### Donate

| Currency | Address | Deposit Tag |
| ------ | ------ | ------ |
| Bitcoin | 3Ne8jAQM6koKaNuSkZEJmWBGzNC1gy8NZM | 
| Ripple | rpXTzCuXtjiPDFysxq8uNmtZBe9Xo97JbW | 1075605645
| Stellar | GBS2RTBGEWBT7DJOH7CTA4PDVLIPONCPCIILJPPESWSHDIV4NFZJHRP3 | 1020775332
| Binance | bnb1g7kg0yl50u5xj5kumga24uudc5204pzgxkgg4u | 1072588774
