import imp


import json
from time import time
import time
from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):

	def connect(self):
		self.accept()

		count=0
		for i in range(1000):
			if count < 10:
				count += 1
				self.send(json.dumps({"message": count}))
				time.sleep(1)
			else:
				count = 0
				self.send(json.dumps({"message": count}))
