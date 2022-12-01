import paho.mqtt.client as mqtt
import recordsound as rs

def on_connect(client, userdata, flags, rc):
     print("Connected flags"+str(flags)+"result code " +str(rc)+"client1_id ")

def on_message(client, userdata, msg):
     print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883)

def mqtt_sub():
    print("Ready to start aquisition")
    button = client.subscribe("AAIB/MP")

def mqtt_pub():
    message = rs.record
    client.publish("AAIB/MP", message)

loop_start()

if button == 'START':
    mqtt_pub()