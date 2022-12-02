import paho.mqtt.client as mqtt
import streamlit_app as myapp

ready = False

def on_connect(client, userdata, flags, rc):
     print("Connected flags"+str(flags)+"result code " +str(rc)+"client1_id ")

def on_message(client, userdata, msg):
     print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883)

def mqtt_ready():
    return ready

client.loop_start()

sound = client.subscribe("AAIB/MP")
print(sound)
