In today's lab we learned how to utilize the Raspberry Pi Zero, Raspberry Pi 3,
and STM32 Discovery board to send and receive character strings from the MQTT
server. Connecting the STM32 to the RPi 3 through the RPi 0, we could receive a
variety of setup commands to the STM32 that would return select responses to
subscribe and send messages to the online MQTT server for visual reading.
Establishing this kind of message transmission between the RPis and STM32 gave
us the last bits of code necessary to begin our final projects.

These were some of the setup messages sent through the RPi and STM32:
Each "Action" message was sent by the RPi 3 and each "Response" was the 
corresponding message returned from the STM32. (Gathered from Lab 3)

```
Setup Wifi
    {"Action":"WifiSetup","Wifi":{"SSID":"ece631Lab","Password":"stm32IOT!"}}
    {"Response":"WifiStatus","Wifi":{"IP": null, "MAC": "a536d748f900", "Gateway": "192.168.1.1", "isGWPingable": null}}
Setup MQTT
    {"Action":"MQTTSetup","MQTT":{"Host":"192.168.1.222","Port":"1883"}}
    {"Response":"MQTTSetup","Message":{"MQTT":"{\"Result\":\"Success\"}"}}
Setup MQTT Subscriptions
    {"Action":"MQTTSubs","MQTT":{"Topics":["ece631/Topic1"]}}
    {"Response":"MQTTSubs","Message":{"MQTT":"{\"Action\":\"Subscribed\",\"Topics\":[\"ece631/Topic1\"]}"}}
Publish MQTT JSON String
    {"Action":"MQTTPub","MQTT":{"Topic":"Topic String","Message":"Needs to Be JSON String"}}
    {"Response":"MQTTPub","Message":{"MQTT":"Sent"}}
    {"Response":"SubscribedMessage","Message":{"MQTT":"String Probably JSON"}}
```


Once again I had to use the following process to upload my code to the Discovery board.
Go into the Project Explorer and right click:
Clean project>Build Project>Target>Program chip
Then click the black reset button on the board and your most recent code should run.

Additionally the serial monitor from the Arduino IDE was used to perform some
manual message transfers to debug and test the STM32 and read responses through
the RPi 0 to verify the action messages sent through the RPi 3.
The following was used to refresh the serial monitor with every new build of my code:
Tools>Port>/dev/cu.usbserial
Tools>Serial Monitor (or the magnify glass icon on main GUI)