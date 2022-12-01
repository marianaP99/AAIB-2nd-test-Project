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

def mqtt_sub():
    ready = True
    sound = client.subscribe("AAIB/MP")

def mqtt_pub():
    message = 'start'
    client.publish("AAIB/MP", message)

from streamlit_app import get_button
button = myapp.get_button()

client.loop_start()

if button:
    mqtt_pub()
    mqtt_sub()
    
