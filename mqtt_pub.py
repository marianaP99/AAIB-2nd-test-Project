import paho.mqtt.client as mqtt
2. client = mqtt.Client()
3. client.on_connect = on_connect
4. client.connect("test.mosquitto.org", 1883, 60)
5. client.publish("AAIB/test", “hello world”)
