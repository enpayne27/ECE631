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
				if msg.topic == "ece631/Lab2Python/temperature/":
					Temp = json.loads(msg.payload)
					TempVal = Temp.get('Fahrenheit', None)
					if TempVal is not  None:
						TempCel = (TempVal - 32) / 1.8
						celDict = dict()
						celDict['Celsius'] = TempCel
						celStrJson = json.dumps(celDict)
						print("Topic: "+msg.topic+"Message: "+str(msg.payload))
						print(celStrJson)
						MQTTPub.PushData("ece631/Lab2Python/temperature/", celStrJson) 
	finally:
		del MQTTSub
		del MQTTPub
