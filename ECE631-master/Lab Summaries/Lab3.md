In today's lab we learned how subscribe, send and receive messages on the
Raspberry Pi Zero. This was done using the USB connection to the Zero and 
Arduino IDE's serial monitor. Message transaction was also viewable through
HiveMQ once subscribed to corresponding topics. Furthermore, in sending and
receiving messages, we were able to practice our JSON writing to properly
display various types and values. 

Note: In order to run the Zero from my Macbook, I had to download drivers from
the following website: [(https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/software-installation-mac)](url)

The following were some of the JSON commands and messages used in today's lab:

```
Wifi Setup:
    {"Action":"WifiSetup","Wifi":{"SSID":"ece631Lab","Password":"stm32IOT!"}}
MQTT Setup:
    {"Action":"MQTTSetup","MQTT":{"Host":"192.168.1.150","Port":"1883"}}
Subscribing:
    {"Action":"MQTTSubs","MQTT":{"Topics":["ece631/Topic1","ece631/Topic2","ece631/debug/erin","ece631/auto/erin","ece631/weather/erin"]}}
Sample JSON Messages:
    {"Action":"MQTTPub","MQTT":{"Topic":"ece631/debug/erin","Message":"{\"Count\": 20}"}}
    {"Action":"MQTTPub","MQTT":{"Topic":"ece631/auto/erin","Message":"{\"Car\":{\"Seats\":2,\"Doors\":4,\"Windows\":\"Electric\"}}"}}
    {"Action":"MQTTPub","MQTT":{"Topic":"ece631/weather/erin","Message":"{\"Temp\":20,\"Humidity\":55,\"Type\":{\"Temp\":\"C\",\"Humidity\":\"%\"}}"}}
```
