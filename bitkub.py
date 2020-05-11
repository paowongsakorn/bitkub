import hashlib
import hmac
import json
import requests

class bitkub():
	def __init__ (self,API_HOST=None,API_KEY=None,API_SECRET=None,name=None,orderid=None,side=None,amount=None,rate=None,ordertype=None):
		self.API_HOST = API_HOST
		self.API_KEY = API_KEY
		self.API_SECRET = API_SECRET
		self.header = {
			'Accept': 'application/json',
			'Content-Type': 'application/json',
			'X-BTK-APIKEY': self.API_KEY}


	def getprice(self,name):
		self.product = name
		self.rticker = requests.get(self.API_HOST + '/api/market/ticker')
		self.rticker = self.rticker.json()
		self.price = float(self.rticker[self.product]['last'])
		return self.price


	def timeserver(self):
		self.response = requests.get(self.API_HOST + '/api/servertime')
		self.ts = int(self.response.text)
		# print('Server time: ' + response.text)
		return self.ts


	def my_open_orders(self,name):
		self.name = name		
		self.open_orders = {
		'sym': self.name,
		'ts': self.timeserver()}

		self.signature = self.sign(self.open_orders)
		self.open_orders['sig'] = self.signature
		self.r = requests.post(self.API_HOST + '/api/market/my-open-orders', headers=self.header, data=self.json_encode(self.open_orders))
		self.r = self.r.json()
		return self.r


	def sign(self,data):
		self.data = data
		self.j = self.json_encode(self.data)
		# print('Signing payload: ' + self.j)
		self.h = hmac.new(self.API_SECRET, msg=self.j.encode(), digestmod=hashlib.sha256)
		return self.h.hexdigest()


	def json_encode(self,datajson):
		self.datajson = datajson
		return json.dumps(self.datajson, separators=(',', ':'), sort_keys=True)


	def orderinfo(self,name,orderid,side):
		self.symbol = name
		self.orderid = orderid
		self.side = side

		self.order_info = {
		'sym': self.symbol,
		'id': self.orderid,
		'sd': self.side,
		'ts': self.timeserver(),}

		self.signature = self.sign(self.order_info)
		self.order_info['sig'] = self.signature
		#print('Payload with signature: ' + json_encode(order_info))
		self.response = requests.post(self.API_HOST + '/api/market/order-info', headers=self.header, data=self.json_encode(self.order_info))
		self.x = self.response.json()
		#print(x)
		return self.x

	def addresses(self):
		self.address = {
		'ts': self.timeserver(),}

		self.signature = self.sign(self.address)
		self.address['sig'] = self.signature
		#print('Payload with signature: ' + json_encode(order_info))
		self.response = requests.post(self.API_HOST + '/api/crypto/addresses', headers=self.header, data=self.json_encode(self.address))
		self.x = self.response.json()
		#print(x)
		return self.x


	def addresses(self):
		self.address = {
		'ts': self.timeserver(),}

		self.signature = self.sign(self.address)
		self.address['sig'] = self.signature
		#print('Payload with signature: ' + json_encode(order_info))
		self.response = requests.post(self.API_HOST + '/api/crypto/addresses', headers=self.header, data=self.json_encode(self.address))
		self.x = self.response.json()
		#print(x)
		return self.x



	def wallets(self):
		self.address = {
		'ts': self.timeserver(),}

		self.signature = self.sign(self.address)
		self.address['sig'] = self.signature
		#print('Payload with signature: ' + json_encode(order_info))
		self.response = requests.post(self.API_HOST + '/api/market/wallet', headers=self.header, data=self.json_encode(self.address))
		self.x = self.response.json()
		#print(x)
		return self.x



	def balances(self):
		self.address = {
		'ts': self.timeserver(),}

		self.signature = self.sign(self.address)
		self.address['sig'] = self.signature
		#print('Payload with signature: ' + json_encode(order_info))
		self.response = requests.post(self.API_HOST + '/api/market/balances', headers=self.header, data=self.json_encode(self.address))
		self.x = self.response.json()
		#print(x)
		return self.x



	def order_history(self,name):
		self.symbol = name

		self.data = {
			'sym': self.symbol,
			'ts': self.timeserver(),
		}
		self.signature = self.sign(self.data)
		self.data['sig'] = self.signature

		#print('Payload with signature: ' + json_encode(data))
		self.r = requests.post(self.API_HOST + '/api/market/my-order-history', headers=self.header, data=self.json_encode(self.data))
		print('Response: ' + self.r.text)
		return self.r	


	def createbuy(self,name,amount,rate,ordertype):
		self.symbol = name
		self.amount = amount
		self.rate = rate
		self.ordertype = ordertype
		self.data = {
		'sym': self.symbol,
		'amt': self.amount, # THB amount you want to spend
		'rat': self.rate,
		'typ': self.ordertype,
		'ts': self.timeserver(),}

		self.signature = self.sign(self.data)
		self.data['sig'] = self.signature

		#print('Payload with signature: ' + json_encode(data))
		self.r = requests.post(self.API_HOST + '/api/market/place-bid', headers=self.header, data=self.json_encode(self.data))
		print('Response: ' + self.r.text)
		return self.r


	def createsell(self,name,amount,rate,ordertype):
		self.symbol = name
		self.amount = amount
		self.rate = rate
		self.ordertype = ordertype
		self.data = {
		'sym': self.symbol,
		'amt': self.amount, # THB amount you want to spend
		'rat': self.rate,
		'typ': self.ordertype,
		'ts': self.timeserver(),}

		self.signature = self.sign(self.data)
		self.data['sig'] = self.signature

		#print('Payload with signature: ' + json_encode(data))
		self.r = requests.post(self.API_HOST + '/api/market/place-ask', headers=self.header, data=self.json_encode(self.data))
		#print('Response: ' + r.text)
		self.x = self.r.json()
		return self.x
