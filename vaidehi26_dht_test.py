import context
import adafruit_dht
import time
import board
import paho.mqtt.client as mqtt
import json

dhtDevice = adafruit_dht.DHT11(board.D4)
broker_url = "broker.emqx.io"
broker_port = 1883

client = mqtt.Client()
client.connect(broker_url, broker_port)

while True:
    try:
      temperature_c = dhtDevice.temperature
      humidity = dhtDevice.humidity
      temperature_data = json.dumps({'Temperature':temperature_c, 'Humidity':humidity})
      print(temperature_data)
      client.publish(topic="dhtDataTopic", payload=temperature_data, qos=0, retain=False)
    except RuntimeError as error:
      print(error.args[0])
      time.sleep(3.0)
      continue
    except Exception as error:
      dhtDevice.exit()
      raise error
    time.sleep(3.0)

