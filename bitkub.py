import hashlib
import hmac
import json
import requests

# API info
API_HOST = 'https://api.bitkub.com'
API_KEY = 'xxxxxxxxxxxxxxxx'
API_SECRET = b'xxxxxxxxxxxxxxxx'

header = {
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'X-BTK-APIKEY': API_KEY,
}

def json_encode(data):
	return json.dumps(data, separators=(',', ':'), sort_keys=True)

def sign(data):
	j = json_encode(data)
	print('Signing payload: ' + j)
	h = hmac.new(API_SECRET, msg=j.encode(), digestmod=hashlib.sha256)
	return h.hexdigest()

# check server time
def timeserver():
    response = requests.get(API_HOST + '/api/servertime')
    ts = int(response.text)
    print('Server time: ' + response.text)
    return ts

# get last price
def getprice(name):
	product = name
	rticker = requests.get(API_HOST + '/api/market/ticker')
	rticker = rticker.json()
	price = float(rticker[product]['last'])
	return price

# get order info
def orderinfo(symbol,orderid,side):
	order_info = {
	'sym': symbol,
	'id': orderid,
	'sd': side,
	'ts': timeserver(),}

	signature = sign(order_info)
	order_info['sig'] = signature
	r = requests.post(API_HOST + '/api/market/order-info', headers=header, data=json_encode(order_info))
	return r

# get my-open-orders
def my_open_orders(symbol):
	open_orders = {
	'sym': symbol,
	'ts': timeserver(),}

	signature = sign(open_orders)
	open_orders['sig'] = signature
	r = requests.post(API_HOST + '/api/market/my-open-orders', headers=header, data=json_encode(open_orders))
	return r
