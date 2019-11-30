import hashlib
import hmac
import json
import requests


def json_encode(data):
	return json.dumps(data, separators=(',', ':'), sort_keys=True)

def sign(data):
	j = json_encode(data)
	print('Signing payload: ' + j)
	h = hmac.new(API_SECRET, msg=j.encode(), digestmod=hashlib.sha256)
	return h.hexdigest()

# check server time
def t():
    response = requests.get(API_HOST + '/api/servertime')
    ts = int(response.text)
    print('Server time: ' + response.text)
    return ts

def getprice(product):
	product = product
	rticker = requests.get(API_HOST + '/api/market/ticker')
	rticker = rticker.json()
	rproduct = float(rticker[product]['last'])
	return rproduct
