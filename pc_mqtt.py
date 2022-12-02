import paho.mqtt.client as mqtt
import recordsound as rs

def on_connect(client, userdata, flags, rc):
     print("Connected")

def on_message(client, userdata, msg):
     print(msg.topic+" "+str(msg.payload))

def mqtt_sub():
    print("Ready to start aquisition")
    button = client.subscribe("AAIB/MP/READY")

def mqtt_pub():
    message = rs.record
    client.publish("AAIB/MP/SOUND", message)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883)

client.loop_start()

if button == 'start':
    mqtt_pub