import paho.mqtt.client as mqtt
client = mqtt.Client()
client.on_connect = on_connect
client.connect("test.mosquitto.org", 1883, 60)
client.publish("AAIB/test", “hello world”)
