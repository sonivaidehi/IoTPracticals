import json
import context
import sqlite3
import paho.mqtt.client as mqtt

connection = sqlite3.connect("mqtt_dht.db")
crsr = connection.cursor()

def on_message(client, userdata, msg):
	#print(msg.topic+ " "+ str(msg.payload))
	decodedData = msg.payload.decode("utf-8") 
	#print(decodedData)
	temperatureData = json.loads(decodedData)
	temperature_c = temperatureData["Temperature"]
	humidity = temperatureData["Humidity"]
	sql_command = """INSERT INTO dht_data(temperature,humidity,notice_time) VALUES('{}','{}',CURRENT_TIMESTAMP)""".format(str(temperature_c),str(humidity))
	#print(sql_command)
	crsr.execute(sql_command)
	connection.commit()

broker_url = "broker.emqx.io"
broker_port = 1883

client = mqtt.Client()
client.on_message = on_message

client.connect(broker_url,broker_port)
client.subscribe("dhtDataTopic", qos=0)

client.loop_forever()
