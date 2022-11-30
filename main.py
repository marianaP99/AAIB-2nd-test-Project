import paho.mqtt.client as mqtt
import recordsound as rs

client = mqtt.Client()
client.on_connect = on_connect
client.connect("test.mosquitto.org", 1883, 60)
message = rs.record
client.publish("AAIB/test", message)
