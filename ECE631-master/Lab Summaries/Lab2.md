It today's lab we began using Freeboard to learn how to establish connections to
send and receive messages and data. In this lab we were able to subscribe to the
ece631Lab2 datasource to observe a variety of data files like text, images, 
gauges and GPS map locations. In addition to learning the basics of Freeboard,
we were able to use HiveMQ from last week's lab to subscribe to the same file
client to visually observe incoming data message updates being sent to our RPi. 
Knowing the ways the RPi can exchange data through Freeboard allows us to begin 
to understand the ways we can manipulate this information for our own future 
data exchanges.

The following was my JSON code for my Lab 2 freeboard panels:

{
	"version": 1,
	"allow_edit": true,
	"plugins": [],
	"panes": [
		{
			"width": 1,
			"row": {
				"3": 1
			},
			"col": {
				"3": -24
			},
			"col_width": 1,
			"widgets": [
				{
					"type": "text_widget",
					"settings": {
						"title": "Pass",
						"size": "regular",
						"value": "datasources[\"Lab2\"][\"msg\"][\"Pass\"]",
						"animate": true
					}
				},
				{
					"type": "text_widget",
					"settings": {
						"title": "Lat",
						"size": "regular",
						"value": "datasources[\"Lab2\"][\"msg\"][\"Lat\"]",
						"animate": true
					}
				},
				{
					"type": "text_widget",
					"settings": {
						"title": "Long",
						"size": "regular",
						"value": "datasources[\"Lab2\"][\"msg\"][\"Long\"]",
						"animate": true
					}
				},
				{
					"type": "gauge",
					"settings": {
						"value": "datasources[\"Lab2\"][\"msg\"][\"Count\"]",
						"min_value": 0,
						"max_value": 100
					}
				}
			]
		},
		{
			"width": 1,
			"row": {
				"3": 1
			},
			"col": {
				"3": 2
			},
			"col_width": 1,
			"widgets": [
				{
					"type": "picture",
					"settings": {
						"src": "datasources[\"Lab2\"][\"msg\"][\"Picture\"]",
						"refresh": 5
					}
				}
			]
		},
		{
			"width": 1,
			"row": {
				"3": 1
			},
			"col": {
				"3": 3
			},
			"col_width": 1,
			"widgets": [
				{
					"type": "google_map",
					"settings": {
						"lat": "datasources[\"Lab2\"][\"msg\"][\"Lat\"]",
						"lon": "datasources[\"Lab2\"][\"msg\"][\"Long\"]"
					}
				}
			]
		}
	],
	"datasources": [
		{
			"name": "Lab2",
			"type": "paho_mqtt",
			"settings": {
				"server": "192.168.1.222",
				"port": 8080,
				"use_ssl": false,
				"client_id": "",
				"username": "",
				"password": "",
				"topic": "ece631/#",
				"json_data": true
			}
		}
	],
	"columns": 3
}