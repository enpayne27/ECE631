#! /usr/bin/env python
#
# Jay Herrmann
# ECE631 Spring 2016
#MQTT Clients for Publish and Subscript
#
import paho.mqtt.client as mqtt
import time

class MQTTPusher(object):
	Messages = []
	def __init__(self,Host,Port):
		# The callback for when the client receives a CONNACK response from the server.
		def on_connect(client, userdata, rc):
			pass
			#print("Connected with result code "+str(rc))
			# Subscribing in on_connect() means that if we lose the connection and
			# reconnect then subscriptions will be renewed.
		#	client.subscribe("$SYS/#")

		# The callback for when a PUBLISH message is received from the server.

		self.client = mqtt.Client()
		self.client.on_connect = on_connect
		self.client.connect_async(Host, Port, 60)
		self.client.loop_start()

	def __del__(self):
		self.client.loop_stop()

	def PushData(self,Topic,Message):
		self.client.publish(Topic, Message, qos=0, retain=False)


class MQTTListener(object):
	Messages = []
	def __init__(self,Host,Port,ListenTopic='#'):
		# The callback for when the client receives a CONNACK response from the server.
		def on_connect(client, userdata, rc):
			pass
			#~ print("Connected with result code "+str(rc))
			# Subscribing in on_connect() means that if we lose the connection and
			# reconnect then subscriptions will be renewed.
			client.subscribe(ListenTopic)

		def on_disconnect(client, userdata, rc):
			pass
			#~ print "Disconnect: %s"%rc

		# The callback for when a PUBLISH message is received from the server.
		def on_message(client, userdata, msg):
			#~ print ("OnMessage:")
			self.Messages.append(msg)

		def on_subscribe(client, userdata, mid, granted_qos):
			#print ("Sub Topic: %s"%userdata)
			pass

		def on_unsubscribe(client, userdata, mid):
			#print ("UnSub Topic: %s"%userdata)
			pass

		def on_log(client, userdata, level, buf):
			#print "Log: %s"%userdata
			pass

		self.client = mqtt.Client()
		self.client.on_connect = on_connect
		self.client.on_message = on_message
		#~ self.client.on_disconnect = on_disconnect
		#~ self.client.on_subscribe = on_subscribe
		#~ self.client.on_unsubscribe = on_unsubscribe
		#~ self.client.on_log = on_log

		self.client.connect_async(Host, Port, 30)
		self.client.loop_start()

	def __del__(self):
		self.client.loop_stop()

if __name__ == "__main__":
	MQTTListener = MQTTListener('127.0.0.1',1883)
	try:
		while (True):
			time.sleep(0.05)
			if len(MQTTListener.Messages)>0:
				msg = MQTTListener.Messages.pop()
				print("Topic: "+msg.topic+" Message: "+str(msg.payload))
	finally:
		del MQTTListener
