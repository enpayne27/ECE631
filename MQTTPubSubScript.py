#! /usr/bin/env python
# ECE 631 Spring 2019
# Author: Erin Payne
# Demo of how Publisher/Subscriber works
#

import json
import MQTTClients
import time
MQTTSub = MQTTClients.MQTTListener('127.0.0.1', 1883)
MQTTPub = MQTTClients.MQTTPusher('127.0.0.1', 1883)

if __name__=="__main__":
	print("Hello World")

	try:
		while(True):
			time.sleep(0.05)
			if len(MQTTSub.Messages)>0:
				msg = MQTTSub.Messages.pop()
				print("Topic: " +msg.topic+"Message: "+str(msg.payload))
	finally:
		del MQTTSub
		del MQTTPub
